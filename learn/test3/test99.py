def A():
    print('into a')
    a = 1
    aa =2
    return a, aa

def B():
    print('into b')
    return A()

a,b = B()
print(a,b)
