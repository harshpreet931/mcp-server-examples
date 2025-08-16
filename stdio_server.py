from fastmcp import FastMCP

# Create a FastMCP server instance
mcp = FastMCP(name="StdioExampleServer")

@mcp.tool
def echo(message: str) -> str:
    """Echoes the provided message back to the client."""
    return f"You said: {message}"

if __name__ == "__main__":
    # Run the server with the default STDIO transport
    mcp.run()
