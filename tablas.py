puntaje = 0
num = int(input("ingrese numero: "))
for i in range(1,11):
  respuesta = int(input(f"{i}x{num}= "))
  if respuesta == i*num:
    print("correcto")
    puntaje += 1
  else:
    print("incorrecto")
print(f"tu puntaje fue {puntaje}/10")
if puntaje == 10:
    print("hiciste la mayor marca")