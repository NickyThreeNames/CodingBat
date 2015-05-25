"""Given a string, return a new string where the first and last chars have been exchanged. """

def front_back(str):
    if len(str) <=1:
        return str
    else:
        a = str[0]
        b = str[-1]
        c = str[1:len(str)-1]
        return b + c + a    
