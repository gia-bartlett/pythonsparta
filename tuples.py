# TUPLES:

dob = ("name", "dob", "passport number")
print(dob) # ('name', 'dob', 'passport number')

print(dob[0:2]) # ('name', 'dob')


# convert tuple into a list
dob_list = list(dob)
print(type(dob_list))
# add name to lsit a 0 index
dob_list.insert(0, "Georgina")
# display list
print(dob_list)
