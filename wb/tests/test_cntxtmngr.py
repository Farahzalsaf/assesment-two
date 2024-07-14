# cntxtmngr.py
from webserver import host, server
from aiohttp import web #type: ignore

class ServerContextManager:
    def __init__(self, runner: web.AppRunner):
        self.runner = runner

    async def __aenter__(self):
        await self.runner.setup()
        self.site = web.TCPSite(self.runner, host, server)
        await self.site.start()
        print("Starting server...")
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.site.stop()
        await self.runner.cleanup()
        print("Stopping server...")
