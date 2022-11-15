from cs50 import get_float

# Get change
while True:
    dolar = get_float("Amount of Change: ")
    if dolar > 0:
        break
dolar = round(dolar * 100)

# Declare variables
count = 0


# while dolar


while dolar > 0:
    if dolar >= 25:
        dolar = dolar - 25
        count = count + 1
    elif dolar >= 10:
        dolar = dolar - 10
        count = count + 1
    elif dolar >= 5:
        dolar = dolar - 5
        count = count + 1
    elif dolar >= 1:
        dolar = dolar - 1
        count = count + 1
# print
print(count)
