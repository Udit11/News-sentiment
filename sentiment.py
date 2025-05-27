from transformers import BertTokenizer, BertForSequenceClassification
import torch

tokenizer = BertTokenizer.from_pretrained("yiyanghkust/finbert-tone")
model = BertForSequenceClassification.from_pretrained("yiyanghkust/finbert-tone")

labels = ['positive', 'negative', 'neutral']

def get_sentiment(text: str):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
    with torch.no_grad():
        logits = model(**inputs).logits
    probs = torch.softmax(logits, dim=1).squeeze()
    return {
        "sentiment": labels[probs.argmax()],
        "confidence": {label: round(float(prob), 3) for label, prob in zip(labels, probs)}
    }