"""
Proyecto Python
El programa realiza preguntas las cuales te ayudaran a sacar la mejor opcion de ropa.
Al final del programa tu outfit sera revelado.
"""


"""
Pregunta por la estacion y la persona responde a)invierno, b) verano, c) primavera, d) otono

Recibe: a),b),c) o d)
devuelve: resultado escogido y pasa a la siguiente parte
"""



"""
Despues de eso se establecera un si cuando se cumple cada estacion para dar la aesthethic.
Por ejemplo:

si a) (invierno):
    ( winter_fairy_coquete o winter_academia)
Esto estara establecido para cada estacion*


Recibe: Tipo_ae1 o Tipo_ae2
devuelve: resultado escogido
"""



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


"""
El siguiente articulo para preguntar serian las prendas exteriores:

a) abrigos de piel +20
b) cardigan +20
c) Chaqueta de lana +20
d) parka +10

Recibe: a),b),c) o d)
devuelve: resultado de lo escogido
"""



"""
Al acabar te mostrara tus articulos escogidos con la compatibilidad o porcentaje que tienen con la aesthetic
Sumar todas las prendas escogidas y despues print 
Ejemplo:
    resultados:
        Mini dress, corset, calentadores de pierna, chaqueta de piel 90% de compatibilidad con la aesthetic

*Esto sera elaborado para cada tipo de aesthetic con diferentes opciones

"""
