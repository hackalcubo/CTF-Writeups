import string

with open('message.txt') as file:
    message = file.read()
    flag = ''.join(filter(lambda x: x in string.printable, message))
    punct_set = ('.',',',' ','!','?')
    flag = ''.join(filter(lambda x: x not in punct_set, flag))
    print(flag)