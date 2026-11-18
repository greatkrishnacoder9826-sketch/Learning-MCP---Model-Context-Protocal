
import asyncio
from mcp import Client


async def main():
    async with Client("http://localhost:8000/mcp") as client:

        # Discover available tools
        tools = await client.list_tools()

        print("Available MCP tools:")
        for tool in tools.tools:
            print("-", tool.name)

        # Call the add tool
        result = await client.call_tool(
            "add",
            {"a": 85, "b": 35}
        )

        print("\nAddition result:")
        print(result.structured_content)


if __name__ == "__main__":
    asyncio.run(main())
