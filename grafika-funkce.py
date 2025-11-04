import tkinter as tk
import random, math
from tkinter import simpledialog, colorchooser

try:
    from happiness.ui_menu import attach_happiness_menu
except Exception:
    attach_happiness_menu = None


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
        # Nejprve vytvoříme podmenu pro barvy; atribut tearoff=False zakáže oddělovací čáru nahoře
        m_colors = tk.Menu(menubar, tearoff=False)
        # Přidáme příkazy pro změnu barvy pozadí canvasu; každý příkaz volá metodu set_bg s příslušnou barvou
        # Používáme lambda pro vytvoření anonymní funkce, která zavolá set_bg s daným argumentem
        m_colors.add_command(label="Červená", command=lambda: self.set_bg("red"))
        m_colors.add_command(label="Zelená", command=lambda: self.set_bg("green"))
        m_colors.add_command(label="Modrá", command=lambda: self.set_bg("blue"))
        menubar.add_cascade(label="Barvy", menu=m_colors)

        # Úlohy
        m_tasks = tk.Menu(menubar, tearoff=False)
        m_tasks.add_command(label="Čáry", command=self.lines)
        # m_tasks.add_command(label="Šachovnice", command=lambda: self.chessboard())
        m_tasks.add_command(label="Šachovnice", command=self.chessboard_dialog)
        m_tasks.add_command(label="Terč", command=self.target)
        menubar.add_cascade(label="Úlohy", menu=m_tasks)

        # po vytvoření menubar:
        if attach_happiness_menu:
            self._happy = attach_happiness_menu(self.root, menubar)

        # Při změně velikosti překreslit poslední úlohu (jednoduše zavoláme znovu)
        self._last_draw = None
        # Událost <Configure> se vyvolá při změně velikosti okna, připneme k ní lambda funkci, která zavolá poslední vykreslovací funkci, pokud existuje
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
        x = 0
        while x < w:
            weight = random.randint(1, 8)
            color = f"#{random.randint(0,0xFFFFFF):06x}"
            self.canvas.create_line(x, 0, x, h, fill=color, width=weight)
            x += weight

    def chessboard(self, size: int = 8, light="#f0d9b5", dark="#b58863"):
        """Vykreslí šachovnici size×size vycentrovanou do plátna."""
        self.clear()
        self.canvas.config(bg="white")
        w, h = self._canvas_size()
        margin = 10
        board = min(w, h) - 2 * margin
        if board <= 0:
            return
        cell = board / size
        x0 = (w - board) / 2
        y0 = (h - board) / 2
        for r in range(size):
            for c in range(size):
                x1 = x0 + c*cell
                y1 = y0 + r*cell
                x2 = x1 + cell
                y2 = y1 + cell
                fill = light if (r + c) % 2 == 0 else dark
                self.canvas.create_rectangle(x1, y1 , x2, y2, fill=fill, outline="#333")

    def chessboard_dialog(self):
        # zadání velikosti
        size = simpledialog.askinteger(
            "Šachovnice",
            "Zadej velikost (počet polí na stranu):",
            parent=self.root,
            initialvalue=8,
            minvalue=2,
            maxvalue=30
        )
        if not size:
            return

        # výběr světlé barvy
        light_color = colorchooser.askcolor(
            title="Vyber světlou barvu",
            initialcolor="#f0d9b5"
        )[1]  # askcolor vrací (RGB, HEX), my chceme HEX kód
        if not light_color:
            light_color = "#f0d9b5"

        # výběr tmavé barvy
        dark_color = colorchooser.askcolor(
            title="Vyber tmavou barvu",
            initialcolor="#b58863"
        )[1]
        if not dark_color:
            dark_color = "#b58863"

        # vykreslení šachovnice s barvami
        self.chessboard(size=size, light=light_color, dark=dark_color)
        self._last_draw = lambda s=size, l=light_color, d=dark_color: self.chessboard(s, l, d)


    def target(self, rings: int = 10):
        """Soustředné kružnice se skóre prstenců (10 uprostřed → 1 na okraji)."""
        self.clear()
        self.canvas.config(bg="white")
        w, h = self._canvas_size()
        cx, cy = w/2, h/2
        R = int(min(w, h) * 0.45)
        step = R / rings
        # střídání barev pro čitelnost
        for i in range(rings, 0, -1):
            r = i*step
            color = "#ffdede" if i%2==0 else "#ffffff"
            self.canvas.create_oval(cx-r, cy-r, cx+r, cy+r, fill=color, outline="#333")
            score = rings - i + 1  # 1..10
            # vyznač skóre na pravé straně prstence
            if score < rings:  # největší prstenec nemá skóre
                tx = cx + r - step/2
                self.canvas.create_text(tx, cy, text=str(score), font=("Segoe UI", 10, "bold"))
                tx = cx - r + step / 2
                self.canvas.create_text(tx, cy, text=str(score), font=("Segoe UI", 10, "bold"))
                ty = cy + r - step/2
                self.canvas.create_text(cx, ty, text=str(score), font=("Segoe UI", 10, "bold"))
                ty = cy - r + step/2
                self.canvas.create_text(cx, ty, text=str(score), font=("Segoe UI", 10, "bold"))
        # středová tečka
        self.canvas.create_oval(cx-2, cy-2, cx+2, cy+2, fill="#333", outline="")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    App().run()