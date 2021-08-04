# convert integer to string
# the least significant digit is x%10
# the rest of the digits is x//10
# edge case int is 0
def to_str(num):
    if num == 0:
        return '0' 
    if num < 0:
        neg = "-"
    else:
        neg = ""
    num = abs(num)
    result = []
    while num != 0:
        result.append(chr(ord('0')+ num%10))
        num = num//10
    result.append(neg)
    return "".join(result[::-1])
x = [123, 0, -231, 45, -100, -98734]
for num in x:
    print(to_str(num))

    