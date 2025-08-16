from fastmcp import FastMCP

# Create a FastMCP server instance
mcp = FastMCP(name="StreamableHttpExampleServer")

@mcp.tool
def echo(message: str) -> str:
    """Echoes the provided message back to the client."""
    return f"You said via StreamableHTTP: {message}"

if __name__ == "__main__":
    # Run the server with StreamableHTTP transport
    mcp.run(transport="http", host="127.0.0.1", port=8000)
