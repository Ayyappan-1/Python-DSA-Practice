# identical detection of two trees which has the time complexity of O(n) and space complexity of O(n)
from collections import deque

class operations:
    def identical(t1, t2):
        if t1 is None and t2 is None:
            return True
        if t1 is None or t2 is None:
            return False

        q = deque()
        q.append((t1, t2))
        while q:
            node1, node2 = q.popleft()
            if node1 is None and node2 is None:
                continue

            if node1 is None or node2 is None:
                return False

            if node1.data != node2.data:
                return False
            q.append((node1.left, node2.left))
            q.append((node1.right, node2.right))

        return True
