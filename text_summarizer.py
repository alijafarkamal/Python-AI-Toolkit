from transformers import pipeline

# Load summarization pipeline
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# Input text
text = """
Climate change refers to long-term shifts in temperatures and weather patterns. These changes 
may be natural, such as through variations in the solar cycle. But since the 1800s, human 
activities have been the main driver of climate change, primarily due to burning fossil fuels 
like coal, oil, and gas.
"""

# Summarize text
summary = summarizer(text, max_length=50, min_length=25, do_sample=False)
print("Summary:")
print(summary[0]['summary_text'])
