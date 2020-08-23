import n_reinas
import turtle

wn = turtle.Screen()
wn.title("N_Reinas")
wn.bgcolor("black")
wn.setup(width = 700, height = 700)

class Otros(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("grey")
        self.penup()
        self.speed(0)

class Reinas(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("triangle")
        self.color("gold")
        self.penup()
        self.speed(0)

def graficar(nivel):
    for fila in range(len(nivel)):
        for columna in range(len(nivel[fila])):
            variable = nivel[fila][columna]
            n_x = -288 + (columna * 24)
            n_y = 288 - (fila * 24)

            if variable == 0:
                otro.goto(n_x,n_y)
                otro.stamp()
            if variable == 1:
                reina.goto(n_x,n_y)
                reina.stamp()

otro = Otros()
reina = Reinas()

solucion = n_reinas.n_reinas(18)

graficar(solucion)

wn.tracer(0)

while True:
    wn.update()


turtle.done()