list1 = ["4", "45", "55", "5", "93", "9", "1"]

# T : O(n + m log m) & S : O(m)  ## n is length of list and m is total no. of characters  ##Faster (C-level ops)
def form_largest_num(data):
    return ''.join(sorted(''.join(data), reverse=True))

## T : O(m log m) & S : O(m) ## m is total no. of characters  ##  Slower (Python loop)
# def form_largest_num(data):
#     tmp = []
#     for s in data:
#         if len(s) == 1:
#             tmp.append(s)
#         else:
#             j = 0
#             while j < len(s):
#                 tmp.append(s[j])
#                 j += 1

#     tmp.sort(reverse=True)
#     result = ''.join(tmp)

#     return result

result = form_largest_num(list1)
print(result)