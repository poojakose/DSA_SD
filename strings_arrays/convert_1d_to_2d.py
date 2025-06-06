original = [1,2,3,4]
m, n = 2, 2

def solution(original, m, n):
    if m*n != len(original):
            return []
        
    result = []
    
    for r in range(m):
        start = r * n 
        end = start + n
        result.append(original[start:end])
    return result

result = solution(original, m, n)
print(result)