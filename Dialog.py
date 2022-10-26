import tkinter as tk

class Dialog():

    def __init__(self):

        self.value = None

    def setVal(self, value):

        self.value = value
        
    def dialog(self, hint):

        window = tk.Tk()
        window.option_add('*font', 'Arial 12')
        window.title("Parameter settings")
        window.resizable(False, False)

        l = tk.Label(window, text = "Insert  <parameter>: ", width = 19)
        l.grid(column = 0, row = 0)
        
        T = tk.Text(window, height = 1, width = 10)
        T.grid(column = 1, row = 0, columnspan = 2, sticky="news")

        L_info = tk. Label(window, text = hint)
        L_info.grid(column = 0, row = 1, columnspan = 2)

        B_leave = tk.Button(window, text = "Acept", bg = "red",
                            command = lambda : [self.setVal(T.get("1.0","end-1c")), window.destroy()])
        B_leave.grid(column = 2, row = 1)
        
        tk.mainloop()

        
