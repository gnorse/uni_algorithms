while True:
	n = int(input("enter n"))
	if n > 0:
			break
while True:
	r = int(input("enter r"))
	if r > 0:
			break
s = 0
p = 1
i = 1
while i <= n:
	p = p * r
	s = s + p
	i = i + 1
print(s)
