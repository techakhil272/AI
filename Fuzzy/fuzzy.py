name = ["varun", "Salvin", "Ankit", "Shruti", "Sejal",
        "Yojit", "Daniel", "Valencia", "apporv", "roniyo"]
cgpa = [0.9, 0.8, 0.97, 0.75, 0.6, 0.4, 0.2, 1.0, 0.0, 0.35]
hsc = [0.87, 0.75, 0.63, 0.19, 0.9, 0.4, 0.97, 0.1, 1.0, 0.0]
ssc = [0.54, 0.79, 0.68, 0.54, 0.78, 0.32, 0.91, 0.65, 0.20, 0.83]
# def take_input():
#     for i in range(0,3):
#         print(i)
#         print("Name:")
#         name_input=input()
#         name.append(name_input)
#         print("cgpa:")
#         cgpa_input=float(input())
#         cgpa.append(cgpa_input)
#         print("hsc:")
#         hsc_input=float(input())
#         hsc.append(hsc_input)
#         print("ssc:")
#         ssc_input=float(input())
#         ssc.append(ssc_input)


def intersection(value1, value2):
    intersection = []
    for i in range(0, 10):
        temp = min(value1[i], value2[i])
        intersection.append(temp)
    return intersection

def union(value1, value2):
    union = []
    for i in range(0, 10):
        temp = max(value1[i], value2[i])
        union.append(temp)
    return union


def compliment(value):
    compliment = []
    for i in range(0, 10):
        temp = 1-value[i]
        compliment.append(temp)
    return compliment


def alpha(result, alpha):
    index = []
    for i in range(0, 10):
        if (result[i] >= alpha):
            temp = i
            index.append(temp)
    return index


def print_name(name, index):
    for i in range(0, 10):
        if i in index:
            print(name[i])


# Q1
result = intersection(cgpa, hsc)
print("Intersection Result:Students Whose cgpa is 9.0 and HSC is 80%")
print(result)
index = alpha(result, 0.5)
print("Index of students qualified")
print_name(name, index)

# Q2
print("#Q2")
result2 = alpha(intersection(cgpa, compliment(ssc)),0.3)
print("Index of students qualified")
print_name(name,result2)

#Q3
print("#Q3")
print_name(name,alpha(intersection(cgpa,union(hsc,ssc)),0.6))