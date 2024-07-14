from abc import ABC, abstractmethod
from http.server import BaseHTTPRequestHandler

class BaseRequestHandler(ABC):
    @abstractmethod
    def handle_request(self, handler):
        pass

class GetRequestHandler(BaseRequestHandler):
    def handle_request(self, handler: BaseHTTPRequestHandler):
        handler.send_response(200)
        handler.send_header("Content-type", "text/html")
        handler.end_headers()
        handler.wfile.write(bytes("<html><head><title>GET Request</title></head></html>", "utf-8"))
        handler.wfile.write(bytes("<p>This is a GET request.</p>", "utf-8"))

class PostRequestHandler(BaseRequestHandler):
    def handle_request(self, handler: BaseHTTPRequestHandler):
        content_length = int(handler.headers['Content-Length'])
        post_data = handler.rfile.read(content_length)

        handler.send_response(200)
        handler.send_header("Content-type", "text/html")
        handler.end_headers()
        handler.wfile.write(bytes("<html><head><title>POST Request</title></head></html>", "utf-8"))
        handler.wfile.write(bytes("<p>This is a POST request.</p>", "utf-8"))
        handler.wfile.write(bytes(f"<p>Received: {post_data.decode('utf-8')}</p>", "utf-8"))
