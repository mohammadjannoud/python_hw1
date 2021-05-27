graduate_students=['mohammad','ahmad','ali','sami','reem','khaled']
student = input("Please enter your name: ")
for s in graduate_students:
    if s==student:
        print("you Are Graduate")
        break
else:
    print("you Are Not Graduate")
