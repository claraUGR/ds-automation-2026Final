Feature: Análisis de Spam
  Scenario: Detectar palabra prohibida
    Given que el analizador está listo
    When analizo el texto "Esta es una oferta secreta"
    Then el sistema debe marcar que tiene spam