from pytest_bdd import scenario, given, when, then
from app.logic import TextAnalyzer

@scenario('../../features/analyzer.feature', 'Detectar palabra prohibida')
def test_spam_detection():
    pass

@given('que el analizador está listo', target_fixture="analyzer")
def analyzer():
    return TextAnalyzer()

@when('analizo el texto "Esta es una oferta secreta"', target_fixture="result")
def analyze(analyzer):
    return analyzer.has_forbidden_word("Esta es una oferta secreta", "oferta")

@then('el sistema debe marcar que tiene spam')
def check_result(result):
    assert result is True

#python -m pytest tests/steps/test_bdd.py