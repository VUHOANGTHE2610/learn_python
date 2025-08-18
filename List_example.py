#Tương tác cơ bản
teams = ["barcelona", "Arsenal", "Manchester United", "Liverpool", "Chelsea"]
print(teams) #['barcelona', 'Arsenal', 'Manchester United']
print(teams[0]) #barcelona
print(teams[-1]) #Manchester United
print(teams[1:]) #['Arsenal', 'Manchester United', 'Liverpool', 'Chelsea']
print(teams[1:4]) #['Arsenal', 'Manchester United', 'Liverpool']
teams[1] = "Real Madrid"


#Các hàm thao tác với list
student_names = ["Vũ", "Nguyên", "Dũng"]
math_scores = [8, 10, 9]

#student_names.extend(math_scores)
print(student_names) #['Vũ', 'Nguyên', 'Dũng', 8, 10, 9]

student_names.append("Tris")
print(student_names) #['Vũ', 'Nguyên', 'Dũng', 'Tris']

student_names.insert(2, "Thomas")
print(student_names) #['Vũ', 'Nguyên', 'Thomas', 'Dũng', 'Tris']

student_names.remove("Thomas")
print(student_names) #['Vũ', 'Nguyên', 'Dũng', 'Tris']

student_names.pop()
print(student_names) #['Vũ', 'Nguyên', 'Dũng']

print(student_names.index("Vũ")) #0

print(student_names.count("Vũ")) #1

student_names.sort()
print(student_names) #['Dũng', 'Nguyên', 'Vũ']

student_names.reverse()
print(student_names) #['Vũ', 'Nguyên', 'Dũng']

student_names2 = student_names.copy()
print(student_names2) #['Vũ', 'Nguyên', 'Dũng']

student_names.clear()
print(student_names) #[]