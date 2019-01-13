import os 


def MemWin():
    os.system("dxdiag /t file")
    arq = open('file.txt', 'r')
    for linha in arq:
        if linha.find("Display Memory:") > -1 or linha.find("Shared Memory:") > -1:
            graf = print(linha.lstrip(" "))

    arq.close()
