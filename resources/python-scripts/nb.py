nombres = []
while True:
        answer = raw_input('data point?')
	if answer == '':
                break
	nombres.append(float(answer))

sum, sumsq = 0.0, 0.0
for x in nombres:
	sum = sum + x
	sumsq = sum + x*x

print(sum/len(nombres))
print(sumqq/len(nombres))

