class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        ptr = head
        forOdd = []
        forEven = []
        i = 1
        while ptr:
            if i % 2 == 0:
                forEven.append(ptr)
            else:
                forOdd.append(ptr)
            ptr = ptr.next
            i += 1

        stores = None
        if forOdd:
            stores = forOdd.pop(0)
        elif forEven:
            stores = forEven.pop(0)
        else:
            return None

        final = stores
        while forOdd:
            stores.next = forOdd.pop(0)
            stores = stores.next

        while forEven:
            stores.next = forEven.pop(0)
            stores = stores.next

        stores.next = None
        return final