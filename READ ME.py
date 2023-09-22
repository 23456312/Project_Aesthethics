"""
Proyecto Python
El programa realiza preguntas las cuales te ayudaran a sacar la mejor opcion de ropa.
Al final del programa tu outfit sera revelado.
Durante el proyecto usé 1,2,3 esto va a ser cambiado eventualmente por a, b y c. :)
"""
"""
Pregunta por la estacion y la persona responde a)invierno, b) verano, c) primavera, d) otono

Recibe: a),b),c) o d)
devuelve: resultado escogido y pasa a la siguiente parte
"""

print("Que tipo de estación te gustaría para realizar tu aesthethic. \n 1)invierno. \n 2)verano. \n 3)primavera \n 4)otoño  ")
seasons=int(input())



"""
Despues de eso se establecera un si cuando se cumple cada estacion para dar la aesthethic.
Por ejemplo:

si a) (invierno):
    ( winter_fairy_coquete o winter_academia)
Esto estara establecido para cada estacion*


Recibe: Tipo_ae1 o Tipo_ae2
devuelve: resultado escogido
"""

if seasons == 1:
    print("Has escogido invierno. Cual de las siguientes dos opciones escogerias \n 1)winter_fairy_coquete \n 2)winter_academia ")
else:
    print("No existe perdón :(")

"""
Despues sera establecida otra condicion para cada articulo de ropa de aesthethic
por ejemplo:
    si winter_fairy_coquette preguntar:
    "que tipo de top usarias"
        a) mini dress +60
        b) cuello de tortuga +40
        c) crop top +60
        d) camiseta +40 
Cada articulo de ropa tiene un porcentaje de compatibilidad, dicho porcentaje hara una sumatoria al final
y dira que compatible tu outfit es respecto a la aesthetic.

Recibe: a),b),c) o d)
devuelve: resultado de lo escogido

"""

winter_1 = int(input())

if winter_1 ==1:
    print("¿Que tipo de top usarías? \n 1)Mini Dress \n 2)Cuello de tortuga \n 3)Crop Top \n 4)Camiseta")
else:
    print("No existe perdon :(")

    

"""
Despues de esto el siguiente articulo de ropa seria los bottoms, en el caso de haber escogido mini dress en el inciso anterior esta parte sera saltada

por ejemplo,

si a) (mini dress):
    saltar a la parte de accesorios
else:

a) pantalon +0
b) falda +0

Recibe: a) o b)
devuelve: resultado de lo escogido
"""

top_inv=int(input())

if top_inv == 1:
    print("¿Que tipo de accesorio usarías? \n 1)Corset \n 2)Orejeras \n 3)Calentadores de brazo \n 4)Calentadores de pierna \n 5)Pulseras de perlas \n 6)Medias")
    def fairy_coquette(num):
        dress = num*0+60
        return dress
    
elif top_inv == 2 or top_inv ==4:
    print("¿Que tipo de bottom usarías? \n 1)pantalones \n 2)falda")
    def fairy_coquette(num):
        dress = num*0+40
        return dress

elif top_inv == 3:
    print("¿Que tipo de bottom usarías? \n 1)pantalones \n 2)falda")
    def fairy_coquette(num):
        dress = num*0+60
        return dress
    
else:
    print("Not available, sorry :(")

"""
Despues de esto el siguiente articulo de ropa seria los accesorios
aqui se podria crear un ciclo para escoger varios accesorios solo como maximo dos intentos antes de moverse
a la siguiente parte.
por ejemplo:
    preguntar al usuario "que articulo escogerias"
    a) corset +0
    b) orejeras +10
    c) calentadores de brazo +10
    d) calentadores de pierna +10
    e) pulseras de perlas +0
    f) medias +10
    
    
    Recibe: a),b),c),d), e), o f)
    devuelve: resultado de lo escogido
"""

if top_inv ==2 or top_inv ==3 or top_inv ==4:
    bottom_inv= int(input())
    if bottom_inv == 1 or bottom_inv == 2:
        print("¿Que tipo de accesorio usarías? \n 1)Corset \n 2)Orejeras \n 3)Calentadores de brazo \n 4)Calentadores de pierna \n 5)Pulseras de perlas \n 6)Medias")
        def corset(num2):
            acc_opt_1 = num2* 0
            return acc_opt_1
    else:
       print("Not available, sorry :(")


accs_inv= int(input())
if accs_inv ==1 or accs_inv==5:
    print("¿Que tipo de prenda de extererior usarías? \n 1)Abrigo de piel \n 2)Cardigan \n 3)Chaqueta de lana \n 4)Parka")
    def corset(num2):
        acc_opt_1 = num2* 0
        return acc_opt_1
elif accs_inv ==2 or accs_inv == 3 or  accs_inv ==4 or accs_inv ==6:
    print("¿Que tipo de prenda de extererior usarías? \n 1)Abrigo de piel \n 2)Cardigan \n 3)Chaqueta de lana \n 4)Parka")
    def corset(num2):
        acc_opt_1 = num2* 0+10
        return acc_opt_1

else:
    print("Not available, sorry :(")


"""
El siguiente articulo para preguntar serian las prendas exteriores:

a) abrigos de piel +20
b) cardigan +20
c) Chaqueta de lana +20
d) parka +10

Recibe: a),b),c) o d)
devuelve: resultado de lo escogido
"""


ext_inv = int(input())
if ext_inv == 1 or ext_inv ==2 or ext_inv ==3:
    print("---------Resultado Final---------")
    def ext_inv_1(num3):
        ext_opt = num3*0+20
        return ext_opt
elif ext_inv == 4:
    print("---------Resultado Final---------")
    def ext_inv_1(num3):
        ext_opt = num3*0+20
        return ext_opt

else:
    print("Not available, sorry :(")



"""
Al acabar te mostrara tus articulos escogidos con la compatibilidad o porcentaje que tienen con la aesthetic
Sumar todas las prendas escogidas y despues print 
Ejemplo:
    resultados:
        Mini dress, corset, calentadores de pierna, chaqueta de piel 90% de compatibilidad con la aesthetic

*Esto sera elaborado para cada tipo de aesthetic con diferentes opciones

"""

def closet(num, num2, num3):

    dress = fairy_coquette(num)
    acc_opt_1 = corset(num2)
    ext_opt = ext_inv_1(num3)
    
    
    return dress, acc_opt_1, ext_opt

print("Los árticulos escogidos tienen el siguiente procentaje con la aesthetic escogida:")
print(closet(1, 1, 1))


var1, var2, var3 = closet(1, 1, 1)

final_res_1= var1+var2+var3

print(final_res_1,"%" )



