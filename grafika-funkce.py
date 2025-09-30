import tkinter as tk
import random, math

class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Jednoduché menu – barvy + úlohy")
        self.root.geometry("800x800")

        # Canvas pro vykreslování
        self.canvas = tk.Canvas(self.root, bg="white")
        self.canvas.pack(fill="both", expand=True)

        # Menu
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)

        # Barvy
        m_colors = tk.Menu(menubar, tearoff=False)
        m_colors.add_command(label="Červená", command=lambda: self.set_bg("red"))
        m_colors.add_command(label="Zelená", command=lambda: self.set_bg("green"))
        m_colors.add_command(label="Modrá", command=lambda: self.set_bg("blue"))
        menubar.add_cascade(label="Barvy", menu=m_colors)

        # Úlohy
        m_tasks = tk.Menu(menubar, tearoff=False)
        m_tasks.add_command(label="Svislé čáry (lines)", command=self.lines)
        m_tasks.add_command(label="Šachovnice 8×8 (chessboard)", command=lambda: self.chessboard())
        m_tasks.add_command(label="Terč (target)", command=self.target)
        menubar.add_cascade(label="Úlohy", menu=m_tasks)

        # Při změně velikosti překreslit poslední úlohu (jednoduše zavoláme znovu)
        self._last_draw = None
        self.canvas.bind("<Configure>", lambda e: self._last_draw and self._last_draw())

    # ----------------- Helpers -----------------
    def _canvas_size(self):
        w = self.canvas.winfo_width() or int(self.canvas["width"]) or 640
        h = self.canvas.winfo_height() or int(self.canvas["height"]) or 420
        return w, h

    def clear(self):
        self.canvas.delete("all")

    # ----------------- Barvy -------------------
    def set_bg(self, color: str):
        self.canvas.config(bg=color)
        self._last_draw = None

    # ----------------- Úlohy -------------------
    def lines(self):
        """Vykreslí náhodně tučné, náhodně barevné svislé čáry zleva doprava."""
        self.clear()
        self.canvas.config(bg="white")
        w, h = self._canvas_size()
        count = max(12, w // 20)  # hrubý odhad počtu čar podle šířky
        step = w / count
        x = step / 2
        for _ in range(count):
            width = random.randint(1, 8)
            color = f"#{random.randint(0,0xFFFFFF):06x}"
            self.canvas.create_line(x, 0, x, h, fill=color, width=width)
            x += step

    def chessboard(self, size: int = 8):
        """Vykreslí šachovnici size×size vycentrovanou do plátna."""
        self.clear()
        self.canvas.config(bg="white")
        w, h = self._canvas_size()
        margin = 10
        board = min(w, h) - 2*margin
        if board <= 0:
            return
        cell = board / size
        x0 = (w - board)/2
        y0 = (h - board)/2
        light = "#f0d9b5"
        dark  = "#b58863"
        for r in range(size):
            for c in range(size):
                x1 = x0 + c*cell; y1 = y0 + r*cell
                x2 = x1 + cell;   y2 = y1 + cell
                fill = light if (r+c)%2==0 else dark
                self.canvas.create_rectangle(x1,y1,x2,y2, fill=fill, outline="#333")

    def target(self):
        """Soustředné kružnice se skóre prstenců (10 uprostřed → 1 na okraji)."""
        self.clear()
        self.canvas.config(bg="white")
        w, h = self._canvas_size()
        cx, cy = w/2, h/2
        rings = 5
        R = int(min(w, h)*0.45)
        step = R / rings
        # střídání barev pro čitelnost
        for i in range(rings, 0, -1):
            r = i*step
            color = "#ffdede" if i%2==0 else "#ffffff"
            self.canvas.create_oval(cx-r, cy-r, cx+r, cy+r, fill=color, outline="#333")
            score = rings - i + 1  # 1..10
            # vyznač skóre na pravé straně prstence
            tx = cx + r - step/2
            self.canvas.create_text(tx, cy, text=str(score), font=("Segoe UI", 10, "bold"))
        # středová tečka
        self.canvas.create_oval(cx-2, cy-2, cx+2, cy+2, fill="#333", outline="")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    App().run()