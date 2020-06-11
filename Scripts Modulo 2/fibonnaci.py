import time
import sys
def fibonnaci_recursivo(n):
    if n == 0 or n == 1:
        return 1
    
    return fibonnaci_recursivo(n - 1) + fibonnaci_recursivo(n - 2)

def fibonnaci_dinamico(n, memo = {}):
    if n == 0 or n == 1:
        return 1
    
    try:
        return memo[n]
    except KeyError as e:
        resultado = fibonnaci_dinamico(n - 1, memo) + fibonnaci_dinamico(n - 2, memo)
        memo[n] = resultado
        print(memo)
        return resultado
        
if __name__ == "__main__":
    sys.setrecursionlimit(1000002)
    n = int(input('Escogeun numero: '))
    comienzo = time.time()
    resultado = fibonnaci_dinamico(n)
    print(resultado)
    final = time.time()
    print(final - comienzo)
