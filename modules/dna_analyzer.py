def analyze_news(news):

    emotional = min(len(news)//10, 100)

    return {
        "Emotion": f"{emotional}%",
        "Bias": "High",
        "Evidence": "Low",
        "Clickbait": "Medium",
        "Credibility": "55%"
    }


def get_reasons():

    return [
        "Excessive emotional language",
        "Low evidence score",
        "Clickbait headline detected",
        "Similar fake patterns found"
    ]