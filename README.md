# FastMCP Server Examples

This repository contains simple examples of FastMCP servers using different transport protocols: STDIO, SSE, and StreamableHTTP.

## Prerequisites

- Python 3.8+
- `uv` (recommended for environment management)

If you don't have `uv`, you can install it with:
```bash
pip install uv
```

## Setup

1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Create a virtual environment and install the dependencies:
   ```bash
   uv venv
   uv pip install -r requirements.txt
   ```
   If you are not using `uv`, you can use `venv` and `pip`:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```

## Running the Servers

You can run each server individually.

### STDIO Server

This is the default transport and is used by clients like Claude Desktop.

```bash
python stdio_server.py
```

### SSE Server (Legacy HTTP)

```bash
python sse_server.py
```
The server will be available at `http://127.0.0.1:8000/sse`.

### StreamableHTTP Server (Recommended HTTP)

```bash
python streamable_http_server.py
```
The server will be available at `http://127.0.0.1:8000/mcp/`.

## Testing with the Client

A client is provided to test the servers.

### Test STDIO Server

Make sure the STDIO server is **not** running in a separate terminal. The client will start it as a subprocess.

```bash
python client.py stdio
```

### Test SSE Server

Make sure the SSE server **is** running in a separate terminal.

```bash
python client.py sse
```

### Test StreamableHTTP Server

Make sure the StreamableHTTP server **is** running in a separate terminal.

```bash
python client.py http
