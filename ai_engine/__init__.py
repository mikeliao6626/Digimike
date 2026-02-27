# Mike 廖：AI 引擎模块 — LangChain/LangGraph Agent 核心
# 负责：长时记忆管理、微博内容 Embedding、Agent 工具调用
#
# 模块结构：
#   ai_engine/
#   ├── agents/          # LangGraph Agent 定义
#   ├── memory/          # 长时记忆（Qdrant 向量检索）
#   ├── embeddings/      # Sentence Transformers Embedding 工具
#   ├── tools/           # Agent 可调用工具（如查询主 ERP、发布内容）
#   └── main.py          # AI 引擎服务入口（独立微服务，可选）
#
# Iteration 2 实现：
#   - 微博 2000 条数据导入 Qdrant
#   - Mike 廖数字孪生 Agent 构建
#   - 与主 ERP 的工具调用对接

__version__ = "0.1.0"
