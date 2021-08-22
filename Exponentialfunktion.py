print(2**4)     #Eine Möglichkeit 2 hoch 4 zu rechnen

def raise_to_power(base_num, power_num):
    loop = 1
    num = base_num
    while loop < power_num:
        num = num * base_num
        loop += 1
    return num

print(str(raise_to_power(float(input("Bitte Basiswert eingeben.:")), float(input("… hoch ")))))

def raise_to_power(base_num, power_num):
    result = 1
    for index in range(power_num):
        result = result * base_num
    return result

print(str(raise_to_power(float(input("Bitte Basiswert eingeben.:")), int(input("… hoch ")))))
