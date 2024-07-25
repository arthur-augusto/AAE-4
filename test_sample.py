import pytest

agenda = [
    {
        'nome': 'natacao',
        'horaInicio': '2024-07-25 14:42',
        'horaTermino': '2024-07-25 15:42' 
    },
]


def add_evento(nome, horaInicio, horaTermino):
    # Gerenciar conflito      
    e = {
        'nome': nome,
        'hora-inicio': horaInicio,
        'hora-termino': horaTermino,
    }
  
    agenda.append(e)
    return e 

def test_adicionatest():
    assert add_evento('ginastica', '2024-07-26 12:00', '2024-07-26 14:00') == agenda[0]

def test_adicionatest2():
    assert add_evento('natacao', '2024-07-25 14:42', '2024-07-25 15:42') == agenda[2]

