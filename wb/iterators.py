import asyncio
class RequestIterator:
    def __init__(self, requests):
        self.requests = requests
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.requests):
            result = self.requests[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration


#async iterators
async def async_request_handler(requests):
    for request in requests:
        await asyncio.sleep(1)
        print(f"Handled request: {request}")

class AsyncRequestIterator:
    def __init__(self, requests):
        self.requests = requests

    def __aiter__(self):
        self.index = 0
        return self

    async def __anext__(self):
        if self.index < len(self.requests):
            result = self.requests[self.index]
            self.index += 1
            await asyncio.sleep(1)
            return result
        else:
            raise StopAsyncIteration