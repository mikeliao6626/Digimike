# Mike 廖：Digimike Sub-ERP 后端主入口
# FastAPI 应用，包含 CORS 跨域处理、Google OAuth 2.0 登录预留接口
# Architecture: Microservices - Backend Service

from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Optional, Any
import os
from dotenv import load_dotenv

load_dotenv()

# Mike 廖：应用元数据，版本化管理，便于未来对接主 ERP
app = FastAPI(
    title="Digimike Sub-ERP API",
    description="Mike 廖的个人智能中台 — 数字孪生与 Agent 驱动系统",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

# Mike 廖：CORS 跨域配置，开发阶段允许所有来源，生产环境应锁定域名
ALLOWED_ORIGINS: list[str] = os.getenv(
    "ALLOWED_ORIGINS",
    "http://localhost:5173,http://localhost:3000"
).split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ─────────────────────────────────────────
# Schemas
# ─────────────────────────────────────────

class GoogleAuthRequest(BaseModel):
    """Google OAuth 2.0 授权码请求体"""
    code: str
    redirect_uri: str


class TokenResponse(BaseModel):
    """JWT Token 响应体"""
    access_token: str
    token_type: str = "bearer"
    user_email: Optional[str] = None


class HealthResponse(BaseModel):
    """健康检查响应体"""
    status: str
    version: str
    service: str


# ─────────────────────────────────────────
# Routers (预留，后续拆分为独立 router 文件)
# ─────────────────────────────────────────

# Mike 廖：健康检查端点，供 K8s / 负载均衡器探活使用
@app.get("/health", response_model=HealthResponse, tags=["System"])
async def health_check() -> HealthResponse:
    return HealthResponse(
        status="ok",
        version="0.1.0",
        service="digimike-sub-erp-backend",
    )


# Mike 廖：Google OAuth 2.0 登录预留接口
# 完整实现需要：authlib 或 httpx + Google Token Endpoint
@app.post("/auth/google", response_model=TokenResponse, tags=["Auth"])
async def google_login(payload: GoogleAuthRequest) -> TokenResponse:
    """
    接收前端传来的 Google Authorization Code，
    换取 Google ID Token，验证后签发本系统 JWT。
    TODO: 接入 authlib / python-jose 完成完整 OAuth flow
    """
    # 占位逻辑，待 Iteration 2 实现
    raise HTTPException(
        status_code=501,
        detail="Google OAuth 2.0 integration pending — Iteration 2",
    )


# Mike 廖：微博内容语义检索接口预留（对接 Qdrant 向量库）
@app.get("/api/v1/weibo/search", tags=["AI Memory"])
async def search_weibo(q: str, limit: int = 10) -> dict[str, Any]:
    """
    基于向量语义检索 Mike 廖的 2000 条微博内容。
    TODO: 对接 Qdrant / pgvector，使用 Sentence Transformers 做 embedding
    """
    raise HTTPException(
        status_code=501,
        detail="Vector search pending — Iteration 2",
    )


# Mike 廖：Agent 指令接口预留（对接 LangGraph Agent）
@app.post("/api/v1/agent/invoke", tags=["Agent"])
async def invoke_agent(instruction: str) -> dict[str, Any]:
    """
    接收自然语言指令，驱动 LangGraph Agent 执行任务。
    TODO: 接入 LangChain / LangGraph，集成工具调用（Tool use）
    """
    raise HTTPException(
        status_code=501,
        detail="Agent engine pending — Iteration 2",
    )


# ─────────────────────────────────────────
# Dev Entry Point
# ─────────────────────────────────────────
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info",
    )
