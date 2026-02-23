import json
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# 加载模型
model = SentenceTransformer("all-MiniLM-L6-v2")

# 加载知识库
with open("data/knowledge_base.json", "r", encoding="utf-8") as f:
    knowledge_base = json.load(f)

# 英语向量
questions_en = [item["question"] for item in knowledge_base]
answers_en = [item["answer"] for item in knowledge_base]
question_embeddings_en = model.encode(questions_en)

# 乌兹别克语向量（多问法）
questions_uz = []
answers_uz = []
idx_map_uz = []
for i, item in enumerate(knowledge_base):
    for q in item["question_uz"]:
        questions_uz.append(q)
        answers_uz.append(item["answer_uz"])
        idx_map_uz.append(i)
question_embeddings_uz = model.encode(questions_uz)

def search(query, language="en", top_k=3):
    if language == "en":
        embeddings = question_embeddings_en
        questions = questions_en
        answers = answers_en
    else:
        embeddings = question_embeddings_uz
        questions = questions_uz
        answers = answers_uz

    query_embedding = model.encode([query])
    similarities = cosine_similarity(query_embedding, embeddings)[0]

    # top_k 索引
    top_indices = similarities.argsort()[-top_k:][::-1]

    results = []
    for idx in top_indices:
        if similarities[idx] < 0.3:
            continue
        results.append({
            "matched_question": questions[idx],
            "answer": answers[idx],
            "confidence": float(similarities[idx])
        })
    return results