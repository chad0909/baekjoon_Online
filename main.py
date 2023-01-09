num = int(input())
QuickClose = False

for _ in range(num):
	bracket = list(input())
	if bracket[0] == ")":
		print("NO")
	else:
		count = 0
		for i in bracket:
			if i == "(":
				count += 1
			else:
				count -= 1

			if count < 0:
				QuickClose = True
				break

		if count == 0:
			print("YES")
		else:
			print("NO")
		
