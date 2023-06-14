p = int(input("input money"))
days = int(p/50)
if p <= 3000:
	days = days + int(p/500)
else:
	days = days + 6
if p == 7500:
        days = days + 30
print(days)
