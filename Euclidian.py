import LL

def incircle(center, parameter, point):

    return( (int(point.m_x) - int(center.m_x))**2 + (int(point.m_y) - int(center.m_y))**2) < (int(parameter)**2)

def algorithm(Linked_List, parameter):

    LL_mod = LL.LL()
    
    current = Linked_List.head.m_next
    LL_mod.append(Linked_List.head)
    center = Linked_List.head
    
    while current.m_next is not None:

        if not incircle(center, parameter, current):

            LL_mod.append(current)
            center = current
            current = center.m_next

        else:

            current = current.m_next

    LL_mod.append(current)
    print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    LL_mod.print()
    print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    return LL_mod

    
