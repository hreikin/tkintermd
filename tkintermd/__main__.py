from tkintermd.frame import TkintermdFrame

import tkinter as tk
from tkinter.constants import *

def main():
    root = tk.Tk()
    app = TkintermdFrame(root)
    app.pack(fill="both", expand=1)
    app.mainloop()

if __name__ == "__main__":
    main()