list = [0, 1]

def Fibonacci(n):
    i = 1
    while n > list[i]:
        value = list[i] + list[i - 1]
        if value > n:
            break
        list.append(value)
        i += 1
    return list

input = int(input("Ingrese un número: "))

print("La lista Fibonacci es : ")

list = Fibonacci(input)
for l in list:
    print(l)