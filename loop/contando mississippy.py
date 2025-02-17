# Você sabe o que é o Mississipi? Bem, é o nome de um dos estados e riachos dos Estados Unidos. O Rio Mississipi tem cerca de 2.340 milhas de comprimento, o que o torna o segundo maior rio dos Estados Unidos (o mais longo é o Rio Missouri). É tão longo que uma única gota de água precisa de 90 dias para percorrer todo o seu comprimento!

# A palavra Mississipi também é usada para uma finalidade ligeiramente diferente: contar com erros de sorte.

# Se você não está familiarizado com a frase, estamos aqui para explicar o que ela significa: ela é usada para contar segundos.

# A ideia por trás disso é que adicionar a palavra Mississipi a um número ao contar segundos em voz alta faz com que soem mais perto do relógio e, portanto, "um Mississipi, dois Mississipi, três Mississaipi" levará aproximadamente três segundos reais! É frequentemente usado por crianças que brincam de esconde-esconde para garantir que o candidato faça uma contagem honesta.

# Sua tarefa é muito simples aqui: escreva um programa que use um loop for para "contar de forma incorreta" para cinco. Depois de contar até cinco, o programa deve imprimir na tela a mensagem final "Pronto ou não, aqui vou eu!"
import time

for i in range(1, 6):
    print(f"{i} Mississippi")
    time.sleep(1)

print("Pronto ou não, aqui vou eu!")
