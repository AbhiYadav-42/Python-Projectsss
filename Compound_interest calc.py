principle = 0
rate = 0
time = 0

while principle <= 0:
 principle =int(input("enter the principle amount: "))
 if  principle <= 0:
    print("principle can't be less than or equa; to zero")

while rate <= 0:
 rate =int(input("enter the rate amount: "))
 if  rate <= 0:
    print(" can't be   less than or equal to zero")


while time <= 0:
 time =int(input("enter the time amount: "))
 if  time <= 0:
    print("tiem can't be less than or equa; to zero")


total = principle * pow((1 + rate / 100), time) 
print(f" Balance after{time} year/s: ${total:.2f}")



# we can use while true which mean it will run forever u need to 
# break it to stop the loop 