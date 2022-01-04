'''
Given a sentence, reverse the words in the sentence.
 
Eg. 
Input:
This is it.
Output: 
it. is This
'''

# This is it.
# [This, is, it.]
#[it., is, This]
#     start
#     end
# it. is This
def reverse(s:str):
    arr = s.split(' ')
    start, end = 0, len(arr)-1
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

    return " ".join(arr)