import unittest
from aiohttp.test_utils import AioHTTPTestCase, unittest_run_loop # type: ignore
from aiohttp import web # type: ignore
from webserver import MyServer, handle_get, handle_post

class TestWebServer(AioHTTPTestCase):

    async def get_application(self):
        server = MyServer()
        return server.app

    @unittest_run_loop
    async def test_handle_get(self):
        request = await self.client.request("GET", "/")
        assert request.status == 200
        text = await request.text()
        assert "This is a GET request." in text

    @unittest_run_loop
    async def test_handle_post(self):
        data = {"key": "value"}
        request = await self.client.request("POST", "/", data=data)
        assert request.status == 200
        text = await request.text()
        assert "This is a POST request." in text
        assert "Received: " in text

if __name__ == '__main__':
    unittest.main()
