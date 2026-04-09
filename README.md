# 智能背单词机器人 📚

> 一个简单友好的背单词应用，支持 AI 对话式学习，帮助你高效掌握英语词汇。

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/)

## 📖 目录

- [功能特点](#功能特点)
- [快速开始](#快速开始)
- [部署指南](#部署指南)
- [使用说明](#使用说明)
- [项目结构](#项目结构)
- [扩展单词库](#扩展单词库)
- [常见问题](#常见问题)
- [技术栈](#技术栈)
- [许可协议](#许可协议)

## ✨ 功能特点

| 功能 | 说明 |
|------|------|
| 🎯 **专注学习** | 每次只显示 1 个单词，避免信息过载 |
| 📚 **完整信息** | 包含音标、词性、中文释义、实用例句 |
| 🔢 **难度分级** | 简单、中等、困难三种难度，适应不同水平 |
| 📊 **进度追踪** | 实时显示已掌握单词数量 |
| 💬 **AI 对话** | 智能助手解答单词用法、同义词、例句等问题 |
| 🎨 **精美界面** | 渐变色设计，简洁美观 |
| 🚀 **一键部署** | 支持 Streamlit Cloud 免费托管 |

## 🚀 快速开始

### 方式一：本地运行

```bash
# 1. 克隆项目
git clone https://github.com/12345yxy12345-cyber/happy.git
cd happy

# 2. 安装依赖
pip install -r requirements.txt

# 3. 配置 API Key（可选，用于 AI 功能）
export ZHIPU_API_KEY="your-api-key-here"

# 4. 运行应用
streamlit run vocab_bot.py
```

访问 http://localhost:8501 开始使用！

### 方式二：在线使用

直接访问已部署的应用：[点击这里](https://...)

## 🌐 部署指南

### 部署到 Streamlit Cloud（推荐）

**Step 1: 准备代码**
```bash
git add .
git commit -m "Update: Ready for deployment"
git push
```

**Step 2: 创建应用**

1. 访问 [Streamlit Cloud](https://share.streamlit.io/)
2. 点击 **"New app"**
3. 选择你的 GitHub 仓库：`12345yxy12345-cyber/happy`
4. 配置：
   - **Repository**: `12345yxy12345-cyber/happy`
   - **Branch**: `main`
   - **Main file path**: `vocab_bot.py`
5. 点击 **"Deploy"**

**Step 3: 配置 Secrets（启用 AI 功能）**

1. 进入应用设置页面，点击 **"Secrets"** 标签
2. 添加以下配置（注意使用双引号）：
```toml
ZHIPU_API_KEY = "your-api-key-here"
ZHIPU_BASE_URL = "https://api.z.ai/api/anthropic"
```
3. 保存后应用会自动重启

### 部署到 Replit

1. 访问 [Replit](https://replit.com/) 创建 Python 项目
2. 上传所有项目文件
3. 在 `.env` 文件中配置 API Key
4. 点击 **Deploy** → 选择 **Streamlit**

## 📚 使用说明

### 学习模式

1. **选择难度**：点击"简单"、"中等"或"困难"按钮
2. **开始学习**：点击"🚀 开始学习"
3. **查看单词**：单词卡片会显示英文单词和音标
4. **显示答案**：点击"👀 显示答案"查看释义和例句
5. **自测**：输入你记得的意思，点击"✅ 我知道"或"❌ 我不知道"
6. **继续**：点击"➡️ 下一个单词"

### 对话模式

**进入方式：**
- 点击顶部"💬 AI 对话模式"按钮
- 或在学习界面点击"💬 对这个单词有疑问？问问 AI 助手"

**可用问题示例：**
| 问题类型 | 示例 |
|----------|------|
| 同义词 | "abandon 有什么同义词？" |
| 例句 | "给我一个更简单的例句" |
| 用法 | "这个词在口语中常用吗？" |
| 词根 | "帮我分析这个词的词根" |
| 搭配 | "这个词常和什么词搭配？" |
| 辨析 | "abandon 和 give up 有什么区别？" |

**快捷指令：**
- "换难度" - 切换学习难度
- "复习刚才的" - 重新查看当前单词
- "停一下" - 暂停学习

## 📁 项目结构

```
happy/
├── vocab_bot.py              # 主应用文件
├── requirements.txt          # Python 依赖
├── README.md                 # 项目说明
├── .gitignore               # Git 忽略文件
└── .streamlit/
    └── secrets.toml.example # Secrets 配置模板
```

## 🔧 扩展单词库

编辑 `vocab_bot.py` 中的 `word_bank` 列表：

```python
word_bank = [
    {
        "word": "example",           # 单词
        "phonetic": "/ɪɡˈzæmpl/",    # 音标
        "pos": "n.",                 # 词性
        "meaning": "例子；榜样",      # 中文释义
        "example": "This is a good example."
    },
    # 添加更多单词...
]
```

**提示：**
- 按难度分组，每组 5 个单词
- 简单：`word_bank[0:5]`
- 中等：`word_bank[5:10]`
- 困难：`word_bank[10:]`

## ❓ 常见问题

### Q: AI 功能无法使用？
**A:** 检查以下配置：
1. Secrets 中是否正确配置了 `ZHIPU_API_KEY`
2. API Key 格式是否正确（使用双引号）
3. API Key 是否有效

### Q: 部署后报错 "NameError"？
**A:** 可能是依赖安装问题，检查 `requirements.txt` 是否正确。

### Q: 如何添加更多单词？
**A:** 编辑 `vocab_bot.py` 中的 `word_bank` 列表，按格式添加即可。

### Q: 可以离线使用吗？
**A:** 可以，不配置 API Key 时，AI 功能不可用，但单词学习功能正常。

### Q: 如何重置学习进度？
**A:** 刷新页面即可重置当前会话的进度。

## 🛠 技术栈

| 组件 | 技术 |
|------|------|
| **前端框架** | [Streamlit](https://streamlit.io/) |
| **HTTP 客户端** | [httpx](https://www.python-httpx.org/) |
| **AI 模型** | Claude 3.5 Sonnet |
| **API 提供商** | 智谱海外版 |
| **部署平台** | Streamlit Cloud |

## 📄 许可协议

MIT License - 详见 [LICENSE](LICENSE) 文件

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

1. Fork 本项目
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启 Pull Request

## 📮 联系方式

- 项目地址：[GitHub](https://github.com/12345yxy12345-cyber/happy)
- 问题反馈：[Issues](https://github.com/12345yxy12345-cyber/happy/issues)

---

⭐ 如果这个项目对你有帮助，请给个 Star！
