a = ["10", "abc", "25", "7x", "100"]
digit = []
for i in a:
    if i.isdigit():
        digit.append(int(i))

print("The digits: ",digit)
print("The sum of digits: ",sum(digit))

b = ["11", "mama", "m5", "121", "papa1"]
number = [int(i) for i in b if i.isdigit()]
print(number)
print(sum(number))


