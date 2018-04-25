emoji = "\U0001f600"


for x in range(1, 11):
    print(emoji * x)

times = 1
while times < 11:
    print(emoji * times)
    times += 1

for num in range(1, 11):
    count = 1
    smileys = ''
    while count <= num:
        smileys += emoji
        count += 1
    print(smileys)
