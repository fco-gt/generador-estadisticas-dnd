import random
Cantidad = int

Razas = ["Humano" , "Enano" , "Elfo" , "Dragonborn" , "Gnome" , "Half-Elf" , 
         "Half-Orc" , "Halfling" , "Tiefling"]
Clases = ["Guerrero" , "Mago" , "Explorador" , "Barbaro" , "Artificiero" , 
          "Bardo" , "Clerigo" , "Druida" , "Monje" , "Paladin" , "Rogue" , 
          "Hechizero" , "Brujo"]
puntosbase = {
    "Humano":{ "STR": 1 , "DEX": 1 , "CON": 1 , "WIS": 1 , "INT": 1 , "CHA": 1},
    "Enano":{  "STR": 0 , "DEX": 0 , "CON": 2 , "WIS": 0 , "INT": 0 , "CHA": 0},
    "Elfo":{  "STR": 0 , "DEX": 2 , "CON": 0 , "WIS": 0 , "INT": 0 , "CHA": 0},
    "Dragonborn":{ "STR": 2 , "DEX": 0 , "CON": 0 , "WIS": 0 , "INT": 0 , "CHA": 1},
    "Gnome":{ "STR": 0 , "DEX": 0 , "CON": 0 , "WIS": 0 , "INT": 2 , "CHA": 0},
    "Half-Elf":{ "STR": 0 , "DEX": 1 , "CON": 0 , "WIS": 0 , "INT": 1 , "CHA": 2},
    "Half-Orc":{ "STR": 2 , "DEX": 0 , "CON": 1 , "WIS": 0 , "INT": 0 , "CHA": 0},
    "Halfling":{"STR": 0 , "DEX": 2 , "CON": 0 , "WIS": 0 , "INT": 0 , "CHA": 0},
    "Tiefling":{"STR": 0 , "DEX": 0 , "CON": 0 , "WIS": 0 , "INT": 0 , "CHA": 2}}

nraza = random.randint(0,len(Razas)-1)
nclase = random.randint(0,len(Clases)-1)

print("¿Cuantos personajes desea crear? \n indique cantidad: ")
Cantidad = int(input())
for i in range(Cantidad):
  nraza = random.randint(0,len(Razas)-1)
  nclase = random.randint(0,len(Clases)-1)
  
  print("Personaje:")
  print("Razas:" , Razas[nraza])
  print("Clases:" , Clases[nclase])
  estadisticas = ["STR" , "DEX" , "CON" , "WIS" , "INT" , "CHA"]
  for m in range(6):
    Resultados = []
    for x in range(4):
      Resultados.append(random.randint(1, 6))
    VM = 0
    total = 0
    for x in Resultados:
      if VM == 0 or x < VM:
        VM = x
      total = total + x
    total = total - VM + puntosbase[Razas[nraza]][estadisticas[m]]
    print(estadisticas[m],":",total)