def response_generator(handler, content):
    handler.send_response(200)
    handler.send_header("Content-type", "text/plain")
    handler.end_headers()
    yield bytes(content, "utf-8")

def streaming_response_generator(handler):
    handler.send_response(200)
    handler.send_header("Content-type", "text/plain")
    handler.end_headers()
    for i in range(10):
        yield bytes(f"Stream chunk {i}\n", "utf-8")