from aiohttp import web #type: ignore
from webserver import host, server

class ServerContextManager:
    def __init__(self, runner):
        self.runner = runner

    async def __aenter__(self):
        await self.runner.setup()
        self.site = web.TCPSite(self.runner, host, server)
        await self.site.start()
        print("Starting server...")
        return self

    async def __aexit__(self, exc_type, exc_value, traceback):
        await self.site.stop()
        await self.runner.cleanup()
        print("Stopping server...")