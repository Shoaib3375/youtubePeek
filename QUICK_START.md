# Installation & Quick Start Guide

## System Requirements

- Python 3.8+
- pip (Python package manager)
- Modern web browser (Chrome, Firefox, Safari, Edge)
- Internet connection for video extraction

## Installation Steps

### 1. Clone or Download the Project
```bash
cd E:\ML\FlaskProject
```

### 2. Create Virtual Environment (Recommended)
```bash
# Create virtual environment
python -m venv .venv

# Activate virtual environment
# On Windows:
.venv\Scripts\activate

# On macOS/Linux:
source .venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

## Running the Application

### Quick Start (Recommended)
```bash
python start.py
```

This will:
- ✓ Find an available port automatically
- ✓ Display server information
- ✓ Show the access URL in terminal
- ✓ Auto-reload on code changes

### Alternative: Direct Flask Run
```bash
python app.py
```

### Using Waitress WSGI Server
```bash
python run_server.py
```

## Accessing the Application

Once started, open your browser to the URL shown in terminal:
```
http://127.0.0.1:PORT/
```

Example:
```
http://127.0.0.1:5000/
```

## First Use

1. **Enter a Video URL**
   - Copy and paste any video URL
   - Supported: YouTube, Vimeo, TikTok, Instagram, and 1000+ other platforms

2. **Click "Extract Info"**
   - Wait for the extraction process (usually 2-5 seconds)
   - Server will fetch video metadata

3. **View Available Formats**
   - Video formats grouped by quality
   - Audio formats with bitrate
   - File sizes displayed

4. **Choose Download Method**
   - **Direct Link**: Redirects to original source
   - **Via Server**: Downloads through our server (up to 200MB)

5. **Download Your Video**
   - Click either button
   - Browser handles the download automatically

## File Structure

```
FlaskProject/
├── app.py                 # Flask application & API endpoints
├── start.py              # Simple startup script (recommended)
├── run_server.py         # Waitress WSGI server runner
├── requirements.txt      # Python dependencies
├── README.md             # Project documentation
├── DESIGN_GUIDE.md       # UI/UX design specifications
├── UI_FEATURES.md        # Detailed feature documentation
├── QUICK_START.md        # This file
├── templates/
│   └── index.html        # Main web interface
├── static/               # Static assets (CSS, JS images)
└── __pycache__/          # Python cache files
```

## API Reference

### POST /api/peek
Extract video metadata

**Request:**
```bash
curl -X POST http://localhost:5000/api/peek \
  -H "Content-Type: application/json" \
  -d '{"url": "https://example.com/video"}'
```

**Response:**
```json
{
  "id": "video_id",
  "title": "Video Title",
  "uploader": "Channel Name",
  "duration": 1234,
  "thumbnails": [
    {"url": "https://...", "width": 120, "height": 90}
  ],
  "formats": [
    {
      "format_id": "22",
      "ext": "mp4",
      "height": 720,
      "width": 1280,
      "filesize": 52428800,
      "protocol": "https"
    }
  ]
}
```

### GET /api/download
Download or redirect to video

**Parameters:**
- `url` (required): Video URL
- `format_id` (optional): Specific format
- `mode` (optional): "redirect" or "proxy"

**Example:**
```
http://localhost:5000/api/download?url=...&format_id=22&mode=proxy
```

## Troubleshooting

### Port Already in Use
**Error:** `Address already in use`
**Solution:** 
- `start.py` automatically finds a free port
- Or manually: set PORT environment variable
  ```bash
  set PORT=8000
  python run_server.py
  ```

### Video Extraction Fails
**Error:** `Failed to extract info`
**Possible Causes:**
- Video is private or removed
- Platform not supported
- Network connectivity issue
**Solution:**
- Try different video
- Check internet connection
- Wait and retry

### Can't Access from Mobile
**Error:** Cannot reach `http://127.0.0.1:PORT`
**Solution:**
- Get your computer's local IP: `ipconfig` (Windows)
- Access from: `http://YOUR_IP:PORT`
- Example: `http://192.168.1.100:5000`

### Import Errors
**Error:** `ModuleNotFoundError: No module named 'yt_dlp'`
**Solution:** Reinstall dependencies
```bash
pip install -r requirements.txt
```

### Server Crashes
**Error:** Unexpected crash or hang
**Solution:**
1. Stop the server (Ctrl+C)
2. Check error message in terminal
3. Verify dependencies: `pip check`
4. Restart server: `python start.py`

## Configuration

Edit `app.py` to customize:

```python
# Maximum file size for proxy downloads
PROXY_MAX_BYTES = 200 * 1024 * 1024  # 200 MB

# Timeout for video info extraction
YTDLP_TIMEOUT = 15  # seconds

# Allowed URL schemes
ALLOWED_SCHEMES = ("http", "https")
```

## Performance Tips

1. **Use Direct Link Mode**
   - Saves server bandwidth
   - Faster for user (direct to source)

2. **Proxy for Blocked Sites**
   - When direct linking fails
   - Limited to 200MB

3. **First Extraction Slower**
   - yt-dlp caches info
   - Subsequent calls faster

## Security Notes

- ✓ No data stored on server
- ✓ URLs not logged
- ✓ Only video metadata extracted
- ✓ HTTPS supported for all sources
- ⚠️ Respect content copyright
- ⚠️ Follow platform terms of service

## Updating yt-dlp

yt-dlp updates regularly to support new platforms:

```bash
pip install --upgrade yt-dlp
```

## Getting Help

### Check Documentation
- README.md - Overview & API docs
- DESIGN_GUIDE.md - UI/UX specifications
- UI_FEATURES.md - Feature details

### Debug Mode
Enable more verbose output:
```python
# In app.py, uncomment:
# app.run(host=host, port=port, debug=True)
```

### Common Issues
Most issues are due to:
1. Network connectivity
2. Outdated yt-dlp
3. Platform changes
4. Video restrictions

## Next Steps

1. **Try Different Videos**
   - YouTube, Vimeo, Instagram
   - Different resolutions available

2. **Customize Appearance**
   - Edit `templates/index.html`
   - Modify colors in `<style>` section

3. **Add Features**
   - Batch downloads
   - Playlist support
   - Custom formats

4. **Deploy Online**
   - Use Heroku, PythonAnywhere, etc.
   - Set proper environment variables
   - Use production WSGI server

## Support

For issues or questions:
1. Check this guide first
2. Review error messages carefully
3. Check terminal output for details
4. Verify dependencies are installed

---

**Happy downloading!** 🎬

Last updated: January 16, 2026
