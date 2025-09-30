import tkinter as tk

class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Jednoduché menu – barvy pozadí")
        self.root.geometry("800x600")

        # Canvas pro vykreslování
        self.canvas = tk.Canvas(self.root, bg="white")
        self.canvas.pack(fill="both", expand=True)

        # Menu
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)

        m_tasks = tk.Menu(menubar, tearoff=False)
        m_tasks.add_command(label="Červená", command=lambda: self.set_bg("red"))
        m_tasks.add_command(label="Zelená", command=lambda: self.set_bg("green"))
        m_tasks.add_command(label="Modrá", command=lambda: self.set_bg("blue"))
        menubar.add_cascade(label="Barvy", menu=m_tasks)

    def set_bg(self, color: str):
        self.canvas.config(bg=color)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    App().run()
