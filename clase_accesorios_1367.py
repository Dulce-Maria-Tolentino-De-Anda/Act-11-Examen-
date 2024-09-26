# zona de clases
class accesorio1367:
        
# LISTAS
    print("***** Listas ***** \n")
    def lista_MondayDancing_1367(self):
        Tipo_accesorios_1367 = ["cargador ","lente profesional","mochila para camara",
                            "tripie de camra", "lente camara 4k" ]
        print(Tipo_accesorios_1367)
        for y in Tipo_accesorios_1367:
            print(y)
        print("\n")

# TUPLAS
    def tupla_MondayDancing_1367(self):
        print("***** Tuplas ***** \n")
        ## esto se refiere a la cantidad de camras que se necesita para una sucursal
        Modelo_1367 = ("120 pares", "60 pares", "200 pares","50 pares", "40 pares", "100 pares","250 pares")
        print(Modelo_1367)
        for a in Modelo_1367:
            print(a)
        print("\n")

# CONJUNTOS
    def diccionario_MondayDancing_1367(self):
        print("***** Diccionarios ***** \n")
        ## esto se refiere al precio que tiene cada accesorio
        Precio_1367 = {
        "lente profesional-":450, "tripie de camara -":400,
        "aro de luz led-":450 ,"mochila para camara-":800,
        "lente camara 4k-":1500, "cargador-":3500
        } 
        print(Precio_1367)
        for b, z in Precio_1367.items():
            print(b,z)
        print("\n")

# SETS
    def sets_MondayDancing_1367(self):
        print("***** Sets ***** \n")
        ## esto se refiere a la capacidad maxima de calzados que puede tener una susucrsal
        existencias_1367 = {"3500 cargador","4005 cargador","450 lente profesional","400 tripie de camra", "1500 lente camara 4k", "2020 mochila para camra", " 450 aro de luz led"}
        print(existencias_1367)
        for c in existencias_1367:
            print(c)

# utilizacion del objeto
x = accesorio1367 ()
x.lista_MondayDancing_1367()
x.tupla_MondayDancing_1367()
x.diccionario_MondayDancing_1367()
x.sets_MondayDancing_1367()