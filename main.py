from datetime import datetime

agenda = [{

    "nome": "Reunião de equipe",
    "inicio": "2021-10-01 09:00",
    "termino": "2021-10-01 10:00"
}]

def validarDataHora(dataHora):
    try:
        datetime.strptime(dataHora, "%Y-%m-%d %H:%M")
        return True
    except ValueError:
        return False

def verificarConflito(dataHoraInicio, dataHoraTermino):
    inicioNovo = datetime.strptime(dataHoraInicio, "%Y-%m-%d %H:%M")
    terminoNovo = datetime.strptime(dataHoraTermino, "%Y-%m-%d %H:%M")
    
    for evento in agenda:
        inicioExistente = datetime.strptime(evento["inicio"], "%Y-%m-%d %H:%M")
        terminoExistente = datetime.strptime(evento["termino"], "%Y-%m-%d %H:%M")
        
        if (inicioNovo < terminoExistente and terminoNovo > inicioExistente):
            return True
    return False

def addEvento(nomeEvento, dataHoraInicio, dataHoraTermino):
    if not validarDataHora(dataHoraInicio):
        print("Erro: A hora de início é inválida. O formato correto é YYYY-MM-DD HH:MM.")
        return
    
    if not validarDataHora(dataHoraTermino):
        print("Erro: A hora de término é inválida. O formato correto é YYYY-MM-DD HH:MM.")
        return
    
    if verificarConflito(dataHoraInicio, dataHoraTermino):
        print("Erro: Conflito de agendamento detectado.")
        return
    
    evento = {
        "nome": nomeEvento,
        "inicio": dataHoraInicio,
        "termino": dataHoraTermino
    }
    agenda.append(evento)
    print("Evento adicionado com sucesso.")

def main():
    while True:
        resposta = input("Digite a ação (adicionar, remover, mostrar, sair): ")
        
        if resposta == "adicionar":
            nomeEvento = input("Digite o nome do evento: ")
            horaInicio = input("Digite a hora de início (YYYY-MM-DD HH:MM): ")
            horaTermino = input("Digite a hora de término (YYYY-MM-DD HH:MM): ")
            
            addEvento(nomeEvento, horaInicio, horaTermino)
        
        elif resposta == "sair":
            break
        
        else:
            print("Ação inválida. Tente novamente.")
        
if __name__ == "__main__":
    main()
