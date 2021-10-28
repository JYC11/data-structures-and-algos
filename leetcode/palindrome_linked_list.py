class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        string = ''

        while head != None:
            string += str(head.val)
            head = head.next

        return string == string[::-1]