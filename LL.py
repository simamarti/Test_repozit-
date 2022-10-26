import Vertex
import math

class LL:

    def __init__(self):

        self.head = None
        self.m_counter = 0
        self.min_dist = math.inf
    
    def append(self, p_node):
                
        if self.isEmpty():

            self.head = p_node
            return True
        
        if self.head.m_next == None:

            if self.head == p_node:

                return False
        
            p_node.m_prev = self.head
            self.head.m_next = p_node
            
            return True

        current = self.head
        prev = None
        
        while current is not None:

            if current == p_node:

                return False
            
            prev = current
            current = current.m_next
            
        current = prev
        
        p_node.m_prev = current
        current.m_next = p_node
        
        return True
        
    def insert(self, p_prev, p_node):
        
        if self.isEmpty():
            print("1")
            return False
        
        if self.head.m_next == None:

            if p_prev == self.head:
                    
                p_node.m_prev = self.head
                self.head.m_next = p_node
                
                return True
                
            else:
                
                return False

        current = self.head
        pointer = None
        
        if self.search(p_node):

            return False
            
        if item := self.search(p_prev):

                p_node.m_prev = item
                p_node.m_next = item.m_next
                
                if item.m_next is not None:

                    item.m_next.m_prev = p_node

                item.m_next = p_node

                return True

        return False
    
    def delete(self, p_node):

        if self.isEmpty():

            return False

        if self.head.m_next == None:

            self.head = None
            return True
        
        if item := self.search(p_node):

            item.m_prev.m_next = item.m_next
                
            if item.m_next is not None:

                item.m_next.m_prev = item.m_prev
                    
            return True

        else:

            return False
    
    def search(self, p_node):

        if self.isEmpty():

            return False
        
        current = self.head
        
        while current is not None:

            if current == p_node:

                return current

            current = current.m_next
            
        return False
    
    def minDist(self):

        current_1 = self.head
        current_2 = self.head.m_next
        dist_min = math.inf
        
        while current_1.m_next is not None:

            current_2 = current_1.m_next
            
            while current_2 is not None:

                dist_min = min(dist_min, current_1.dist(current_2))
                current_2 = current_2.m_next

            current_1 = current_1.m_next

        return dist_min
                
    def print(self):

        current = self.head
        
        if current == None:

            return False
        
        if current.m_next == None:

            print("prev: None")
            print("data: (" + str(current.m_x) + ", " + str(current.m_y) + ")")
            print("next: None")
            print("-------------")
            return True
        
        while current is not None:

            if current.m_prev == None:

                print("prev: None")

            else:

                print("prev: (" + str(current.m_prev.m_x) + ", " + str(current.m_prev.m_y) + ")")

            print("data: (" + str(current.m_x) + ", " + str(current.m_y) + ")")

            if current.m_next == None:

                print("next: None")

            else:
                
                print("next: (" + str(current.m_next.m_x) + ", " + str(current.m_next.m_y) + ")")

            current = current.m_next
            print("-------------")

        print("---------------------------")
        return True

    def draw(self, canvas):

        if self.isEmpty():

            print ("Linked list is empty, try load the data one more.")
                
        else:
        
            current = self.head

            canvas.create_oval(int(current.m_x) - 2, int(current.m_y) - 2,
                           int(current.m_x) + 2, int(current.m_y) + 2, fill="#000000")
        
            current = current.m_next
        
            while current is not None:
        
                canvas.create_oval(int(current.m_x) - 2, int(current.m_y) - 2,
                           int(current.m_x) + 2, int(current.m_y) + 2, fill="#000000")

                current = current.m_next
            
    def isEmpty(self):

        if self.head == None:

            return True

        return False
    
