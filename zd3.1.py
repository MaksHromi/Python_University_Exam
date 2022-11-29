def max(*argumenty):
    m=argumenty[0]
    for x in argumenty [1:]:
        if m<x:
            m=x
    return m
print(max(20000, 995, 2525, 21))
liczbamax = max(85, 34 , 300000, 73)
print(liczbamax)