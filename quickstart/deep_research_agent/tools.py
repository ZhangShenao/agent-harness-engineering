import os
from typing import Any, Literal

from dotenv import load_dotenv
from tavily import TavilyClient

load_dotenv()

_api_key = os.getenv("TAVILY_API_KEY")
if not _api_key:
    raise EnvironmentError("Missing required environment variable: TAVILY_API_KEY")

_tavily_client = TavilyClient(api_key=_api_key)


def internet_search(
    query: str,
    max_results: int = 5,
    topic: Literal["general", "news", "finance"] = "general",
    include_raw_content: bool = False,
) -> dict[str, Any]:
    """Run a web search"""
    return _tavily_client.search(
        query,
        max_results=max_results,
        include_raw_content=include_raw_content,
        topic=topic,
    )
