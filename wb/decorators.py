import logging
from functools import wraps

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def log_request(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        handler = args[0]
        print(f"Function {func.__name__} called")
        print(f"Request from: {handler.client_address}")
        print(f"Request path: {handler.path}")
        return func(*args, **kwargs)
    return wrapper

def authorize_request(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        handler = args[0]
        print("Authorizing request...")
        # For testing, authorize all requests
        authorized = True  # Change this to your actual authorization logic
        if authorized:
            return func(*args, **kwargs)
        else:
            handler.send_response(403)
            handler.end_headers()
            return
    return wrapper
