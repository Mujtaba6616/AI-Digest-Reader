from transformers import pipeline
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
import re
from collections import Counter

class ArticleSummarizer:
    def __init__(self):
        # Initialize Hugging Face summarization pipeline
        try:
            self.summarizer = pipeline("summarization", 
                                     model="facebook/bart-large-cnn")
        except:
            print("⚠️ BART model failed, using extractive summarization")
            self.summarizer = None
        
        # Download required NLTK data if not present
        try:
            nltk.data.find('tokenizers/punkt')
        except LookupError:
            nltk.download('punkt')
        
        try:
            nltk.data.find('corpora/stopwords')
        except LookupError:
            nltk.download('stopwords')
    
    def clean_text(self, text):
        """Clean and preprocess text"""
        # Remove truncation indicators
        text = re.sub(r'\[\+\s*\d+\s*chars?\]', '', text)
        text = re.sub(r'\[\+\s*\d+\s*characters?\]', '', text)
        
        # Remove extra whitespace and clean text
        text = re.sub(r'\s+', ' ', text)
        text = re.sub(r'[^\w\s.,!?-]', '', text)
        return text.strip()
    
    def extractive_summary(self, text, num_sentences=2):
        """Create extractive summary using sentence scoring"""
        try:
            sentences = sent_tokenize(text)
            if len(sentences) <= 2:
                return text
            
            # Score sentences based on word frequency
            words = word_tokenize(text.lower())
            stop_words = set(stopwords.words('english'))
            words = [word for word in words if word.isalnum() and word not in stop_words]
            
            word_freq = Counter(words)
            
            sentence_scores = {}
            for sentence in sentences:
                sentence_words = word_tokenize(sentence.lower())
                score = 0
                word_count = 0
                
                for word in sentence_words:
                    if word in word_freq:
                        score += word_freq[word]
                        word_count += 1
                
                if word_count > 0:
                    sentence_scores[sentence] = score / word_count
            
            # Get top sentences
            top_sentences = sorted(sentence_scores.items(), key=lambda x: x[1], reverse=True)
            summary_sentences = [sent[0] for sent in top_sentences[:num_sentences]]
            
            # Maintain original order
            summary = []
            for sentence in sentences:
                if sentence in summary_sentences:
                    summary.append(sentence)
            
            return ' '.join(summary)
            
        except Exception as e:
            print(f"❌ Extractive summarization error: {e}")
            sentences = sent_tokenize(text)
            return ' '.join(sentences[:2])
    
    def summarize(self, text, max_length=3):
        """Main summarization method with multiple fallbacks"""
        try:
            # Clean the text first
            clean_text = self.clean_text(text)
            
            # If text is very short, return as is
            if len(clean_text) < 100:
                return clean_text
            
            # Method 1: Try AI summarization if available
            if self.summarizer:
                try:
                    # Limit input length for the model
                    if len(clean_text) > 1024:
                        clean_text = clean_text[:1024]
                    
                    summary = self.summarizer(
                        clean_text, 
                        max_length=100,
                        min_length=40,
                        do_sample=False
                    )
                    
                    result = summary[0]['summary_text']
                    if len(result) > 50:  # Valid summary
                        return result
                        
                except Exception as e:
                    print(f"❌ AI Summarization failed: {e}")
            
            # Method 2: Extractive summarization fallback
            return self.extractive_summary(clean_text, num_sentences=2)
            
        except Exception as e:
            print(f"❌ All summarization methods failed: {e}")
            # Final fallback: first 2 sentences
            sentences = sent_tokenize(text)
            return ' '.join(sentences[:2]) if sentences else text[:200] + "..."