import collections

q = collections.deque([])
q.append(123)
q.append(456)
q.append(789)
print(q.popleft())
print(len(q))
