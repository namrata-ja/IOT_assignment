num = int(input("Enter four digit number: "))

d4 = num % 10
num = num // 10

d3 = num % 10
num = num // 10

d2 = num % 10
num = num // 10

d1 = num

print(f"\na. Face values: {d1} {d2} {d3} {d4}")

print(f"\nb. Place values: {d1*1000} + {d2*100} + {d3*10} + {d4}")

reverse = d4*1000 + d3*100 + d2*10 + d1
print(f"\nc. Reversed number: {reverse}")
