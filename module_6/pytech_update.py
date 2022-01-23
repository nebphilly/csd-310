""" import statements """
from pymongo import MongoClient

# MongoDB connection string
#url = "mongodb+srv://admin:admin@cluster0.rsnru.mongodb.net/pytech?retryWrites=true&w=majority"
url = "mongodb+srv://admin:admin@cluster0.qu1hy.mongodb.net/pytech?retryWrites=true&w=majority"

# connect to the MongoDB cluster
client = MongoClient(url)

# connect pytech database
db = client.pytech

# get the students collection
students = db.students

# find all students in the collection
student_list = students.find({})

# display message
print("\n  -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

# loop over the collection and output the results
for doc in student_list:
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " +
          doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")

# update student_id 1007
result = students.update_one({"student_id": "1007"},
                             {"$set": {
                                 "last_name": "Phillips Jr."
                             }})

# find the updated student document
ben = students.find_one({"student_id": "1007"})

# display message
print("\n  -- DISPLAYING STUDENT DOCUMENT 1007 --")

# output the updated document to the terminal window
print("  Student ID: " + ben["student_id"] + "\n  First Name: " +
      ben["first_name"] + "\n  Last Name: " + ben["last_name"] + "\n")

# exit message
input("\n\n  End of program, press any key to continue...")
'''
References
Krasso, R. (2020, July 27). CSD 310 Database Development and Use. Retrieved from GitHub:
    https://github.com/buwebdev/csd-310
'''