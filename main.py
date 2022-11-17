import future
import itertools

list(itertools.product("01", repeat=5))
listone = (list(itertools.product("01", repeat=5)))

print("Total permutations of 0 and 1 length 5:", len(listone))

# formatting only convert to string and strip unwanted characters
listtwo = str(listone)
i= 1
while i == 1:
    for character in listtwo:
        listtwo = listtwo.replace(',','')
        listtwo = listtwo.replace(' ','')
        listtwo = listtwo.replace('(','')
        listtwo = listtwo.replace("]", "")
        listtwo = listtwo.replace('[','')
        listtwo = listtwo.replace(']',',')
        listtwo = listtwo.replace('"','')
        listtwo = listtwo.replace("'",'')
    i-=1

# separate permutations with comma
while i == 0:
    for character in listtwo:
        listtwo = listtwo.replace(")", ", ")
    listtwo = listtwo[:-1]
    i-=1
print("\nAs a String:")
print(listtwo)


# function converts to list for storage or comparisons
def toList(string):
    newlist = list(string.split(", "))
    # print("Total Permutaions:", len(newlist))
    return newlist

print("\nAs a List:")
print(toList(listtwo))

listPerms = ['00000', '00001', '00010', '00011', '00100', '00101', '00110', '00111', '01000', '01001', '01010', '01011', '01100', '01101', '01110', '01111', '10000', '10001', '10010', '10011', '10100', '10101', '10110', '10111', '11000', '11001', '11010', '11011', '11100', '11101', '11110', '11111']

print("\nAll Combinations starting with 0:")
for i in listPerms:
    if i[0]=="0":
        print(i)


print("\nthe following does not contain any two consecutive 00 or 11:")
substr1 = "00"
substr2= "11"


for i in listPerms:
    if (substr2 not in i) and (substr1 not in i):
        print(i)