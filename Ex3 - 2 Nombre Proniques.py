
while True:
	n = int(input(""))
	if n >= 0:
		break
i = 0
while i < n:
	p = i * (i + 1)
	i = i + 1
	print(p)
