from textblob import TextBlob

def analyze_sentiment(text):
    score = TextBlob(text).sentiment.polarity

    if score > 0.2:
        return score, "Genuine"
    elif score < -0.2:
        return score, "Fake"
    else:
        return score, "Neutral"
