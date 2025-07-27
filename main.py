import json
import webbrowser
import os
from datetime import datetime
from news_fetcher import NewsFetcher
from summarizer import ArticleSummarizer
from email_sender import EmailSender
from config import Config

class NewsAgent:
    def __init__(self):
        self.config = Config()
        self.fetcher = NewsFetcher(self.config.NEWS_API_KEY)
        self.summarizer = ArticleSummarizer()
        self.email_sender = EmailSender(self.config)
        
    def load_preferences(self):
        with open('user_preferences.json', 'r') as f:
            return json.load(f)
    
    def generate_frontend_html(self, summaries):
        """Generate a dynamic HTML frontend with real news data"""
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        # Convert summaries to JavaScript format
        js_articles = []
        for item in summaries:
            js_articles.append({
                'title': item['title'].replace('"', '\\"').replace("'", "\\'"),
                'summary': item['summary'].replace('"', '\\"').replace("'", "\\'"),
                'source': item['source'],
                'url': item['url']
            })
        
        articles_json = json.dumps(js_articles, indent=2)
        
        html_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI News Digest - {current_time}</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #0c0c0c 0%, #1a1a2e 50%, #16213e 100%);
            color: #ffffff;
            min-height: 100vh;
            overflow-x: hidden;
        }}

        .container {{
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
            position: relative;
        }}

        .header {{
            text-align: center;
            margin-bottom: 40px;
            position: relative;
        }}

        .header::before {{
            content: '';
            position: absolute;
            top: -50px;
            left: 50%;
            transform: translateX(-50%);
            width: 200px;
            height: 200px;
            background: radial-gradient(circle, rgba(0, 255, 255, 0.1) 0%, transparent 70%);
            border-radius: 50%;
            z-index: -1;
        }}

        h1 {{
            font-size: 3rem;
            font-weight: 700;
            background: linear-gradient(45deg, #00ffff, #ff00ff, #ffff00);
            background-size: 300% 300%;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            animation: gradientShift 3s ease-in-out infinite;
            margin-bottom: 10px;
        }}

        @keyframes gradientShift {{
            0%, 100% {{ background-position: 0% 50%; }}
            50% {{ background-position: 100% 50%; }}
        }}

        .subtitle {{
            font-size: 1.2rem;
            color: #a0a0a0;
            margin-bottom: 30px;
        }}

        .news-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
            gap: 30px;
            margin-top: 40px;
        }}

        .news-card {{
            background: rgba(255, 255, 255, 0.05);
            backdrop-filter: blur(20px);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 20px;
            padding: 30px;
            transition: all 0.3s ease;
            position: relative;
            overflow: hidden;
            animation: slideInUp 0.6s ease forwards;
        }}

        .news-card::before {{
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.1), transparent);
            transition: left 0.5s ease;
        }}

        .news-card:hover::before {{
            left: 100%;
        }}

        .news-card:hover {{
            transform: translateY(-10px);
            box-shadow: 0 20px 60px rgba(0, 255, 255, 0.2);
            border-color: rgba(0, 255, 255, 0.3);
        }}

        .news-header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 20px;
        }}

        .news-number {{
            background: linear-gradient(45deg, #ff6b6b, #ee5a24);
            color: white;
            width: 40px;
            height: 40px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: bold;
            font-size: 1.2rem;
        }}

        .news-source {{
            background: rgba(0, 255, 255, 0.2);
            color: #00ffff;
            padding: 6px 15px;
            border-radius: 15px;
            font-size: 0.9rem;
            font-weight: 600;
        }}

        .news-title {{
            font-size: 1.3rem;
            font-weight: 600;
            margin-bottom: 15px;
            line-height: 1.4;
            color: #ffffff;
        }}

        .news-summary {{
            color: #b0b0b0;
            line-height: 1.6;
            margin-bottom: 20px;
            font-size: 1rem;
        }}

        .news-link {{
            display: inline-flex;
            align-items: center;
            gap: 8px;
            color: #00ffff;
            text-decoration: none;
            font-weight: 600;
            transition: all 0.3s ease;
            padding: 8px 0;
        }}

        .news-link:hover {{
            color: #ff00ff;
            transform: translateX(5px);
        }}

        .stats {{
            display: flex;
            justify-content: center;
            gap: 40px;
            margin: 40px 0;
            flex-wrap: wrap;
        }}

        .stat {{
            text-align: center;
            padding: 20px;
            background: rgba(255, 255, 255, 0.05);
            border-radius: 15px;
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.1);
            min-width: 150px;
        }}

        .stat-number {{
            font-size: 2rem;
            font-weight: bold;
            color: #00ffff;
            display: block;
        }}

        .stat-label {{
            color: #a0a0a0;
            font-size: 0.9rem;
        }}

        .footer {{
            text-align: center;
            margin-top: 60px;
            padding: 30px;
            border-top: 1px solid rgba(255, 255, 255, 0.1);
            background: rgba(0, 0, 0, 0.3);
            border-radius: 20px;
        }}

        .footer p {{
            color: #888;
            margin-bottom: 10px;
        }}

        @keyframes slideInUp {{
            from {{
                opacity: 0;
                transform: translateY(30px);
            }}
            to {{
                opacity: 1;
                transform: translateY(0);
            }}
        }}

        @media (max-width: 768px) {{
            .news-grid {{
                grid-template-columns: 1fr;
            }}
            
            h1 {{
                font-size: 2rem;
            }}
        }}

        .auto-refresh {{
            position: fixed;
            top: 20px;
            right: 20px;
            background: rgba(0, 255, 255, 0.2);
            color: #00ffff;
            padding: 10px 20px;
            border-radius: 20px;
            font-size: 0.9rem;
            backdrop-filter: blur(10px);
            border: 1px solid rgba(0, 255, 255, 0.3);
        }}
    </style>
</head>
<body>
    <div class="auto-refresh">
        <i class="fas fa-sync-alt"></i> Auto-generated: {current_time}
    </div>

    <div class="container">
        <div class="header">
            <h1><i class="fas fa-robot"></i> AI News Digest</h1>
            <p class="subtitle">Your personalized daily news summary powered by AI</p>
            <p class="subtitle">Generated on {current_time}</p>
        </div>

        <div class="stats">
            <div class="stat">
                <span class="stat-number">{len(summaries)}</span>
                <span class="stat-label">Articles</span>
            </div>
            <div class="stat">
                <span class="stat-number">{len(set(item['source'] for item in summaries))}</span>
                <span class="stat-label">Sources</span>
            </div>
            <div class="stat">
                <span class="stat-number">{len(summaries) * 2}</span>
                <span class="stat-label">Min Read</span>
            </div>
        </div>

        <div class="news-grid">
            {"".join([f'''
            <div class="news-card" style="animation-delay: {i * 0.1}s;">
                <div class="news-header">
                    <div class="news-number">{i + 1}</div>
                    <div class="news-source">{item['source']}</div>
                </div>
                <h3 class="news-title">{item['title']}</h3>
                <p class="news-summary">{item['summary']}</p>
                <a href="{item['url']}" target="_blank" class="news-link">
                    <i class="fas fa-external-link-alt"></i>
                    Read Full Article
                </a>
            </div>
            ''' for i, item in enumerate(summaries)])}
        </div>

        <div class="footer">
            <p><i class="fas fa-heart" style="color: #ff6b6b;"></i> News Summarization</p>
            <p>Stay informed, stay ahead</p>
        </div>
    </div>

    <script>
        // Add floating particles effect
        function createParticle() {{
            const particle = document.createElement('div');
            particle.style.cssText = `
                position: fixed;
                width: 4px;
                height: 4px;
                background: rgba(0, 255, 255, 0.5);
                border-radius: 50%;
                pointer-events: none;
                z-index: -1;
                left: ${{Math.random() * 100}}vw;
                top: 100vh;
                animation: float 8s linear infinite;
            `;
            
            document.body.appendChild(particle);
            
            setTimeout(() => {{
                particle.remove();
            }}, 8000);
        }}

        // Add floating animation
        const floatStyle = document.createElement('style');
        floatStyle.textContent = `
            @keyframes float {{
                to {{
                    transform: translateY(-100vh);
                    opacity: 0;
                }}
            }}
        `;
        document.head.appendChild(floatStyle);

        // Create particles periodically
        setInterval(createParticle, 500);

        // Auto-scroll effect
        let scrollDirection = 1;
        setInterval(() => {{
            window.scrollBy(0, scrollDirection);
            if (window.scrollY >= document.body.scrollHeight - window.innerHeight - 10) {{
                scrollDirection = -1;
            }} else if (window.scrollY <= 0) {{
                scrollDirection = 1;
            }}
        }}, 100);
    </script>
</body>
</html>'''
        
        return html_content
    
    def run_daily_digest(self):
        print(f"🚀 Starting news digest - {datetime.now()}")
        
        preferences = self.load_preferences()
        
        # Fetch articles
        articles = self.fetcher.get_articles(
            topics=preferences['topics'],
            max_articles=preferences['max_articles']
        )
        
        print(f"📰 Fetched {len(articles)} articles")
        
        # Summarize articles
        summaries = []
        for article in articles:
            summary = self.summarizer.summarize(article['content'])
            summaries.append({
                'title': article['title'],
                'summary': summary,
                'url': article['url'],
                'source': article['source']
            })
        
        # Generate and save HTML frontend
        html_content = self.generate_frontend_html(summaries)
        html_filename = f"news_digest_{datetime.now().strftime('%Y%m%d_%H%M')}.html"
        
        with open(html_filename, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        print(f"✅ Frontend generated: {html_filename}")
        
        # Open in browser
        file_path = os.path.abspath(html_filename)
        webbrowser.open(f'file://{file_path}')
        print("🌐 Opening in browser...")
        
        # Also send email if requested
        if preferences.get('send_email', True):
            try:
                digest_email = self.create_email_digest(summaries)
                for recipient in preferences['email_recipients']:
                    self.email_sender.send_digest(recipient, digest_email)
                print("📧 Email digest sent successfully!")
            except Exception as e:
                print(f"❌ Email sending failed: {e}")
        
        # Save text version too
        self.save_to_txt(summaries)
        
        print("✅ Digest completed!")
        
    def create_email_digest(self, summaries):
        """Create HTML email digest"""
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M')
        
        digest = f"""
        <div style="font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto; background: #1a1a1a; color: #ffffff; padding: 20px;">
            <div style="text-align: center; margin-bottom: 30px;">
                <h1 style="color: #00ffff; font-size: 28px; margin-bottom: 10px;">🤖 AI News Digest</h1>
                <p style="color: #a0a0a0; font-size: 16px;">Generated on {current_time}</p>
            </div>
            
            <div style="background: rgba(255,255,255,0.05); padding: 20px; border-radius: 10px; margin-bottom: 20px; text-align: center;">
                <span style="color: #00ffff; font-size: 24px; font-weight: bold;">{len(summaries)}</span>
                <span style="color: #a0a0a0; margin-left: 10px;">Articles Summarized</span>
            </div>
        """
        
        for i, item in enumerate(summaries, 1):
            digest += f"""
            <div style="background: rgba(255,255,255,0.05); border-radius: 15px; padding: 25px; margin-bottom: 20px; border-left: 4px solid #00ffff;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 15px;">
                    <span style="background: #ff6b6b; color: white; width: 30px; height: 30px; border-radius: 50%; display: inline-flex; align-items: center; justify-content: center; font-weight: bold;">{i}</span>
                    <span style="background: rgba(0,255,255,0.2); color: #00ffff; padding: 5px 15px; border-radius: 10px; font-size: 12px;">{item['source']}</span>
                </div>
                <h3 style="color: #ffffff; font-size: 18px; margin-bottom: 15px; line-height: 1.4;">{item['title']}</h3>
                <p style="color: #b0b0b0; line-height: 1.6; margin-bottom: 15px; font-size: 14px;">{item['summary']}</p>
                <a href="{item['url']}" style="color: #00ffff; text-decoration: none; font-weight: 600; font-size: 14px;" target="_blank">
                    📖 Read Full Article →
                </a>
            </div>
            """
        
        digest += """
            <div style="text-align: center; margin-top: 30px; padding: 20px; border-top: 1px solid rgba(255,255,255,0.1);">
                <p style="color: #888; margin-bottom: 10px;">💖 AI-Summary</p>
                <p style="color: #888;">Stay informed, stay ahead</p>
            </div>
        </div>
        """
        
        return digest
        
    def save_to_txt(self, summaries):
        """Save text version for backup"""
        filename = f"news_digest_{datetime.now().strftime('%Y%m%d_%H%M')}.txt"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(f"AI NEWS DIGEST - {datetime.now().strftime('%Y-%m-%d %H:%M')}\n")
            f.write("="*60 + "\n\n")
            
            for i, item in enumerate(summaries, 1):
                f.write(f"{i}. {item['title']}\n")
                f.write(f"Source: {item['source']}\n")
                f.write(f"Summary: {item['summary']}\n")
                f.write(f"URL: {item['url']}\n")
                f.write("-" * 50 + "\n\n")
        
        print(f"💾 Text backup saved: {filename}")

if __name__ == "__main__":
    agent = NewsAgent()
    agent.run_daily_digest()
    print("🎉 All done! Check your browser and email!")
    input("Press Enter to exit...")