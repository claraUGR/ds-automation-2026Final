class TextAnalyzer:
    def count_words(self, text: str) -> int:
        if not text:
            return 0
        return len(text.split())

    def has_forbidden_word(self, text: str, word: str) -> bool:
        return word.lower() in text.lower()