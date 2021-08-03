import math

def pow_to_db(x):
    return str(10 * math.log(x, 10)) + " dB"

def db_to_pow(x):
    return str(math.pow(10, x/10)) + " W"

def volt_to_db(x):
    return str(20 * math.log(x, 10)) + " dB"

def db_to_volt(x):
    return str(math.pow(10, x/20)) + " V"

switcher = {
    0: pow_to_db,
    1: db_to_pow,
    2: volt_to_db,
    3: db_to_volt,
    }

print("Select conversion")
print("1 - power to dB")
print("2 - dB to power")
print("3 - volt to dB")
print("4 - dB to volt")
print(" ")

while(True):
    opt = float(input("Enter option: "))
    x = float(input("Argument: "))
    print(switcher[opt-1](x))
    print(" ")

