{
"Tanulók": [
{
        "név": "Keserű Tibor",
        "jegy1": "matek",
        "jegy2": "magyar",
        "jegy3": "angol",
        "jegy4": "töri",
        "jegy5": "infó",
        
        "név": "Borsos Ferenc",
        "jegy1": "matek",
        "jegy2": "magyar",
        "jegy3": "angol",
        "jegy4": "töri",
        "jegy5": "infó",
         
         
        "név": "Kiss János",
        "jegy1": "matek",
        "jegy2": "magyar",
        "jegy3": "angol",
        "jegy4": "töri",
        "jegy5": "infó",
         
         
         "név": "Kovács Penelope",
        "jegy1": "matek",
        "jegy2": "magyar",
        "jegy3": "angol",
        "jegy4": "töri",
        "jegy5": "infó",
         
         
         "név": "Nagy Károly",
        "jegy1": "matek",
        "jegy2": "magyar",
        "jegy3": "angol",
        "jegy4": "töri",
        "jegy5": "infó",
         
         
            }, 
]
}
jegyek = []
osztály = ['Keserű Tibor','Borsos Ferenc','Nagy Károly','Kovács Penelope','Kiss János','Fegyver Richard','Patai Dániel','Nagy Hunor','Kiss Péter','Sulyák Dániel']
for i in range(10):
    név = input("add meg a neved! ")
    if név =='Keserű Tibor':
        print("A neved Tibor")
    elif név != osztály:
        print("hibás név vagy nem található")
    
    matek = int(input("add meg a Matek jegyed! "))
    jegyek.append(matek)
    angol = int(input("add meg a Angol jegyed! "))
    jegyek.append(angol)
    magyar = int(input("add meg a Magyar jegyed! "))
    jegyek.append(magyar)
    info = int(input("add meg a Infó jegyed! "))
    jegyek.append(info)
    töri = int(input("add meg a Történelem jegyed! "))
    jegyek.append(töri)
    osztály.append(osztály)
print("osztály tanulói: ",osztály)
if név in osztály:
    print(név, + angol ,+ matek ,+ magyar ,+ info, + töri, " már létezik!")
eredmenyek = [int(x.strip()) for x in osztály]

def average(lst):
    return sum(lst) / len(lst)

print("Az átlag:", average(eredmenyek))