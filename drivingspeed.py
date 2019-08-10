# Write a function for checking the speed of drivers. This function should have one parameter: speed.

#     If speed is less than 70, it should print “Ok”.
#     Otherwise, for every 5km above the speed limit (70), it should give the driver one demerit point and print the total number of demerit points. For example, if the speed is 80, it should print: “Points: 2”.
#     If the driver gets more than 12 points, the function should print: “License suspended”

speed = int(input('input driving speed: '))
demerit = 0

if speed >= 70:
    divide = int(speed - 70) // 5
    demerit = divide

remarks = ''
if demerit == 0:
    remarks = 'Ok'
elif demerit > 12:
    remarks = 'License suspended'
else:
    remarks = 'Demerit points: ' + str(demerit)

print(remarks)