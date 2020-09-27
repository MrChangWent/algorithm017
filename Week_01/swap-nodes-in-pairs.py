#coding:utf-8
#2020-09-24 22:30
#两两交换链表中的节点,步骤为：1.首先判断链表是否为空或者只有一个节点，是则直接return head，否则即开始递归，每次将第一个节点的next指向第三个节点，然后将第二个节点的next指向head，即完成了第一次调换，递归开始于此，每次调换动作执行都会判断first.next是否为空或者head.next为空，是则一层一层返回，最后return变换之后的head即可



class Solution(object):
	def swapPairs(self, head):
		if not head or head.next is None:
			return head
		first = head
		second = first.next
		first.next = self.swapPairs(second.next)
		second.next = first
		return second

