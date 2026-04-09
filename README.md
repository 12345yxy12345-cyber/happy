# 智能背单词机器人 📚

一个简单友好的背单词应用，帮助你高效学习英语词汇。

## 功能特点

- ✅ 每次只显示 1 个单词，专注学习
- 📚 包含音标、中文释义、词性、例句
- 🎯 三种难度等级：简单、中等、困难
- 💡 学习进度追踪
- 🎨 美观的界面设计

## 本地运行

```bash
pip install -r requirements.txt
streamlit run vocab_bot.py
```

## 部署到 Streamlit Cloud

1. 将代码推送到 GitHub 仓库
2. 访问 [Streamlit Cloud](https://share.streamlit.io/)
3. 点击 "New app"
4. 选择你的 GitHub 仓库
5. 主文件填写：`vocab_bot.py`
6. 点击 "Deploy"

## 扩展单词库

编辑 `vocab_bot.py` 中的 `word_bank` 列表，添加更多单词即可。

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
