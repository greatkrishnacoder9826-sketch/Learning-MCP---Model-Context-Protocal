
from mcp.server.mcpserver import MCPServer

mcp = MCPServer("Krishna-MCP")


@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers and return the result."""
    return a + b


if __name__ == "__main__":
    mcp.run()

# 
# uv run mcp dev server.py
