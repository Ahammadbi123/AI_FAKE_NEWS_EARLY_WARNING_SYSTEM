from flask import Flask, render_template, request

from modules.dna_analyzer import analyze_news, get_reasons
from modules.early_warning import warning_system
from modules.propagation_tracker import track_news
from modules.detector import predict_news

app = Flask(__name__)
from dotenv import load_dotenv
load_dotenv()
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/analyze', methods=['POST'])
def analyze():

    news = request.form['news']

    # Prediction
    prediction = predict_news(news)

    # DNA Analysis
    dna = analyze_news(news)

    # Risk Analysis
    risk = warning_system(dna)

    # Timeline
    timeline = track_news(news)

    # Explainable AI
    reasons = get_reasons()

    # Graph Data
    dna_chart = {
        "Emotion": 82,
        "Bias": 70,
        "Evidence": 25,
        "Clickbait": 60,
        "Credibility": 40
    }

    risk_chart = {
        "Fake Risk": 68,
        "Authentic": 32
    }

    return render_template(
        'result.html',
        prediction=prediction,
        dna=dna,
        risk=risk,
        timeline=timeline,
        reasons=reasons,
        dna_chart=dna_chart,
        risk_chart=risk_chart
    )


if __name__ == "__main__":
    app.run(debug=True)
    app.run(host="0.0.0.0", port=5000)
