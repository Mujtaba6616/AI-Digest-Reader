# 🤖 AI News Summarizer

> A beautiful, AI-powered news summarizer that fetches articles, creates intelligent summaries, and presents them in a stunning dark-themed web interface.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![AI](https://img.shields.io/badge/AI-Transformers-green.svg)
![Status](https://img.shields.io/badge/Status-Active-brightgreen.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## ✨ Features

- 🎯 **Smart News Fetching** - Integrates with NewsAPI for real-time articles
- 🤖 **AI-Powered Summarization** - Uses Facebook's BART model with extractive fallbacks
- 🎨 **Stunning Dark UI** - Glassmorphism design with animations and particles
- 📧 **Email Integration** - Sends beautiful HTML digests to your inbox
- ⚡ **Lightning Fast** - Optimized processing with smart caching
- 📱 **Responsive Design** - Works perfectly on all devices
- 🔧 **Highly Customizable** - Easy configuration via JSON preferences

## 🎥 Demo

![News Summarizer Demo](screenshots/demo.gif)

*Beautiful dark-themed interface with real-time news summaries*

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- NewsAPI account (free)
- Gmail account with App Password

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/ai-news-summarizer.git
   cd ai-news-summarizer
   ```

2. **Create virtual environment**
   ```bash
   python -m venv news_env
   
   # Windows
   news_env\Scripts\activate
   
   # macOS/Linux
   source news_env/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   python -m spacy download en_core_web_sm
   ```

4. **Set up environment variables**
   
   Create a `.env` file in the project root:
   ```env
   NEWS_API_KEY=your_newsapi_key_here
   EMAIL_ADDRESS=your_gmail@gmail.com
   EMAIL_PASSWORD=your_gmail_app_password
   SMTP_SERVER=smtp.gmail.com
   SMTP_PORT=587
   ```

5. **Configure preferences**
   
   Edit `user_preferences.json`:
   ```json
   {
     "topics": ["technology", "business", "science"],
     "max_articles": 6,
     "send_email": true,
     "email_recipients": ["your_email@gmail.com"]
   }
   ```

6. **Run the application**
   ```bash
   python main.py
   ```

## 📸 Screenshots

<div align="center">

### Dark Theme Interface

<img width="1256" height="836" alt="image" src="https://github.com/user-attachments/assets/85638caf-08d5-49c9-af7c-596e234b1bd1" />


</div>

## 🛠️ Tech Stack

| Component | Technology |
|-----------|------------|
| **Backend** | Python 3.8+ |
| **AI/ML** | Hugging Face Transformers, NLTK, spaCy |
| **APIs** | NewsAPI, SMTP |
| **Frontend** | HTML5, CSS3, Vanilla JavaScript |
| **Design** | Glassmorphism, CSS Grid, Animations |
| **Email** | HTML Templates, SMTP |

## ⚙️ Configuration

### News Sources
Customize your news sources in `user_preferences.json`:
```json
{
  "topics": ["technology", "sports", "business"],
  "sources": ["bbc-news", "cnn", "techcrunch"],
  "max_articles": 10,
  "summary_length": 3
}
```

### Email Settings
Configure email delivery:
```json
{
  "send_email": true,
  "email_recipients": ["user1@example.com", "user2@example.com"],
  "send_time": "08:00"
}
```

## 🎨 Features Overview

### AI Summarization
- **Primary**: Facebook BART model for abstractive summarization
- **Fallback**: Extractive summarization using TF-IDF
- **Smart Processing**: Dynamic length adjustment based on content

### Frontend Design
- **Glassmorphism UI** with backdrop filters
- **Animated gradients** and floating particles
- **Smooth hover effects** and transitions
- **Responsive grid layout**
- **Auto-generated content** from real news data

### Email Integration
- **HTML email templates** with inline CSS
- **Professional styling** matching the web theme
- **Article cards** with source attribution
- **Direct links** to full articles

## 📊 Performance

- **Processing Time**: ~30-60 seconds for 6 articles
- **Memory Usage**: ~200MB (includes AI models)
- **Storage**: HTML files ~500KB, Text backups ~50KB
- **Email Delivery**: <5 seconds via SMTP

## 🔧 API Keys Setup

### NewsAPI
1. Go to [NewsAPI.org](https://newsapi.org/)
2. Create free account (100 requests/day)
3. Copy your API key to `.env`

### Gmail App Password
1. Enable 2-Factor Authentication
2. Go to Google Account → Security → App Passwords
3. Generate password for "Mail"
4. Use this password in `.env` (not your regular password)

## 🤝 Contributing

Contributions are welcome! Here are some ways you can help:

- 🐛 **Bug Reports**: Found an issue? Open an issue with details
- 💡 **Feature Requests**: Have ideas? Let's discuss them
- 🔧 **Code Contributions**: Fork, develop, and submit PRs
- 📖 **Documentation**: Help improve our docs
- 🎨 **UI/UX**: Design improvements and suggestions

### Development Setup
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📈 Roadmap

- [ ] **Web Dashboard** - Real-time web interface with refresh buttons
- [ ] **Database Integration** - Store articles and summaries
- [ ] **Sentiment Analysis** - Add emotional context to summaries
- [ ] **Discord Bot** - Deliver summaries via Discord
- [ ] **Mobile App** - React Native companion app
- [ ] **RSS Feeds** - Support for RSS/Atom feed sources
- [ ] **Multi-language** - Support for multiple languages
- [ ] **Analytics Dashboard** - Track reading patterns and preferences

## 🐛 Troubleshooting

### Common Issues

**"Module not found" errors**
```bash
# Ensure virtual environment is activated
news_env\Scripts\activate  # Windows
source news_env/bin/activate  # macOS/Linux

# Reinstall dependencies
pip install -r requirements.txt
```

**"API key not found" errors**
```bash
# Check .env file exists and has correct format
# No quotes around values, no spaces around =
NEWS_API_KEY=your_actual_key_here
```

**Email sending fails**
```bash
# Use Gmail App Password, not regular password
# Enable 2-Factor Authentication first
# Check SMTP settings in .env
```

### Debug Mode
Enable detailed logging:
```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Hugging Face** for the amazing Transformers library
- **NewsAPI** for reliable news data
- **Facebook AI** for the BART summarization model
- **The Python Community** for excellent libraries and tools

## 📞 Contact

- **GitHub**: [@yourusername](https://github.com/yourusername)
- **LinkedIn**: [Your LinkedIn](https://linkedin.com/in/yourprofile)
- **Email**: your.email@example.com

---

<div align="center">

**⭐ Star this repo if you found it helpful! ⭐**

Made with ❤️ and lots of ☕

</div>
