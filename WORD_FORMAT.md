# 单词格式说明 📝

## 单词数据结构

每个单词是一个 Python 字典，包含以下 5 个字段：

```python
{
    "word": "单词",
    "phonetic": "/音标/",
    "pos": "词性",
    "meaning": "中文释义",
    "example": "英文例句."
}
```

## 字段详解

| 字段 | 说明 | 示例 | 必填 |
|------|------|------|------|
| `word` | 英文单词（小写） | `"abandon"` | ✅ 是 |
| `phonetic` | 国际音标（斜杠包裹） | `"/əˈbændən/"` | ✅ 是 |
| `pos` | 词性（简写 + 点） | `"v."` | ✅ 是 |
| `meaning` | 中文释义（分号分隔多个意思） | `"放弃；抛弃"` | ✅ 是 |
| `example` | 英文例句（以句号结尾） | `"He abandoned his car."` | ✅ 是 |

## 词性缩写参考

| 缩写 | 完整形式 | 中文 |
|------|----------|------|
| n. | noun | 名词 |
| v. | verb | 动词 |
| adj. | adjective | 形容词 |
| adv. | adverb | 副词 |
| prep. | preposition | 介词 |
| pron. | pronoun | 代词 |
| conj. | conjunction | 连词 |
| int. | interjection | 感叹词 |

## 完整示例

### 示例 1：动词
```python
{
    "word": "abandon",
    "phonetic": "/əˈbændən/",
    "pos": "v.",
    "meaning": "放弃；抛弃；遗弃",
    "example": "He abandoned his car in the snow."
}
```

### 示例 2：名词
```python
{
    "word": "ability",
    "phonetic": "/əˈbɪləti/",
    "pos": "n.",
    "meaning": "能力；才能；本领",
    "example": "She has the ability to learn quickly."
}
```

### 示例 3：形容词
```python
{
    "word": "active",
    "phonetic": "/ˈæktɪv/",
    "pos": "adj.",
    "meaning": "活跃的；积极的；主动的",
    "example": "He stays active by running every day."
}
```

## 添加新单词

### 方法一：直接编辑 vocab_bot.py

```python
word_bank = [
    # 现有单词...

    # 添加新单词
    {
        "word": "your_word",
        "phonetic": "/your-phonetic/",
        "pos": "n.",
        "meaning": "你的中文释义",
        "example": "Your example sentence."
    },
]
```

### 方法二：创建独立的单词文件

创建 `words.py`：
```python
# words.py

easy_words = [
    {
        "word": "hello",
        "phonetic": "/həˈləʊ/",
        "pos": "int.",
        "meaning": "你好；问候",
        "example": "Hello, how are you?"
    },
    # 更多简单单词...
]

medium_words = [
    {
        "word": "beautiful",
        "phonetic": "/ˈbjuːtɪfl/",
        "pos": "adj.",
        "meaning": "美丽的；漂亮的",
        "example": "The sunset was beautiful."
    },
    # 更多中等单词...
]

hard_words = [
    {
        "word": "philosophy",
        "phonetic": "/fɪˈlɒsəfi/",
        "pos": "n.",
        "meaning": "哲学；人生观",
        "example": "Philosophy helps us understand life."
    },
    # 更多困难单词...
]
```

然后在 `vocab_bot.py` 中导入：
```python
from words import easy_words, medium_words, hard_words

word_bank = easy_words + medium_words + hard_words
```

## 难度分组规则

```python
# 简单：基础高频词
word_bank[0:5]

# 中等：日常常用词
word_bank[5:10]

# 困难：进阶词汇
word_bank[10:]
```

## 工具推荐

### 获取音标
- [Cambridge Dictionary](https://dictionary.cambridge.org/)
- [牛津词典](https://www.oxfordlearnersdictionaries.com/)
- [YouGlish](https://youglish.com/) (发音示例)

### 获取例句
- [Reverso Context](https://context.reverso.net/)
- [Linguee](https://www.linguee.com/)

## 注意事项

1. ⚠️ **音标必须用斜杠包裹**：`/音标/`
2. ⚠️ **例句必须以句号结尾**：`"sentence."`
3. ⚠️ **多个释义用分号分隔**：`"意思1；意思2；意思3"`
4. ⚠️ **词性缩写后加句点**：`"n."` 而不是 `"n"`
5. ✅ **单词用小写**：`"hello"` 而不是 `"Hello"`

## 批量生成模板

复制以下模板快速添加单词：

```python
{
    "word": "",
    "phonetic": "/",
    "pos": "",
    "meaning": "",
    "example": "."
},
```
