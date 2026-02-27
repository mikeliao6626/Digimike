# Mike 廖：共享模块 — 跨服务复用的类型定义与工具函数
# 设计原则：零外部依赖，纯 Python，便于各微服务引用
#
# 模块结构：
#   shared/
#   ├── schemas/         # Pydantic 共享数据模型（跨服务 DTO）
#   ├── constants/       # 全局常量（业务状态码、枚举值）
#   ├── utils/           # 通用工具（时间处理、加密、分页）
#   └── exceptions/      # 统一异常定义

__version__ = "0.1.0"
