from tkintermd.tkintermd_frame import TkinterMDFrame

import tkinter as tk
from tkinter.constants import *

def main():
    root = tk.Tk()
    app = TkinterMDFrame(root)
    app.pack(fill="both", expand=1)
    app.mainloop()

if __name__ == "__main__":
    main()