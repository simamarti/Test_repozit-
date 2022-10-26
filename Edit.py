import LL
import math

def customize(LL, x, y):

    max_x = -math.inf
    max_y = -math.inf
    min_x = math.inf
    min_y = math.inf
    print(str(x) + ", " + str(y))
    current = LL.head
    while current is not None:

        current.m_y = int(current.m_y)*(-1)
        
        max_x = max(max_x, float(current.m_x))
        max_y = max(max_y, float(current.m_y))
        min_x = min(min_x, float(current.m_x))
        min_y = min(min_y, float(current.m_y))
        
        current = current.m_next

    x_range = max_x - min_x
    y_range = max_y - min_y
    print("rozsah: " + str(x_range) + " X " + str(y_range))

    width = x - 50
    height = y - 50
    
    scaling_x = 0
    scaling_y = 0
    
    if x_range == 0 and not y_range == 0:

        scaling_x = 1
        scaling_y = height/y_range
        
    elif y_range == 0 and not x_range == 0:
        
        scaling_x = height/x_range
        scaling_y = 1

    elif not x_range == 0 and not y_range == 0:

        scaling_x = min(width/x_range, height/y_range)
        scaling_y = scaling_x
        
    else:

        return (LL, x, y, 0, 0, False)      
    
    print("Rozměr mínus 50, scaling: " + str(width) + " X " + str(height) + ", " + str(scaling_x) + ", " + str(scaling_y))
    current = LL.head
    while current is not None:

        print("Před <" + str(current.m_x) + ", " + str(current.m_y) + ">")
        current.m_x = int(current.m_x) * scaling_x
        current.m_y = int(current.m_y) * scaling_y
        print("Po <" + str(current.m_x) + ", " + str(current.m_y) + ">")
        current = current.m_next
        print("------------------------------------")

    min_Dist = LL.minDist()
    
    if min_Dist < 3:
        
        return (0, 0, 0, 0, 0, True)
    
    center_x = (scaling_x * x_range)//2
    center_y = (scaling_y * y_range)//2
    min_x *= scaling_x
    min_y *= scaling_y
    print("min_x = " + str(min_x))
    print("min_y = " + str(min_y))

    print("centrum: " + str(min_x + center_x) + " X " + str(min_y + center_y))
    
    return (LL, x, y, min_x + center_x, min_y + center_y, False)

def move(LL, width, height, centroid_x, centroid_y):

        print("Centroid <" + str(centroid_x) + ", " + str(centroid_y) + ">")
        move_x = -centroid_x + (width/2)
        move_y = -centroid_y + (height/2)
        print("Move <" + str(move_x) + ", " + str(move_y) + ">")
        current = LL.head
        while current is not None:
            print("Před <" + str(current.m_x) + ", " + str(current.m_y) + ">")
            current.m_x = int(current.m_x) + move_x
            current.m_y = int(current.m_y) + move_y
            print("Po <" + str(current.m_x) + ", " + str(current.m_y) + ">")
            current = current.m_next

        return LL

def edit(LL, x, y):

    LL, canvas_x, canvas_y, center_x, center_y, error = customize(LL, x, y)
    
    if error == True:
        print("ERROR")
        return False
    
    return move(LL, canvas_x, canvas_y, center_x, center_y)
