from abc import ABC, abstractmethod

class BaseRequestHandler(ABC):
    @abstractmethod
    def handle_request(self, handler):
        pass

class GetRequestHandler(BaseRequestHandler):
    def handle_request(self, handler):
        handler.send_response(200)
        handler.send_header("Content-type", "text/html")
        handler.end_headers()
        handler.wfile.write(bytes("<html><head><title>GET Request</title></head>", "utf-8"))
        handler.wfile.write(bytes("<p>This is a GET request.</p>", "utf-8"))
        handler.wfile.write(bytes("</body></html>", "utf-8"))

class PostRequestHandler(BaseRequestHandler):
    def handle_request(self, handler):
        handler.send_response(200)
        handler.send_header("Content-type", "text/html")
        handler.end_headers()
        handler.wfile.write(bytes("<html><head><title>POST Request</title></head>", "utf-8"))
        handler.wfile.write(bytes("<p>This is a POST request.</p>", "utf-8"))
        handler.wfile.write(bytes("</body></html>", "utf-8"))
