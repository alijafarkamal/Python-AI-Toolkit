from transformers import pipeline
import requests

# Load summarization pipeline
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# Fetch top news articles (example: BBC News)
news_api_url = "https://newsapi.org/v2/top-headlines?country=us&apiKey=your_newsapi_key"
response = requests.get(news_api_url)
articles = response.json()["articles"]

# Summarize articles
print("Top News Headlines:")
for article in articles[:5]:
    print(f"Title: {article['title']}")
    summary = summarizer(article['description'], max_length=50, min_length=25, do_sample=False)
    print(f"Summary: {summary[0]['summary_text']}")
    print("-" * 20)
