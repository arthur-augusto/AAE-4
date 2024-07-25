import pytest
from main import *

def test_removerEvento_existente():
   
    addEvento('natação', '2024-07-26 15:00', '2024-07-26 16:00')
    removerEvento('natação')
    
    # Verificar se o evento foi removido corretamente
    assert not any(evento['nome'] == 'natação' for evento in agenda)