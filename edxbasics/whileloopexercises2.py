last_int = 0
counter = 0
while counter <= 100:

    if (counter % 2 == 1):
        last_int = last_int + counter * (counter+1)
    else:
        last_int = last_int - counter * (counter+1)
    counter = counter+1
print(last_int)