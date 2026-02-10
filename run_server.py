#!/usr/bin/env python3
"""
Simple local static file server for the project.

Usage:
  python3 run_server.py --port 8000

From the host machine you can open the site with:
  "$BROWSER" http://localhost:8000

This script intentionally avoids opening the browser automatically so the host
user can choose how to open the forwarded port from their environment.
"""
import argparse
import http.server
import socketserver
import os


def main():
    parser = argparse.ArgumentParser(description='Serve current directory over HTTP')
    parser.add_argument('--port', type=int, default=8000, help='Port to serve on')
    args = parser.parse_args()
    port = args.port

    web_dir = os.getcwd()
    handler_class = lambda *p, directory=web_dir, **kw: http.server.SimpleHTTPRequestHandler(*p, directory=directory, **kw)

    with socketserver.TCPServer(("", port), handler_class) as httpd:
        print(f"Serving {web_dir}")
        print(f"Open in host browser with: \"$BROWSER\" http://localhost:{port}")
        print("Press Ctrl+C to stop")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print('\nServer stopped')


if __name__ == '__main__':
    main()
