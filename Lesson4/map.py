numbers = [1,2,3,4,5,6]

squ = map(lambda x:x**2,numbers)

print(squ)
print(list(squ))
print(list(squ))

print()

def to_apper(s):
    return s.upper()
status = ["past","failed","skip"]
upper_status = list(map(to_apper,status))
print(upper_status)