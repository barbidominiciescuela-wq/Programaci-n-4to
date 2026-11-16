import tkinter as tk
import random

TAM = 20            # tamaño de cada casilla
CASILLAS = 20       # tablero de 20x20
VELOCIDAD = 180     # milisegundos entre movimientos (más alto = más lento)


class Snake:
    def __init__(self, ventana):
        self.ventana = ventana
        ventana.title("Snake")
        ventana.resizable(False, False)

        self.etiqueta = tk.Label(ventana, font=("Arial", 14))
        self.etiqueta.pack(pady=5)

        self.canvas = tk.Canvas(
            ventana,
            width=TAM * CASILLAS,
            height=TAM * CASILLAS,
            bg="#16213e",
            highlightthickness=0,
        )
        self.canvas.pack()

        self.record = 0
        ventana.bind("<Key>", self.tecla)
        self.iniciar()

    def iniciar(self):
        self.serpiente = [(10, 10), (9, 10), (8, 10)]
        self.direccion = (1, 0)
        self.prox_direccion = (1, 0)
        self.puntaje = 0
        self.jugando = True
        self.nueva_manzana()
        self.actualizar_puntaje()
        self.paso()

    def nueva_manzana(self):
        while True:
            pos = (random.randint(0, CASILLAS - 1), random.randint(0, CASILLAS - 1))
            if pos not in self.serpiente:
                self.manzana = pos
                break

    def actualizar_puntaje(self):
        self.etiqueta.config(text=f"Puntaje: {self.puntaje}  |  Récord: {self.record}")

    def tecla(self, evento):
        k = evento.keysym.lower()
        dx, dy = self.direccion

        if k == "space" and not self.jugando:
            self.iniciar()
        elif k in ("up", "w") and dy != 1:
            self.prox_direccion = (0, -1)
        elif k in ("down", "s") and dy != -1:
            self.prox_direccion = (0, 1)
        elif k in ("left", "a") and dx != 1:
            self.prox_direccion = (-1, 0)
        elif k in ("right", "d") and dx != -1:
            self.prox_direccion = (1, 0)

    def paso(self):
        if not self.jugando:
            return

        self.direccion = self.prox_direccion
        x, y = self.serpiente[0]
        cabeza = (x + self.direccion[0], y + self.direccion[1])

        # Choque con paredes o con ella misma
        if (
            cabeza[0] < 0 or cabeza[1] < 0
            or cabeza[0] >= CASILLAS or cabeza[1] >= CASILLAS
            or cabeza in self.serpiente
        ):
            self.terminar()
            return

        self.serpiente.insert(0, cabeza)

        if cabeza == self.manzana:
            self.puntaje += 1
            self.record = max(self.record, self.puntaje)
            self.actualizar_puntaje()
            self.nueva_manzana()
        else:
            self.serpiente.pop()

        self.dibujar()
        self.ventana.after(VELOCIDAD, self.paso)

    def dibujar(self):
        self.canvas.delete("all")

        # Manzana
        mx, my = self.manzana
        self.canvas.create_oval(
            mx * TAM + 2, my * TAM + 2,
            (mx + 1) * TAM - 2, (my + 1) * TAM - 2,
            fill="#e94560", outline="",
        )

        # Serpiente
        for i, (sx, sy) in enumerate(self.serpiente):
            color = "#7CFC00" if i == 0 else "#4caf50"
            self.canvas.create_rectangle(
                sx * TAM + 1, sy * TAM + 1,
                (sx + 1) * TAM - 1, (sy + 1) * TAM - 1,
                fill=color, outline="",
            )

    def terminar(self):
        self.jugando = False
        centro = TAM * CASILLAS // 2
        self.canvas.create_text(
            centro, centro - 15, text="Game Over",
            fill="white", font=("Arial", 28, "bold"),
        )
        self.canvas.create_text(
            centro, centro + 20, text="Apretá Espacio para jugar de nuevo",
            fill="white", font=("Arial", 12),
        )


ventana = tk.Tk()
Snake(ventana)
ventana.mainloop()
