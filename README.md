# 智能背单词机器人 📚

一个简单友好的背单词应用，帮助你高效学习英语词汇，支持 AI 对话式学习。

## 功能特点

- ✅ 每次只显示 1 个单词，专注学习
- 📚 包含音标、中文释义、词性、例句
- 🎯 三种难度等级：简单、中等、困难
- 💡 学习进度追踪
- 💬 **AI 对话式学习** - 询问单词用法、获取更多解释
- 🎨 美观的界面设计

## 本地运行

### 1. 安装依赖
```bash
pip install -r requirements.txt
```

### 2. 配置 API Key（可选，用于 AI 对话功能）

**方式一：使用环境变量**
```bash
export ZHIPU_API_KEY="your-api-key-here"
```

**方式二：使用 secrets.toml（推荐）**
```bash
# 复制模板文件
cp .streamlit/secrets.toml.example .streamlit/secrets.toml

# 编辑 secrets.toml，填入你的 API Key
```

secrets.toml 内容：
```toml
ZHIPU_API_KEY = "your-api-key-here"
ZHIPU_BASE_URL = "https://api.z.ai/api/anthropic"
```

### 3. 运行应用
```bash
streamlit run vocab_bot.py
```

## 部署到 Streamlit Cloud

### 1. 推送代码到 GitHub
```bash
git add .
git commit -m "Update: Add AI chat feature"
git push
```

### 2. 配置 Secrets

在 Streamlit Cloud 中配置 API Key：

1. 访问你的应用设置页面
2. 进入 **Secrets** 标签
3. 添加以下配置：
```toml
ZHIPU_API_KEY = "your-api-key-here"
ZHIPU_BASE_URL = "https://api.z.ai/api/anthropic"
```

### 3. 部署应用

1. 访问 [Streamlit Cloud](https://share.streamlit.io/)
2. 点击 "New app"
3. 选择你的 GitHub 仓库
4. 主文件填写：`vocab_bot.py`
5. 点击 "Deploy"

## 使用说明

### 学习模式
- 选择难度（简单/中等/困难）
- 点击"开始学习"
- 显示单词后，点击"显示答案"查看释义
- 输入你记得的意思，点击"我知道"或"我不知道"
- 点击"下一个单词"继续

### 对话模式
- 点击"AI 对话模式"或"对这个单词有疑问？问问 AI 助手"
- 输入问题，例如：
  - "abandon 有什么同义词？"
  - "给我一个更简单的例句"
  - "这个词在口语中常用吗？"
  - "帮我分析这个词的词根"

## 扩展单词库

编辑 `vocab_bot.py` 中的 `word_bank` 列表，添加更多单词。

每个单词格式：
```python
{
    "word": "单词",
    "phonetic": "/音标/",
    "pos": "词性",
    "meaning": "中文释义",
    "example": "英文例句."
}
```

## 技术栈

- **Frontend**: Streamlit
- **AI**: Claude API (通过智谱海外版)
- **Deployment**: Streamlit Cloud
