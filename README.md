# 🚀 鸿森智汇 AI 运维系统

一个基于 OpenAI GPT-4 的企业级 AI 运维助手系统，可以帮助 IT 运维团队进行系统分析、问题诊断和优化建议。

## ✨ 功能特性

- **AI 智能问答** - 利用 GPT-4 提供企业级运维建议
- **自动分析** - 自动分析系统性能并给出优化建议
- **健康检查** - 系统状态监控
- **错误处理** - 完善的异常处理和日志记录
- **安全验证** - 请求数据验证和清理

## 📋 系统要求

- Python 3.8+
- pip 包管理器

## 🔧 安装与配置

### 1. 克隆仓库
```bash
git clone https://github.com/hongshen0001-tech/hongsen-ai-ops.git
cd hongsen-ai-ops
```

### 2. 创建虚拟环境
```bash
python -m venv venv

# Linux/Mac
source venv/bin/activate

# Windows
venv\Scripts\activate
```

### 3. 安装依赖
```bash
pip install -r requirements.txt
```

### 4. 配置环境变量
```bash
# 复制示例配置文件
cp .env.example .env

# 编辑 .env 文件，添加你的 OpenAI API Key
# OPENAI_API_KEY=your_api_key_here
```

## 🚀 运行应用

### 开发环境
```bash
python app.py
```

应用将在 `http://0.0.0.0:3000` 启动

### 生产环境
```bash
gunicorn -w 4 -b 0.0.0.0:3000 app:app
```

## 📚 API 文档

### 1. 健康检查
**请求:**
```
GET /
```

**响应:**
```json
{
  "status": "success",
  "message": "🚀 鸿森智汇 AI 运维系统已运行",
  "version": "1.0.0"
}
```

### 2. AI 问答
**请求:**
```
POST /ai
Content-Type: application/json

{
  "prompt": "如何优化 Docker 容器性能？"
}
```

**响应:**
```json
{
  "id": "chatcmpl-xxx",
  "object": "chat.completion",
  "created": 1234567890,
  "model": "gpt-4o-mini",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "优化 Docker 容器性能的几个关键方法..."
      },
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 50,
    "completion_tokens": 150,
    "total_tokens": 200
  }
}
```

**参数说明:**
- `prompt` (string, 必需): 用户的问题或命令
  - 最大长度: 2000 字符
  - 不能为空

**错误响应:**
- 400: 请求格式错误
- 422: 参数验证失败
- 500: 服务器内部错误

### 3. 自动分析
**请求:**
```
GET /auto
```

**功能:** 自动分析服务器 CPU、内存、网络状态并给出优化建议

**响应:** 同 AI 问答接口

## 🏗️ 项目结构

```
hongsen-ai-ops/
├── app.py                   # Flask 应用主文件
├── config.py               # 配置管理
├── logger.py               # 日志配置
├── openai_service.py       # OpenAI API 服务层
├── validators.py           # 请求验证工具
├── requirements.txt        # 项目依赖
├── .env.example           # 环境变量示例
└── README.md              # 项目文档
```

## 🔐 安全建议

- ✅ 使用环境变量保存敏感信息（API Key 等）
- ✅ 验证和清理所有用户输入
- ✅ 在生产环境使用 HTTPS
- ✅ 限制 API 调用频率
- ✅ 启用日志监控

## 📊 配置说明

编辑 `.env` 文件配置以下参数：

```env
# OpenAI API 配置
OPENAI_API_KEY=your_api_key_here

# Flask 配置
FLASK_ENV=production          # development 或 production
FLASK_DEBUG=False             # 调试模式开关
HOST=0.0.0.0                 # 监听地址
PORT=3000                    # 监听端口

# 日志级别
LOG_LEVEL=INFO               # DEBUG, INFO, WARNING, ERROR, CRITICAL
```

## 🛠️ 开发指南

### 添加新的路由
在 `app.py` 中添加新的 `@app.route()` 装饰器

### 添加新的服务
在项目根目录创建新的 `*_service.py` 文件，使用相同的模式

### 添加验证规则
在 `validators.py` 中扩展 `RequestValidator` 类

## 📝 日志输出

应用会输出详细的操作日志：
```
2024-01-15 10:30:45,123 - __main__ - INFO - Starting application on 0.0.0.0:3000
2024-01-15 10:30:50,456 - __main__ - INFO - Health check requested
2024-01-15 10:30:55,789 - __main__ - INFO - Processing AI request with prompt length: 45
```

## 🐛 故障排除

### 错误: OPENAI_API_KEY 未设置
- **解决:** 检查 `.env` 文件是否存在且包含有效的 API Key

### 错误: Connection timeout
- **解决:** 检查网络连接和防火墙设置

### 错误: 400 Bad Request
- **解决:** 确保请求头包含 `Content-Type: application/json`

## 📄 许可证

本项目采用 MIT 许可证

## 👥 贡献

欢迎提交 Issue 和 Pull Request！

## 📧 联系方式

- GitHub: [@hongshen0001-tech](https://github.com/hongshen0001-tech)

---

**最后更新:** 2024年1月
