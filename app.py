import streamlit as st
from search import search
from langdetect import detect, DetectorFactory

DetectorFactory.seed = 0  # 保证语言检测稳定

st.set_page_config(page_title="AI & Digital Economy Knowledge Assistant")

query = st.text_input("Enter your question / Savolingizni kiriting:")

if st.button("Search / Qidirish"):
    if not query.strip():
        st.warning("Please enter a question. / Iltimos, savol kiriting.")
    else:
        # 自动语言检测
        try:
            lang_detected = detect(query)
            lang_code = "uz" if lang_detected == "uz" else "en"
        except:
            lang_code = "en"

        results = search(query, language=lang_code, top_k=3)

        if not results:
            st.info("No matching answer found." if lang_code=="en" else "Kechirasiz, mos javob topilmadi.")
        else:
            seen_answers = set()
            for i, r in enumerate(results, 1):
                if r['answer'] in seen_answers:
                    continue
                seen_answers.add(r['answer'])

                st.markdown(f"**Match {i}: {r['matched_question']}**")
                st.write(r['answer'])
                st.write(f"Confidence Score: {r['confidence']:.2f}")
                st.markdown("---")