# Créé par aduguaitschupp, le 21/03/2016 en Python


x = [122,38,45,11,58,68,12,1,5,35,48]
tri = []





def minimum (x) :
    lg  = len(x)
    min = x[0]
    for i in range (lg):
        if x[i]<min :
            min = x[i]
    return (min)

print('le minimum dans la liste est : ',minimum(x))

for i in x :
    tri.append(minimum(x))
    print (tri)
    min = minimum(x)
    x.remove (min)
    print(x)








