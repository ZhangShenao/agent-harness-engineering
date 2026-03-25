import os
from typing import Any


# 定义工具
def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"{city} 天气晴朗，阳光明媚，气温适宜，适合出行。"


def extract_final_result_text(result: dict[str, Any]) -> str:
    """Extract the final assistant text from the DeepAgent result."""
    messages = result.get("messages", [])
    if not messages:
        return str(result)

    final_message = messages[-1]
    content = getattr(final_message, "content", final_message)

    if isinstance(content, str):
        return content

    return str(content)


def main() -> None:
    from deepagents import create_deep_agent
    from dotenv import load_dotenv
    from langchain_openai import ChatOpenAI

    # 加载环境变量
    load_dotenv()

    # 创建LLM
    llm = ChatOpenAI(
        model=os.getenv("OPENAI_MODEL"),
        api_key=os.getenv("OPENAI_API_KEY"),
        base_url=os.getenv("OPENAI_BASE_URL"),
    )

    # 创建DeepAgent
    agent = create_deep_agent(
        model=llm,  # 指定LLM模型
        tools=[get_weather],  # 绑定工具
        system_prompt="你是一位全能的AI助手",  # 设置System Prompt
    )

    # 运行Agent，仅打印最终回答文本
    result = agent.invoke(
        {"messages": [{"role": "user", "content": "北京的天气怎么样？"}]}
    )
    print(extract_final_result_text(result))


if __name__ == "__main__":
    main()
