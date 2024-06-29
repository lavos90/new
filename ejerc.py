cursos_min=2.5
cursos_max=7
cursos_promedio=4
dalto_curso=1.5

#duracion de crudo
crudoPromedio=5
crudoDalto=3.5

diferencia_con_min=100-dalto_curso/cursos_min*100
diferencia_con_max=100-dalto_curso//cursos_max*100 #otro eje:sust(1000=10000 y (10=100) result78.58
if diferencia_con_max>90:
  diferencia_con_max=100-dalto_curso*10000//cursos_max/100
diferencia_con_promedio=100-dalto_curso/cursos_promedio*100

tiempoVacioPromedio=100-cursos_promedio*1000//crudoPromedio/10
tiempoVacioDalto=100-dalto_curso*1000//crudoDalto/10

print('el curso de dalto dura un ..')
print(f'.. {diferencia_con_min} % menos ke el mas rapido')
print(f'.. {diferencia_con_max} % menos ke el mas lento')
print(f'.. {diferencia_con_promedio} % menos ke el mas promedio')
#print(dir(100))
print('_________________________')

print(f'un curso promedio elimina un {tiempoVacioPromedio} % de tiempo vacio')
print(f'este curso elimino el {tiempoVacioDalto} % de tiempo vacio')
print('_________________________')

print('ver 10 hora de.. ')
print(f'.. este curso ekivale a ver {cursos_promedio*100//dalto_curso/10} horas de otros cursos')
print(f'.. otros curso ekivale a ver {dalto_curso*100//cursos_promedio/10} horas de este curso')

#ejercicio 2 velocidad palabras dalto-------------------------------------------------
frase=input('dame una frase y te calculo el tiempo en decirla: ')
# palabrasSeparadas=frase.split(' ')
# cantidadDePalabras=len(palabrasSeparadas)
# print(palabrasSeparadas)
# cantidadDePalabras=len(frase)
cantidadDePalabras=frase.count(' ')
        
if cantidadDePalabras>30:
    print('mano no t pedi un libro ')
    
print(f'dijiste {cantidadDePalabras} palabras y tardarias {cantidadDePalabras/2} segundos en decirlo')
print(f'dalto lo diria en {cantidadDePalabras*100//2*1.3/100} segundos')
