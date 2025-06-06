val = "11dd10111012345050adfd5607610000"

# T : O(n) & S : O(n)  ## Preserves order
def move_zeros_to_left(val):
    result = [''] * len(val)
    j = len(val) - 1
    zero_index = 0

    for i in range(len(val)-1, -1, -1):
        if val[i] != '0':
            result[j] = val[i]
            j -= 1
        else:
            result[zero_index] = '0'
            zero_index += 1

    return ''.join(result)

# # T : O(n log n) & S : O(n)  ## Order will be changed
# def move_zeros_to_left(val):
#     return ''.join(sorted(val))

## T : O(n2) & S : O(n)  ## Preserves order
# def move_zeros_to_left(val):
#     zeros = ''
#     non_zeros = ''
#     for c in val:
#         if c == '0':
#             zeros += c
#         else:
#             non_zeros += c
#     return zeros + non_zeros

## T : O(n2) & S : O(n)  ## Preserves order
# def move_zeros_to_left(val):
#     tmp = ""

#     for c in val:
#         if c != '0':
#             tmp += c
#         else:
#             tmp = '0' + tmp

#     return tmp

result = move_zeros_to_left(val)
print(result)

