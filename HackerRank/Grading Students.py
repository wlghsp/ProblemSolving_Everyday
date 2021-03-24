

def gradingStudents(grades):
    # Write your code here
    result = []
    for i in grades:
        fiveMultiple = ((i//5)+1) * 5
        if i < 38:
            result.append(i)
        elif (fiveMultiple - i) < 3:
            result.append(fiveMultiple)
        elif (fiveMultiple - i) >= 3:
            result.append(i)

    return result


a = [73, 67, 38, 33]
print(gradingStudents(a))
