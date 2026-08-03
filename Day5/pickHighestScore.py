student_score = [1,2,19,30,37]
print(student_score) #print each score
print(max(student_score))

#need to replicate max func outcome using loop, list, condition learning
max_score = 0
for score in student_score:
    if score > max_score:
        max_score = score

print(max_score)


