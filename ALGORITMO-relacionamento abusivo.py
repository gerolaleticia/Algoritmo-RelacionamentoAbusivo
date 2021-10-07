from __future__ import print_function, unicode_literals
from time import sleep
from os import system, name
from PyInquirer import prompt


def clear():
    # windows
    if name == "nt":
        _ = system("cls")

    # mac e linux(os.name = 'posix')
    else:
        _ = system("clear")


def introducao() -> None:
    clear()
    print("-=" * 20)
    print(
        "\033[31m Olá! Este algoritmo te ajuda a saber se você se encontra em um relacionamento abusivo.\033[m"
    )
    print("-=" * 20)
    sleep(3)
    print(
        "\033[31mSerão 10 perguntas no total. Para responder as questões, utilize as setas do teclado e ENTER para selecionar as opções."
    )
    sleep(3)
    print("\033[31mVamos começar!\033[37m")
    sleep(3)


def criar_perguntas():
    opcoes_resposta = ["Frequentemente", "Às vezes", "Raramente", "Nunca me aconteceu"]
    perguntas = [
        {
            "type": "list",
            "name": "p1",
            "message": "Pergunta 1: O ciúme do seu parceiro alguma vez virou argumento para controlar\nsuas decisões, adentrar sua privacidade e/ou já levou a ofensas?",
            "choices": opcoes_resposta,
        },
        {
            "type": "list",
            "name": "p2",
            "message": 'Pergunta 2: "Por que eu te amo demais" ou "é para o seu bem" e\ou similares já foram utilizados\npelo seu parceiro para indicar roupas que você devia vestir, atividades que devia fazer, etc? ',
            "choices": opcoes_resposta,
        },
        {
            "type": "list",
            "name": "p3",
            "message": 'Pergunta 3: Seu parceiro já teve acesso a senhas pessoais, mexeu no seu celular ou leu mensagens suas \nsem o seu conhecimento?(Ou sob a justificativa de que "quem ama não tem nada a esconder"?',
            "choices": opcoes_resposta,
        },
        {
            "type": "list",
            "name": "p4",
            "message": 'Pergunta 4: Você já se afastou de algumas amizades para evitar conflito com seu parceiro? Ou "fulano é má influência" ou \n"ciclano dé encima de você" são frases que você costuma ouvir?',
            "choices": opcoes_resposta,
        },
        {
            "type": "list",
            "name": "p5",
            "message": 'Pergunta 5: Você já percebeu seu parceiro utilizando frases de chantagem para conseguir o que quer? \n"Vou ficar doente assim" ou "vou me matar" ou algo específico que ele saiba que mexe com você?',
            "choices": opcoes_resposta,
        },
        {
            "type": "list",
            "name": "p6",
            "message": 'Pergunta 6: "Críticas construtivas" são cada vez mais comuns e um pesadas?',
            "choices": opcoes_resposta,
        },
        {
            "type": "list",
            "name": "p7",
            "message": 'Pergunta 7: Se você diz que ficou chateada com alguma coisa que ele falou ou fez, costuma ouvir que é\n"besteira sua" ou "drama" e derivados?',
            "choices": opcoes_resposta,
        },
        {
            "type": "list",
            "name": "p8",
            "message": "Pergunta 8: Seu parceiro já insistiu em uma relação sexual mesmo após você ter dito não? Ou já tentou \niniciar uma relação sexual com você dormindo\desacordada\etc?",
            "choices": opcoes_resposta,
        },
        {
            "type": "list",
            "name": "p9",
            "message": "Pergunta 9: Seu parceiro tem acesso ao seu dinheiro? Se sim, com que frequência ele tenta controlar\nos seus gastos ou fazê-la se sentir mal com suas decisões financeiras?",
            "choices": opcoes_resposta,
        },
        {
            "type": "list",
            "name": "p10",
            "message": "Pergunta 10: Tirar dinheiro, sumir com os filhos, agressões verbais ou outros tipos de ameaça já foram feitas a você?",
            "choices": opcoes_resposta,
        },
    ]
    return perguntas


def pegar_score(respostas) -> float:
    score = 0.0
    opcoes_resposta = {
        "Frequentemente": 2.0,
        "Às vezes": 1.0,
        "Raramente": 0.5,
        "Nunca me aconteceu": 0,
    }
    for key in respostas:
        resposta = respostas[key]
        score += opcoes_resposta[resposta]

    return score


def print_resultado(score):
    print(score)
    print("\n")
    if score > 10:
        print("\33[1:36mRESULTADO: Seu relacionamento é abusivo! Peça ajuda!\33[m")
    elif score > 7 and score <= 10:
        print(
            "\33[1:34mRESULTADO: Seu relacionamento tem MUITOS momentos abusivos. Peça ajuda!\33[m"
        )
    elif score > 4 and score <= 7:
        print(
            "\33[1:35mRESULTADO: Seu relacionamento tem alguns momentos abusivos. Fique atenta!\33[m"
        )
    elif score <= 4:
        print(
            "\33[1:33mRESULTADO: Aparentemente não há muitos sinais abusivos. Mantenha-se alerta!\33[m"
        )


def main():
    introducao()
    perguntas = criar_perguntas()
    respostas = prompt(perguntas)
    score = pegar_score(respostas)
    print_resultado(score)


if __name__ == "__main__":
    main()
