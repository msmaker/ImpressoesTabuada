def tabuadas(n1,n2):
    if(n2 < n1):
        print("Nenhuma tabuada nesse intervalo")
    else:
        for i in range (n1,n2+1):
            for j in range(1,10):
                print(i , "x" , j , "=" , (i * j))
            print()

valor = 0;
n1 = 0
n2 = 0

while(valor == 0):
    n1 = int(input())
    if(n1 > 0 and n1 <= 9):
        valor = 1
    else:
        print("Insira um número inicial entre 1 e 9")

valor = 0

while(valor == 0):
    n2 = int(input())
    if(n2 > 0 and n2 <= 9):
        valor = 1
    else:
        print("Insira um número final entre 1 e 9")

tabuadas(n1,n2)




