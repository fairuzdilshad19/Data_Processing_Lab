temperatures=(30,32,29,31,33,28)
count=0

for temperature in temperatures:
    if count<3:
        print("Saturday temperature:", temperature)
    else:
        print("Sunday temperature:", temperature)

    count=count+1

print("Highest temperature:",max(temperatures))
print("Lowest temperature:",min(temperatures))