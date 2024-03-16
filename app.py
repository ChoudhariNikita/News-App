# app.py
from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

NEWS_API_KEY = '50700ae6b8ef4705ab7f58fd220c1d52'  # Replace this with your News API key

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_news', methods=['POST'])
def get_news():
    selected_date = request.form['date']
    news = fetch_news(selected_date)
    return render_template('news.html', news=news)

def fetch_news(date):
    url = f'https://newsapi.org/v2/everything?q=apple&from={date}&to={date}&sortBy=popularity&apiKey={NEWS_API_KEY}'
    response = requests.get(url)
    data = response.json()
    articles = data.get('articles')
    if articles:
        return articles[:5]
    else:
        return []

if __name__ == '__main__':
    app.run(debug=True)
