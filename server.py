
from mcp.server.mcpserver import MCPServer

from pathlib import Path


mcp = MCPServer("Krishna-MCP")


@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers and return the result."""
    return a + b


@mcp.tool()
def multiply(a: int, b: int) -> int:
    """Multiply two numbers and return the result."""
    return a * b



@mcp.tool()
def subtract(a: int, b: int) -> int:
    """Subtract the second number from the first."""
    return a - b


@mcp.tool()
def divide(a: float, b: float) -> float:
    """Divide the first number by the second."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b



@mcp.tool()
def read_notes() -> str:
    """Read the contents of the MCP learning notes file."""
    file_path = Path(__file__).parent / "notes.txt"

    if not file_path.exists():
        raise FileNotFoundError("notes.txt was not found.")

    return file_path.read_text(encoding="utf-8")



@mcp.resource("learning://roadmap")
def learning_roadmap() -> str:
    """Provide Krishna's MCP learning roadmap."""
    return """
    MCP Learning Roadmap

    1. Build an MCP server
    2. Create calculator tools
    3. Read project files
    4. Connect an MCP client
    5. Learn resources and prompts
    6. Build an AI agent
    """



@mcp.prompt()
def explain_mcp(topic: str) -> str:
    """Create a beginner-friendly prompt to explain an MCP topic."""
    return (
        f"Explain {topic} in simple Hinglish. "
        "Use a real-world example and explain it step by step."
    )




if __name__ == "__main__":
    mcp.run()

# 
# uv run mcp dev server.py
