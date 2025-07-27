from fastmcp import FastMCP
from dotenv import load_dotenv
from starlette.middleware.cors import CORSMiddleware

load_dotenv()

mcp = FastMCP(name="Notes App")

@mcp.tool()
def get_notes() -> str:
    """Get all notes from user"""
    return "No notes"

@mcp.tool()  # Added missing decorator
def add_notes(content: str) -> str:
    """Add notes to user"""
    return f"Added note: {content}"

"""
if __name__ == "__main__":
    mcp.run(
        transport="http",
        host="127.0.0.1",
        port=8000,
        middleware=[
            (CORSMiddleware, [], {
                "allow_origins": ["*"],
                "allow_credentials": True,
                "allow_methods": ["*"],
                "allow_headers": ["*"]
            })
        ]
    )
    
  """
if __name__ == "__main__":
    mcp.run(transport="stdio")  # Sin middleware, sin host, sin port