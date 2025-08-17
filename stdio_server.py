from fastmcp import FastMCP

# Create a FastMCP server instance
mcp = FastMCP(name="StdioExampleServer")

@mcp.tool
def echo(message: str) -> str:
    """Echoes the provided message back to the client."""
    return f"You said: {message}"

@mcp.tool
def api_fetch(url: str) -> str: 
    """Fetches data from the provided URL."""
    import requests
    response = requests.get(url)
    return response.text if response.status_code == 200 else f"Error fetching {url}: {response.status_code}"

if __name__ == "__main__":
    # Run the server with the default STDIO transport
    mcp.run()
