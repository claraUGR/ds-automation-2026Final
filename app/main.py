from fastapi import FastAPI
from app.logic import TextAnalyzer

app = FastAPI()
analyzer = TextAnalyzer()

@app.get("/analyze")
def analyze_text(text: str):
    return {
        "word_count": analyzer.count_words(text),
        "has_spam": analyzer.has_forbidden_word(text, "oferta")
    }