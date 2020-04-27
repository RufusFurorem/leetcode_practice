# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        list_processed = 0
        merged_list = None
        prev = None
        
        if not lists:
            return 

        for i, val in enumerate(lists):
            if val:
                merged_list = val
                list_processed = i + 1
                break
                
        if merged_list == None:
            return
        
        while list_processed < len(lists):
            head = point = ListNode(0)
            while merged_list and lists[list_processed]:
                if merged_list.val <= lists[list_processed].val:
                    point.next = merged_list
                    merged_list = merged_list.next
                else:
                    point.next = lists[list_processed]
                    lists[list_processed] = merged_list
                    merged_list = point.next.next
                point = point.next
            if not merged_list:
                point.next=lists[list_processed]
            else:
                point.next=merged_list
            
            merged_list = head.next
                
            list_processed += 1
        
        return merged_list
        