import tkinter as tk
from tkinter import ttk, messagebox
import random

"""
Výuková aplikace: Procvičování základů Pythonu s Tkinterem
---------------------------------------------------------
Témata: funkce, cykly, podmínky, práce s GUI prvky (Entry, Button, Listbox, Text, Canvas)

Struktura:
- Vlevo je seznam úloh (vzestupná náročnost)
- Vpravo se zobrazuje obsah aktuálně vybrané úlohy

Každá úloha má:
- Krátké zadání
- Jednoduché rozhraní pro vstup/výstup
- Vzorové řešení, které využívá funkce/cykly/podmínky
- (Volitelně) nápady na rozšíření

Pedagogická poznámka: Úlohy jsou napsané "čistě", s komentáři. Můžete je žákům
postupně odkrývat: např. nejprve smazat část řešení a nechat je doplnit.
"""

# --------------------------- Pomocné věci ------------------------------------

def clear_frame(frame: tk.Widget):
    """Zničí všechny potomky ve frame – použito při přepínání úloh."""
    for child in frame.winfo_children():
        child.destroy()

# --------------------------- Úlohy -------------------------------------------

# Úloha 1: Pozdrav funkcí (funkce + podmínka)
def build_task_1(parent: tk.Widget):
    frame = ttk.Frame(parent)

    ttk.Label(frame, text="Úloha 1 – Pozdrav funkcí", font=("Segoe UI", 12, "bold")).pack(anchor="w", pady=(0, 6))
    ttk.Label(frame, text=(
        "Zadej své jméno a stiskni tlačítko. Funkce greet rozhodne, jaký pozdrav zobrazit.\n"
        "Procvičíš: definici funkce, podmínky if/else."
    )).pack(anchor="w", pady=(0, 8))

    row = ttk.Frame(frame)
    row.pack(fill="x", pady=4)
    ttk.Label(row, text="Jméno:").pack(side="left")
    name_var = tk.StringVar()
    ttk.Entry(row, textvariable=name_var, width=24).pack(side="left", padx=6)

    output = tk.StringVar(value="Čekám na zadání…")
    ttk.Label(frame, textvariable=output, foreground="#205b2b").pack(anchor="w", pady=6)

    def greet(name: str) -> str:
        # Funkce + podmínka
        name = name.strip()
        if not name:
            return "Nejprve zadej jméno."
        # Příklad další podmínky – když jméno začíná na A
        if name[0].lower() == "a":
            return f"Ahoj, {name}! Áčka mají přednost 😄"
        return f"Ahoj, {name}!"

    ttk.Button(frame, text="Pozdrav", command=lambda: output.set(greet(name_var.get()))).pack(anchor="w")

    return frame

# Úloha 2: Součet 1..N (cyklus for + validace)
def build_task_2(parent: tk.Widget):
    frame = ttk.Frame(parent)
    ttk.Label(frame, text="Úloha 2 – Součet čísel 1..N", font=("Segoe UI", 12, "bold")).pack(anchor="w", pady=(0,6))
    ttk.Label(frame, text=(
        "Zadej N a spočítej součet 1 + 2 + … + N pomocí cyklu for.\n"
        "Procvičíš: převod vstupu na int, for, podmínky pro validaci."
    )).pack(anchor="w", pady=(0,8))

    row = ttk.Frame(frame)
    row.pack(fill="x", pady=4)
    ttk.Label(row, text="N:").pack(side="left")
    n_var = tk.StringVar(value="10")
    ttk.Entry(row, textvariable=n_var, width=10).pack(side="left", padx=6)

    result = tk.StringVar(value="Výsledek se zobrazí zde…")
    ttk.Label(frame, textvariable=result, foreground="#205b2b").pack(anchor="w", pady=6)

    def sum_to_n(n: int) -> int:
        total = 0
        for i in range(1, n + 1):
            total += i
        return total

    def run():
        try:
            n = int(n_var.get())
            if n < 0:
                result.set("N musí být nezáporné celé číslo.")
                return
            result.set(f"Součet 1..{n} = {sum_to_n(n)}")
        except ValueError:
            result.set("Zadej celé číslo.")

    ttk.Button(frame, text="Spočítej", command=run).pack(anchor="w")
    return frame

# Úloha 3: FizzBuzz (podmínky + cyklus)
def build_task_3(parent: tk.Widget):
    frame = ttk.Frame(parent)
    ttk.Label(frame, text="Úloha 3 – FizzBuzz", font=("Segoe UI", 12, "bold")).pack(anchor="w", pady=(0,6))
    ttk.Label(frame, text=(
        "Vypiš čísla 1..N, ale: násobky 3 nahraď 'Fizz', násobky 5 'Buzz', násobky 15 'FizzBuzz'.\n"
        "Procvičíš: zbytek po dělení (%), if/elif/else, for."
    )).pack(anchor="w", pady=(0,8))

    row = ttk.Frame(frame)
    row.pack(fill="x", pady=4)
    ttk.Label(row, text="N:").pack(side="left")
    n_var = tk.StringVar(value="30")
    ttk.Entry(row, textvariable=n_var, width=10).pack(side="left", padx=6)

    text = tk.Text(frame, width=48, height=10)
    text.pack(fill="both", expand=True, pady=6)

    def fizzbuzz(n: int) -> list[str]:
        out = []
        for i in range(1, n + 1):
            if i % 15 == 0:
                out.append("FizzBuzz")
            elif i % 3 == 0:
                out.append("Fizz")
            elif i % 5 == 0:
                out.append("Buzz")
            else:
                out.append(str(i))
        return out

    def run():
        text.delete("1.0", "end")
        try:
            n = int(n_var.get())
            if n <= 0:
                raise ValueError
            for line in fizzbuzz(n):
                text.insert("end", line + "\n")
        except ValueError:
            messagebox.showerror("Chyba", "Zadej kladné celé číslo N.")

    ttk.Button(frame, text="Vypiš", command=run).pack(anchor="w")
    return frame

# Úloha 4: Násobilková tabulka (vnořený cyklus)
def build_task_4(parent: tk.Widget):
    frame = ttk.Frame(parent)
    ttk.Label(frame, text="Úloha 4 – Násobilková tabulka", font=("Segoe UI", 12, "bold")).pack(anchor="w", pady=(0,6))
    ttk.Label(frame, text=(
        "Vygeneruj tabulku N×M pomocí vnořených cyklů.\n"
        "Procvičíš: for v for, formátování řetězců."
    )).pack(anchor="w", pady=(0,8))

    row = ttk.Frame(frame)
    row.pack(fill="x", pady=4)
    n_var = tk.StringVar(value="5")
    m_var = tk.StringVar(value="5")
    ttk.Label(row, text="N:").pack(side="left")
    ttk.Entry(row, textvariable=n_var, width=6).pack(side="left", padx=6)
    ttk.Label(row, text="M:").pack(side="left")
    ttk.Entry(row, textvariable=m_var, width=6).pack(side="left", padx=6)

    text = tk.Text(frame, width=48, height=10)
    text.pack(fill="both", expand=True, pady=6)

    def table(n: int, m: int) -> list[str]:
        lines = []
        for i in range(1, n + 1):
            row_vals = []
            for j in range(1, m + 1):
                row_vals.append(f"{i*j:>4}")
            lines.append("".join(row_vals))
        return lines

    def run():
        text.delete("1.0", "end")
        try:
            n = int(n_var.get()); m = int(m_var.get())
            if n <= 0 or m <= 0:
                raise ValueError
            for line in table(n, m):
                text.insert("end", line + "\n")
        except ValueError:
            messagebox.showerror("Chyba", "N a M musí být kladná celá čísla.")

    ttk.Button(frame, text="Vygeneruj", command=run).pack(anchor="w")
    return frame

# Úloha 5: Minimum ze seznamu (cyklus + podmínka)
def build_task_5(parent: tk.Widget):
    frame = ttk.Frame(parent)
    ttk.Label(frame, text="Úloha 5 – Nejmenší číslo v seznamu", font=("Segoe UI", 12, "bold")).pack(anchor="w", pady=(0,6))
    ttk.Label(frame, text=(
        "Zadej čísla oddělená čárkou a zjisti minimum bez použití built-in min().\n"
        "Procvičíš: parsování vstupu, for, podmíněné přiřazení."
    )).pack(anchor="w", pady=(0,8))

    entry = ttk.Entry(frame, width=48)
    entry.insert(0, "10, 3, 7, -2, 5")
    entry.pack(anchor="w", pady=4)

    result = tk.StringVar(value="Výsledek se zobrazí zde…")
    ttk.Label(frame, textvariable=result, foreground="#205b2b").pack(anchor="w", pady=6)

    def parse_numbers(s: str) -> list[float]:
        nums = []
        for part in s.split(','):
            part = part.strip()
            if not part:
                continue
            nums.append(float(part))
        return nums

    def min_manual(nums: list[float]) -> float:
        if not nums:
            raise ValueError("Seznam je prázdný")
        m = nums[0]
        for x in nums[1:]:
            if x < m:
                m = x
        return m

    def run():
        try:
            nums = parse_numbers(entry.get())
            result.set(f"Minimum = {min_manual(nums)}")
        except Exception as e:
            messagebox.showerror("Chyba", str(e))

    ttk.Button(frame, text="Zjisti minimum", command=run).pack(anchor="w")
    return frame

# Úloha 6: Prvočísla do N (cykly + podmínky)
def build_task_6(parent: tk.Widget):
    frame = ttk.Frame(parent)
    ttk.Label(frame, text="Úloha 6 – Prvočísla do N", font=("Segoe UI", 12, "bold")).pack(anchor="w", pady=(0,6))
    ttk.Label(frame, text=(
        "Vypiš všechna prvočísla ≤ N jednoduchou metodou.\n"
        "Procvičíš: vnořené cykly, continue/break, podmínky."
    )).pack(anchor="w", pady=(0,8))

    row = ttk.Frame(frame)
    row.pack(fill="x", pady=4)
    ttk.Label(row, text="N:").pack(side="left")
    n_var = tk.StringVar(value="50")
    ttk.Entry(row, textvariable=n_var, width=10).pack(side="left", padx=6)

    text = tk.Text(frame, width=48, height=10)
    text.pack(fill="both", expand=True, pady=6)

    def is_prime(n: int) -> bool:
        if n < 2:
            return False
        # Kontrola dělitelů do odmocniny n (efektivnější než do n-1)
        i = 2
        while i * i <= n:
            if n % i == 0:
                return False
            i += 1
        return True

    def run():
        text.delete("1.0", "end")
        try:
            N = int(n_var.get())
            if N < 2:
                text.insert("end", "Pro N < 2 nejsou žádná prvočísla.\n")
                return
            primes = [str(k) for k in range(2, N + 1) if is_prime(k)]
            text.insert("end", ", ".join(primes) + "\n")
        except ValueError:
            messagebox.showerror("Chyba", "Zadej celé číslo N.")

    ttk.Button(frame, text="Vypiš prvočísla", command=run).pack(anchor="w")
    return frame

# Úloha 7: Hádej číslo (podmínky + cyklus na pokusy)
class GuessingGame:
    def __init__(self):
        self.secret = random.randint(1, 100)
        self.tries = 0

    def guess(self, x: int) -> str:
        self.tries += 1
        if x < self.secret:
            return "Větší!"
        elif x > self.secret:
            return "Menší!"
        else:
            return f"Správně 🎉 Za {self.tries} pokusů. Nové číslo je vygenerováno."


def build_task_7(parent: tk.Widget):
    frame = ttk.Frame(parent)
    ttk.Label(frame, text="Úloha 7 – Hádej číslo 1..100", font=("Segoe UI", 12, "bold")).pack(anchor="w", pady=(0,6))
    ttk.Label(frame, text=(
        "Zkus uhodnout tajné číslo. Po každém pokusu dostaneš nápovědu.\n"
        "Procvičíš: podmínky, počítání pokusů, práci se stavem."
    )).pack(anchor="w", pady=(0,8))

    game = GuessingGame()

    row = ttk.Frame(frame); row.pack(fill="x", pady=4)
    ttk.Label(row, text="Tip:").pack(side="left")
    tip_var = tk.StringVar()
    ttk.Entry(row, textvariable=tip_var, width=10).pack(side="left", padx=6)

    out = tk.StringVar(value="Zadej číslo a stiskni Hádej…")
    ttk.Label(frame, textvariable=out, foreground="#205b2b").pack(anchor="w", pady=6)

    def run():
        try:
            x = int(tip_var.get())
            msg = game.guess(x)
            out.set(msg)
            if "Správně" in msg:
                game.__init__()  # rychlý reset (nové tajné číslo)
        except ValueError:
            messagebox.showerror("Chyba", "Zadej celé číslo 1..100.")

    ttk.Button(frame, text="Hádej", command=run).pack(anchor="w")
    return frame

# Úloha 8: Kreslení na Canvas (cyklus + podmínka)
def build_task_8(parent: tk.Widget):
    frame = ttk.Frame(parent)
    ttk.Label(frame, text="Úloha 8 – Kreslení čtverců na Canvas", font=("Segoe UI", 12, "bold")).pack(anchor="w", pady=(0,6))
    ttk.Label(frame, text=(
        "Vykresli N čtverců vedle sebe. Sudé budou vyplněné, liché prázdné.\n"
        "Procvičíš: for, if, práci s Canvas."
    )).pack(anchor="w", pady=(0,8))

    row = ttk.Frame(frame); row.pack(fill="x", pady=4)
    ttk.Label(row, text="N:").pack(side="left")
    n_var = tk.StringVar(value="12")
    ttk.Entry(row, textvariable=n_var, width=8).pack(side="left", padx=6)

    c = tk.Canvas(frame, width=600, height=120, background="#ffffff")
    c.pack(fill="x", pady=8)

    def draw():
        c.delete("all")
        try:
            n = int(n_var.get())
            if n <= 0:
                raise ValueError
            size = 40
            margin = 6
            x = margin
            y = margin
            for i in range(1, n + 1):
                x2 = x + size
                y2 = y + size
                if i % 2 == 0:
                    # sudé vyplněné
                    c.create_rectangle(x, y, x2, y2, fill="#87CEFA", outline="#333333")
                else:
                    # liché prázdné
                    c.create_rectangle(x, y, x2, y2, outline="#333333", width=2)
                x += size + margin
                if x2 + size + margin > c.winfo_width():
                    # nový řádek, když se nevejdeme
                    x = margin
                    y += size + margin
        except ValueError:
            messagebox.showerror("Chyba", "Zadej kladné celé číslo N.")

    ttk.Button(frame, text="Vykresli", command=draw).pack(anchor="w")
    return frame

# --------------------------- Aplikace ----------------------------------------

TASKS = [
    ("1. Pozdrav funkcí", build_task_1),
    ("2. Součet 1..N", build_task_2),
    ("3. FizzBuzz", build_task_3),
    ("4. Násobilková tabulka", build_task_4),
    ("5. Minimum v seznamu", build_task_5),
    ("6. Prvočísla do N", build_task_6),
    ("7. Hádej číslo", build_task_7),
    ("8. Kreslení na Canvas", build_task_8),
]

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Procvičování Pythonu – Tkinter")
        self.geometry("980x560")
        self.minsize(820, 520)

        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)

        # Sidebar se seznamem úloh
        sidebar = ttk.Frame(self, padding=10)
        sidebar.grid(row=0, column=0, sticky="nsw")
        ttk.Label(sidebar, text="Úlohy", font=("Segoe UI", 12, "bold")).pack(anchor="w")

        self.listbox = tk.Listbox(sidebar, height=18, activestyle="dotbox")
        self.listbox.pack(fill="y", expand=False, pady=6)
        for name, _ in TASKS:
            self.listbox.insert("end", name)

        ttk.Button(sidebar, text="Otevřít úlohu", command=self.open_selected).pack(fill="x", pady=(6, 0))

        # Hlavní obsah
        self.content = ttk.Frame(self, padding=14)
        self.content.grid(row=0, column=1, sticky="nsew")
        self.content.columnconfigure(0, weight=1)
        self.content.rowconfigure(0, weight=1)

        # Info panel při startu
        self.show_welcome()

        # Menu (rychlý výběr úlohy)
        self._build_menu()

    def _build_menu(self):
        menubar = tk.Menu(self)
        self.config(menu=menubar)

        m_tasks = tk.Menu(menubar, tearoff=False)
        for idx, (name, _) in enumerate(TASKS):
            m_tasks.add_command(label=name, command=lambda i=idx: self.open_task(i))
        menubar.add_cascade(label="Úlohy", menu=m_tasks)

        m_help = tk.Menu(menubar, tearoff=False)
        m_help.add_command(label="O aplikaci", command=self.show_about)
        menubar.add_cascade(label="Nápověda", menu=m_help)

    def show_welcome(self):
        clear_frame(self.content)
        box = ttk.Frame(self.content)
        box.grid(row=0, column=0, sticky="nsew")
        box.columnconfigure(0, weight=1)

        ttk.Label(box, text="Procvičování Pythonu s Tkinterem", font=("Segoe UI", 16, "bold")).grid(row=0, column=0, sticky="w")
        ttk.Label(box, text=(
            "Vyber zleva úlohu. Úlohy jdou přibližně od jednodušších ke složitějším a pokrývají funkce, cykly a podmínky.\n"
            "Zkuste si kód upravovat: např. přidat nové podmínky, další cykly nebo vlastní vstupy/výstupy."
        ), wraplength=720).grid(row=1, column=0, sticky="w", pady=(8, 0))

        # Tipy na rozšíření jako checklist
        tips = [
            "[ ] Ú1: Přidej pozdrav podle denní doby (ráno/odpoledne/večer).",
            "[ ] Ú2: Porovnej cyklický součet se vzorcem n*(n+1)/2.",
            "[ ] Ú3: Uprav FizzBuzz tak, aby šla pravidla měnit (např. 4→'Bim').",
            "[ ] Ú4: Zobraz i hlavičky řádků a sloupců (1..N, 1..M).",
            "[ ] Ú5: Doplň i maximum a aritmetický průměr.",
            "[ ] Ú6: Spočítej počet prvočísel ≤ N a průměr mezer mezi nimi.",
            "[ ] Ú7: Vedení rekordů – nejmenší počet pokusů od spuštění.",
            "[ ] Ú8: Náhodné barvy, přepínač pro kruhy/čtverce."
        ]

        ttk.Label(box, text="Nápady na rozšíření:", font=("Segoe UI", 11, "bold")).grid(row=2, column=0, sticky="w", pady=(12, 4))
        txt = tk.Text(box, height=8, width=88)
        txt.grid(row=3, column=0, sticky="nsew")
        txt.insert("end", "\n".join(tips))
        txt.config(state="disabled")

    def show_about(self):
        messagebox.showinfo(
            "O aplikaci",
            "Výuková ukázka Tkinter – funkce, cykly, podmínky.\nAutor: (doplňte)."
        )

    def open_selected(self):
        idx = self.listbox.curselection()
        if not idx:
            messagebox.showwarning("Nic nevybráno", "Vyber v seznamu úlohu.")
            return
        self.open_task(idx[0])

    def open_task(self, index: int):
        clear_frame(self.content)
        # Každá úloha vrací připravený Frame
        _, builder = TASKS[index]
        task_frame = builder(self.content)
        task_frame.grid(row=0, column=0, sticky="nsew")


if __name__ == "__main__":
    app = App()
    app.mainloop()
