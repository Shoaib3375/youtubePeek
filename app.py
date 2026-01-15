from flask import Flask, request, jsonify, redirect, Response, render_template
import yt_dlp
import requests
import re
from urllib.parse import urlparse
import os

app = Flask(__name__)

# Configuration
PROXY_MAX_BYTES = 200 * 1024 * 1024  # 200 MB max for proxied downloads
YTDLP_TIMEOUT = 15  # seconds for yt-dlp resolution
ALLOWED_SCHEMES = ("http", "https")

# Helpers
_filename_sanitize_re = re.compile(r"[^A-Za-z0-9._-]")

def sanitize_filename(name: str) -> str:
    if not name:
        return "download"
    # replace disallowed characters with underscore
    safe = _filename_sanitize_re.sub("_", name)
    return safe[:200]


def validate_url(url: str) -> bool:
    try:
        p = urlparse(url)
        return p.scheme in ALLOWED_SCHEMES and p.netloc != ""
    except Exception:
        return False


def yt_dlp_extract(url: str):
    ydl_opts = {
        'skip_download': True,
        'quiet': True,
        'no_warnings': True,
        # Prefer JSON output via the python API
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
    return info


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/peek', methods=['POST'])
def api_peek():
    payload = request.get_json(force=True, silent=True)
    if not payload or 'url' not in payload:
        return jsonify({'error': 'Missing "url" in request body', 'code': 'E_MISSING_URL'}), 400
    url = payload['url']
    if not validate_url(url):
        return jsonify({'error': 'Invalid or unsupported URL', 'code': 'E_INVALID_URL'}), 400

    try:
        info = yt_dlp_extract(url)
    except yt_dlp.utils.DownloadError as e:
        return jsonify({'error': 'Failed to extract info: ' + str(e), 'code': 'E_YTDLP_FAIL'}), 502
    except Exception as e:
        return jsonify({'error': 'Unexpected error while extracting info', 'code': 'E_INTERNAL'}), 500

    # Normalize response
    formats = []
    for f in info.get('formats', []) or []:
        formats.append({
            'format_id': f.get('format_id'),
            'ext': f.get('ext'),
            'height': f.get('height'),
            'width': f.get('width'),
            'filesize': f.get('filesize'),
            'tbr': f.get('tbr'),
            'protocol': f.get('protocol'),
            # We avoid returning direct URLs in the peek response by default
            'has_url': 'url' in f and bool(f.get('url'))
        })

    out = {
        'id': info.get('id'),
        'title': info.get('title'),
        'uploader': info.get('uploader'),
        'duration': info.get('duration'),
        'thumbnails': info.get('thumbnails') or [],
        'formats': formats,
    }
    return jsonify(out)


@app.route('/api/download', methods=['GET'])
def api_download():
    # Query params: url, format_id (optional), mode=redirect|proxy
    url = request.args.get('url')
    format_id = request.args.get('format_id')
    mode = request.args.get('mode', 'redirect')

    if not url or not validate_url(url):
        return jsonify({'error': 'Missing or invalid "url" query parameter', 'code': 'E_INVALID_URL'}), 400
    if mode not in ('redirect', 'proxy'):
        return jsonify({'error': 'Invalid mode (must be "redirect" or "proxy")', 'code': 'E_INVALID_MODE'}), 400

    try:
        info = yt_dlp_extract(url)
    except yt_dlp.utils.DownloadError as e:
        return jsonify({'error': 'Failed to extract info: ' + str(e), 'code': 'E_YTDLP_FAIL'}), 502
    except Exception as e:
        return jsonify({'error': 'Unexpected error while extracting info', 'code': 'E_INTERNAL'}), 500

    # select format
    chosen = None
    formats = info.get('formats') or []
    if format_id:
        for f in formats:
            if f.get('format_id') == format_id:
                chosen = f
                break
    if not chosen:
        # fallback to best
        for f in reversed(formats):
            # prefer mp4/mkv with a direct url
            if f.get('url') and f.get('ext') in ('mp4', 'mkv'):
                chosen = f
                break
        if not chosen and formats:
            chosen = formats[-1]

    if not chosen or not chosen.get('url'):
        return jsonify({'error': 'No downloadable format URL found for this selection', 'code': 'E_NO_URL'}), 422

    direct_url = chosen.get('url')
    filename = sanitize_filename(info.get('title') or info.get('id')) + '.' + (chosen.get('ext') or 'bin')

    if mode == 'redirect':
        # Redirect client to the upstream direct URL
        return redirect(direct_url, code=302)

    # Proxy mode: stream the upstream response back to the client
    try:
        upstream = requests.get(direct_url, stream=True, timeout=10)
    except Exception as e:
        return jsonify({'error': 'Failed to fetch upstream media: ' + str(e), 'code': 'E_UPSTREAM_FAIL'}), 502

    def generate():
        bytes_sent = 0
        try:
            for chunk in upstream.iter_content(chunk_size=64 * 1024):
                if not chunk:
                    continue
                bytes_sent += len(chunk)
                if bytes_sent > PROXY_MAX_BYTES:
                    # Stop streaming if file too large
                    break
                yield chunk
        finally:
            try:
                upstream.close()
            except Exception:
                pass

    headers = {
        'Content-Disposition': f'attachment; filename="{filename}"'
    }
    content_type = upstream.headers.get('Content-Type', 'application/octet-stream')
    return Response(generate(), headers=headers, content_type=content_type)


if __name__ == '__main__':
    host = os.environ.get('HOST', '127.0.0.1')
    port = int(os.environ.get('PORT', '8080'))
    debug = os.environ.get('FLASK_DEBUG', '0') in ('1', 'true', 'True')
    app.run(host=host, port=port, debug=debug, use_reloader=False)
