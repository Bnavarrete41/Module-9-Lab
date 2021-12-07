# Brandon Navarrete

# 11/27/2021
# This loop will keep adding the users number till it reaches 100 where it will end

L = []

while sum(L) < 100:
    n = int(input('Please Choose a number:'))
    L.append(n)
print(L)
'''
No use of the following codes 
counter = 0 
tens = []
while counter <= 50:
    if counter % 10 == 0:
        tens.append(counter)
    counter = counter + 1

print(tens)
'''
