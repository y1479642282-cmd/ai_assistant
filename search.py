import streamlit as st
from engine import FAQEngine

# 初始化引擎 (使用 st.cache_resource 避免每次刷新网页都重新加载庞大的模型)
@st.cache_resource
def load_engine():
    return FAQEngine()


engine = load_engine()

# --- 网页界面设计 ---
st.title("AI & Digital Economy FAQ Bot")
st.markdown("Ask me anything about AI adoption, Digital Transformation, Smart Governance, etc.")
st.markdown("*Supported languages: English, Русский, O'zbekcha*")

# 聊天记录存储
if "messages" not in st.session_state:
    st.session_state.messages = []

# 显示历史聊天
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
        if msg.get("confidence"):
            st.caption(
                f"Topic: {msg['topic']} | Language: {msg['lang'].upper()} | Confidence: {msg['confidence'] * 100}%")

# 接收用户输入
if user_query := st.chat_input("Enter your question here... / Введите ваш вопрос..."):
    # 显示用户问题
    with st.chat_message("user"):
        st.markdown(user_query)
    st.session_state.messages.append({"role": "user", "content": user_query})

    # 进行检索
    result = engine.search(user_query)
    answer = result["answer"]
    conf = result["confidence"]
    lang = result["detected_lang"]
    topic = result["topic"]

    # 逻辑判断：如果置信度太低，给出提示
    if conf < 0.4:
        answer = "I'm sorry, I couldn't find a matching answer in my knowledge base. / Извините, я не смог найти ответ. / Kechirasiz, javob topolmadim."
        conf_display = conf
    else:
        conf_display = conf

    # 显示机器人回答
    with st.chat_message("assistant"):
        st.markdown(answer)
        st.caption(f"Topic: {topic} | Detected Lang: {lang.upper()} | Confidence: {conf_display * 100}%")

    st.session_state.messages.append({
        "role": "assistant",
        "content": answer,
        "confidence": conf_display,
        "lang": lang,
        "topic": topic
    })

    #cd ai_assistant
    #streamlit run search.py