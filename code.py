class Solution(object):
    def rotateRight(self, head, k):
        n, pre, current = 0, None, head
        while current:
            pre, current = current, current.next
            n += 1

        if not n or not k % n:
            return head

        tail = head
        for _ in range(n - k % n - 1):
            tail = tail.next

        next, tail.next, pre.next = tail.next, None, head
        return next

'''
 the idea behind n - k % n - 1 is to find the element of your new tail, but since it's a singly linked list, we want to walk from the head, not backwards from the tail.

For example:

A -> B -> C ->D, k = 6

If we walk 6 back from D, we land on B. We can skip the circular walk back using the modulus operator, 6% 4 = 2, which also lands on B. 
We want to know how many steps it takes from our current head (A) to get to our new tail(B), we take 1 step less than the result of the modulus to avoid off by 1.
'''

