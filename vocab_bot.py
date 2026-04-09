import streamlit as st
import anthropic
import os

# 配置 API
API_KEY = st.secrets.get("ZHIPU_API_KEY") or os.environ.get("ZHIPU_API_KEY")
BASE_URL = st.secrets.get("ZHIPU_BASE_URL", "https://api.z.ai/api/anthropic")

# 初始化客户端
client = None
if API_KEY:
    try:
        client = anthropic.Anthropic(api_key=API_KEY, base_url=BASE_URL)
    except Exception as e:
        st.error(f"API 初始化失败: {e}")

# 单词库（可扩展）
word_bank = [
    # 高频基础词
    {"word": "abandon", "phonetic": "/əˈbændən/", "pos": "v.", "meaning": "放弃；抛弃", "example": "He abandoned his car in the snow."},
    {"word": "ability", "phonetic": "/əˈbɪləti/", "pos": "n.", "meaning": "能力；才能", "example": "She has the ability to learn quickly."},
    {"word": "abroad", "phonetic": "/əˈbrɔːd/", "pos": "adv.", "meaning": "在国外；到国外", "example": "She plans to study abroad next year."},
    {"word": "absence", "phonetic": "/ˈæbsəns/", "pos": "n.", "meaning": "缺席；不在", "example": "His absence was noticed by everyone."},
    {"word": "absolute", "phonetic": "/ˈæbsəluːt/", "pos": "adj.", "meaning": "绝对的；完全的", "example": "I have absolute confidence in you."},

    # 日常常用
    {"word": "accept", "phonetic": "/əkˈsept/", "pos": "v.", "meaning": "接受；同意", "example": "Please accept my sincere apologies."},
    {"word": "accident", "phonetic": "/ˈæksɪdənt/", "pos": "n.", "meaning": "事故；意外", "example": "He was injured in a car accident."},
    {"word": "account", "phonetic": "/əˈkaʊnt/", "pos": "n.", "meaning": "账户；解释", "example": "I opened a new bank account."},
    {"word": "achieve", "phonetic": "/əˈtʃiːv/", "pos": "v.", "meaning": "实现；达到", "example": "You can achieve anything if you try."},
    {"word": "active", "phonetic": "/ˈæktɪv/", "pos": "adj.", "meaning": "活跃的；积极的", "example": "He stays active by running every day."},

    # 工作学习
    {"word": "advance", "phonetic": "/ədˈvɑːns/", "pos": "v./n.", "meaning": "前进；提前", "example": "Technology continues to advance rapidly."},
    {"word": "advantage", "phonetic": "/əˈvɑːntɪdʒ/", "pos": "n.", "meaning": "优势；利益", "example": "Experience is a big advantage."},
    {"word": "advice", "phonetic": "/ədˈvaɪs/", "pos": "n.", "meaning": "建议；忠告", "example": "Can you give me some advice?"},
    {"word": "affect", "phonetic": "/əˈfekt/", "pos": "v.", "meaning": "影响；感动", "example": "The weather will affect our plans."},
    {"word": "afford", "phonetic": "/əˈfɔːrd/", "pos": "v.", "meaning": "买得起；承担得起", "example": "I can't afford a new car right now."},
]

# 初始化 session state
if "current_word" not in st.session_state:
    st.session_state.current_word = None
if "answered" not in st.session_state:
    st.session_state.answered = False
if "show_answer" not in st.session_state:
    st.session_state.show_answer = False
if "correct_count" not in st.session_state:
    st.session_state.correct_count = 0
if "difficulty" not in st.session_state:
    st.session_state.difficulty = "easy"
if "messages" not in st.session_state:
    st.session_state.messages = []
if "chat_mode" not in st.session_state:
    st.session_state.chat_mode = False

# 页面配置
st.set_page_config(
    page_title="智能背单词机器人",
    page_icon="📚",
    layout="centered"
)

# 标题
st.title("📚 智能背单词机器人")
st.markdown("---")

# API 状态
if client:
    st.success("✅ AI 助手已就绪")
else:
    st.warning("⚠️ 未配置 API Key，对话功能不可用")

# 模式切换
col1, col2 = st.columns(2)
with col1:
    if st.button("📖 单词学习模式", use_container_width=True, type="primary" if not st.session_state.chat_mode else "secondary"):
        st.session_state.chat_mode = False
with col2:
    if st.button("💬 AI 对话模式", use_container_width=True, type="primary" if st.session_state.chat_mode else "secondary"):
        st.session_state.chat_mode = True

# ==================== 对话模式 ====================
if st.session_state.chat_mode:
    st.markdown("### 💬 与 AI 助手对话")

    # 显示聊天历史
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # 聊天输入
    if prompt := st.chat_input("输入你的问题..."):
        # 显示用户消息
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # AI 回复
        if client:
            with st.chat_message("assistant"):
                message_placeholder = st.empty()

                # 构建系统提示词
                current_word_info = ""
                if st.session_state.current_word:
                    word = st.session_state.current_word
                    current_word_info = f"""
当前学习的单词：{word['word']}
音标：{word['phonetic']}
词性：{word['pos']}
中文释义：{word['meaning']}
例句：{word['example']}
"""

                system_prompt = f"""你是一个专业、耐心的英语单词学习助手。你的任务是帮助学生更好地理解和记忆单词。

{current_word_info}

你的特点：
- 语气轻松友好，不啰嗦
- 当学生回答正确时，表扬鼓励
- 当学生回答错误时，温柔纠正并解释
- 可以提供更多例句、同义词、词根词缀分析等
- 可以回答关于单词用法、搭配、文化背景等问题
- 回答简洁明了，重点突出
"""

                try:
                    response = client.messages.create(
                        model="claude-3-5-sonnet-20241022",
                        max_tokens=1024,
                        system=system_prompt,
                        messages=st.session_state.messages
                    )
                    assistant_message = response.content[0].text
                    message_placeholder.markdown(assistant_message)
                    st.session_state.messages.append({"role": "assistant", "content": assistant_message})
                except Exception as e:
                    message_placeholder.error(f"API 调用失败: {e}")
        else:
            st.error("请先配置 API Key")

    # 清除对话
    if st.button("🗑️ 清除对话历史", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

    # 返回学习模式
    if st.button("📖 返回单词学习", use_container_width=True):
        st.session_state.chat_mode = False
        st.rerun()

# ==================== 学习模式 ====================
else:
    # 难度选择
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("简单", use_container_width=True):
            st.session_state.difficulty = "easy"
    with col2:
        if st.button("中等", use_container_width=True):
            st.session_state.difficulty = "medium"
    with col3:
        if st.button("困难", use_container_width=True):
            st.session_state.difficulty = "hard"

    st.caption(f"当前难度：{st.session_state.difficulty} | 已掌握：{st.session_state.correct_count} 个单词")

    # 获取新单词
    def get_new_word():
        if st.session_state.difficulty == "easy":
            pool = word_bank[:5]
        elif st.session_state.difficulty == "medium":
            pool = word_bank[5:10]
        else:
            pool = word_bank[10:]

        # 如果 pool 为空，从整个单词库中选择
        if not pool:
            pool = word_bank

        return random.choice(pool)

    # 显示当前单词或按钮
    if st.session_state.current_word is None:
        st.markdown("### 准备好开始背单词了吗？")
        if st.button("🚀 开始学习", use_container_width=True, type="primary"):
            st.session_state.current_word = get_new_word()
            st.session_state.answered = False
            st.session_state.show_answer = False
            st.rerun()
    else:
        word = st.session_state.current_word

        # 显示单词卡片
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                    padding: 2rem; border-radius: 15px; color: white; text-align: center; margin: 1rem 0;">
            <h1 style="font-size: 3rem; margin: 0;">{word['word']}</h1>
            <p style="font-size: 1.5rem; opacity: 0.9;">{word['phonetic']}</p>
        </div>
        """, unsafe_allow_html=True)

        # 显示答案
        if st.session_state.show_answer:
            st.markdown(f"""
            <div style="background: #f0f2f6; padding: 1.5rem; border-radius: 10px; margin: 1rem 0;">
                <p><strong>词性：</strong> {word['pos']}</p>
                <p><strong>中文释义：</strong> {word['meaning']}</p>
                <p><strong>例句：</strong> {word['example']}</p>
            </div>
            """, unsafe_allow_html=True)

            # 用户输入
            if not st.session_state.answered:
                user_answer = st.text_input("输入你记得的意思（中文或英文）：", key="user_input")

                col_a, col_b = st.columns(2)
                with col_a:
                    if st.button("✅ 我知道", use_container_width=True):
                        if user_answer.strip():
                            st.session_state.correct_count += 1
                            st.success(f"🎉 太棒了！'{word['word']}' 记住了！")
                        st.session_state.answered = True
                        st.rerun()

                with col_b:
                    if st.button("❌ 我不知道", use_container_width=True):
                        st.warning(f"没关系，'{word['word']}' 的意思是：{word['meaning']}")
                        st.session_state.answered = True
                        st.rerun()

            # 下一个单词
            if st.session_state.answered:
                if st.button("➡️ 下一个单词", use_container_width=True, type="primary"):
                    st.session_state.current_word = get_new_word()
                    st.session_state.answered = False
                    st.session_state.show_answer = False
                    st.rerun()
        else:
            # 显示答案按钮
            if st.button("👀 显示答案", use_container_width=True):
                st.session_state.show_answer = True
                st.rerun()

        # 进入对话模式按钮
        st.markdown("---")
        if st.button("💬 对这个单词有疑问？问问 AI 助手", use_container_width=True):
            st.session_state.chat_mode = True
            st.rerun()

# 底部提示
st.markdown("---")
st.caption("💡 提示：可以随时说「换难度」「复习刚才的」「停一下」")
