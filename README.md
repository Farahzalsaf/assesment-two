<<<<<<< HEAD
# Webserver

## Overview

This project implements a basic web server for AI document summarization using Python's asyncio and aiohttp libraries. The server handles HTTP GET and POST requests and demonstrates the usage of advanced Python features such as decorators, generators, coroutines, and async iterators.

## Design Choices

### Structure

- **Separation of Concerns**: The project is divided into multiple modules, each handling a specific aspect of the server's functionality:
  - **`webserver.py`**: Main server setup and configuration.
  - **`singleton.py`**: Implements the Singleton pattern for the server instance.
  - **`iterators.py`**: Defines synchronous and asynchronous iterators.
  - **`inheratince.py`**: Defines request handlers using inheritance.
  - **`generators.py`**: Implements response generators.
  - **`decorators.py`**: Provides request logging and authorization decorators.
  - **`cntxtmngr.py`**: Implements a context manager for managing the server's lifecycle.
  - **`tests/`**: Directory containing unit tests for each module.

### Asynchronous Programming

- **Asyncio and aiohttp**: The server is built using `asyncio` and `aiohttp` to handle asynchronous HTTP requests efficiently. This allows the server to handle multiple requests concurrently without blocking.

### Context Management

- **ServerContextManager**: A custom context manager is implemented in `cntxtmngr.py` to manage the server's lifecycle, ensuring that resources are properly allocated and cleaned up.

### Testing

- **Unit Tests**: Comprehensive unit tests are provided in the `tests` directory. These tests cover different aspects of the server, including request handling, iterators, decorators, and context management.

# How to Run the Server

### Install Dependencies :
This project uses Poetry for dependency management.
run the following command to install the project dependencies:
```bash poetry install ["dependency name"]```

### Running the server: 

use this command to run the server: python3 -m webserver


## Dependencies

- **python**: `^3.10`
- **http-client**: `^0.1.22`
- **httpserver**: `^1.1.0`
- **asyncio**: `^3.4.3`
- **wraps**: `^0.13.0`
- **requests**: `^2.32.3`
- **aiohttp**: `^3.9.5`
- **aiohttp-test-utils**: `^0.5.0`
- **unittest**: Built-in Python module for writing and running tests.

### File Descriptions
## webserver.py
Contains the server configuration, including host and server definitions.
Starts the server using aiohttp's web.Application.
## singleton.py
Implements the Singleton pattern for the server instance to ensure only one instance of the server is running.
## iterators.py
Defines RequestIterator for synchronous iteration over requests.
Defines AsyncRequestIterator and async_request_handler for asynchronous iteration and handling of requests.
## inheratince.py
Defines BaseRequestHandler, GetRequestHandler, and PostRequestHandler classes.
Implements request handling logic for GET and POST requests.
## generators.py
Implements response generators for handling streaming responses.
## decorators.py
Provides log_request and authorize_request decorators for logging and authorizing requests.
## cntxtmngr.py
Defines ServerContextManager for managing the server's lifecycle.
Uses async context management methods to setup and cleanup the server.
## tests/
Contains unit tests for each module to ensure correct functionality.

### Example Usage

## GET
curl -X GET http://localhost:8080
Sending a POST Request
You can test the POST request handler by sending a request with data to the server using curl:

## POST

curl -X POST -d "Body content" http://localhost:8080
This will return an HTML response indicating that the POST request was received along with the data sent.





## For testing unit tests:
python3 -m unittest tests
=======
# Webserver

## Overview

This project implements a basic web server for AI document summarization using Python's asyncio and aiohttp libraries. The server handles HTTP GET and POST requests and demonstrates the usage of advanced Python features such as decorators, generators, coroutines, and async iterators.

## Design Choices

### Structure

- **Separation of Concerns**: The project is divided into multiple modules, each handling a specific aspect of the server's functionality:
  - **`webserver.py`**: Main server setup and configuration.
  - **`singleton.py`**: Implements the Singleton pattern for the server instance.
  - **`iterators.py`**: Defines synchronous and asynchronous iterators.
  - **`inheratince.py`**: Defines request handlers using inheritance.
  - **`generators.py`**: Implements response generators.
  - **`decorators.py`**: Provides request logging and authorization decorators.
  - **`cntxtmngr.py`**: Implements a context manager for managing the server's lifecycle.
  - **`tests/`**: Directory containing unit tests for each module.

### Asynchronous Programming

- **Asyncio and aiohttp**: The server is built using `asyncio` and `aiohttp` to handle asynchronous HTTP requests efficiently. This allows the server to handle multiple requests concurrently without blocking.

### Context Management

- **ServerContextManager**: A custom context manager is implemented in `cntxtmngr.py` to manage the server's lifecycle, ensuring that resources are properly allocated and cleaned up.

### Testing

- **Unit Tests**: Comprehensive unit tests are provided in the `tests` directory. These tests cover different aspects of the server, including request handling, iterators, decorators, and context management.

# How to Run the Server

### Install Dependencies :
This project uses Poetry for dependency management.
run the following command to install the project dependencies:
```bash poetry install ["dependency name"]```

### Running the server: 

use this command to run the server: python3 -m webserver


## Dependencies

- **python**: `^3.10`
- **http-client**: `^0.1.22`
- **httpserver**: `^1.1.0`
- **asyncio**: `^3.4.3`
- **wraps**: `^0.13.0`
- **requests**: `^2.32.3`
- **aiohttp**: `^3.9.5`
- **aiohttp-test-utils**: `^0.5.0`
- **unittest**: Built-in Python module for writing and running tests.

### File Descriptions
## webserver.py
Contains the server configuration, including host and server definitions.
Starts the server using aiohttp's web.Application.
## singleton.py
Implements the Singleton pattern for the server instance to ensure only one instance of the server is running.
## iterators.py
Defines RequestIterator for synchronous iteration over requests.
Defines AsyncRequestIterator and async_request_handler for asynchronous iteration and handling of requests.
## inheratince.py
Defines BaseRequestHandler, GetRequestHandler, and PostRequestHandler classes.
Implements request handling logic for GET and POST requests.
## generators.py
Implements response generators for handling streaming responses.
## decorators.py
Provides log_request and authorize_request decorators for logging and authorizing requests.
## cntxtmngr.py
Defines ServerContextManager for managing the server's lifecycle.
Uses async context management methods to setup and cleanup the server.
## tests/
Contains unit tests for each module to ensure correct functionality.

### Example Usage

## GET
curl -X GET http://localhost:8080
Sending a POST Request
You can test the POST request handler by sending a request with data to the server using curl:

## POST

curl -X POST -d "Body content" http://localhost:8080
This will return an HTML response indicating that the POST request was received along with the data sent.





## For testing unit tests:
python3 -m unittest tests

