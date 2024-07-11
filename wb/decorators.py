from functools import wraps

# Decorator to log requests
def log_request(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        print(f"Function {func.__name__} called")
        print(f"Request from: {self.client_address}")
        print(f"Request path: {self.path}")
        result = func(self, *args, **kwargs)
        print(f"Function {func.__name__} executed")
        return result
    return wrapper

# Decorator to authorize requests
def authorize_request(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        print("Authorizing request...")
        authorized = False  # Toggle this value to simulate authorization
        if authorized:
            return func(self, *args, **kwargs)
        else:
            self.send_response(403)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b"<html><body><h1>403 Forbidden</h1><p>You are not authorized to access this page.</p></body></html>")
            print("Unauthorized request")
            return
    return wrapper
