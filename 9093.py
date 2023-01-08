num_sen = int(input())

for i in range(num_sen):
	sentence = list(input())
	save = []
	for j in sentence:
		if j != " ":
			save.append(j)
		else:
			save.reverse()
			for k in save:
				print(k, end="")
			print(" ", end="")
			save = []
	save.reverse()
	for k in save:
		print(k, end="")
	print()