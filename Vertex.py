import math

class Vertex:

    def __init__(self, p_x, p_y):

        self.m_x = p_x
        self.m_y = p_y
        self.m_prev = None
        self.m_next = None
        
    def __eq__(self, other):

        if not isinstance(other, Vertex):

            return False
        
        if self.m_x == other.m_x and self.m_y == other.m_y:

            return True

        else:
            
            return False

    def dist(self, p_node):

        return math.sqrt((int(p_node.m_x) - int(self.m_x))**2 + (int(p_node.m_y) - int(self.m_y))**2)
