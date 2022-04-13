from heapq import heappush,heappop
import queue

class ListNode():
    def __init__(self,val=0,next=None) -> None:
        self.val = val
        self.next = next

class PriorityQueue:
    def __init__(self) -> None:
        self.heap = []

    def insertKey(self,k):
        self.heap.append(k)

    def getMin(self):
        return min(self.heap)

    def queueLen(self):
        return len(self.heap)

    def delete(self):
        # delete the min ele from self.heap
        try:
            min_idx = 0
            for i in range(len(self.heap)):
                if self.heap[i] < self.heap[min_idx]:
                    min_idx = i
            item = self.heap[min_idx]
            self.heap.pop(min_idx)
            return item
        except:
            pass


class Solution():
    def mergeKLists(self, lists):
        
        dummy = ListNode()
        cur = dummy
        queue = PriorityQueue()

        for node in lists:
            if node:
                queue.insertKey((node.val,node))

        while(queue.queueLen() > 0):
            cur.next = queue.getMin()[1]
            cur = cur.next
            if(cur.next):
                queue.insertKey((cur.next.val, cur.next))
        
        return dummy.next

    def mergeKLists_v2(self, lists):
        from queue import PriorityQueue

        dummy = ListNode()
        cur = dummy
        queue = PriorityQueue()
        cnt = 0

        for node in lists:
            cnt += 1
            if node:
                queue.put((node.val,cnt,node))
                
        while(queue.qsize() > 0):
            cur.next = queue.get()[2]
            cur = cur.next
            cnt += 1
            if(cur.next):
                queue.put((cur.next.val,cnt, cur.next))
        
        return dummy.next

