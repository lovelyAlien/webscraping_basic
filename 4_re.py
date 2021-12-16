import re

p=re.compile("ca.e")



def print_match(m):
    if m:
        print("m.group(): ", m.group())
        print("m.string(): ", m.string)
        print("m.start(): ", m.start())
        print("m.end(): ", m.end())
        print("m.span(): ", m.span())
    else:
        print("Not matching")

# m=p.match("careless")
# m=p.search("good care cafe")
# print_match(m)

lst=p.findall("care cafe cade") # findall: 일치하는 모든 것을 리스트로 반환

print(lst)

