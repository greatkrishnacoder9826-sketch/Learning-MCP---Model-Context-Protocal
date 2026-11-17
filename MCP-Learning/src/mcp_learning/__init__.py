from mcp.server.mcpserver import MCPServer

mcp = MCPServer("Krishna-MCP")


@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers and return the result."""
    return a + b


def main() -> None:
    mcp.run()
