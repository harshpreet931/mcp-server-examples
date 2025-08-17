# MCP Server Examples

A collection of plug-and-play server examples for the [Model Context Protocol (MCP)](https://modelcontextprotocol.io/), built with the powerful [FastMCP](https://gofastmcp.com/) framework. Whether you're building for Claude, Gemini, or any other MCP-compatible client, this repo gives you the foundation you need.

![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
[![GitHub stars](https://img.shields.io/github/stars/harshpreet931/mcp-server-examples.svg?style=social&label=Star)](https://github.com/harshpreet931/mcp-server-examples)

---

## Why This Repo?

This repository is designed to be the fastest way to get started with building your own MCP servers. It provides clear, minimal, and working examples for the three main transport protocols, allowing you to:

- **Learn by Example:** Understand the differences between STDIO, SSE, and StreamableHTTP transports.
- **Bootstrap Your Projects:** Use these examples as a starting point for your own custom tools and resources.
- **Test Your Clients:** Quickly spin up a server to test how your MCP client application behaves.

## Features

- **STDIO Server:** The standard for local clients like Claude Desktop.
- **SSE Server:** A legacy HTTP-based transport for older clients.
- **StreamableHTTP Server:** The modern, recommended HTTP transport for web-accessible servers.
- **Simple `echo` Tool:** A basic tool in each server to verify connectivity.
- **Ready-to-use Client:** A test client to interact with all server types.

## Getting Started

### Prerequisites

- Python 3.8+
- `uv` (recommended for environment management). Install with `pip install uv`.

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/harshpreet931/mcp-server-examples.git
    cd mcp-server-examples
    ```

2.  **Set up the environment:**
    ```bash
    # Create a virtual environment
    uv venv

    # Install dependencies
    uv pip install -r requirements.txt
    ```
    (If not using `uv`, use `python -m venv venv` and `pip install -r requirements.txt`).

## How to Run the Examples

You can run each server individually from your terminal.

### 1. STDIO Server

Ideal for local development and clients like Claude Desktop.

```bash
python stdio_server.py
```

### 2. SSE Server (Legacy HTTP)

Runs a web server on port 8000.

```bash
python sse_server.py
```
*Server will be available at `http://127.0.0.1:8000/sse`*

### 3. StreamableHTTP Server (Modern HTTP)

The recommended way to expose your MCP server over the web.

```bash
python streamable_http_server.py
```
*Server will be available at `http://127.0.0.1:8000/mcp/`*

## Testing the Servers

Use the included client to test each server.

-   **To test the STDIO server:** (ensure it's *not* running)
    ```bash
    python client.py stdio
    ```
-   **To test the SSE server:** (ensure it *is* running)
    ```bash
    python client.py sse
    ```
-   **To test the StreamableHTTP server:** (ensure it *is* running)
    ```bash
    python client.py http
    ```

## Contributing

Contributions are welcome! If you have an idea for a new example, a bug fix, or an improvement, please open an issue or submit a pull request.

1.  Fork the repository.
2.  Create a new branch (`git checkout -b feature/your-feature-name`).
3.  Make your changes.
4.  Commit your changes (`git commit -m 'Add some feature'`).
5.  Push to the branch (`git push origin feature/your-feature-name`).
6.  Open a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
