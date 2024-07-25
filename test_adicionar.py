import pytest
from main import *

def test_adicionarEvento():
    # Limpar a agenda antes do teste
    agenda.clear()

    # Adicionar o evento
    addEvento('ginastica', '2024-07-26 12:00', '2024-07-26 14:00')

    # Verificar se o evento foi adicionado corretamente
    assert agenda[-1] == {
        "nome": 'ginastica',
        "inicio": '2024-07-26 12:00',
        "termino": '2024-07-26 14:00'
    }

