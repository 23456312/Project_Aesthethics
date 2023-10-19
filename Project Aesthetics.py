
ext_values = 0
tops_values = 0
accs_values = 0
result=[]
ipo = ["Organizacion por categoria", ["Tops: "], ["Bottoms: "],
       ["Accesorios: "],["Exterior: "]]
tops=["1)Mini Dress","2)Cuello de Tortuga", "3)Crop Top", "4)Camiseta",
      "1)Overalls","2)Blusa","3)Cuello de Tortuga","4)Camisa con botones",
      "1)Dress","2)Nature Prints","3)Lace", "4)Gypsy",
      "1)Floral Dress","2)Nature Prints",
      "3)Crop Top","4)Camisa con botones"]
pants=["1)Pantalon","2)Falda"]
accs=["1)Corset","2)Orejeras", "3)Calentadores de brazo",
      "4)Calentadores de pierna", "5)Pulseras de perlas", "6)Medias",
      "1)Lentes circulares","2)Boina","3)Tote bag","4)Chaleco",
      "5)Bucket hat","6)Collar de Oro",
      "1)Puffy Sleeves", "2)Lentes de Sol", "3)Basket",
      "4)Collar Y2k", "5)Sombrero", "6)Corona de Flores",
      "1)Bucket Hat","2)Boina","3)Basket","4)Gorra",
      "5)Sombrero","6)Corona de Flores"]
exts=["1)Abrigo de piel","2)Cardigan", "3)Chaqueta de lana", "4)Parka",
      "1)Abrigo", "2)Cardigan",
      "3)Chaqueta de Cuero", "4)Gabardina",
      "1)Chamarra","2)Chaleco","3)Sudadera","4)Ninguna",
      "1)Sweater","2)Cardigan","3)Sudadera","4)Sudadera Oversized"]


print("Bienvenido a Project Aesthetics!!, en este lugar te ayudaremos a"
"escoger los mejores articulos para la temporada!")
ask=int(input("Que tipo de estacion te gustaria para realizar tu aesthetic."
"\nContamos con dos temporadas! \n 1)Invierno \n 2)Verano \n"))


if ask == 1:
    decision=int(input("Winterful decision!!\n"
                               "Has escogido Invierno. Cual de las siguientes dos"
                               "opciones escogerias: \n 1)Winter Fairy Coquete "
                               "\n 2)Winter Academia \n"))
    decision_2 = 0

            
            
elif ask ==2:
    decision_2=int(input("That's blooming great!!\n"
                             "Has escogido Verano. Cual de las siguientes dos"
                             "opciones escogerias: \n 1)Nature Core \n 2)Warmcore \n"))
    decision = 0
    
        

else:
    print("Nah, esa no es una opción")
            
          


def tops_final(decision, decision_2):
    """
    Uso de (funciones, condicionales, listas, listas anidadas)
    La funcion tops_final recibe decision o decision_2 y la
    transforma en la top especifica. Devuelve. estilo de
    Top
    """
    print(("¿Que tipo de top usarías?"))
    
    if decision == 1:
        print("\n",tops[0],"\n",tops[1],"\n",tops[2],"\n",tops[3])
        top_inv_v1=int(input())
        ipo[1].insert(1,tops[top_inv_v1-1])
        result.append(tops[top_inv_v1-1])
        return top_inv_v1
         
        
    elif decision == 2:
        print("\n",tops[4],"\n",tops[5],"\n",tops[6],"\n",tops[7])
        top_inv_v1=int(input())
        ipo[1].insert(1,tops[top_inv_v1+3])
        result.append(tops[top_inv_v1+3])
        return top_inv_v1
    
   
    if decision_2 == 1:
        print("\n",tops[8],"\n",tops[9],"\n",tops[10],"\n",tops[11])
        top_inv_v1=int(input())
        ipo[1].insert(1,tops[top_inv_v1+7])
        result.append(tops[top_inv_v1+7])
        return top_inv_v1
    
    elif decision_2 == 2:
        print("\n",tops[12],"\n",tops[13],"\n",tops[14],"\n",tops[15])
        top_inv_v1=int(input())
        ipo[1].insert(1,tops[top_inv_v1+11])
        result.append(tops[top_inv_v1+11])
        return top_inv_v1

def bottoms(top_inv_v1):
    """
    Uso de (funciones, condicionales, listas)
    La funcion bottoms recibe top_inv_v1 o sea la top de la pregunta
    pasada y la transforma en un bottom dependiendo de la opcion.
    Devuelve estilo de Bottom
    """
    if top_inv_v1 ==1:
        bottom_inv = 0
        top_values = 60
        ipo[2].insert(1,"None")
        return bottom_inv
    elif top_inv_v1 in (2,4):
        bottom_inv= int(input("¿Que tipo de bottom usarías? \n"
        "1)pantalones \n 2)falda \n"))
        tops_values = 40
        ipo[2].insert(1,pants[bottom_inv-1])
        result.append(pants[bottom_inv-1])
        return bottom_inv
    elif top_inv_v1 == 3:
        bottom_inv= int(input("¿Que tipo de bottom usarías?"
        "\n 1)pantalones \n 2)falda \n"))
        tops_values = 60
        ipo[2].insert(1,pants[bottom_inv-1])
        result.append(pants[bottom_inv-1])
        return bottom_inv
    else:
        print("Not available, sorry :(")

def accessories(bottom_inv):
    """
    Uso de (funciones, condicionales, listas, listas anidadas, ciclos)
    La funcion accessories recibe bottom_inv o sea el bottom de la
    pregunta pasada y la transforma en un accesorio dependiendo
    de la opcion. Devuelve estilo de accesorio
    """
    if bottom_inv in (0,1,2):
        print("Muy bien! \n¿Que tipo de accesorio usarías?")
        if decision == 1:
            print("\n",accs[0],"\n",accs[1],"\n",
                  accs[2],"\n",accs[3],"\n",accs[4],"\n",accs[5])
        elif decision == 2:
            print("\n",accs[6],"\n",accs[7],"\n",accs[8],"\n",
                  accs[9],"\n",accs[10],"\n",accs[11])
        if decision_2 == 1:
            print("\n",accs[12],"\n",accs[13],"\n",accs[14],"\n",
                  accs[15],"\n",accs[16],"\n",accs[17])
        elif decision_2 == 2:
            print("\n",accs[18],"\n",accs[19],"\n",accs[20],"\n",
                  accs[21],"\n",accs[22],"\n",accs[23])
        accesor=int(input())
        yes_no = int(input(("¿Otro accesorio? \n 1)Si \n 2)No \n")))
        if yes_no ==1:
            while yes_no <= 2:
                print("¿Que otro tipo de accesorio usarías?")
                if decision == 1:
                    print("\n",accs[0],"\n",accs[1],"\n",accs[2],
                          "\n",accs[3],"\n",accs[4],"\n",accs[5])
                    ipo[3].insert(1,accs[accesor-1])
                    result.append(accs[accesor-1])
                elif decision == 2:
                    print("\n",accs[6],"\n",accs[7],"\n",
                          accs[8],"\n",accs[9],"\n",
                          accs[10],"\n",accs[11])
                    ipo[3].insert(1,accs[accesor+5])
                    result.append(accs[accesor+5])
                if decision_2 == 1:
                    print("\n",accs[12],"\n",accs[13],"\n",
                          accs[14],"\n",
                          accs[15],"\n",accs[16],"\n",accs[17])
                    ipo[3].insert(1,accs[accesor+11])
                    result.append(accs[accesor+11])
                elif decision_2 == 2:
                    print("\n",accs[18],"\n",accs[19],"\n",
                          accs[20],"\n",accs[21],"\n",accs[22],
                          "\n",accs[23])
                    ipo[3].insert(1,accs[accesor+17])
                    result.append(accs[accesor+17])
                accesor=int(input())
                yes_no += 1
                nono = int(input(("¿Otro accesorio? \n 1)Si \n 2)No \n")))
                if nono ==2:
                    
                    return accesor
                    
            
            print("Ya basta!")
            return accesor
        
        elif yes_no == 2:
            if decision == 1:
                ipo[3].insert(1,accs[accesor-1])
                result.append(accs[accesor-1])
            elif decision == 2:
                ipo[3].insert(1,accs[accesor+5])
                result.append(accs[accesor+5])
            if decision_2 == 1:
                ipo[3].insert(1,accs[accesor+11])
                result.append(accs[accesor+11])
            elif decision_2 == 2:
                ipo[3].insert(1,accs[accesor+17])
                result.append(accs[accesor+17])
            
            return accesor
      
def exterior(accesor):
    """
    Uso de (funciones, condicionales, listas, listas anidadas)
    La funcion exterior recibe accesor o sea el accesorio de la
    pregunta pasada y la transforma en un prenda exterior dependiendo
    de la opcion. Devuelve estilo de prenda de exterior
    """
    if accesor in (1,5):
        accs_value = 0
        if decision ==1:
            print("¿Que tipo de prenda de extererior usarías?"
            "\n",exts[0],"\n",exts[1],"\n",exts[2],"\n",exts[3])
            ext = int(input())
            ipo[4].insert(1,exts[ext-1])
            result.append(exts[ext-1])
        elif decision ==2:
            print("¿Que tipo de prenda de extererior usarías?"
            "\n",exts[4],"\n",exts[5],"\n",exts[6],"\n",exts[7])
            ext = int(input())
            ipo[4].insert(1,exts[ext+3])
            result.append(exts[ext+3])
        if decision_2 == 1:
            print("¿Que tipo de prenda de extererior usarías?"
            "\n",exts[8],"\n",exts[9],"\n",exts[10],"\n",exts[11])
            ext = int(input())
            ipo[4].insert(1,exts[ext+7])
            result.append(exts[ext+7])
        elif decision_2 ==2:
            print("¿Que tipo de prenda de extererior usarías?"
            "\n",exts[12],"\n",exts[13],"\n",exts[14],"\n",exts[15])
            ext = int(input())
            ipo[4].insert(1,exts[ext+11])
            result.append(exts[ext+11])
        return ext
    elif accesor in (2,3,4,6):
        accs_value = 10
        if decision ==1:
            print("¿Que tipo de prenda de extererior usarías?"
            "\n",exts[0],"\n",exts[1],"\n",exts[2],"\n",exts[3])
            ext = int(input())
            ipo[4].insert(1,exts[ext-1])
            result.append(exts[ext-1])
        elif decision ==2:
            print("¿Que tipo de prenda de extererior usarías?"
            "\n",exts[4],"\n",exts[5],"\n",exts[6],"\n",exts[7])
            ext = int(input())
            ipo[4].insert(1,exts[ext+3])
            result.append(exts[ext+3])
        if decision_2 == 1:
            print("¿Que tipo de prenda de extererior usarías?"
            "\n",exts[8],"\n",exts[9],"\n",exts[10],"\n",exts[11])
            ext = int(input())
            ipo[4].insert(1,exts[ext+7])
            result.append(exts[ext+7])
        elif decision_2 ==2:
            print("¿Que tipo de prenda de extererior usarías?"
            "\n",exts[12],"\n",exts[13],"\n",exts[14],"\n",exts[15])
            ext = int(input())
            ipo[4].insert(1,exts[ext+11])
            result.append(exts[ext+11])
        return ext
    else:
        print("Not available, sorry :(")
       
def final(ext,ext_values,top_inv_v1,accs_values):
    """
    Uso de (funciones, condicionales, operadores)
    La funcion final recibe ext,ext_values,top_inv_v1,accs_values
    o sea valores asignados por la aesthetic de las 
    preguntas pasadas y la transformas en un un numero que
    posteriormente los suma para dar el porcentaje final
    de la aesthetic obtenida. Devuelve el porcentaje
    """
    if ext in (1,2,3):
        ext_values = 35
    elif ext == 4:
        ext_values = 20
    if top_inv_v1 in (1,3):
        top_values = 60
    elif top_inv_v1 in (2,4):
        top_values = 35
    return top_values,ext_values
    
        
    
        
top_choice = tops_final(decision, decision_2)
bottom_choice = bottoms(top_choice)
accesor_choice = accessories(bottom_choice)
exterior_choice = exterior(accesor_choice)
ext_values, top_values = final(exterior_choice,ext_values,
                               top_choice,accs_values)





final_sum = ext_values + top_values
print("El porcentaje de tu outfit es de:", final_sum,
      "% comparandolo con la aesthetic")
print("Tus resultados escogidos fueron los siguientes:", result)
print("Tus resultados, separados por categoria son:")
print(ipo)

