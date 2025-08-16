from fastmcp import FastMCP

# Create a FastMCP server instance
mcp = FastMCP(name="SseExampleServer")

@mcp.tool
def echo(message: str) -> str:
    """Echoes the provided message back to the client."""
    return f"You said via SSE: {message}"

if __name__ == "__main__":
    # Run the server with SSE transport
    mcp.run(transport="sse", host="127.0.0.1", port=8000)
