import logging
from functools import wraps

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

"""def log_request(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Received request: {args[1].path}")
        return func(*args, **kwargs)
    return wrapper

def authorize_request(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if kwargs.get('authorized', False):
            return func(*args, **kwargs)
        else:
            raise PermissionError("Request not authorized")
    return wrapper"""

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
        authorized = False  # Simulate authorization check
        if authorized:
            return func(self, *args, **kwargs)
        else:
            self.send_response(403)
            self.end_headers()
            return
    return wrapper

