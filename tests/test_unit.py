from app.logic import TextAnalyzer

def test_word_count():
    ta = TextAnalyzer()
    assert ta.count_words("Hola mundo") == 2

def test_empty_text():
    ta = TextAnalyzer()
    assert ta.count_words("") == 0

# def test_strange_character():
#     ta = TextAnalyzer()
#     assert ta.count_words("*") == 1

# python -m pytest tests/test_unit.py
