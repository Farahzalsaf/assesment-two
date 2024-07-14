import asyncio
from aiohttp import web  # type: ignore
from singleton import SingletonMeta
from decorators import log_request, authorize_request
from iterators import async_request_handler
host = "localhost"
server = 8080
class MyServer(metaclass=SingletonMeta):
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.app = web.Application()
        self.app.router.add_get('/', self.handle_get)
        self.app.router.add_post('/', self.handle_post)

    @log_request
    @authorize_request
    async def handle_get(self, request):
        return web.Response(text="<html><head><title>GET Request</title></head><body><p>This is a GET request.</p></body></html>", content_type='text/html')

    @log_request
    @authorize_request
    async def handle_post(self, request):
        try:
            post_data = await request.post()
            await async_request_handler([str(post_data)])
            response_text = f"<html><head><title>POST Request</title></head><body><p>This is a POST request.</p><p>Received: {post_data}</p></body></html>"
            return web.Response(text=response_text, content_type='text/html')
        except Exception as e:
            return web.Response(text="<html><body><h1>500 Internal Server Error</h1></body></html>", content_type='text/html', status=500)

    def run(self):
        web.run_app(self.app, host=self.host, port=self.port)

if __name__ == "__main__":
    server = MyServer("localhost", 8080)
    server.run()
