# 🧠 AI News Sentiment Analyzer

A real-time AI-powered News Sentiment Analysis microservice for Stocks and Futures & Options (F&O) trading decisions — built with **FastAPI**, **HuggingFace Transformers**, and **Docker**. Perfect for integration into algo-trading dashboards.

---

## 🚀 Features

- 🔍 Real-time sentiment analysis of news content
- 🧠 Powered by a fine-tuned BERT transformer
- 🐳 Dockerized for easy deployment anywhere
- ⚡ FastAPI-based RESTful API with Swagger docs
- 📦 Ready for integration into trading systems or web/mobile dashboards

---

## 🧰 Tech Stack

| Layer       | Technology                         |
|------------|-------------------------------------|
| Backend     | FastAPI, Python                    |
| AI/NLP      | HuggingFace Transformers (`distilbert-base-uncased-finetuned-sst-2-english`) |
| Containerization | Docker                         |
| API Testing | Postman, Swagger UI (`/docs`)      |
| Optional    | React / Next.js frontend integration |

---

## 📁 Project Structure

ai-news-sentiment/
├── app.py # FastAPI main entrypoint
├── sentiment.py # Core NLP sentiment logic using HuggingFace
├── news.py # Utility for fetching external news (optional)
├── requirements.txt
├── Dockerfile
├── .dockerignore
├── .gitignore
└── README.md

---

## 🧪 API Usage

### 🔗 Base URL
http://localhost:8000

### 📬 Endpoint

#### `POST /sentiment`

Analyze the sentiment of a news headline, paragraph, or summary.

**Request JSON:**

```json
{
  "text": "Adani shares rally after Q4 earnings beat estimates"
}

Response JSON:
{
  "label": "POSITIVE",
  "score": 0.9871
}

🐳 Docker Setup
1. Clone the Repo
git clone https://github.com/<your-username>/ai-news-sentiment.git
cd ai-news-sentiment
2. Build the Docker Image
docker build -t news-sentiment-app .
3. Run the Container
docker run -d -p 8000:8000 --name sentiment news-sentiment-app
Your service is now live at http://localhost:8000.


💻 Development (Without Docker)
If you prefer to run locally without Docker:
# Install dependencies
pip install -r requirements.txt

# Run server
uvicorn app:app --reload

📜 License
This project is open-sourced under the MIT License.

👨‍💻 Author
Udit Srivastava
AI/ML Engineer | MSc Computing (AI), Dublin City University
✉️ uditsrivastava2347@gmail.com