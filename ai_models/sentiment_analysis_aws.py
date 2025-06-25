import boto3

# Initialize AWS Comprehend
client = boto3.client('comprehend', region_name='us-east-1')

# Input text
text = "Amazon Web Services makes sentiment analysis easy!"

# Detect sentiment
response = client.detect_sentiment(Text=text, LanguageCode='en')
print(f"Sentiment: {response['Sentiment']}")
