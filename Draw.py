import tkinter

def draw(LL, color, canvas):

    current = LL.head
            
    while current.m_next is not None:
            print("<" + str(current.m_x)  + ", " + str(current.m_y) + ">")
            canvas.create_oval(int(current.m_x) - 2, int(current.m_y) - 2,
                               int(current.m_x) + 2, int(current.m_y) + 2, fill = color)
            canvas.create_line(int(current.m_x), int(current.m_y),
                               int(current.m_next.m_x), int(current.m_next.m_y), fill = color)
                
            current = current.m_next
                
    canvas.create_oval(int(current.m_x) - 2, int(current.m_y) - 2,
                int(current.m_x) + 2, int(current.m_y) + 2, fill = color)

