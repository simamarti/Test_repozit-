import tkinter as tk
import tkinter.filedialog
import Input
import LL
import Draw
import Edit
import Algorithms

class interface():

    def __init__(self):

        self.window = tk.Tk()
        self.Linked_List = LL.LL()
        self.LL_mod = LL.LL()
        self.LL_gen = LL.LL()
        self.canvas = tk.Canvas(width = 650, height = 500)
        
        self.var = tk.IntVar()
        self.text = None
       

    def load(self, data):

        self.Linked_List = Input.load(data[:-1])

    def inport(self):

        name = tkinter.filedialog.askopenfilename(title = "Open a file", initialdir = '/Tests')

        self.Linked_List = Input.input(name)

    def draw(self):

        if self.text is not None:

            self.canvas.delete(self.text)
            self.text = None

        if not self.Linked_List.isEmpty():
            
            self.LL_mod = Edit.edit(self.Linked_List, 650, 500)
            self.canvas.delete('all')

            if self.LL_mod == False:

                self.text = self.canvas.create_text(300, 50,
                                   text = "Points cannot be printed due to big differencies between x/y coordinates.",
                                    fill = "red", font = ("Arial 8"))
                
                return False
            
            else:
  
                print(">>>>>" + str(self.canvas))
                current = self.Linked_List.head

                if not self.LL_gen.isEmpty():
                    
                    Draw.draw(self.LL_gen, "#ff0000", self.canvas)
                    return True

                self.canvas.delete('all')
                Draw.draw(self.LL_mod, "#000000", self.canvas)
                       
    def setLL_gen(self, LL):

        self.LL_gen = LL
        
    def layout(self):

       
        self.window.option_add('*font', 'Arial 12')
        self.window.geometry("1300x625")
        self.window.title("User interface")
        self.window.config(bg='green')
        self.window.resizable(False, False)

        l = tk.Label( self.window, text="Input data", bg = 'red')
        l.grid(column = 0, row = 0, columnspan = 2, sticky = "W")
        
        l = tk.Label( self.window, text="Vizualization", bg = 'red')
        l.grid(column = 2, row = 0, sticky = "W")

        l = tk.Label( self.window, text="Select algorithm", bg = 'red')
        l.grid(column = 3, row = 0, sticky = "news")

        
        self.canvas.grid(column = 2, row = 1, rowspan = 8, sticky = "news")

        tx = tk.Text(self.window, width = 20, height = 10)
        tx.grid(column = 0, row = 1, columnspan = 2, rowspan = 8, sticky = "news")
        
        
        B_Load = tk.Button(self.window, text = "Load",
                           command = lambda :  [self.load(tx.get("1.0","end")), self.draw()])

        B_Load.grid(column = 0, row = 9, sticky = "news")
        
        B_ln = tk.Button(self.window,text = "Inport",
                            command = lambda : [self.inport()])
        B_ln.grid(column = 1, row = 9, sticky = "news")
        
        rb_1 = tk.Radiobutton(self.window, text = "Euclidian", variable =  self.var,
            value = 1, indicatoron = 0,
                              command = lambda : [self.setLL_gen(Algorithms.euclidian(self.LL_mod)),
                            self.draw()]).grid(column = 3, row = 1, sticky = "news")
        
        rb_2 = tk.Radiobutton(self.window, text = "Euclidian_weighted", variable =  self.var,
            value = 2, indicatoron = 0).grid(column = 3, row = 2, sticky = "news")
        
        rb_3 = tk.Radiobutton(self.window, text = "Vzdálenost bodu od strany", variable =  self.var,
            value = 3, indicatoron = 0).grid(column = 3, row = 3, sticky = "news")

        rb_4 = tk.Radiobutton(self.window, text = "Reumann-Witkam", variable =  self.var,
            value = 4, indicatoron = 0).grid(column = 3, row = 4, sticky = "news")

        rb_5 = tk.Radiobutton(self.window, text = "Lang", variable =  self.var,
            value = 5, indicatoron = 0).grid(column = 3, row = 5, sticky = "news")

        rb_6 = tk.Radiobutton(self.window, text = "Min-Max", variable =  self.var,
            value = 6, indicatoron = 0).grid(column = 3, row = 6, sticky = "news")

        rb_7 = tk.Radiobutton(self.window, text = "Douglas & Peucker", variable =  self.var,
            value = 7, indicatoron = 0).grid(column = 3, row = 7, sticky = "news")
        
        rb_8 = tk.Radiobutton(self.window, text = "Bend Simplify", variable =  self.var,
            value = 8, indicatoron = 0).grid(column = 3, row = 8, sticky = "news")
        
        tk.mainloop()
