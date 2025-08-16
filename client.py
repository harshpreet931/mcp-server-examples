import asyncio
from fastmcp import Client
from cyclopts import App

app = App()

async def run_test(client: Client):
    """Connects to the server, calls the echo tool, and prints the result."""
    async with client:
        print(f"Pinging {client.transport}...")
        await client.ping()
        print("Ping successful!")
        
        result = await client.call_tool("echo", {"message": "Hello, MCP!"})
        print(f"Server response: {result.data}")

@app.command
def stdio():
    """Test the STDIO server."""
    client = Client("stdio_server.py")
    asyncio.run(run_test(client))

@app.command
def sse():
    """Test the SSE server."""
    client = Client("http://127.0.0.1:8000/sse")
    asyncio.run(run_test(client))

@app.command
def http():
    """Test the StreamableHTTP server."""
    client = Client("http://127.0.0.1:8000/mcp/")
    asyncio.run(run_test(client))

if __name__ == "__main__":
    app()
