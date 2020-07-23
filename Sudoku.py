from tkinter import *
from random import *

def preencher(Matriz,n):
    for i in range(n):
        L = randint(0,8)
        C = randint(0,8)
        X = randint(1,9)
        while True:
            if X not in Matriz[L] and X not in tmatriz[C]:
                Matriz[L][C] = X
                tmatriz[C][L] = X
                break
            else:
                X = randint(1,9)


def Regioes(Matriz):

    SUDOKU = []
    SUDOKU_FINAL = []
    for i in range(0,9,3):
        for j in range(0,9,3):
            MR = []
            for Lin in range(3):
                for Col in range(3):
                    MR += [Matriz[i + Lin][j + Col]]
            Lista = []
            for a in range(len(MR)):
                if a == " ":
                    Lista += [MR[a]]
                elif MR[a] == " ":
                    Lista += [MR[a]]
                else:
                    while True:
                        if MR[a] in Lista:
                            MR[a] = randint(1,9)
                        elif MR[a] not in Lista:
                            Lista += [MR[a]]
                            break

            MR = [MR[i:i+3] for i in range(0, len(MR), 3)]
            for b in range(len(MR)):
                SUDOKU.append(MR[b])
    lista = []
    cont1 = 0
    cont2 = 3
    cont3 = 6
    for i in range(9):
        if i == 3:
            cont1 = 9
            cont2 = 12
            cont3 = 15
        if i > 3 and i <= 5:
            cont1 += 1
            cont2 += 1
            cont3 += 1
        if i == 6:
            cont1 = 18
            cont2 = 21
            cont3 = 24
        if i > 6:
            cont1 += 1
            cont2 += 1
            cont3 += 1

        for j in range(3):
            lista.append(SUDOKU[cont1][j])
        for j in range(3):
            lista.append(SUDOKU[cont2][j])
        for j in range(3):
            lista.append(SUDOKU[cont3][j])

        if i <= 2:
            cont1 += 1
            cont2 += 1
            cont3 += 1

        SUDOKU_FINAL.append(lista)
        lista = []
    return SUDOKU_FINAL
def removerPorIndice(i, lista):
    novaLista = []
    for n in range(0, i):
        novaLista += [lista[n]]

    for n in range(i, len(lista) - 1):
        novaLista += [lista[n + 1]]

    return novaLista


def verificarLinha(linha, numeros):
    num = numeros[:]
    for n in linha:
        cont = 0
        for j in num:
            if (n == j):
                num = removerPorIndice(cont, num)
            cont += 1
    if (num == []):
        return True

    return False


def verificarSudoku(matriz):
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for n in range(0, 9):
        if (verificarLinha(matriz[n], numeros) == False):
            return "NAO"

    for coluna in range(0, 9):
        col = []
        for linha in range(0, 9):
            col += [matriz[linha][coluna]]
        if (verificarLinha(col, numeros) == False):
            return "NAO"

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            matrizLinha = []
            for auxLin in range(0, 3):
                for auxCol in range(0, 3):
                    matrizLinha += [matriz[i + auxLin][j + auxCol]]
            if (verificarLinha(matrizLinha, numeros) == False):
                return "NAO"

    return "SIM"

def bt_clickf():
    janela.destroy()
    preencher(matriz, n=20)
    global janela2
    janela2 = Tk()
    janela2.geometry("594x639+370+10")
    menu = Menu(janela2)
    file = Menu(menu)
    menu.add_cascade(label="Menu(verificação)", menu=file)
    janela2.config(menu=menu)
    file.add_command(label="Reiniciar", command=lambda: inicio(1))
    file.add_command(label="Verificar", command=verificaganhou)
    print(matriz)
    x = Regioes(matriz)
    for c in x:
        print(*c)
    crateGrid()


def bt_clickm():
    janela.destroy()
    preencher(matriz, n=15)
    global janela2
    janela2 = Tk()
    janela2.geometry("594x639+370+10")
    menu = Menu(janela2)
    file = Menu(menu)
    menu.add_cascade(label="Menu(verificação)", menu=file)
    janela2.config(menu=menu)
    file.add_command(label="Reiniciar", command=lambda: inicio(1))
    file.add_command(label="Verificar", command=verificaganhou)
    for x in matriz:
        print(*x)
    crateGrid()

    janela2.mainloop()
def bt_clickd():
    janela.destroy()
    preencher(matriz, n=10)
    global janela2
    janela2 = Tk()
    janela2.geometry("594x639+370+10")
    menu = Menu(janela2)
    file = Menu(menu)
    menu.add_cascade(label="Menu(verificação)", menu=file)
    janela2.config(menu=menu)
    file.add_command(label="Reiniciar", command=lambda: inicio(1))
    file.add_command(label="Verificar", command=verificaganhou)
    for x in matriz:
        print(*x)
    crateGrid()
    janela2.mainloop()
def verificaganhou():
    global janela4
    janela4 = Tk()
    if verificarSudoku(a) == "NAO":
        lb = Label(janela4, text="SUDOKU COMPLETADO INCORRETAMENTE!")
        lb.pack()
        breset = Button(janela4, text="Reiniciar", width=14, height=4, command= lambda: inicio(2))
        breset.pack()
    elif verificarSudoku(a) == "SIM":
        lb = Label(janela4, text="SUDOKU COMPLETADO CORRETAMENTE!")
        lb.pack()
        breset = Button(janela4, text="Reiniciar", width=14, height=4, command=lambda: inicio(2))
        breset.pack()
    janela4.geometry("460x100+430+75")
    janela4.mainloop()
def printnum(op2, row, col):
    list = [1, 2, 3, 4, 5, 6, 7, 8 , 9]
    janela3.destroy()
    matrizbotoes[row][col]["text"] = op2
    a[row][col] = op2
def colocanumeros(row, col):
    cont = 0
    global janela3
    janela3 = Tk()
    janela3.geometry("+110+55")
    for c in range(3):
        for j in range(3):
            cont+=1
            b1 = Button(janela3, width=8, height=4, text=cont, command=lambda cont=cont: printnum(cont, row, col))
            b1.grid(row=c, column=j, sticky=N + S + E + W)

    janela3.mainloop()
def crateGrid():
    global a
    a = Regioes(matriz)
    for rowindex in range (9):
        for colindex in range (9):
            if (rowindex in (0,1,2,6,7,8) and colindex in (3,4,5) or \
                (rowindex in (3,4,5) and colindex in (0,1,2,6,7,8))):
                    colour="light gray"
            else:
                colour="white"
            x = a[rowindex][colindex]
            if x==" ":
                matrizbotoes[rowindex][colindex]= Button(janela2, width=8, height=4, bg=colour, text=x, cursor="plus")
                matrizbotoes[rowindex][colindex].config(command= lambda rowindex=rowindex, colindex=colindex: colocanumeros(rowindex, colindex))
                matrizbotoes[rowindex][colindex].grid(row=rowindex, column=colindex, sticky=N + S + E + W)

            else:
                colourTxt="black"
                btn1 = Button(janela2, width=8, height=4, bg=colour, text=x, fg=colourTxt)
                btn1.grid(row=rowindex, column=colindex, sticky=N + S + E + W)
                matrizbotoes[rowindex][colindex] = btn1


def inicio(x):
    global matriz, tmatriz, matrizbotoes
    matriz = [[" " for i in range(9)] for j in range(9)]
    tmatriz = [[" " for i in range(9)] for j in range(9)]
    matrizbotoes = [[0 for i in range(9)] for j in range(9)]
    if x == 1:
        janela2.destroy()
    elif x == 2:
        janela2.destroy()
        janela4.destroy()
    global janela
    janela = Tk()
    janela.title("SUDOKU")
    janela["bg"] = "light gray"
    # janela["bg"] = "black" (Trocar de cor)
    lb = Label(janela, text="ESCOLHA A DIFICULDADE")
    lb["bg"] = "light gray"
    lb.pack()
    bt_facil = Button(janela, width=17, height=6, text="Fácil", command=bt_clickf)
    bt_facil.place(x=20, y=140)
    bt_medio = Button(janela, width=17, height=6, text="Médio", command=bt_clickm)
    bt_medio.place(x=165, y=140)
    bt_dificil = Button(janela, width=17, height=6, text="Difícil", command=bt_clickd)
    bt_dificil.place(x=310, y = 140)


    janela.geometry("460x300+430+75") #LarguraxAltura+Esquerda+Topo

    janela.mainloop( )

inicio(0)