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
def task_1(parent: tk.Widget):
    frame = ttk.Frame(parent)
    return frame


def task_2():
    pass


def task_3():
    pass


# --------------------------- Aplikace ----------------------------------------

TASKS = [
    ("1. Pozdrav funkcí", task_1),
    ("2. Součet 1..N", task_2),
    ("3. FizzBuzz", task_3),
]


# Třída hlavní aplikace, která spravuje okno, menu a přepínání úloh
# Dědí z třídy tk.Tk
class App(tk.Tk):
    def __init__(self):
        """Konstruktor: Inicializace hlavního okna a jeho komponent."""
        # Inicializace rodičovské třídy
        super().__init__()
        # Nastavení okna - titulek, velikost, minimální velikost
        self.title("Procvičování Pythonu – Tkinter")
        self.geometry("980x560")
        self.minsize(820, 520)

        # Rozvržení hlavního okna na dvě části: sidebar a content
        # weight určuje, jak se prostor rozdělí při změně velikosti okna
        # v tomto případě sidebar zůstane pevný a content se roztáhne
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)

        # -------------------------------------------------------------------------------------------------------------
        # Sidebar se seznamem úloh - levá část okna
        # odstavce kolem (padding) 10 pixelů
        sidebar = ttk.Frame(self, padding=10)
        # nastavení umístění v gridu, sticky určuje, že se přilepí k severu, jihu a západu
        sidebar.grid(row=0, column=0, sticky="nsw")
        # Nadpis sidebaru
        ttk.Label(sidebar, text="Úlohy", font=("Segoe UI", 12, "bold")).pack(anchor="w")
        # Listbox pro výběr úloh
        # Nejprve vytvoříme Listbox s výškou 18 řádků a stylem aktivního prvku "dotbox"
        self.listbox = tk.Listbox(sidebar, height=18, activestyle="dotbox")
        # Poté ho zabalíme do sidebaru s vertikálním vyplněním (pady) 6 pixelů
        self.listbox.pack(fill="y", expand=False, pady=6)
        # Naplnění Listboxu názvy úloh z konstanty TASKS
        # name je název úlohy, _ je funkce pro vytvoření obsahu (kterou zde nepotřebujeme)
        for name, _ in TASKS:
            self.listbox.insert("end", name)

        # Tlačítko pro otevření vybrané úlohy
        # Při kliknutí zavolá metodu open_selected, která otevře vybranou úlohu
        # Tlačítko se roztáhne na celou šířku sidebaru a má horní odsazení 6 pixelů
        ttk.Button(sidebar, text="Otevřít úlohu", command=self.open_selected).pack(fill="x", pady=(6, 0))

        # -------------------------------------------------------------------------------------------------------------
        # Hlavní obsah - pravá část okna
        # Frame s paddingem 14 pixelů kolem
        self.content = ttk.Frame(self, padding=14)
        # Umístění v gridu, roztáhne se na celou dostupnou plochu (sticky nsew)
        self.content.grid(row=0, column=1, sticky="nsew")
        # Konfigurace řádků a sloupců, aby se obsah roztahoval
        self.content.columnconfigure(0, weight=1)
        self.content.rowconfigure(0, weight=1)

        # Info panel při startu
        self.show_welcome()

        # Menu (rychlý výběr úlohy)
        self._build_menu()

    def _build_menu(self):
        """Vytvoření menu s výběrem úloh a nápovědou."""
        # Vytvoření hlavního menu, přiřazení k oknu
        menubar = tk.Menu(self)
        self.config(menu=menubar)

        # Menu pro výběr úloh, každá úloha je položka menu, při kliknutí se otevře
        m_tasks = tk.Menu(menubar, tearoff=False)
        # Pro každou úlohu přidáme položku do menu podle jejího indexu
        for idx, (name, _) in enumerate(TASKS):
            # Použití lambda výrazu/funkce pro zachycení aktuálního indexu
            m_tasks.add_command(label=name, command=lambda i=idx: self.open_task(i))
        # Přidání menu úloh do hlavního menu pod názvem "Úlohy"
        menubar.add_cascade(label="Úlohy", menu=m_tasks)

        # Menu nápovědy s položkou "O aplikaci", která zobrazí informace o aplikaci
        m_help = tk.Menu(menubar, tearoff=False)
        m_help.add_command(label="O aplikaci", command=self.show_about)
        # Přidání menu nápovědy do hlavního menu pod názvem "Nápověda"
        menubar.add_cascade(label="Nápověda", menu=m_help)

    def show_welcome(self):
        """Zobrazení úvodního textu s informacemi o aplikaci a nápady na rozšíření."""
        # Vyčištění obsahu
        clear_frame(self.content)
        # Vytvoření boxu pro text
        box = ttk.Frame(self.content)
        # Nastavení umístění a konfigurace, aby se roztahoval s obsahem
        box.grid(row=0, column=0, sticky="nsew")
        box.columnconfigure(0, weight=1)

        # Úvodní text, nadpis a popis
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

        # Textové pole s nápady na rozšíření
        ttk.Label(box, text="Nápady na rozšíření:", font=("Segoe UI", 11, "bold")).grid(row=2, column=0, sticky="w", pady=(12, 4))
        # Vytvoření Text widgetu pro zobrazení tipů
        txt = tk.Text(box, height=8, width=88)
        # Nastavení umístění a konfigurace, aby se roztahoval s obsahem
        txt.grid(row=3, column=0, sticky="nsew")
        # Vložení tipů do textového pole
        txt.insert("end", "\n".join(tips))
        # Nastavení textového pole jako pouze pro čtení
        txt.config(state="disabled")

    def show_about(self):
        """Zobrazení informace o aplikaci."""
        # Jednoduché informační okno s popisem aplikace a autorem
        messagebox.showinfo(
            "O aplikaci",
            "Výuková ukázka Tkinter – funkce, cykly, podmínky.\nAutor: (doplňte)."
        )

    def open_selected(self):
        """Otevře úlohu vybranou v Listboxu."""
        # Získání indexu vybrané položky v Listboxu
        idx = self.listbox.curselection()
        # Pokud není nic vybráno, zobrazí varování
        if not idx:
            messagebox.showwarning("Nic nevybráno", "Vyber v seznamu úlohu.")
            return
        # Otevření úlohy podle vybraného indexu
        self.open_task(idx[0])

    def open_task(self, index: int):
        """Otevře úlohu podle jejího indexu v seznamu TASKS."""
        # Vyčištění obsahu před zobrazením nové úlohy
        clear_frame(self.content)
        # Každá úloha vrací připravený Frame
        _, builder = TASKS[index]
        # Vytvoření a umístění frame s úlohou
        task_frame = builder(self.content)
        # Umístění frame s úlohou, roztáhne se na celou dostupnou plochu
        task_frame.grid(row=0, column=0, sticky="nsew")


# Aplikace se spustí, pokud je tento soubor spuštěn jako hlavní program
if __name__ == "__main__":
    app = App()
    app.mainloop()
