import requests
from textblob import TextBlob

# 1. NewsAPI에서 뉴스 데이터 가져오기 (최대 5개의 뉴스로 제한)
def get_news(api_key, query, language='en', page_size=10):
    url = f'https://newsapi.org/v2/everything?q={query}&language={language}&pageSize={page_size}&apiKey={api_key}'
    response = requests.get(url)
    return response.json()

# 2. 감정 분석 수행
def analyze_sentiment(text):
    analysis = TextBlob(text)
    return analysis.sentiment.polarity

# 3. 뉴스 데이터 가져와서 감정 분석 실행
def main(api_key, query):
    news_data = get_news(api_key, query)
    
    if news_data['status'] != 'ok':
        print("Error fetching news data")
        return
    
    for article in news_data['articles']:
        title = article['title']
        date = article['publishedAt']
        description = article['description']
        content = article.get('content', '')
        
        # 감정 분석
        sentiment_score = analyze_sentiment(title + ' ' + description + ' ' + content)
        print(f"Title: {title}, Date: {date}, Content: {content} \nSentiment Score: {sentiment_score}\n")

# API 키와 검색어 설정
api_key = ''
query = 'los+angeles+housing+market+analysis+2024'

main(api_key, query)