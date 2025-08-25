from fastmcp import FastMCP

# Create a FastMCP server instance
mcp = FastMCP(name="StreamableHttpExampleServer")

@mcp.tool
def echo(message: str) -> str:
    """Echoes the provided message back to the client."""
    return f"You said via StreamableHTTP: {message}"

@mcp.tool
def api_fetch(url: str) -> str: 
    """Fetches data from the provided URL."""
    import requests
    response = requests.get(url)
    return response.text if response.status_code == 200 else f"Error fetching {url}: {response.status_code}"

@mcp.tool
def add(a: int, b: int) -> int:
    """Adds two numbers."""
    return a + b

if __name__ == "__main__":
    # Run the server with StreamableHTTP transport
    mcp.run(transport="http", host="127.0.0.1", port=8000)
