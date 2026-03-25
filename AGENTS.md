# AGENTS

## 项目定位

这个仓库是一个围绕 `Agent Harness Engineering` 的实战，用来探索如何把模型放进可持续工作的工程系统中。


## 开发环境

- Python：`>=3.12`
- 推荐包管理器：`uv`
- 建议使用本地 `.env` 管理环境变量

运行 `quickstart/deep_agent_quickstart.py` 前，至少需要配置以下环境变量：

- `OPENAI_MODEL`：要调用的模型名
- `OPENAI_API_KEY`：模型服务的 API Key
- `OPENAI_BASE_URL`：模型服务的 Base URL

不要提交 `.env`、`__pycache__/`、`.pyc` 等本地产物。

## 常用命令

安装依赖：

```bash
uv sync
```

运行 quickstart 示例：

```bash
uv run python quickstart/deep_agent_quickstart.py
```

如果未配置上面的环境变量，示例中的 `ChatOpenAI(...)` 初始化会失败。

运行测试：

```bash
uv run python -m unittest discover -s tests -p 'test_*.py'
```


## 协作约定

- 默认使用中文输出，保持术语准确。
- 优先做小步修改，避免一次性引入大量无验证的结构调整。
- 完成改动前至少运行一次相关测试或验证命令。
- 若新增依赖，必须同步更新 `pyproject.toml` 与 `uv.lock`。

## CI 说明

仓库使用 GitHub Actions 执行基础 CI。当前 CI 目标只有一项：

- 安装依赖
- 运行 `unittest`

当前不包含 CD、发布或部署流程。如果以后增加发布动作，应单独新增 workflow，而不是把发布逻辑混入现有 CI。

## 开发纪律（必读）

在编写或修改调用 **LangChain、LangGraph、DeepAgents、LangSmith、** 等相关代码前：

1. 使用 **Context7 MCP**（`user-context7` → `query-docs`）查询**当前版本**的官方 API 与示例。
2. 若未知 library id，先通过 Context7 的 **Resolve Library ID** 流程得到 `/org/project` 或带版本的形式，再发起 `query-docs`。
