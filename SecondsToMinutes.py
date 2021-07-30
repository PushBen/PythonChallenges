#TODO
#Clean up Code, potentially put timeType into function
#Add '1 Minute' 2 'Minute's'' into code

def timeConversion(time, conversionType):
	if conversionType:
		return time * 60

	else:
		return round(time / 60, 2)		

print("Minute to Second Convertor")
print("If you would like to convert 'minutes to seconds' press 1")
print("If you would like to convert 'seconds to minutes' press 2")


timeType = input("> ")

timeInput = input("How much time?: ")
	
if timeType == "1":
	time = timeConversion(int(timeInput), True)
	print(str(timeInput) + " minutes is " + str(time) + " seconds")
elif timeType == "2":
	time = timeConversion(int(timeInput), False)
	print(str(timeInput) + " seconds is " + str(time) + " minutes")
else:
	print("Error, please select 1 or 2")







