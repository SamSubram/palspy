import mysql.connector

con = mysql.connector.connect(
    user = "ardit700_student",
    password = "ardit700_student",
    host = "108.167.140.122",
    database = "ardit700_pm1database"
)

word = input("Please enter a word: ")
cursor = con.cursor()
query = cursor.execute("SELECT * FROM Dictionary WHERE Expression = '%s'" %word)
#query = cursor.execute("SELECT * FROM Dictionary WHERE Expression = 'Pal' ")
results = cursor.fetchall()
#print(results)

# Testing with the user entered input
if(results):
    for result in results:
        #print("Inside the for loop")
        print(result[1])
else:
    print("Word not found!")