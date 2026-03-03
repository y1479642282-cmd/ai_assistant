import json
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from langdetect import detect


class FAQEngine:
    def __init__(self, data_path="data/faq_data.json"):
        #加载支持多语言的开源文本嵌入模型
        self.model = SentenceTransformer('sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2')

        #加载数据
        with open(data_path, 'r', encoding='utf-8') as f:
            self.faq_data = json.load(f)

        #提取所有预设问题，并进行向量化存储
        self.questions = [item["question"] for item in self.faq_data]
        self.question_embeddings = self.model.encode(self.questions)

    def detect_language(self, text):
        """语言检测逻辑"""
        try:
            lang = detect(text)
            if lang == 'ru':
                return 'ru'
            elif lang in ['uz', 'tr', 'kk']:
                return 'uz'  # langdetect 对 uz 识别可能漂移，做个宽泛匹配
            else:
                return 'en'
        except:
            return 'en'

    def search(self, user_query):
        """相似度检索主逻辑"""
        #检测用户输入语言
        lang = self.detect_language(user_query)

        #将用户问题向量化
        query_embedding = self.model.encode([user_query])

        #计算余弦相似度 (Cosine similarity search)
        similarities = cosine_similarity(query_embedding, self.question_embeddings)[0]

        #找到最高分
        best_match_idx = np.argmax(similarities)
        confidence_score = similarities[best_match_idx]

        #格式化返回结果
        best_faq = self.faq_data[best_match_idx]

        #根据检测到的语言返回对应的答案
        answer_key = f"answer_{lang}"
        answer = best_faq.get(answer_key, best_faq["answer_en"])  # 默认回退到英文

        return {
            "answer": answer,
            "confidence": round(float(confidence_score), 2),
            "detected_lang": lang,
            "topic": best_faq["topic"]
        }