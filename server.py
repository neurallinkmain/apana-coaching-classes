#!/usr/bin/env python3
import http.server
import socketserver
import socket
import os

PORT = 8000

# Get local IP address
def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        return "127.0.0.1"

# Change to the directory where the script is located
os.chdir(os.path.dirname(os.path.abspath(__file__)))

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()

# Start the server
with socketserver.TCPServer(("0.0.0.0", PORT), MyHTTPRequestHandler) as httpd:
    local_ip = get_local_ip()
    print("=" * 60)
    print("🌐  APANA COACHING CLASSES - WEB SERVER".center(60))
    print("=" * 60)
    print(f"\n✅ Server is running!")
    print(f"\n📱 Access URLs:")
    print(f"   • Local:   http://localhost:{PORT}")
    print(f"   • Network: http://{local_ip}:{PORT}")
    print(f"\n📂 Serving files from: {os.getcwd()}")
    print(f"\n⏹️  Press Ctrl+C to stop the server")
    print("\n" + "=" * 60)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n\n🛑 Server stopped successfully!")
