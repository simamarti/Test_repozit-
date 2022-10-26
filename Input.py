import Vertex
import LL
import os
import re
import tkinter
import math
   
def load(data):

    Linked_List = LL.LL()
            
    Splitted = data.split('\n')
    
    if Splitted[0] == "":

        print("Empty input.")
        return Linked_List
        
    for item in Splitted:
        
        try:
            
            x, y = item.split('\t')
            
        except ValueError:

            print("<" + str(item) + "> Wrong format, row has been skpped.")
            
        else:
            
            if not check(x, y):

                print("<" + str(x) + ">, <" + str(y) + "> Value must be numeric, row has been skpped.")
            
            else:
            
                if not Linked_List.append(Vertex.Vertex(x, y)):

                    print("You don't alow to append duplicite point.")

                else:

                    print("(" + str(x) + "; " + str(y) + ") Point has been successfully loaded.")
            

    return Linked_List

def check(x, y):

    if (re.search("^(\+|-)?([0-9]+.)?[0-9]+$", x) and re.search("^(\+|-)?([0-9]+.)?[0-9]+$", y)):

        return True
                
    else:
        
        return False
    
def input(name):

    with open(name, 'r', encoding = 'utf-8') as file:
        
        Linked_List = LL.LL()
        
        for line in file:
            
            item = line.split("\n")[0]
            
            Splitted = item.split('\t')
            x=Splitted[0]
            y=Splitted[1]

            if not check(x, y):

                print("Unexpected error, row has beeb skiped.")

            else:

                 if not Linked_List.append(Vertex.Vertex(x, y)):

                    print("Unexpected error, row has beeb skiped.")
    
        return Linked_List
        
