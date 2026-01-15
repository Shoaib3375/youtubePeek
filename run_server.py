#!/usr/bin/env python
"""Run Flask app with Waitress WSGI server for Windows compatibility."""

from app import app
from waitress import serve
import os

if __name__ == '__main__':
    host = os.environ.get('HOST', '127.0.0.1')
    port = int(os.environ.get('PORT', '5000'))
    print(f"Starting server on {host}:{port}...")
    try:
        serve(app, host=host, port=port)
    except PermissionError:
        print(f"Port {port} access denied, trying Flask development server...")
        app.run(host=host, port=port, debug=True)
