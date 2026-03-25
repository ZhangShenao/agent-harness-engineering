# AGENTS And CI Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 为当前仓库补充基于现有 README 和代码事实的 `AGENTS.md`，并新增仅包含 CI 的 GitHub Actions 工作流。

**Architecture:** 文档层面新增一个仓库级 `AGENTS.md`，说明项目目标、目录结构、环境变量、运行与测试方式、协作约束。自动化层面新增一个轻量 `ci.yml`，使用 `uv` 与 Python 3.12 安装依赖并执行现有 `unittest` 测试，保持与仓库当前工具链一致。

**Tech Stack:** Python 3.12, uv, unittest, GitHub Actions

---

### Task 1: Add Repository Agent Guide

**Files:**
- Create: `AGENTS.md`
- Reference: `README.md`
- Reference: `pyproject.toml`
- Reference: `quickstart/deep_agent_quickstart.py`
- Reference: `tests/test_deep_agent_quickstart.py`

- [ ] **Step 1: Draft the document structure**

明确文档包含项目概述、目录说明、环境变量、运行命令、测试命令、修改约束与提交流程。

- [ ] **Step 2: Write the document**

将内容严格限制在仓库当前已存在的事实，不添加 README 和代码中不存在的模块、服务或发布流程。

- [ ] **Step 3: Review against the repository**

逐项核对命令、路径、环境变量名与现有仓库一致。

### Task 2: Add GitHub CI Workflow

**Files:**
- Create: `.github/workflows/ci.yml`
- Reference: `pyproject.toml`
- Reference: `uv.lock`
- Test: `tests/test_deep_agent_quickstart.py`

- [ ] **Step 1: Define the workflow trigger and runner**

使用 `push` 与 `pull_request` 触发，运行器选择 `ubuntu-latest`。

- [ ] **Step 2: Add dependency installation steps**

使用 `astral-sh/setup-uv` 安装 `uv`，使用 `actions/setup-python` 固定 Python 3.12，再执行 `uv sync`。

- [ ] **Step 3: Add verification command**

运行 `uv run python -m unittest discover -s tests -p 'test_*.py'`，与仓库现有测试结构对齐。

### Task 3: Verify Locally

**Files:**
- Verify: `AGENTS.md`
- Verify: `.github/workflows/ci.yml`

- [ ] **Step 1: Run the repository test command**

Run: `uv run python -m unittest discover -s tests -p 'test_*.py'`
Expected: `OK`

- [ ] **Step 2: Inspect the final diff**

Run: `git diff -- AGENTS.md .github/workflows/ci.yml docs/superpowers/plans/2026-03-25-agents-and-ci.md`
Expected: 只包含本次新增文件和预期内容
