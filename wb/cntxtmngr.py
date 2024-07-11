class ServerContextManager:
    def __init__(self, server):
        self.server = server

    def __enter__(self):
        print("Starting server...")
        return self.server

    def __exit__(self, exc_type, exc_value, traceback):
        print("Stopping server...")
        self.server.server_close()
