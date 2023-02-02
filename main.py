from tkinter import*
import random
import time

screen = Tk()
screen.title("Игра")
screen.wm_attributes("-topmost", 1)
canvas = Canvas(screen, width= 500,
                height= 750,
                bd= 0,
                highlightthickness= 0,
                bg = "grey")
canvas.pack()
screen.update()

class Ball:
    def __init__(self, canvas, color, rocetka, score):
        self.canvas = canvas
        self.id = canvas.create_oval(10, 10,
                                     25, 25,
                                     fill= color)
        self.canvas.move(self.id, 245, 100)
        starts = [-3, -2, -1, 1, 2, 3]
        random.shuffle(starts)
        self.x = starts[0]
        self.y = 1
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.rocetka = rocetka
        self.score = score
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom = False

    def hit_paddle(self, pos):
        platform_pos = self.canvas.coords(self.rocetka.id)
        if pos[2] >= platform_pos[0] and pos[0] <= platform_pos[2]:
            if platform_pos[1] <= pos[3] <= platform_pos[3]:
                self.score.hit()
                return True
        return False

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 4
        if pos[1] <= 0:
            self.y = 4
        if pos[2] >= self.canvas_width:
            self.x = -4
        if pos[3] >= self.canvas_height:
            self.hit_bottom = True
            self.canvas.create_text(250, 325,
                                    text = "Вас победил компьютер.\n \tАхахаха.",
                                    font = ("Courier", 20, "bold"),
                                    fill = "red")
        if self.hit_paddle(pos) == True:
            self.y = -4
        if pos[0] <= 0:
            self.x = 4
        if pos[2] >= self.canvas_width:
            self.x = -4
class Rocetka:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0,
                                          100, 10,
                                          fill= color)
        self.canvas.move(self.id, 200, 600)
        self.canvas_width = self.canvas.winfo_width()
        self.x = 0
        self.canvas.bind_all('<KeyPress-Left>', self.left)
        self.canvas.bind_all('<KeyPress-Right>', self.right)

    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos1 = self.canvas.coords(self.id)
        if pos1[0] <= 0:
            self.x = 0
        elif pos1[2] >= self.canvas_width:
            self.x = 0

    def left(self, event):
        self.x = -2

    def right(self, event):
        self.x = 2

class Score:
    def __init__(self, canvas, color):
        self.score = 0
        self.canvas = canvas
        self.text = canvas.create_text(250, 730,
                                       text = f"Ваш счет: {self.score}",
                                       font = ("Courier", 16, "bold"),
                                       fill = color)
    def hit(self):
        self.score += 1
        self.canvas.itemconfig(self.text, text = f"Ваш счет: {self.score}")


score = Score(canvas, "red")
rocetka = Rocetka(canvas, "blue")
ball = Ball(canvas, "red", rocetka, score)


while True:
    if ball.hit_bottom == False:
        ball.draw()
        rocetka.draw()
    else:
        time.sleep(2)
        break
    screen.update_idletasks()
    screen.update()
    time.sleep(0.01)

