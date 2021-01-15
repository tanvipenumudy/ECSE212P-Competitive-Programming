pos = int(input("Initial position: "))
s = int(input("Steps: "))

def start(init, step):
    print(init, end = "")
    p = init - step
    track(init, step, p)
    
def track(init, step, p):
    if(p == init):
        print(",", init)
    elif(p > 0):
        print(",", p, end = "")
        p -= step
        track(init, step, p)
    else:
        print(",", p, end = "")
        step -= (2 * step)
        p -= step
        track(init, step, p)
start(pos, s)