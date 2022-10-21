frutas = ["mango", "manzana", "fresa","mango"]
verduras = ["brocoli", "espinaca", "pepino"]

print (frutas)
print (verduras)

#borrar una item del arreglo
frutas.remove("mango")
print(frutas)

#borrar se gun la pocicion 
frutas.pop(2)
print(frutas)

# agregar una un nueva fruta al final de la lista
frutas.append("uva")
print(frutas)
##dar pocicion a el items
frutas.insert(1,"uva")
print(frutas)

##para saber el indice o pocicio en la lista
fr= frutas.index("fresa")
print(fr)

#cantidad de elemento que tenga el arreglo
print(len(frutas))

#Diferencia entre listas y duplas es que las duplas son inmutables, y van en paretecis 
# lista = A=[]
# dupla = A=() --- Inmutable
# set = A={} --- No permite valores repetidos  ---