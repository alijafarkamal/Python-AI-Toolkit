from textblob import TextBlob

text = "I love JS programming. It's so intuitive and powerful!"

blob = TextBlob(text)
print(f"Sentiment: {blob.sentiment}")
