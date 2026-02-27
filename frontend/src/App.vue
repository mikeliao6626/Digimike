<template>
  <div class="digimike-app">
    <!-- Navigation Header -->
    <el-header class="app-header">
      <div class="header-content">
        <div class="logo-section">
          <div class="logo-icon">⚡</div>
          <div class="logo-text">
            <span class="logo-title">Digimike</span>
            <span class="logo-sub">Sub-ERP ·  个人智能中台</span>
          </div>
        </div>
        <div class="header-actions">
          <el-tag type="success" size="small" class="status-tag" v-if="backendOnline">
            <el-icon><CircleCheck /></el-icon> API 在线
          </el-tag>
          <el-tag type="danger" size="small" class="status-tag" v-else>
            <el-icon><CircleClose /></el-icon> API 离线
          </el-tag>
          <el-button type="primary" round size="small" @click="handleGoogleLogin">
            <el-icon><User /></el-icon>
            Google 登录
          </el-button>
        </div>
      </div>
    </el-header>

    <!-- Hero Section -->
    <main class="main-content">
      <div class="hero-section">
        <div class="hero-badge">
          <span>🚀 Iteration 1 — 架构初始化完成</span>
        </div>
        <h1 class="hero-title">
          数字化 <span class="highlight">Mike 廖</span><br />
          的管理智慧
        </h1>
        <p class="hero-desc">
          跨境电商 20 年的经验结晶，通过 AI 技术沉淀成<br />
          可复用的数字孪生中台
        </p>

        <div class="module-grid">
          <div
            class="module-card"
            v-for="module in modules"
            :key="module.title"
            :class="module.status"
          >
            <div class="module-icon">{{ module.icon }}</div>
            <div class="module-info">
              <span class="module-title">{{ module.title }}</span>
              <span class="module-desc">{{ module.desc }}</span>
            </div>
            <el-tag :type="module.tagType" size="small">{{ module.tag }}</el-tag>
          </div>
        </div>
      </div>

      <!-- Tech Stack Section -->
      <el-divider>
        <el-icon><Setting /></el-icon>
        <span style="margin-left:8px">技术架构</span>
      </el-divider>

      <div class="tech-grid">
        <div class="tech-item" v-for="tech in techStack" :key="tech.name">
          <span class="tech-emoji">{{ tech.emoji }}</span>
          <span class="tech-name">{{ tech.name }}</span>
          <span class="tech-desc">{{ tech.desc }}</span>
        </div>
      </div>

      <!-- API Status Card -->
      <el-card class="api-card" shadow="hover">
        <template #header>
          <div class="card-header">
            <el-icon><Connection /></el-icon>
            <span>后端 API 状态</span>
            <el-button link type="primary" size="small" @click="checkHealth">刷新</el-button>
          </div>
        </template>
        <div class="api-links">
          <a href="http://localhost:8000/docs" target="_blank" class="api-link">
            <el-icon><Document /></el-icon>
            Swagger 文档 → localhost:8000/docs
          </a>
          <a href="http://localhost:8000/health" target="_blank" class="api-link">
            <el-icon><Monitor /></el-icon>
            健康检查 → /health
          </a>
          <a href="http://localhost:8000/redoc" target="_blank" class="api-link">
            <el-icon><Reading /></el-icon>
            ReDoc → /redoc
          </a>
        </div>
        <div v-if="healthData" class="health-data">
          <el-alert :title="`API 响应：${JSON.stringify(healthData)}`" type="success" :closable="false" />
        </div>
      </el-card>
    </main>

    <footer class="app-footer">
      <span>© 2026 Mike 廖 · Digimike Sub-ERP v0.1.0</span>
      <span>FastAPI + Vue 3 + Element Plus · 微服务架构</span>
    </footer>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { ElMessage } from 'element-plus'
import axios from 'axios'

// Mike 廖：主应用状态管理
const backendOnline = ref(false)
const healthData = ref<any>(null)

interface Module {
  icon: string
  title: string
  desc: string
  tag: string
  tagType: 'success' | 'warning' | 'info' | 'danger'
  status: string
}

const modules: Module[] = [
  { icon: '🧠', title: 'AI Memory', desc: '微博 2000 条语义检索', tag: 'Iter 2', tagType: 'warning', status: 'pending' },
  { icon: '🤖', title: 'Agent 中台', desc: '数字孪生 Mike 廖', tag: 'Iter 2', tagType: 'warning', status: 'pending' },
  { icon: '🔐', title: 'Google 登录', desc: 'OAuth 2.0 联合认证', tag: 'Iter 2', tagType: 'warning', status: 'pending' },
  { icon: '⚡', title: 'FastAPI 后端', desc: '微服务 + CORS 已就绪', tag: '已完成', tagType: 'success', status: 'done' },
  { icon: '🎨', title: 'Vue 3 前端', desc: 'Element Plus UI 已就绪', tag: '已完成', tagType: 'success', status: 'done' },
  { icon: '🗄️', title: 'PostgreSQL', desc: '业务数据库待配置', tag: 'Iter 2', tagType: 'warning', status: 'pending' },
]

interface TechItem {
  emoji: string
  name: string
  desc: string
}

const techStack: TechItem[] = [
  { emoji: '🐍', name: 'FastAPI', desc: 'Python 异步后端' },
  { emoji: '💚', name: 'Vue 3', desc: 'Element Plus UI' },
  { emoji: '🧩', name: 'LangGraph', desc: 'AI Agent 框架' },
  { emoji: '🔮', name: 'Qdrant', desc: '向量数据库' },
  { emoji: '💎', name: 'PostgreSQL', desc: '业务数据库' },
  { emoji: '✨', name: 'Gemini 2.0', desc: 'LLM 引擎' },
]

async function checkHealth(): Promise<void> {
  try {
    const res = await axios.get('/health')
    healthData.value = res.data
    backendOnline.value = true
    ElMessage.success('API 连接正常！')
  } catch {
    backendOnline.value = false
    ElMessage.error('无法连接 API，请确保后端已启动')
  }
}

function handleGoogleLogin(): void {
  ElMessage.info('Google OAuth 将在 Iteration 2 实现，敬请期待！')
}

onMounted(() => {
  checkHealth()
})
</script>

<style scoped>
.digimike-app {
  min-height: 100vh;
  background: linear-gradient(135deg, #0f0c29 0%, #302b63 50%, #24243e 100%);
  color: #fff;
  font-family: 'Inter', 'PingFang SC', sans-serif;
}

.app-header {
  background: rgba(255, 255, 255, 0.05);
  backdrop-filter: blur(12px);
  border-bottom: 1px solid rgba(255, 255, 255, 0.08);
  height: 64px;
  display: flex;
  align-items: center;
}
.header-content {
  width: 100%;
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 24px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.logo-section { display: flex; align-items: center; gap: 12px; }
.logo-icon { font-size: 28px; }
.logo-text { display: flex; flex-direction: column; }
.logo-title { font-size: 20px; font-weight: 700; letter-spacing: 1px; }
.logo-sub { font-size: 11px; color: rgba(255,255,255,0.5); }
.header-actions { display: flex; gap: 12px; align-items: center; }
.status-tag { display: flex; align-items: center; gap: 4px; }

.main-content {
  max-width: 1100px;
  margin: 0 auto;
  padding: 60px 24px 40px;
}

.hero-section { text-align: center; margin-bottom: 60px; }
.hero-badge {
  display: inline-block;
  background: rgba(103, 194, 58, 0.15);
  border: 1px solid rgba(103, 194, 58, 0.3);
  border-radius: 20px;
  padding: 6px 16px;
  font-size: 13px;
  color: #67c23a;
  margin-bottom: 24px;
}
.hero-title {
  font-size: 52px;
  font-weight: 800;
  line-height: 1.2;
  margin-bottom: 20px;
}
.highlight {
  background: linear-gradient(90deg, #7b68ee, #00d2ff);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}
.hero-desc {
  font-size: 16px;
  color: rgba(255, 255, 255, 0.6);
  line-height: 1.8;
  margin-bottom: 48px;
}

.module-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 16px;
  text-align: left;
}
.module-card {
  background: rgba(255, 255, 255, 0.06);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 12px;
  padding: 16px 20px;
  display: flex;
  align-items: center;
  gap: 14px;
  transition: transform 0.2s, background 0.2s;
}
.module-card:hover {
  transform: translateY(-2px);
  background: rgba(255, 255, 255, 0.1);
}
.module-card.done {
  border-color: rgba(103, 194, 58, 0.3);
  background: rgba(103, 194, 58, 0.08);
}
.module-icon { font-size: 28px; }
.module-info { flex: 1; display: flex; flex-direction: column; }
.module-title { font-weight: 600; font-size: 14px; }
.module-desc { font-size: 12px; color: rgba(255,255,255,0.5); }

.tech-grid {
  display: grid;
  grid-template-columns: repeat(6, 1fr);
  gap: 12px;
  margin-bottom: 40px;
}
.tech-item {
  background: rgba(255, 255, 255, 0.05);
  border-radius: 10px;
  padding: 16px 12px;
  text-align: center;
  display: flex;
  flex-direction: column;
  gap: 6px;
  transition: background 0.2s;
}
.tech-item:hover { background: rgba(255, 255, 255, 0.1); }
.tech-emoji { font-size: 24px; }
.tech-name { font-size: 13px; font-weight: 600; }
.tech-desc { font-size: 11px; color: rgba(255,255,255,0.45); }

.api-card {
  background: rgba(255, 255, 255, 0.06) !important;
  border: 1px solid rgba(255, 255, 255, 0.1) !important;
  border-radius: 12px !important;
  color: #fff;
}
:deep(.el-card__header) {
  border-bottom-color: rgba(255,255,255,0.08) !important;
  color: #fff;
}
:deep(.el-card__body) { color: #fff; }
.card-header { display: flex; align-items: center; gap: 8px; font-weight: 600; }
.api-links { display: flex; flex-direction: column; gap: 12px; }
.api-link {
  display: flex;
  align-items: center;
  gap: 8px;
  color: #7b68ee;
  text-decoration: none;
  font-size: 14px;
  transition: color 0.2s;
}
.api-link:hover { color: #00d2ff; }
.health-data { margin-top: 16px; }
:deep(.el-divider__text) { background: transparent; color: rgba(255,255,255,0.5); }
:deep(.el-divider.el-divider--horizontal) { border-color: rgba(255,255,255,0.1); }

.app-footer {
  text-align: center;
  padding: 20px;
  display: flex;
  justify-content: center;
  gap: 40px;
  font-size: 12px;
  color: rgba(255,255,255,0.3);
  border-top: 1px solid rgba(255,255,255,0.06);
}
</style>
