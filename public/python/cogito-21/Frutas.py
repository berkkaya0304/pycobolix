fruits = []
MAX_FRUITS = 10

while len(fruits) < MAX_FRUITS:
    fruit = input("Teclea el nombre de una fruta: ").strip()
    fruits.append(fruit)
    
    if len(fruits) >= MAX_FRUITS:
        print("La tabla está llena.")
        break
        
    while True:
        response = input("Deseas continuar? (S/N): ").strip().upper()
        if response in ['S', 'N']:
            break
        print("Por favor, responde S o N.")
    
    if response == 'N':
        break

if len(fruits) < MAX_FRUITS:
    print("Aún quedan elementos por rellenar.")
