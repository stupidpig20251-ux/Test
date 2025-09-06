import tkinter as tk
import math
import datetime

WIDTH = 300
HEIGHT = 300
CENTER_X = WIDTH // 2
CENTER_Y = HEIGHT // 2
RADIUS = min(WIDTH, HEIGHT) // 2 - 10

class Clock(tk.Canvas):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, width=WIDTH, height=HEIGHT, bg='white', highlightthickness=0, **kwargs)
        self.pack()
        self.draw_face()
        self.hour_hand = self.create_line(CENTER_X, CENTER_Y, CENTER_X, CENTER_Y - RADIUS*0.5, width=4, fill='black')
        self.minute_hand = self.create_line(CENTER_X, CENTER_Y, CENTER_X, CENTER_Y - RADIUS*0.75, width=2, fill='black')
        self.second_hand = self.create_line(CENTER_X, CENTER_Y, CENTER_X, CENTER_Y - RADIUS*0.9, width=1, fill='red')
        self.update_clock()

    def draw_face(self):
        self.create_oval(CENTER_X - RADIUS, CENTER_Y - RADIUS, CENTER_X + RADIUS, CENTER_Y + RADIUS, width=2)
        for i in range(12):
            angle = math.pi / 6 * i
            x_inner = CENTER_X + RADIUS * 0.85 * math.sin(angle)
            y_inner = CENTER_Y - RADIUS * 0.85 * math.cos(angle)
            x_outer = CENTER_X + RADIUS * math.sin(angle)
            y_outer = CENTER_Y - RADIUS * math.cos(angle)
            self.create_line(x_inner, y_inner, x_outer, y_outer, width=2)

    def update_clock(self):
        now = datetime.datetime.now()
        sec = now.second
        minute = now.minute + sec / 60
        hour = now.hour % 12 + minute / 60

        sec_angle = math.pi / 30 * sec
        min_angle = math.pi / 30 * minute
        hour_angle = math.pi / 6 * hour

        self._update_hand(self.second_hand, sec_angle, RADIUS * 0.9)
        self._update_hand(self.minute_hand, min_angle, RADIUS * 0.75)
        self._update_hand(self.hour_hand, hour_angle, RADIUS * 0.5)

        self.after(1000, self.update_clock)

    def _update_hand(self, hand, angle, length):
        x = CENTER_X + length * math.sin(angle)
        y = CENTER_Y - length * math.cos(angle)
        self.coords(hand, CENTER_X, CENTER_Y, x, y)


def main():
    root = tk.Tk()
    root.title("Analog Clock")
    root.attributes('-topmost', True)
    Clock(root)
    root.mainloop()

if __name__ == '__main__':
    main()
