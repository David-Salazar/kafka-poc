from transformers import pipeline
if __name__ == "__main__":
    classifier = pipeline('sentiment-analysis')
    topic_classifier = pipeline("zero-shot-classification")