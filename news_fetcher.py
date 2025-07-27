import requests
from datetime import datetime, timedelta

class NewsFetcher:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://newsapi.org/v2"
    
    def get_articles(self, topics, sources=None, max_articles=10):
        articles = []
        
        for topic in topics:
            url = f"{self.base_url}/everything"
            params = {
                'q': topic,
                'apiKey': self.api_key,
                'language': 'en',
                'sortBy': 'publishedAt',
                'pageSize': max_articles // len(topics),
                'from': (datetime.now() - timedelta(days=1)).isoformat()
            }
            
            if sources:
                params['sources'] = ','.join(sources)
            
            try:
                response = requests.get(url, params=params)
                response.raise_for_status()
                data = response.json()
                
                for article in data.get('articles', []):
                    if article['content'] and len(article['content']) > 100:
                        # Clean content and use description if content is truncated
                        content = article['content']
                        if '[+' in content and 'chars]' in content:
                            # Content is truncated, use description instead
                            content = article.get('description', content)
                        
                        articles.append({
                            'title': article['title'],
                            'content': content,
                            'url': article['url'],
                            'source': article['source']['name'],
                            'published': article['publishedAt']
                        })
                        
            except requests.exceptions.RequestException as e:
                print(f"❌ Error fetching news for {topic}: {e}")
        
        return articles[:max_articles]