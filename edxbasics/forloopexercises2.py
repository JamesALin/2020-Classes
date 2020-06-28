last_int = 0
for counter in range(1, 101):
    if(counter % 2 == 1):
        last_int = last_int + counter*(counter+1)
    else:
        last_int = last_int - counter*(counter+1)
print(last_int)