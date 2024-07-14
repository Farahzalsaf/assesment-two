from functools import wraps
from aiohttp import web #type:ignore

def log_request(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        request = args[1]
        print(f"Function {func.__name__} called")
        print(f"Request from: {request.remote}")
        print(f"Request path: {request.path}")
        result = await func(*args, **kwargs)
        print(f"Function {func.__name__} executed")
        return result
    return wrapper

def authorize_request(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        request = args[1]
        print("Authorizing request...")
        authorized = True  # Toggle this value to simulate authorization
        if authorized:
            return await func(*args, **kwargs)
        else:
            return web.Response(text="<html><body><h1>403 Forbidden</h1><p>You are not authorized to access this page.</p></body></html>", content_type='text/html', status=403)
    return wrapper
