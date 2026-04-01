import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

_required_vars = ["OPENAI_MODEL", "OPENAI_API_KEY", "OPENAI_BASE_URL"]
_missing = [v for v in _required_vars if not os.getenv(v)]
if _missing:
    raise EnvironmentError(
        f"Missing required environment variables: {', '.join(_missing)}"
    )

llm = ChatOpenAI(
    model=os.getenv("OPENAI_MODEL"),
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_BASE_URL"),
)
