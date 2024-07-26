import pytest
from main import listarEventos, agenda, addEvento

def test_semEventos(capfd):
    agenda.clear()
    listarEventos()
    out, err = capfd.readouterr()
    assert out == "Não há eventos na agenda.\n"

def test_comEventos(capfd):
    agenda.clear()
    addEvento('ginastica', '2024-07-27 12:00', '2024-07-27 14:00')
    addEvento('natacao', '2024-07-26 12:00', '2024-07-26 14:00')
    listarEventos()
    out, err = capfd.readouterr()
    expected_output = (
        "Evento adicionado com sucesso.\n"
        "Evento adicionado com sucesso.\n"
        "Nome: ginastica\n"
        "Início: 2024-07-27 12:00\n"
        "Término: 2024-07-27 14:00\n\n"
        "Nome: natacao\n"
        "Início: 2024-07-26 12:00\n"
        "Término: 2024-07-26 14:00\n\n"
    )
    assert out == expected_output