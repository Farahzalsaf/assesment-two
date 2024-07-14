import unittest
from aiohttp import web
from cntxtmngr import ServerContextManager

class TestContextManager(unittest.IsolatedAsyncioTestCase):
    async def test_server_context_manager(self):
        app = web.Application()
        runner = web.AppRunner(app)
        async with ServerContextManager(runner) as manager:
            self.assertIsNotNone(manager)

if __name__ == '__main__':
    unittest.main()
