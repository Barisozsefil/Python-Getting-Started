#key - value 
#newPlakalar = {key : value}  "Tanımlama bu şekilde" 



# city = ["Kocalel", "İstanbul"]
# plakalar = [21 ,34]

# print (plakalar[city.index("Kocalel")]) 




# newPlakalar = {"Kocalei" : 41 , "İstanbul": 34}

# print(newPlakalar["İstanbul"])
# print(newPlakalar["Kocalei"])

# newPlakalar["Ankara"] = 56

# print(newPlakalar)

#-------------------------------------------------------------------------------------------------

students = {}

number = input("Öğrenci No: ")
name = input("İsminiz: ")
surname = input("Soyisminiz: ")
phone = input("Telefon Num: ")

# students [number] ={
#     "Name" : name ,
#     "Surname" : surname ,
#     "Phone" : phone
# }

students.update(
    {
    "number": {
    "Name" : name ,
    "Surname" : surname ,
    "Phone" : phone
}
    }
)
number = input("Öğrenci No: ")
name = input("İsminiz: ")
surname = input("Soyisminiz: ")
phone = input("Telefon Num: ")


students.update(
    {
    "number": {
    "Name" : name ,
    "Surname" : surname ,
    "Phone" : phone
}
    }
)

print(students)


ogrenciNo = input("Öğrenci No: ")
student = students[ogrenciNo]

print(student)




