# Curso de Programación Dinámica y Estocástica con Python

## Modulo 1. Introducción

### Clase 1 Objetivo del Curso

Debes contar con conocimientos de complejidad algoritmica, por lo que es necesario repasar esos conocimientos. Veremos las diferencias entre  la programacion estocastica(cuando no tenemos certeza acerca de los datos con que vamos a trabajar) y la programacion deterministica (con la que siempre he trabajado).

## Modulo 2. Programación Dinámica

### clase 2 Introducción a la Programación Dinámica

En la década de los 50s Richard Bellman necesitaba financiamiento del gobierno para poder continuar con sus investigaciones, por lo que necesitaba un nombre rimbombante para que no fueran capaz de rechazar su solicitud, por lo que eligió programación dinámica. Las propias palabras de Bellman fueron:

“[El nombre] Programación Dinámica se escogió para esconder a patrocinadores gubernamentales el hecho que en realidad estaba haciendo Matemáticas. La frase Programación Dinámica es algo que ningún congresista puede oponerse.” - Richard Bellman.

Ya sabiendo que Programación Dinámica no esta relacionado con su nombre, lo cierto es que si **es una de las técnicas mas poderosas para poder optimizar cierto tipos de problemas**.

Los problemas que puede optimizar son aquellos que tienen una **subestructura óptima**, esto significa que una solución óptima global se puede encontrar al combinar soluciones óptimas de subproblemas locales (_divide y venceras_).

También nos podemos encontrar con los **problemas empalmados**, los cuales implican resolver el mismo problema en varias ocasiones para dar con una solución óptima (recursividad).

#### Memoizaation

- Una técnica para obtener una alta velocidad en nuestro programa es la Memorización, el cual consiste en guardar cómputos previos y evitar realizarlos nuevamente.
- Normalmente se utiliza un diccionario, donde las consultas se pueden hacer en O(1)no importando que tan grande sea el diccionario.
- Intercambiamos tiempo de computo por espacio espacio en memoria.

### Clase 3 Optimización de Fibonacci

La serie de Fibonacci se representa como Fn = Fn-1 + Fn-2 (numero de  fibonnacci menos 1, mas el numero de fibonnaci menos 2)y es muy simple implementarla de forma recursiva en código. Sin embargo es muy ineficiente hacerlo simplemente recursivo, ya que repetimos varias veces el mismo computo.
![src/fibonnaci-algoritmo.jpeg](src/fibonnaci-algoritmo.jpeg)

Si te fijas en la imagen te darás cuenta de que repetimos varias veces el calculo para `f(4), f(3), f(2), f(1) y f(0)`, esto significa que nuestro algoritmo crece de forma exponencial `O(2**n)`.

Para optimizar nuestro algoritmo implementaremos en primer lugar la función recursiva para luego dar paso a la memorización, con esto las mejoras serán realmente sorprendentes.

```py
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
```

**Recuerda** para poder usar la programacion dinamica, debe haber problemas empalmados (_resolver el mismo problema en varias ocasiones para dar con una solución óptima (recursividad)_).

## Modulo 3 Caminos Aleatorios

### clase 4 Que son los caminos aleatorios

Los *caminos aleatorios* son un tipo de simulación que elige aleatoriamente una decisión dentro de un conjunto de decisiones válidas. Se utiliza en muchos campos del conocimiento cuando los sistemas no son deterministas e incluyen elementos de aleatoriedad.

### Clase 5 Camino de Borrachos

Este es un ejercicio toma un punto 0 como origen y aleatoriamente podemos decidir que dirección tomar, dependiendo de las c establecida, para elo haremos 3 clases distintas en tres archivos "borrachos", "coordenadas" y "campo".

Borracho

```py
# Creamos un archivo borracho.py
import random

# Creamos nuestra Clase borracho.
class Borracho:

    def __init__(self, nombre):
        self.nomber = nombre

# Creamos la clase BorrachoTradicional que extiende de Borracho.
class BorrachoTradicional(Borracho):

    def __init__(self, nombre):
        super().__init__(nombre)

    # Y tendrá un método caminar que devolverá la dirección a la que ira.
    def camina(self):
        return random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
```

Coordenadas

```py
# La clase Coordenada guardara las coordenadas de nuestro Borracho
class Coordenada:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    # cuando se mueve simplemente a las coordenadas actuales se les
    # suma las coordenadas X e Y que ingresan como parámetros.
    def mover(self, delta_x, delta_y):
        return Coordenada(self.x + delta_x, self.y + delta_y)

    # Y si queremos saber la distancia del agente con respecto a
    # unas coordenadas, simplemente lo calculamos con el
    # teorema de Pitágoras.
    def distancia(self,otra_coordenada):
        delta_x = self.x - otra_coordenada.x
        delta_y = self.y - otra_coordenada.y

        return (delta_x**2 + delta_y**2)**0.5

```

Campo

```py

class Campo:

    def __init__(self):
        self.coordenadas_de_borrachos = {}

     # Añadimos un agente a nuestro diccionario, nuestra llave sera
    # nuestro parámetro "borracho" y tendrá el valor asignado "coordenada"
    # que es una clase Coordenada creado en coordenada.py.
    def anadir_borrachos(self, borracho, coordenada):
        self.coordenadas_de_borrachos[borracho] = coordenada

    def mover_borracho(self, borracho):
        # Al mover a nuestro agente ejecutamos el método camina de
        # nuestra clase BorrachoTradicional creado en el archivo borracho.py,
        # devolviendo la dirección hacia donde se movió.
        delta_x, delta_y = borracho.camina()

        # Obtenemos el objeto de Coordenada.
        coordenada_actual = self.coordenadas_de_borrachos[borracho]

        # Del objeto Coordenada ejecutamos el método mover con los parámetros
        # que el objeto borracho genero. El resultado lo guardamos en
        # nueva_coordenada.
        nueva_coordenada = coordenada_actual.mover(delta_x, delta_y)

        # El objeto guardado en nueva_coordenada ahora estará asociado
        # a la llave de borracho.
        self.coordenadas_de_borrachos[borracho] = nueva_coordenada

    def obtener_coordenada(self, borracho):
        return self.coordenadas_de_borrachos[borracho]
```

### Clase 6 Desarrollando la simulación

Creamos  camino_aleatorio.py

```py
from borracho import BorrachoTradicional
from campo import Campo
from coordenada import Coordenada

def caminata(campo, borracho, pasos):
    # De la instancia Campo obtenemos las coordenadas actuales de la llave "borracho".
    inicio = campo.obtener_coordenada(borracho)

    # Repetiremos la misma cantidad de pasos definidos.
    for _ in range(pasos):

        # De la instancia campo ejecutaremos mover_borracho.
        campo.mover_borracho(borracho)

     # Y devolveremos la distancia entre las coordenadas de la instancia
    # inicio y campo.
    return inicio.distancia(campo.obtener_coordenada(borracho))


def simular_caminata(pasos, numero_de_intentos, tipo_de_borracho):

    # Definimos los parámetros para crear una instancia de Campo.
    borracho = tipo_de_borracho(nombre='David')
    origen = Coordenada(0,0)

    # Creamos una lista que guardara las distancias en cada simulación.
    distancias = []

    # Por cada numero de intento.
    for _ in range(numero_de_intentos):
        # Creamos una instancia de Campo.
        campo = Campo()

         # A nuestra instancia de Campo le damos la llave borracho y sus coordenadas de origen.
        campo.anadir_borrachos(borracho, origen)

        # Obtenemos la distancia final de la simulación.
        simulacion_caminata = caminata(campo, borracho,pasos)

        # El resultado lo guardamos en la lista de distancias.
        distancias.append(round(simulacion_caminata, 1))

    # Retornamos la lista de distancias.
    return distancias

def main(distancias_de_caminata, numero_de_intentos, tipo_de_borracho):

    for pasos in distancias_de_caminata:
        distancias = simular_caminata(pasos, numero_de_intentos, tipo_de_borracho)
        distancia_media = round(sum(distancias) / len(distancias),4)
        distancia_maxima = max(distancias)
        distancia_minima = min(distancias)
        print(f'{tipo_de_borracho.__name__} caminata aleatoria de {pasos} pasos')
        print(f'Media = {distancia_media}')
        print(f'Max = {distancia_maxima}')
        print(f'Min = {distancia_minima}')

```

### Clase 7 Visualización de Caminos Aleatorios

Ejecutamos caminos aleatorios..

```py
from borracho import BorrachoTradicional
from campo import Campo
from coordenada import Coordenada

from bokeh.plotting import figure, show


def caminata(campo, borracho, pasos):
    # De la instancia Campo obtenemos las coordenadas actuales de la llave "borracho".
    inicio = campo.obtener_coordenada(borracho)

    # Repetiremos la misma cantidad de pasos definidos.
    for _ in range(pasos):

        # De la instancia campo ejecutaremos mover_borracho.
        campo.mover_borracho(borracho)

     # Y devolveremos la distancia entre las coordenadas de la instancia
    # inicio y campo.
    return inicio.distancia(campo.obtener_coordenada(borracho))


def simular_caminata(pasos, numero_de_intentos, tipo_de_borracho):

    # Definimos los parámetros para crear una instancia de Campo.
    borracho = tipo_de_borracho(nombre='David')
    origen = Coordenada(0, 0)

    # Creamos una lista que guardara las distancias en cada simulación.
    distancias = []

    # Por cada numero de intento.
    for _ in range(numero_de_intentos):
        # Creamos una instancia de Campo.
        campo = Campo()

        # A nuestra instancia de Campo le damos la llave borracho y sus coordenadas de origen.
        campo.anadir_borrachos(borracho, origen)

        # Obtenemos la distancia final de la simulación.
        simulacion_caminata = caminata(campo, borracho, pasos)

        # El resultado lo guardamos en la lista de distancias.
        distancias.append(round(simulacion_caminata, 1))

    # Retornamos la lista de distancias.
    return distancias


def graficar(x, y):
    grafica = figure(title='Camino aleatorio de borrachos',
                     x_axis_label='pasos', 
                     y_axis_label='distancia recorrida')
    grafica.line(x,y, legend='distancia media')
    
    show(grafica)


def main(distancias_de_caminata, numero_de_intentos, tipo_de_borracho):
    distancias_media_por_caminata = []
    for pasos in distancias_de_caminata:
        distancias = simular_caminata(
            pasos, numero_de_intentos, tipo_de_borracho)
        distancia_media = round(sum(distancias) / len(distancias), 4)
        distancias_media_por_caminata.append(distancia_media)
        distancia_maxima = max(distancias)
        distancia_minima = min(distancias)
        print(f'{tipo_de_borracho.__name__} caminata aleatoria de {pasos} pasos')
        print(f'Media = {distancia_media}')
        print(f'Max = {distancia_maxima}')
        print(f'Min = {distancia_minima}')

    graficar(distancias_de_caminata, distancias_media_por_caminata)

if __name__ == "__main__":
    distancias_de_caminata = [10, 100, 1000, 10000]
    numero_de_intentos = 10

    main(distancias_de_caminata, numero_de_intentos, BorrachoTradicional)
```

grafica

![src/bokeh_plot_borrachos.png](src/bokeh_plot_borrachos.png)

## Modulo 4. Programas Estocásticos

## Modulo 5. Simulaciones de Montecarlo

## 6. Muestreo e Intervalos de Confianza

## 7. Datos Experimentales

## 8. Conclusiones
