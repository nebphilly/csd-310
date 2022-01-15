""" 
    Title: pytech_insert.py
    Author: Professor Krasso
    Date: 10 July 2020
    Description: Test program for inserting new documents 
                 into the students collection 
"""
""" import statements """
from pymongo import MongoClient

# MongoDB connection string
#url = "mongodb+srv://admin:admin@cluster0.rsnru.mongodb.net/pytech?retryWrites=true&w=majority"
url = "mongodb+srv://admin:admin@cluster0.qu1hy.mongodb.net/pytech?retryWrites=true&w=majority"

# connect to the MongoDB cluster
client = MongoClient(url)

# connect pytech database
db = client.pytech
""" three student documents"""
# Ben's data document
ben = {
    "student_id":
    "1007",
    "first_name":
    "Ben",
    "last_name":
    "Phillips",
    "enrollments": [{
        "term":
        "Spring",
        "gpa":
        "3.5",
        "start_date":
        "January 1, 2021",
        "end_date":
        "June 1, 2021",
        "courses": [{
            "course_id": "100",
            "description": "History",
            "instructor": "Mr. Smith",
            "grade": "92%"
        }, {
            "course_id": "101",
            "description": "Science",
            "instructor": "Mr. Douglas",
            "grade": "93%"
        }]
    }]
}

# Mac's data document
mac = {
    "student_id":
    "1008",
    "first_name":
    "Mac",
    "last_name":
    "Phillips",
    "enrollments": [{
        "term":
        "Summer",
        "gpa":
        "3.9",
        "start_date":
        "June 15, 2021",
        "end_date":
        "August 20, 2021",
        "courses": [{
            "course_id": "102",
            "description": "Programming",
            "instructor": "Mrs. Reese",
            "grade": "90%"
        }, {
            "course_id": "103",
            "description": "Calculus",
            "instructor": "Mrs. Johnson",
            "grade": "89%"
        }]
    }]
}

# Jay's data document
jay = {
    "student_id":
    "1009",
    "first_name":
    "Jay",
    "last_name":
    "Phillips",
    "enrollments": [{
        "term":
        "fall",
        "gpa":
        "2.9",
        "start_date":
        "September 1, 2021",
        "end_date":
        "December 20, 2021",
        "courses": [{
            "course_id": "104",
            "description": "Physics",
            "instructor": "Mr. Brown",
            "grade": "86%"
        }, {
            "course_id": "105",
            "description": "Health",
            "instructor": "Mrs. Nightingale",
            "grade": "87%"
        }]
    }]
}

# get the students collection
students = db.students

# insert statements with output
print("\n  -- INSERT STATEMENTS --")
ben_student_id = students.insert_one(ben).inserted_id
print(
    "  Inserted student record Ben Phillips into the students collection with document_id "
    + str(ben_student_id))

mac_student_id = students.insert_one(mac).inserted_id
print(
    "  Inserted student record Mac Phillips into the students collection with document_id "
    + str(mac_student_id))

jay_student_id = students.insert_one(jay).inserted_id
print(
    "  Inserted student record Jay Phillips into the students collection with document_id "
    + str(jay_student_id))

input("\n\n  End of program, press any key to exit... ")
'''
References
Krasso, R. (2020, July 27). CSD 310 Database Development and Use. Retrieved from GitHub:
    https://github.com/buwebdev/csd-310
'''