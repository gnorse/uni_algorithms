while True:
	n = int(input("enter n"))
	if n > 0:
			break
while True:
	r = int(input("enter r"))
	if r > 0:
			break
while True:
	x = int(input("enter x"))
	if x > 0:
			break
s = 0
p = 1
i = 1
p2 = 1

while i <= n:
	i2 = 1
	while i2 < int((n - i + 1)):
		p2 = p2 * x
	p = p * r
	s = s + int(p/p2)
	i = i + 1
print(s)
