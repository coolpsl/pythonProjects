students = [
['Joey', 'A', 15],
['Monica', 'B', 10],
['Ross', 'C', 8],
['Rachel', 'B', 12]
]
student_sort_1 = sorted(students)
student_sort = sorted(students, key = lambda student : student[2])

print(student_sort_1)
#output:[[['Joey', 'A', 15], ['Monica', 'B', 10], ['Rachel', 'B', 12], ['Ross', 'C', 8]]
print(student_sort)
#output:[['Ross', 'C', 8], ['Monica', 'B', 10], ['Rachel', 'B', 12], ['Joey', 'A', 15]]
