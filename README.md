# 🧠 AI News Sentiment Analyzer

An AI-powered microservice for real-time **news sentiment analysis** tailored for Stocks and F&O trading strategies. Built using **FastAPI**, **HuggingFace Transformers**, and **Docker**, this service is production-ready and easily integrable into trading platforms and dashboards.

---

## 🚀 Features

- 🔍 Analyze sentiment of news headlines or paragraphs in real-time
- 🤖 Powered by a fine-tuned BERT-based transformer from HuggingFace
- 🐳 Dockerized for seamless deployment
- ⚡ High-performance RESTful API via FastAPI
- 📄 Auto-generated interactive Swagger docs (`/docs`)

---

## 🧰 Tech Stack

| Layer           | Technology                                                               |
|----------------|--------------------------------------------------------------------------|
| **Backend**     | FastAPI, Python                                                          |
| **AI/NLP**       | `distilbert-base-uncased-finetuned-sst-2-english` (HuggingFace)          |
| **Containerization** | Docker                                                             |
| **API Testing**  | Postman, Swagger UI                                                     |
| **Optional Frontend** | React / Next.js (integration ready)                              |

---

## 📁 Project Structure

```
ai-news-sentiment/
├── app.py              # FastAPI main application
├── sentiment.py        # Sentiment analysis logic using HuggingFace
├── news.py             # Utility functions to fetch news (optional)
├── requirements.txt    # Python dependencies
├── Dockerfile          # Docker build configuration
├── .dockerignore
├── .gitignore
└── README.md
```

---

## 🧪 API Usage

### 🔗 Base URL
```
http://localhost:8000
```

### 📬 Endpoint: `POST /sentiment`

Perform sentiment analysis on news content.

**Request JSON:**
```json
{
  "text": "Adani shares rally after Q4 earnings beat estimates"
}
```

**Response JSON:**
```json
{
  "label": "POSITIVE",
  "score": 0.9871
}
```

---

## 🐳 Docker Setup

1. **Clone the repository:**

```bash
git clone https://github.com/Udit11/ai-news-sentiment.git
cd ai-news-sentiment
```

2. **Build the Docker image:**

```bash
docker build -t news-sentiment-app .
```

3. **Run the Docker container:**

```bash
docker run -d -p 8000:8000 --name sentiment news-sentiment-app
```

Your service will be live at: [http://localhost:8000](http://localhost:8000)

---

## 💻 Development Without Docker

If you prefer a local development setup:

1. **Install Python dependencies:**

```bash
pip install -r requirements.txt
```

2. **Run the FastAPI server:**

```bash
uvicorn app:app --reload
```

---

## 📜 License

This project is licensed under the **MIT License**. See the `LICENSE` file for more information.

---

## 👨‍💻 Author

**Udit Srivastava**  
AI/ML Engineer | MSc in Computing (AI), Dublin City University  
📧 Email: uditsrivastava2347@gmail.com  
🔗 [LinkedIn](https://www.linkedin.com/in/udit-srivastava/)

---
