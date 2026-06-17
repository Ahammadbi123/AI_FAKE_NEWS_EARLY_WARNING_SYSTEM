import os

from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def manual_detector(news):

    news = news.lower()

    fake_words = [
        "alien",
        "aliens",
        "miracle",
        "secret",
        "shocking",
        "viral",
        "conspiracy",
        "hidden truth",
        "100% cure",
        "government hiding",
        "breaking secret"
    ]

    for word in fake_words:
        if word in news:
            return "FAKE"

    return "REAL"


def predict_news(news):

    try:

        prompt = f"""
Analyze the following news article.

Return ONLY one word:

FAKE

or

REAL

News:
{news}
"""

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0
        )

        result = response.choices[0].message.content.strip().upper()

        print("GROQ RESPONSE =", result)

        if "FAKE" in result:
            return "FAKE"

        return "REAL"

    except Exception as e:

        print("Groq Error:", e)
        print("Using Manual Detector...")

        return manual_detector(news)