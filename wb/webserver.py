from http.server import BaseHTTPRequestHandler, HTTPServer
from singleton import SingletonMeta
from cntxtmngr import ServerContextManager
from decorators import log_request, authorize_request

hostName = "localhost"
serverPort = 8080

class MyServer(BaseHTTPRequestHandler, metaclass=SingletonMeta):
    @log_request
    @authorize_request
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>GET Request</title></head>", "utf-8"))
        self.wfile.write(bytes("<p>This is a GET request.</p>", "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))

    @log_request
    @authorize_request
    def do_POST(self):
        print("POST request received")
        content_length = int(self.headers['Content-Length'])  # Get the size of the data
        post_data = self.rfile.read(content_length)  # Read the data
        print(f"Received data: {post_data}")  # Debugging statement

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>POST Request</title></head>", "utf-8"))
        self.wfile.write(bytes("<p>This is a POST request.</p>", "utf-8"))
        self.wfile.write(bytes(f"<p>Received: {post_data}</p>", "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))

if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print(f"Server started http://{hostName}:{serverPort}")

    # Using the context manager to manage server resources
    with ServerContextManager(webServer):
        try:
            webServer.serve_forever()
        except KeyboardInterrupt:
            pass

    print("Server stopped.")
