osztály = ['Keserű Tibor','Borsos Ferenc','Nagy Károly','Kovács Penelope','Kiss János','Fegyver Richard','Patai Dániel','Nagy Hunor','Kiss Péter','Sulyák Dániel']
for i in range(1):
    név = input("add meg a neved! ")
    matek = int(input("add meg a Matek jegyed! "))
    angol = int(input("add meg a Angol jegyed! "))
    magyar = int(input("add meg a Magyar jegyed! "))
    info = int(input("add meg a Infó jegyed! "))
    töri = int(input("add meg a Történelem jegyed! "))
    osztály.append(osztály)
print("osztály tanulói: ",osztály)
if név in osztály:
    print(név, + angol ,+ matek ,+ magyar ,+ info, + töri, " már létezik!")


