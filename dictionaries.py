# DICTIONARY:

# create a dictionary

student_record = {
    "name": "Georgina",
    "stream": "DevOps",
    "completed_lesson": 5,
    "completed_lessons": ["strings", "tuples", "variables"]

}

# print(student_record); # {'name': 'Georgina', 'stream': 'DevOps', 'completed_lesson': 5, 'completed_lessons': ['strings', 'tuples', 'variables']}
# print(type(student_record)); # <class 'dict'>
#
# print(sorted(student_record)); # ['completed_lesson', 'completed_lessons', 'name', 'stream']
#
# print(student_record.values()); # dict_values(['Georgina', 'DevOps', 5, ['strings', 'tuples', 'variables']])
# print(student_record.keys()) # dict_keys(['name', 'stream', 'completed_lesson', 'completed_lessons'])
#
# student_record["completed_lesson"] = 3
# new_list = student_record["completed_lesson"]
# print(new_list) # 3
#
# #add a topic
# student_record["completed_lessons"].append("python")
# # display list
# print(student_record) # added python to the lessons list
#
# print(student_record["name"]) # Georgina (fetch value of a stream)
# print(student_record["completed_lessons"][2]) # variables


