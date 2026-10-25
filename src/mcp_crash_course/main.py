import asyncio
import os

from dotenv import load_dotenv
from langchain_mcp_adapters.tools import load_mcp_tools
from langchain_openai import ChatOpenAI
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

load_dotenv()
llm = ChatOpenAI()
stdio_server_parameter = StdioServerParameters(
    command="python",
    args=["/Users/vikramadityamore/Desktop/Learning/Code/mcp/mcp-crash-course/src/mcp_crash_course/servers/math_server.py"]
)

async def main() -> None:
    print("Hello from mcp-crash-course!")


if __name__ == "__main__":
    asyncio.run(main())