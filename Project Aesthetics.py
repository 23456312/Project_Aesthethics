
def seasons_winter():
    """Calcula tu porcentaje de compatibilidad con la ropa usada en Winter Fairy Coquette."""
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
        
    
        if bottom_inv_down == 1 or bottom_inv_down == 2:
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
       
        if bottom_inv_down == 1 or bottom_inv_down == 2:
            ipo[1].insert(1, top_inv_v1)
            ipo[3].insert(1, accs_inv)
            ipo[2].insert(1, bottom_inv_down)
            ipo[4].insert(1, ext_inv)
        else:
            ipo[1].insert(1, top_inv_v1)
            ipo[3].insert(1, accs_inv)
            ipo[2].insert(1, "none")
            ipo[4].insert(1, ext_inv)
    


def season_winter_2():
    """Calcula tu porcentaje de compatibilidad con la ropa usada en Winter Academia."""
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
            
        if bottom_inv_down == 1 or bottom_inv_down == 2:
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
       
        if bottom_inv_down == 1 or bottom_inv_down == 2:
            ipo[1].insert(1, top_inv_v1)
            ipo[3].insert(1, accs_inv)
            ipo[2].insert(1, bottom_inv_down)
            ipo[4].insert(1, ext_inv)
        else:
            ipo[1].insert(1, top_inv_v1)
            ipo[3].insert(1, accs_inv)
            ipo[2].insert(1, "none")
            ipo[4].insert(1, ext_inv)

def season_verano_1():
    """Calcula tu porcentaje de compatibilidad con la ropa usada en Nature Core."""
    if spring ==1:
        top_inv_v1=int(input("¿Que tipo de top usarías? \n 1)Floral Dress \n 2)Nature Prints \n 3)Crop Top \n 4)Camisa con botones \n"))
        if top_inv_v1 ==1:
            bottom_inv_down = 0
            tops_values = 0
            accs_inv= int(input("¿Que tipo de accesorio usarías? \n 1)Bucket Hat \n 2)Boina \n 3)Basket \n 4)Gorra \n 5)Sombrero \n 6)Corona de flores \n"))
            yes_no= int(input("¿Escoge otro accesorio? \n 1)si \n 2)No \n"))
            while yes_no ==1:
                accs_inv= int(input("¿Que tipo de accesorio usarías? \n 1)Bucket Hat \n 2)Boina \n 3)Basket \n 4)Gorra \n 5)Sombrero \n 6)Corona de flores \n"))
                yes_no= int(input("¿Escoge otro accesorio? \n 1)Si \n 2)No \n"))
        elif top_inv_v1 == 3 or top_inv_v1 ==4:
            bottom_inv_down= int(input("¿Que tipo de bottom usarías? \n 1)pantalones \n 2)falda \n"))
            tops_values = 30
        elif top_inv_v1 == 2:
            bottom_inv_down= int(input("¿Que tipo de bottom usarías? \n 1)pantalones \n 2)falda \n"))
            tops_values = 60
        else:
            print("Not available, sorry :(")
        if bottom_inv_down in (1,2):
            accs_inv= int(input("¿Que tipo de accesorio usarías? \n 1)Bucket Hat \n 2)Boina \n 3)Basket \n 4)Gorra \n 5)Sombrero \n 6)Corona de flores \n"))
            yes_no= int(input("¿Escoge otro accesorio? \n 1)si \n 2)No \n"))
            while yes_no ==1:
                accs_inv= int(input("¿Que tipo de accesorio usarías? \n 1)Bucket Hat \n 2)Boina \n 3)Basket \n 4)Gorra \n 5)Sombrero \n 6)Corona de flores \n"))
                yes_no= int(input("¿Escoge otro accesorio? \n 1)Si \n 2)No \n"))
        if accs_inv in (2,4):
            ext_inv=int(input("¿Que tipo de prenda de extererior usarías? \n 1)Sweater \n 2)Cardigan \n 3)Sudadera \n 4)Sudadera Oversized \n"))
            accs_values = 0
        elif accs_inv in (3,6,1,5):
            ext_inv=int(input("¿Que tipo de prenda de extererior usarías? \n 1)Sweater \n 2)Cardigan \n 3)Sudadera \n 4)Sudadera Oversized \n"))
            accs_values = 10
        else:
            print("Not available, sorry :(")
        if ext_inv in (1,2):
            ext_values = 20
        elif ext_inv in (3,4):
            ext_values = 0
          
        if top_inv_v1 ==1:
            top_inv_v1 = 'Floral Dress'
        elif top_inv_v1 ==2:
            top_inv_v1 = 'Nature Prints'
        elif top_inv_v1 == 3:
            top_inv_v1 = 'Crop Top '
        elif top_inv_v1 == 4:
            top_inv_v1 = 'Camisa con botones'
            
        if accs_inv ==1:
            accs_inv = 'Bucket Hat'
        elif accs_inv ==2:
            accs_inv = 'Boina'
        elif accs_inv == 3:
            accs_inv = 'Basket'
        elif accs_inv == 4:
            accs_inv = 'Gorra'
        elif accs_inv == 5:
            accs_inv = 'Sombrero'
        elif accs_inv == 6:
            accs_inv = 'Corona de flores'
            
        if ext_inv ==1:
            ext_inv = 'Sweater'
        elif ext_inv ==2:
            ext_inv = 'Cardigan'
        elif ext_inv == 3:
            ext_inv = 'Sudadera'
        elif ext_inv == 4:
            ext_inv = 'Sudadera Oversized'
        if bottom_inv_down == 0:
            bottom_inv_down = 'None'
            
        if bottom_inv_down == 1 or bottom_inv_down == 2:
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
       
        if bottom_inv_down == 1 or bottom_inv_down == 2:
            ipo[1].insert(1, top_inv_v1)
            ipo[3].insert(1, accs_inv)
            ipo[2].insert(1, bottom_inv_down)
            ipo[4].insert(1, ext_inv)
        else:
            ipo[1].insert(1, top_inv_v1)
            ipo[3].insert(1, accs_inv)
            ipo[2].insert(1, "none")
            ipo[4].insert(1, ext_inv)

def season_verano_2():
    """Calcula tu porcentaje de compatibilidad con la ropa usada en Winter Fairy WarmCore."""
    if spring ==2:
        top_inv_v1=int(input("¿Que tipo de top usarías? \n 1)Dress \n 2)Nature Prints \n 3)Lace \n 4)Blusa con botones \n"))
        if top_inv_v1 ==1:
            bottom_inv_down = 0
            tops_values = 0
            accs_inv= int(input("¿Que tipo de accesorio usarías? \n 1)Puffy Sleeves \n 2)Lentes de sol \n 3)Basket \n 4)Collar Y2k \n 5)Sombrero \n 6)Corona de flores \n"))
            yes_no= int(input("¿Escoge otro accesorio? \n 1)si \n 2)No \n"))
            while yes_no ==1:
                accs_inv= int(input("¿Que tipo de accesorio usarías? \n 1)Puffy Sleeves \n 2)Lentes de sol \n 3)Basket \n 4)Collar Y2k \n 5)Sombrero \n 6)Corona de flores \n"))
                yes_no= int(input("¿Escoge otro accesorio? \n 1)Si \n 2)No \n"))
        elif top_inv_v1 == 3 or top_inv_v1 ==4:
            bottom_inv_down= int(input("¿Que tipo de bottom usarías? \n 1)pantalones \n 2)falda \n"))
            tops_values = 60
        elif top_inv_v1 == 2:
            bottom_inv_down= int(input("¿Que tipo de bottom usarías? \n 1)pantalones \n 2)falda \n"))
            tops_values = 30
        else:
            print("Not available, sorry :(")
        if bottom_inv_down in (1,2):
            accs_inv= int(input("¿Que tipo de accesorio usarías? \n 1)Puffy Sleeves \n 2)Lentes de sol \n 3)Basket \n 4)Collar Y2k \n 5)Sombrero \n 6)Corona de flores \n"))
            yes_no= int(input("¿Escoge otro accesorio? \n 1)si \n 2)No \n"))
            while yes_no ==1:
                accs_inv= int(input("¿Que tipo de accesorio usarías? \n 1)Puffy Sleeves \n 2)Lentes de sol \n 3)Basket \n 4)Collar Y2k \n 5)Sombrero \n 6)Corona de flores \n"))
                yes_no= int(input("¿Escoge otro accesorio? \n 1)Si \n 2)No \n"))
        if accs_inv in (1,2,4):
            ext_inv=int(input("¿Que tipo de prenda de extererior usarías? \n 1)Chamarra \n 2)Chaleco \n 3)Sudadera \n 4)Ninguna \n"))
            accs_values = 0
        elif accs_inv in (3,6,5):
            ext_inv=int(input("¿Que tipo de prenda de extererior usarías? \n 1)Chamarra \n 2)Chaleco \n 3)Sudadera \n 4)Ninguna \n"))
            accs_values = 10
        else:
            print("Not available, sorry :(")
        if ext_inv in (1,2,4):
            ext_values = 20
        elif ext_inv == 4:
            ext_values = 0
          
        if top_inv_v1 ==1:
            top_inv_v1 = 'Dress'
        elif top_inv_v1 ==2:
            top_inv_v1 = 'Nature Prints'
        elif top_inv_v1 == 3:
            top_inv_v1 = 'Lace'
        elif top_inv_v1 == 4:
            top_inv_v1 = 'Blusa con botones'
            
        if accs_inv ==1:
            accs_inv = 'Puffy Sleeves'
        elif accs_inv ==2:
            accs_inv = 'Lentes de Sol'
        elif accs_inv == 3:
            accs_inv = 'Basket'
        elif accs_inv == 4:
            accs_inv = 'Collar Y2k'
        elif accs_inv == 5:
            accs_inv = 'Sombrero'
        elif accs_inv == 6:
            accs_inv = 'Corona de flores'
            
        if ext_inv ==1:
            ext_inv = 'Chamarra'
        elif ext_inv ==2:
            ext_inv = 'Chaleco'
        elif ext_inv == 3:
            ext_inv = 'Sudadera'
        elif ext_inv == 4:
            ext_inv = 'None'
        if bottom_inv_down == 0:
            bottom_inv_down = 'None'
            
        if bottom_inv_down == 1 or bottom_inv_down == 2:
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
       
        if bottom_inv_down == 1 or bottom_inv_down == 2:
            ipo[1].insert(1, top_inv_v1)
            ipo[3].insert(1, accs_inv)
            ipo[2].insert(1, bottom_inv_down)
            ipo[4].insert(1, ext_inv)
        else:
            ipo[1].insert(1, top_inv_v1)
            ipo[3].insert(1, accs_inv)
            ipo[2].insert(1, "none")
            ipo[4].insert(1, ext_inv)




result=[]
ipo = ["Organizacion por categoria", ["Tops: "], ["Bottoms: "], ["Accesorios: "], ["Exterior: "]]


ask=int(input("Que tipo de estacion te gustaria para realizar tu aesthetic.\n 1)invierno \n 2)verano \n"))
if ask == 1:
    winter_1=int(input("Has escogido invierno. Cual de las siguientes dos opciones escogerias \n 1)winter_fairy_coquete \n 2)winter_academia \n"))
    spring =0
elif ask ==2:
    winter_1 = 0
    spring=int(input("Has escogido verano. Cual de las siguientes dos opciones escogerias \n 1)Nature_core \n 2)Warmcore \n"))

seasons_winter()

season_winter_2()

season_verano_1()

season_verano_2()

print("Tus resultados escogidos fueron los siguientes:", result)
print("Tus resultados, separados por categoria son:")
print(ipo)


