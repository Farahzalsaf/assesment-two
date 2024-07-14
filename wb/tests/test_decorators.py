import unittest
from aiohttp.test_utils import AioHTTPTestCase, unittest_run_loop # type: ignore
from aiohttp import web # type: ignore
from decorators import log_request, authorize_request

class TestDecorators(AioHTTPTestCase):

    async def get_application(self):
        app = web.Application()
        app.router.add_get('/', self.handle_get)
        return app

    @log_request
    @authorize_request
    async def handle_get(self, request):
        return web.Response(text="GET request authorized")

    @unittest_run_loop
    async def test_handle_get(self):
        request = await self.client.request("GET", "/")
        assert request.status == 200
        text = await request.text()
        assert "GET request authorized" in text

if __name__ == '__main__':
    unittest.main()
