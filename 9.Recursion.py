#head recursion  

def n(count):
    if count == 5:
        return

    n(count + 1)       # Recursive call first
    print(count)       # Work after the recursive call

n(0)

#tail recursion 

def n(count):
    if count == 5:
        return

    print(count)
    n(count + 1)  # Recursive call at the end

n(0)