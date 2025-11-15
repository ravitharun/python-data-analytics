student = {
    "name": "Tharun",
    "age": 21,
    "course": "CSE"

}
# to axcess
print(student['name'])
# add the item 
student['inofAdd']='andhrapradesh'
print(student)

# to update 
student["name"]='ravi tharun kumar'
print(student)
# it gives the keys
print(student.keys())

# it gives the values
print(student.values())
# Returns key + value pairs as tuples.
print(student.items())

# it gives the vaule of the key
print(student.get("name"))


# it updated the data or add the data
student.update({"course": "CSE", "city": "Bangalore",'age':23})
print(student)

# pop it rmv the required key
student.pop("age")
print(student)

# it clear the all data to empyt
student.clear()
print(student)