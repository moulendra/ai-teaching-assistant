# 🎓 AI-Powered Adaptive Teaching Assistant

An AI-driven teaching assistant that understands student queries using NLP + Transformer embeddings and adapts learning paths using reinforcement-inspired personalization logic.

---

## 📌 Problem Statement

This system implements two core capabilities:

### 1️⃣ Student Query Understanding (Q1)

Given a natural language student query, the system classifies:

- **Intent Type** → Explanation / Example / Doubt Clarification / Revision  
- **Topic** → e.g., Backpropagation, Gradient Descent, Neural Networks  
- **Difficulty Level** → Beginner / Intermediate / Advanced  

Example:

Input:
"I don't understand backpropagation."

Output:
```json
{
  "intent": "Explanation",
  "topic": "Backpropagation",
  "difficulty_level": "Beginner"
}
```

---

### 2️⃣ Adaptive Learning Path Recommendation (Q2)

Based on student performance and behavior, the system recommends:

- Next topic to study  
- Whether revision is required  
- Difficulty adjustment (Increase / Decrease / Same)

Example:

```json
{
  "next_topic": "Backpropagation",
  "action": "Revision",
  "difficulty_adjustment": "Decrease"
}
```

---

# 🧠 System Architecture

```
Student Query
     ↓
Sentence Embeddings (MiniLM / SBERT)
     ↓
ML Classifiers (Intent + Difficulty)
     ↓
Topic Detection
     ↓
LLM Prompt Refinement (Optional)
     ↓
Adaptive Engine (RL-inspired logic)
     ↓
Personalized Recommendation
```

---

# 🔍 Q1: Student Query Understanding

## 🧩 Techniques Used

### 1. Sentence Embeddings
- Model: sentence-transformers/all-MiniLM-L6-v2
- Converts queries into dense semantic vectors
- Captures contextual meaning beyond keywords

### 2. Intent Classification
- ML Model: Logistic Regression
- Input: Sentence embeddings
- Output: Intent category

### 3. Difficulty Classification
- ML Model: Logistic Regression
- Predicts Beginner / Intermediate / Advanced

### 4. Topic Classification
- Lightweight topic model using trained classifier

### 5. LLM Refinement (Prompt-Based)
- LLM used to refine ambiguous cases
- Improves semantic consistency
- Used for interpretation, not raw prediction

---

## 📊 Q1 Model Performance

- Intent Classification Accuracy: ~100% (Synthetic Balanced Dataset)
- Difficulty Classification Accuracy: ~32–40% (Multiclass realistic distribution)

Classification reports available during training phase.

---

# 🔁 Q2: Adaptive Learning Recommendation

## 🎯 Inputs

- Quiz score
- Number of attempts
- Time spent on topic
- Mastery score
- Current topic

---

## ⚙️ Personalization Logic

The adaptive engine combines:

### 1️⃣ Rule-Based Layer
- Low score → Recommend revision
- High mastery → Increase difficulty
- Many attempts + low score → Decrease difficulty

### 2️⃣ Reinforcement-Inspired Policy

State:
(score, mastery, attempts, time_spent)

Action:
(Next Topic, Revision/Advance, Difficulty Change)

The policy optimizes:
- Learning stability
- Progressive complexity
- Reduced frustration

### 3️⃣ Knowledge Tracing (Basic)
Mastery score updates simulate student knowledge progression.

---

# 📂 Project Structure

```
ai-teaching-assistant/
│
├── app.py
├── train_models.py
├── evaluate_q2.py
├── requirements.txt
│
├── data/
│   └── synthetic_queries.csv
│
├── models/
│   ├── intent_classifier.pkl
│   └── difficulty_classifier.pkl
│
└── src/
    ├── embeddings.py
    ├── intent_model.py
    ├── difficulty_model.py
    ├── topic_model.py
    ├── knowledge_tracing.py
    ├── reinforcement_learning.py
    ├── adaptive_engine.py
    └── llm_refinement.py
```

---

# 📊 Dataset Information

Since no dataset was provided, synthetic data was generated.

## Synthetic Data Generation

- Generated structured queries per topic
- Balanced intent distribution
- Difficulty labels assigned programmatically
- Dataset size < 50MB (as per constraints)

### Assumptions:
- Queries follow academic style
- Difficulty correlates with conceptual depth
- Students behave rationally based on performance

### Limitations:
- Synthetic data lacks real-world noise
- Reinforcement logic is simplified (not full Q-learning)
- Limited topic diversity

---

# 🚀 Setup Instructions

## 1️⃣ Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/ai-teaching-assistant.git
cd ai-teaching-assistant
```

---

## 2️⃣ Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Train Models

```bash
python train_models.py
```

---

## 5️⃣ Run Application

```bash
uvicorn app:app --reload
```

Open in browser:

http://127.0.0.1:8000/docs

---

# 🧪 API Endpoints

## Q1 — Query Analysis

POST `/analyze`

Example:
```json
{
  "query": "I don't understand backpropagation"
}
```

---

## Q2 — Learning Recommendation

POST `/recommend`

Example:
```json
{
  "mastery": 0.3,
  "score": 40,
  "attempts": 3,
  "time_spent": 120,
  "current_topic": "Backpropagation"
}
```

---

# 📈 Evaluation

### Q1
- Accuracy
- Precision / Recall / F1-score
- Classification report

### Q2
- Policy consistency
- Logical adaptation
- Scenario testing

Run:
```
python evaluate_q2.py
```

---

# 🎯 Alignment with Evaluation Criteria

| Criteria | Implementation |
|----------|---------------|
| ML Algorithm Depth | Transformer embeddings + classifiers |
| LLM Usage Quality | Prompt-based refinement |
| Personalization Logic | RL-inspired adaptive engine |
| System Design | Modular architecture |
| Innovation | Hybrid ML + policy-based adaptation |

---

# 🎬 Demo Video Outline (3–5 Minutes)

1. Explain architecture
2. Show Q1 classification
3. Show Q2 recommendation
4. Explain personalization logic
5. Explain model decisions

---

# 🔮 Future Improvements

- Real student dataset integration
- True reinforcement learning (Q-learning / DQN)
- Knowledge graph for topic relationships
- Student profiling memory
- Performance dashboard

---

# 👨‍💻 Author

Mouli P  
AI Teaching Assistant Project

---

# 📌 Conclusion

This system demonstrates a complete pipeline for:

- NLP-based query understanding  
- ML-driven intent and difficulty classification  
- Reinforcement-inspired adaptive learning  
- Modular and scalable architecture  

The design balances interpretability, ML depth, and practical personalization.
