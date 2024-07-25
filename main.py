agenda = []

def addEvento(nomeEvento, horaInicio, horaTermino):
    evento = {
        "nome": nomeEvento,
        "inicio": horaInicio,
        "termino": horaTermino
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
        
        else:
            print("Ação inválida. Tente novamente.")
        
if __name__ == "__main__":
    main()
