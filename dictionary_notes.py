student1 = {
    "name": "John", 
    "birthdate": "January 1, 2010", 
    "grade": 9 
    }
    
    print(student1)
    print(student1["name"])
    if student1["name"] == "Mrs. Adams":
        print("We have the same name!")
    else:
        print("Hi, " + student1["name"])
        
#change value of their grade
student1["grade"] = 10
print(student1)

#add a key:value pair to the dictionary
student1["favorite color"] = "green"
print(student1)