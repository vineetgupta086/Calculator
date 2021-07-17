def GetCoor(obj):
    """Returns the row and column of a key

    Args:
        obj (string): the name of the key

    Returns:
        int: row of 
        int: 
    """
    if isinstance(obj,int):
        if obj == 0:
            row, col = 4, obj
        
        elif obj!=0:
            row, col = 3 - int((obj-1)/3), (obj-1)%3

    else:
        if obj == ".":
            row, col = 4, 1
        elif obj == "=":
            row, col = 4, 2
        elif obj == "÷":
            row, col = 1, 3
        elif obj == "×":
            row, col = 2, 3
        elif obj == "-":
            row, col = 3, 3
        elif obj == "+":
            row, col = 4, 3

    return row, col

def GetFun():
    pass