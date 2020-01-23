print('-='*20)
print('\033[31m Olá! Este algoritmo te ajuda a saber se você se encontra em um relacionamento abusivo.\033[m')
print('-='*20)
from time import sleep
sleep(3)
print('\033[31mSerão 10 perguntas no total. Para responder as questões, utilize números: 2, 1, 0.5 ou 0. \nCada número corresponde à opção abaixo:\033[m \n \033[1:36m 2 --> frequentemente \n \033[1:34m 1 --> às vezes \n \033[1:35m 0.5 --> raramente \n \033[1:33m 0 --> nunca me aconteceu\033[m')
sleep(8)
print('\033[31mApós identificar & digitar o número que corresponde à sua resposta, precione ENTER. Vamos começar!')
sleep(4)
p1 = float(input('\033[37mPergunta 1: O ciúme do seu parceiro alguma vez virou argumento para controlar\nsuas decisões, adentrar sua privacidade e/ou já levou a ofensas? '))
print('-='*20)
if p1 > 2:
    print('\33[1:33:41mOps! O número digitado não corresponde à uma resposta. Tente novamente na próxima.\33[m')
    print('-=' * 20)
p2 = float(input('Pergunta 2: "Por que eu te amo demais" ou "é para o seu bem" e\ou similares já foram utilizados\npelo seu parceiro para indicar roupas que você devia vestir, atividades que devia fazer, etc? '))
print('-='*20)
if p2 > 2:
    print('\33[1:33:41mOps! O número digitado não corresponde à uma resposta. Tente novamente na próxima.\33[m')
    print('-=' * 20)
p3 = float(input('Pergunta 3: Seu parceiro já teve acesso a senhas pessoais, mexeu no seu celular ou leu mensagens suas \nsem o seu conhecimento?(Ou sob a justificativa de que "quem ama não tem nada a esconder"? '))
print('-='*20)
if p3 > 2:
    print('\33[1:33:41mOps! O número digitado não corresponde à uma resposta. Tente novamente na próxima.\33[m')
    print('-=' * 20)
p4 = float(input('Pergunta 4: Você já se afastou de algumas amizades para evitar conflito com seu parceiro? Ou "fulano é má influência" ou \n"ciclano dé encima de você" são frases que você costuma ouvir? '))
print('-='*20)
if p4 > 2:
    print('\33[1:33:41mOps! O número digitado não corresponde à uma resposta. Tente novamente na próxima.\33[m')
    print('-=' * 20)
p5 = float(input('Pergunta 5: Você já percebeu seu parceiro utilizando frases de chantagem para conseguir o que quer? \n"Vou ficar doente assim" ou "vou me matar" ou algo específico que ele saiba que mexe com você? '))
print('-='*20)
if p5 > 2:
    print('\33[1:33:41mOps! O número digitado não corresponde à uma resposta. Tente novamente na próxima.\33[m')
    print('-=' * 20)
p6 = float(input('Pergunta 6: "Críticas construtivas" são cada vez mais comuns e um pesadas? '))
print('-='*20)
if p6 > 2:
    print('\33[1:33:41mOps! O número digitado não corresponde à uma resposta. Tente novamente na próxima.\33[m')
    print('-=' * 20)
p7 = float(input('Pergunta 7: Se você diz que ficou chateada com alguma coisa que ele falou ou fez, costuma ouvir que é\n"besteira sua" ou "drama" e derivados? '))
print('-='*20)
if p7 > 2:
    print('\33[1:33:41mOps! O número digitado não corresponde à uma resposta. Tente novamente na próxima.\33[m')
    print('-=' * 20)
p8 = float(input('Pergunta 8: Seu parceiro já insistiu em uma relação sexual mesmo após você ter dito não? Ou já tentou \niniciar uma relação sexual com você dormindo\desacordada\etc? '))
print('-='*20)
if p8 > 2:
    print('\33[1:33:41mOps! O número digitado não corresponde à uma resposta. Tente novamente na próxima.\33[m')
    print('-=' * 20)
p9 = float(input('Pergunta 9: Seu parceiro tem acesso ao seu dinheiro? Se sim, com que frequência ele tenta controlar\nos seus gastos ou fazê-la se sentir mal com suas decisões financeiras? '))
print('-='*20)
if p9 > 2:
    print('\33[1:33:41mOps! O número digitado não corresponde à uma resposta. Tente novamente na próxima.\33[m')
    print('-=' * 20)
p10 = float(input('Pergunta 10: Tirar dinheiro, sumir com os filhos, agressões verbais ou outros tipos de ameaça já foram feitas a você? '))
if p10 > 2:
    print('\33[1:33:41mOps! O número digitado não corresponde à uma resposta. Tente novamente na próxima.\33[m')
    print('-=' * 20)
if p1 + p2 + p3 + p4 + p5 + p6 + p7 + p8 + p9 + p10 >11:
    print('\33[1:36mRESULTADO: Seu relacionamento é abusivo! Peça ajuda!\33[m')
if p1 + p2 + p3 + p4 + p5 + p6 + p7 + p8 + p9 + p10 >7 and p1 + p2 + p3 + p4 + p5 + p6 + p7 + p8 + p9 + p10 <=10:
    print('\33[1:34mRESULTADO: Seu relacionamento tem MUITOS momentos abusivos. Peça ajuda!\33[m')
if p1 + p2 + p3 + p4 + p5 + p6 + p7 + p8 + p9 + p10 >4 and p1 + p2 + p3 + p4 + p5 + p6 + p7 + p8 + p9 + p10 <=6:
    print('\33[1:35mRESULTADO: Seu relacionamento tem alguns momentos abusivos. Fique atenta!\33[m')
if p1 + p2 + p3 + p4 + p5 + p6 + p7 + p8 + p9 + p10 <= 3:
    print('\33[1:33mRESULTADO: Aparentemente não há muitos sinais abusivos. Mantenha-se alerta!\33[m')
