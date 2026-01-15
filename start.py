#!/usr/bin/env python
"""Start the Flask app with a dynamically selected port."""

from app import app
import socket
import sys
import time

def find_free_port():
    """Find a free port to use."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('', 0))
        s.listen(1)
        port = s.getsockname()[1]
    return port

if __name__ == '__main__':
    port = find_free_port()
    host = '127.0.0.1'

    # Banner
    banner = """
╔════════════════════════════════════════════════════════════════╗
║                    🎬 VideoPeek                                ║
║              Video Extraction & Download Tool                  ║
╚════════════════════════════════════════════════════════════════╝

✨ Features:
  • Modern, smooth UI with gradient design
  • Multi-platform video support
  • High-quality format extraction
  • Direct link & proxy download options
  • Responsive design for all devices

📋 UI/UX Components:
  • Sticky navigation bar
  • Hero section with feature badges
  • Advanced video information display
  • Format-grouped download options
  • Professional footer with links

════════════════════════════════════════════════════════════════

🚀 Server Information:
"""

    print(banner)
    print(f"  Host:     {host}")
    print(f"  Port:     {port}")
    print(f"  URL:      http://{host}:{port}/")
    print(f"\n  📖 Design Guide: See DESIGN_GUIDE.md")
    print(f"  📚 API Docs:    See README.md")
    print(f"\n⌨️  Controls:")
    print(f"  • Enter video URL and click 'Extract Info'")
    print(f"  • Choose your preferred format and quality")
    print(f"  • Download directly or via server")
    print(f"\n⚠️  Press Ctrl+C to stop the server\n")
    print("════════════════════════════════════════════════════════════════\n")

    sys.stdout.flush()

    try:
        app.run(host=host, port=port, debug=True, use_reloader=False)
    except KeyboardInterrupt:
        print("\n\n✓ Server stopped gracefully")
        sys.exit(0)
    except Exception as e:
        print(f"\n✗ Error: {e}")
        sys.exit(1)
