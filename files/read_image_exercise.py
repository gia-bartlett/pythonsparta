
# with open("baby.jpg", "r") as rf:
#     with open("baby_copy.jpg", "w") as wf:
#         for line in rf:
#             wf.write(line)
# trying to run this like a txt file will throw an error we need to decode bytes instead of lines

with open("baby.jpg", "rb") as rf:
    with open("baby_copy.jpg", "wb") as wf:
        for line in rf:
            wf.write(line)
# by appending a b to the read and write we are able to convert the input into bytes
