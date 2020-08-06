student_grades = [9.1, 8.8, 10.0, 7.7, 6.8, 8.0, 10.0, 8.1, 10.0, 9.9]
countOften = 0
for i in range(len(student_grades)):
    if(student_grades[i] == 10.0):
        print("Found 10.0 at index" + str(i))
        countOften = countOften+1
        print("Inside the If loop")


print("Number 10.0 occurs " + str(countOften) + " times in the list")
print(countOften)

tuplemor = (10.0, 20.0,30.0)
tuplenoo = (5.0, 6.0, 7.0)
tupleeve = (11.0, 22.0, 33.0)

day_temperatures ={"morning":tuplemor, "noon":tuplenoo, "evening":tupleeve}
print(day_temperatures)

