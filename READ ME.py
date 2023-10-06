
"""----------------Winter 1-------------------------------"""
def seasons_winter():
    if winter_1 ==1:
        top_inv_v1=int(input("¿Que tipo de top usarías? \n 1)Mini Dress \n 2)Cuello de tortuga \n 3)Crop Top \n 4)Camiseta \n"))
        if top_inv_v1 ==1:
            bottom_inv_down = 0
            tops_values = 60
            accs_inv= int(input("¿Que tipo de accesorio usarías? \n 1)Corset \n 2)Orejeras \n 3)Calentadores de brazo \n 4)Calentadores de pierna \n 5)Pulseras de perlas \n 6)Medias \n"))
            yes_no= int(input("¿Escoge otro accesorio? \n 1)si \n 2)No \n"))
            while yes_no ==1:
                accs_inv= int(input("¿Que tipo de accesorio usarías? \n 1)Corset \n 2)Orejeras \n 3)Calentadores de brazo \n 4)Calentadores de pierna \n 5)Pulseras de perlas \n 6)Medias \n"))
                yes_no= int(input("¿Escoge otro accesorio? \n 1)Si \n 2)No \n"))
        elif top_inv_v1 == 2 or top_inv_v1 ==4:
            bottom_inv_down= int(input("¿Que tipo de bottom usarías? \n 1)pantalones \n 2)falda \n"))
            tops_values = 40
        elif top_inv_v1 == 3:
            bottom_inv_down= int(input("¿Que tipo de bottom usarías? \n 1)pantalones \n 2)falda \n"))
            tops_values = 60
        else:
            print("Not available, sorry :(")
        if bottom_inv_down in (1,2):
            accs_inv= int(input("¿Que tipo de accesorio usarías? \n 1)Corset \n 2)Orejeras \n 3)Calentadores de brazo \n 4)Calentadores de pierna \n 5)Pulseras de perlas \n 6)Medias \n"))
            yes_no= int(input("¿Escoge otro accesorio? \n 1)si \n 2)No \n"))
            while yes_no ==1:
                accs_inv= int(input("¿Que tipo de accesorio usarías? \n 1)Corset \n 2)Orejeras \n 3)Calentadores de brazo \n 4)Calentadores de pierna \n 5)Pulseras de perlas \n 6)Medias \n"))
                yes_no= int(input("¿Escoge otro accesorio? \n 1)Si \n 2)No \n"))
        if accs_inv in (1,5):
            ext_inv=int(input("¿Que tipo de prenda de extererior usarías? \n 1)Abrigo de piel \n 2)Cardigan \n 3)Chaqueta de lana \n 4)Parka \n"))
            accs_values = 0
        elif accs_inv in (2,3,4,6):
            ext_inv=int(input("¿Que tipo de prenda de extererior usarías? \n 1)Abrigo de piel \n 2)Cardigan \n 3)Chaqueta de lana \n 4)Parka \n"))
            accs_values = 10
        else:
            print("Not available, sorry :(")
        if ext_inv in (1,2,3):
            ext_values = 20
        elif ext_inv == 4:
            ext_values = 10
            
        if top_inv_v1 ==1:
            top_inv_v1 = 'Mini Dress'
        elif top_inv_v1 ==2:
            top_inv_v1 = 'Cuello de Tortuga'
        elif top_inv_v1 == 3:
            top_inv_v1 = 'Crop Top'
        elif top_inv_v1 == 4:
            top_inv_v1 = 'Camiseta'
            
        if accs_inv ==1:
            accs_inv = 'Corset'
        elif accs_inv ==2:
            accs_inv = 'Orejeras'
        elif accs_inv == 3:
            accs_inv = 'Calentadores de brazo'
        elif accs_inv == 4:
            accs_inv = 'Calentadores de pierna'
        elif accs_inv == 5:
            accs_inv = 'Pulseras de perlas'
        elif accs_inv == 6:
            accs_inv = 'Medias'
            
        if ext_inv ==1:
            ext_inv = 'Abrigo de piel'
        elif ext_inv ==2:
            ext_inv = 'Cardigan'
        elif ext_inv == 3:
            ext_inv = 'Chaqueta de lana'
        elif ext_inv == 4:
            ext_inv = 'Parka'
        if bottom_inv_down == 0:
            bottom_inv_down = 'None'
        
    
        if bottom_inv_down == 1 or bottom_inv_down == 2:#We need to add so that the options chosen by the person pop out in the final list
            if bottom_inv_down ==1:
                bottom_inv_down = 'Pantalones'
            elif bottom_inv_down ==2:
                bottom_inv_down = 'Falda'
            result.append(top_inv_v1)
            result.append(accs_inv)
            result.append(bottom_inv_down)
            result.append(ext_inv)
        else:
            result.append(top_inv_v1)
            result.append(accs_inv)
            result.append(ext_inv)
                
        final_sum = ext_values + tops_values + accs_values
        print("El porcentaje de tu outfit es de:", final_sum, "% comparandolo con la aesthetic")
       
        if bottom_inv_down == 1 or bottom_inv_down == 2:#We need to add so that the options chosen by the person pop out in the final list
            ipo[1].insert(1, top_inv_v1)
            ipo[3].insert(1, accs_inv)
            ipo[2].insert(1, bottom_inv_down)
            ipo[4].insert(1, ext_inv)
        else:
            ipo[1].insert(1, top_inv_v1)
            ipo[3].insert(1, accs_inv)
            ipo[2].insert(1, "none")
            ipo[4].insert(1, ext_inv)
    

"""----------------Winter 2-------------------------------"""

def season_winter_2():
    if winter_1 ==2:
        top_inv_v1=int(input("¿Que tipo de top usarías? \n 1)Overalls \n 2)Cuello de tortuga \n 3)Blusa \n 4)Camisa con botones \n"))
        if top_inv_v1 ==1:
            bottom_inv_down = 0
            tops_values = 0
            accs_inv= int(input("¿Que tipo de accesorio usarías? \n 1)Lentes circulares \n 2)Boina \n 3)Tote bag \n 4)Chaleco \n 5)Bucket hat \n 6)Collar de Oro \n"))
            yes_no= int(input("¿Escoge otro accesorio? \n 1)si \n 2)No \n"))
            while yes_no ==1:
                accs_inv= int(input("¿Que tipo de accesorio usarías? \n 1)Lentes circulares \n 2)Boina \n 3)Tote bag \n 4)Chaleco \n 5)Bucket hat \n 6)Collar de Oro \n"))
                yes_no= int(input("¿Escoge otro accesorio? \n 1)Si \n 2)No \n"))
        elif top_inv_v1 == 3 or top_inv_v1 ==4:
            bottom_inv_down= int(input("¿Que tipo de bottom usarías? \n 1)pantalones \n 2)falda \n"))
            tops_values = 40
        elif top_inv_v1 == 2:
            bottom_inv_down= int(input("¿Que tipo de bottom usarías? \n 1)pantalones \n 2)falda \n"))
            tops_values = 60
        else:
            print("Not available, sorry :(")
        if bottom_inv_down in (1,2):
            accs_inv= int(input("¿Que tipo de accesorio usarías? \n 1)Lentes circulares \n 2)Boina \n 3)Tote bag \n 4)Chaleco \n 5)Bucket hat \n 6)Collar de Oro \n"))
            yes_no= int(input("¿Escoge otro accesorio? \n 1)si \n 2)No \n"))
            while yes_no ==1:
                accs_inv= int(input("¿Que tipo de accesorio usarías? \n 1)Lentes circulares \n 2)Boina \n 3)Tote bag \n 4)Chaleco \n 5)Bucket hat \n 6)Collar de Oro \n"))
                yes_no= int(input("¿Escoge otro accesorio? \n 1)Si \n 2)No \n"))
        if accs_inv in (6,5):
            ext_inv=int(input("¿Que tipo de prenda de extererior usarías? \n 1)Abrigo de piel \n 2)Cardigan \n 3)Chaqueta de lana \n 4)Gabardina \n"))
            accs_values = 0
        elif accs_inv in (2,3,4,1):
            ext_inv=int(input("¿Que tipo de prenda de extererior usarías? \n 1)Abrigo \n 2)Cardigan \n 3)Chaqueta de cuero \n 4)Gabardina \n"))
            accs_values = 10
        else:
            print("Not available, sorry :(")
        if ext_inv in (1,2,4):
            ext_values = 20
        elif ext_inv == 3:
            ext_values = 0
          
        if top_inv_v1 ==1:
            top_inv_v1 = 'Overalls'
        elif top_inv_v1 ==2:
            top_inv_v1 = 'Cuello de Tortuga'
        elif top_inv_v1 == 3:
            top_inv_v1 = 'Blusa '
        elif top_inv_v1 == 4:
            top_inv_v1 = 'Camisa con botones'
            
        if accs_inv ==1:
            accs_inv = 'Lentes Circulares'
        elif accs_inv ==2:
            accs_inv = 'Boina'
        elif accs_inv == 3:
            accs_inv = 'Tote Bag'
        elif accs_inv == 4:
            accs_inv = 'Chaleco'
        elif accs_inv == 5:
            accs_inv = 'Bucket Hat'
        elif accs_inv == 6:
            accs_inv = 'Collar de Oro'
            
        if ext_inv ==1:
            ext_inv = 'Abrigo'
        elif ext_inv ==2:
            ext_inv = 'Cardigan'
        elif ext_inv == 3:
            ext_inv = 'Chaqueta de cuero'
        elif ext_inv == 4:
            ext_inv = 'Gabardina'
        if bottom_inv_down == 0:
            bottom_inv_down = 'None'
            
        if bottom_inv_down == 1 or bottom_inv_down == 2:#We need to add so that the options chosen by the person pop out in the final list
            if bottom_inv_down ==1:
                bottom_inv_down = 'pantalones'
            if bottom_inv_down == 2:
                bottom_inv_down = 'Falda'
            result.append(top_inv_v1)
            result.append(accs_inv)
            result.append(bottom_inv_down)
            result.append(ext_inv)
        else:
            result.append(top_inv_v1)
            result.append(accs_inv)
            result.append(ext_inv)
                
    
        final_sum = ext_values + tops_values + accs_values
        print("El porcentaje de tu outfit es de:", final_sum, "% comparandolo con la aesthetic")
       
        if bottom_inv_down == 1 or bottom_inv_down == 2:#We need to add so that the options chosen by the person pop out in the final list
            ipo[1].insert(1, top_inv_v1)
            ipo[3].insert(1, accs_inv)
            ipo[2].insert(1, bottom_inv_down)
            ipo[4].insert(1, ext_inv)
        else:
            ipo[1].insert(1, top_inv_v1)
            ipo[3].insert(1, accs_inv)
            ipo[2].insert(1, "none")
            ipo[4].insert(1, ext_inv)



"""---------------Defining the lists---------------"""
result=[]
ipo = ["Organizacion por categoria", ["Tops: "], ["Bottoms: "], ["Accesorios: "], ["Exterior: "]]

"""-----------------------------------------------"""
ask=int(input("Que tipo de estacion te gustaria para realizar tu aesthetic.\n 1)invierno. \n 2)verano(NA). \n 3)primavera(NA) \n 4)otoño(NA)\n"))
if ask == 1:
    winter_1=int(input("Has escogido invierno. Cual de las siguientes dos opciones escogerias \n 1)winter_fairy_coquete \n 2)winter_academia \n"))


seasons_winter()

season_winter_2()


print("Tus resultados escogidos fueron los siguientes:", result)
print("Tus resultados, separados por categoria son:")
print(ipo)
    
