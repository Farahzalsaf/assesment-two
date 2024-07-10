from http.server import BaseHTTPRequestHandler, HTTPServer
import asyncio
from singleton import SingletonMeta
from cntxtmngr import ServerContextManager
from decorators import log_request, authorize_request
from generators import streaming_response_generator
from inheratince import GetRequestHandler, PostRequestHandler
from iterators import RequestIterator

hostName = "localhost"
serverPort = 8080

class MyServer(BaseHTTPRequestHandler, metaclass=SingletonMeta):
    @log_request
    @authorize_request
    def do_GET(self):
        if self.path == "/stream":
            for chunk in streaming_response_generator(self):
                self.wfile.write(chunk)
        else:
            handler = GetRequestHandler()
            handler.handle_request(self)

    @log_request
    @authorize_request
    def do_POST(self):
        handler = PostRequestHandler()
        handler.handle_request(self)

async def async_request_handler(handler):
    await asyncio.sleep(2)  # Simulating asynchronous processing
    iterator = RequestIterator([f"Request {i}" for i in range(5)])
    async for request in async_iterator(iterator):
        print(request)
        handler.wfile.write(bytes(request, "utf-8"))

async def async_iterator(iterator):
    for item in iterator:
        yield item

if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print(f"Server started http://{hostName}:{serverPort}")

    # Using the context manager to manage server resources
    with ServerContextManager(webServer):
        try:
            asyncio.run(async_request_handler(MyServer))
            webServer.serve_forever()
        except KeyboardInterrupt:
            pass

    print("Server stopped.")
