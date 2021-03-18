
def urai(x):
    j=0
    l=""
    while j<= len(x):
        l= l+ ((x[0:j]))
        j+=1
    return l
    
print(urai('Code'))
print(urai('Python'))
print(urai('Purwadhika'))


def rajut(x):
    i = 0
    z = 1
    k = ""
    while i <= len(x):
        k=k+x[i]
        z+=1
        i=i+z
    return k

print(rajut('CCoCodCode'))
print(rajut('PPyPytPythPythoPython'))
print(rajut('PPuPurPurwPurwaPurwadPurwadhPurwadhiPurwadhikPurwadhika'))
