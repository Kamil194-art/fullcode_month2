
# def add(name):
#     file = open('user.txt',"a",encoding="utf-8")
#     file.write(name+"\n")
#     file.close()
# add("islam")
#
# def delete_1(name):
#     file = open('user.txt',"r",encoding="utf-8")
#     lines = file.readlines()
#     for i in lines:
#         if i.strip("\n") == name:
#             lines.remove(i)
#     f = open('user.txt',"w",encoding="utf-8")
#     f.writelines(lines)
#     f.close()
#     file.close()
# delete_1("kama")
#
# def  reading():
#     file = open('user.txt',"r",encoding="utf-8")
#     lines = file.read()
#     print(lines)
#     file.close()
# readi
#
# def update(name,update_name):
#     file = open('user.txt',"r",encoding="utf-8")
#     lines = file.readlines()
#     f = open('user.txt',"w",encoding="utf-8")
#     for line in lines:
#         if name == line.strip("\n"):
#             f.write(update_name+"\n")
#         else:
#             f.write(name+"\n")
#     f.close()
#     file.close()
#
# # delete_1("dastan")
# # add("kelsinai")
# # reading()
# update("islam","kanimet")

# import random
#
# def random_number(n):
#     b = []
#     for i in range(n):
#         b.append(random.randint(1,10))
#     return b
# print(random_number(9))