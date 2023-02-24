#List
mon_temp = {8.7, 2.5, 3.6}
#dictionary
student_grades = {"marry": 0.3, "tom": 0.5}

mysum = sum(student_grades.values())
length = len(student_grades)
mean = mysum/length
print(mean)

#tuples
tues_temp = (1,4,5)
print(tues_temp)

data = {"a":[1,2,3],"b":[4,5,6],"c":[7,8,9]}

def mean(value):
    if type(value) == dict:
        the_mean = sum(value.values()) / len(value)
    else:
        the_mean = sum(value) / len(value)
        
    return the_mean

print(mean([1,2,3,4]))

def sentence_maker(sentece):
    capitalized = sentece.capitalize()
    interrogatives = ("how", "why", "what")
    if sentece.startswith(interrogatives):
        return "{}?".format(capitalized)
    else:
        return "{}.".format(capitalized)

sentence_list = []

while True:
    message = input("Say something: ")
    if message == "\end":
        break
    else:
        sentence_list.append(sentence_maker(message))

print(" ".join(sentence_list))
    