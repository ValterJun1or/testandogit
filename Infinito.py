power = 0
while True:
    print("Roxo", end=" / ")
    power += 1
    print(f"{power}%")
    if power == 100:
        print("Potencial máximo alcançado!!!")
        break
