import random
number = 0
for _ in range(0,10):
	number += random.randint(1,10)
number = int(number/9)
print(f"Tu numero magico es: {number}")