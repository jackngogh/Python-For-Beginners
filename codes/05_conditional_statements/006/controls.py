print('Not printing if it is 5 multiplier')
for i in range(1, 11):
    if (i % 5) == 0:
        continue
    print(i)

print()
print('Not print if reach to 5')
for i in range(1, 21):
    if (i == 5):
        break
    print(i)

print()
print('using pass for placeholder')

for i in range(100):
    pass
