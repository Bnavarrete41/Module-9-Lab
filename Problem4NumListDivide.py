# Brandon Navarrete
# 11/30/21
# This will keep printing a number until it reaches 50 and will print a list if they are divisible by ten.

count = 0
tens = []
while count < 51:
    # count +=1
    if count % 10 == 0:
        tens.append(count)
    count += 1
print("Tens: ", tens)