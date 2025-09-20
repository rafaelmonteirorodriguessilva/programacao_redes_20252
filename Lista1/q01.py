velocidade = int (input( "Digite a velocidade de download de sua conexão: "))

if velocidade < 10: 
    print("Conexão lenta")
else:
    if velocidade > 10 and velocidade <= 100:
        print("Conexão Normal")
    else:   
        print("Conexão Rápida")


        