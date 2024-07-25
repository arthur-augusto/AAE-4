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

def test_dataHoraValida():

    assert validarDataHora("Teste falho") is False
    assert validarDataHora("2024-07-26 12:00") is True
    

    # Verificar se os horários de início e término estão no horário correto

def test_conflitoAgenda():
    
    agenda.clear()

    addEvento('ginastica', '2024-07-26 12:00', '2024-07-26 14:00')
    addEvento('natacao', '2024-07-26 12:00', '2024-07-26 14:00')

    assert agenda[-1] == {
        "nome": 'ginastica',
        "inicio": '2024-07-26 12:00',
        "termino": '2024-07-26 14:00'
    }
