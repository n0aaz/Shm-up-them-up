# Créé par aduguaitschupp, le 21/03/2016 en Python


x = [122,38,45,11,58]
tri = []
lg  = len(x)

def minimum (x) :
    lg  = len(x)
    min = x[0]
    for i in range (lg):
        if x[i]<min :
            min = x[i]
    return (min)

print('le minimum dans la liste est : ',minimum(x))

for i in range (lg) :
    tri.append(minimum(x))
    print (tri)
    min = minimum(x)
    x.remove (min)









