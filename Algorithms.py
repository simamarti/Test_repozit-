import LL
import Dialog as dg
import Interface
import Euclidian
import Draw
        
def euclidian(LL):

    Dg = dg.Dialog()

    if (LL is not False):
# Dg.value
        # Dg.dialog("Algorithm delete every following point which is closer\nthan the <parameter> to currently being processed point")
        Linked_List = Euclidian.algorithm(LL, 40)
        
        return Linked_List

    else:

        return False



