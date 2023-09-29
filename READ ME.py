result=[]

seasons=int(input("Que tipo de estación te gustaría para realizar tu aesthethic. \n 1)invierno. \n 2)verano. \n 3)primavera \n 4)otoño\n"))

if seasons == 1:
    winter_v1=int(input("Has escogido invierno. Cual de las siguientes dos opciones escogerias \n 1)winter_fairy_coquete \n 2)winter_academia \n"))
else:
    print("No existe perdón :(")
    
  
if winter_v1 ==1:
    top_inv_v1=int(input("¿Que tipo de top usarías? \n 1)Mini Dress \n 2)Cuello de tortuga \n 3)Crop Top \n 4)Camiseta \n"))
else:
    print("No existe perdon :(")
if top_inv_v1 ==1:
    bottom_inv_down = "DNE"
    
if top_inv_v1 == 1:
    accs_inv= int(input("¿Que tipo de accesorio usarías? \n 1)Corset \n 2)Orejeras \n 3)Calentadores de brazo \n 4)Calentadores de pierna \n 5)Pulseras de perlas \n 6)Medias \n"))
    yes_no= int(input("¿Escoge otro accesorio? \n 1)si \n 2)una vez más \n"))
    while yes_no ==1:
        accs_inv= int(input("¿Que tipo de accesorio usarías? \n 1)Corset \n 2)Orejeras \n 3)Calentadores de brazo \n 4)Calentadores de pierna \n 5)Pulseras de perlas \n 6)Medias \n"))
        yes_no= int(input("¿Escoge otro accesorio? \n 1)si \n 2)una vez más \n"))
    accs_inv= int(input("¿Que tipo de accesorio usarías? \n 1)Corset \n 2)Orejeras \n 3)Calentadores de brazo \n 4)Calentadores de pierna \n 5)Pulseras de perlas \n 6)Medias \n"))

        
elif top_inv_v1 == 2 or top_inv_v1 ==4:
        bottom_inv_down= int(input("¿Que tipo de bottom usarías? \n 1)pantalones \n 2)falda \n"))
        
    
elif top_inv_v1 == 3:
        bottom_inv_down= int(input("¿Que tipo de bottom usarías? \n 1)pantalones \n 2)falda \n"))

else:
    print("Not available, sorry :(")
    
if top_inv_v1 in (2,4,3):
    accs_inv= int(input("¿Que tipo de accesorio usarías? \n 1)Corset \n 2)Orejeras \n 3)Calentadores de brazo \n 4)Calentadores de pierna \n 5)Pulseras de perlas \n 6)Medias \n"))
    yes_no= int(input("¿Escoge otro accesorio? \n 1)si \n 2)una vez más \n"))
    while yes_no ==1:
        accs_inv= int(input("¿Que tipo de accesorio usarías? \n 1)Corset \n 2)Orejeras \n 3)Calentadores de brazo \n 4)Calentadores de pierna \n 5)Pulseras de perlas \n 6)Medias \n"))
        yes_no= int(input("¿Escoge otro accesorio? \n 1)si \n 2)una vez más \n"))
    accs_inv= int(input("¿Que tipo de accesorio usarías? \n 1)Corset \n 2)Orejeras \n 3)Calentadores de brazo \n 4)Calentadores de pierna \n 5)Pulseras de perlas \n 6)Medias \n"))

if accs_inv in (1,5):
    ext_inv=int(input("¿Que tipo de prenda de extererior usarías? \n 1)Abrigo de piel \n 2)Cardigan \n 3)Chaqueta de lana \n 4)Parka \n"))

    
elif accs_inv in (2,3,4,6):
    ext_inv=int(input("¿Que tipo de prenda de extererior usarías? \n 1)Abrigo de piel \n 2)Cardigan \n 3)Chaqueta de lana \n 4)Parka \n"))
    
else:
    print("Not available, sorry :(")
    
if bottom_inv_down == 1 or bottom_inv_down == 2:
    result.append(top_inv_v1)
    result.append(accs_inv)
    result.append(bottom_inv_down)
    result.append(ext_inv)
else:
    result.append(top_inv_v1)
    result.append(accs_inv)
    result.append(ext_inv)
 
print(result)   

    
    
