f = open("a.txt", "w")
# V = []
cnt = 0
freq = 0.5
freqTIM = 1000
maxDAC = 2**12 - 1
Volt_start = int(700 * maxDAC / 3000)
Volt_stop = int(2700 * maxDAC / 3000)
steps = int(freqTIM/0.5)
dV = (Volt_stop - Volt_start) / (steps-1)
for i in range(steps):
    data = int(Volt_start + i * dV)
    # V.append(data)
    f.write(str(data) + ', ')
    cnt+=1

f.close()
print(cnt)

print(steps)
print(Volt_start,"--",  Volt_stop)
# print(V)