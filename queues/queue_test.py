# using list
nums = []
nums.append(2)
nums.append(3)
nums.append(4)
print(nums)

nums.pop(0)
nums.append(5)
print(nums)

## using deque
# from collections import deque
# nums = deque()
# nums.append(2)
# nums.append(3)
# nums.append(4)
# print(nums)

# nums.popleft()
# nums.append(5)
# print(nums)

# ## Using queue.Queue

# from queue import Queue

# nums = Queue(maxsize=3)
# nums.put(2)
# nums.put(3)
# nums.put(4)
# print(list(nums.queue))

# nums.get()
# nums.put(5)
# print(list(nums.queue))

