{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Definition for singly-linked list.\n",
    "# class ListNode:\n",
    "#     def __init__(self, val=0, next=None):\n",
    "#         self.val = val\n",
    "#         self.next = next\n",
    "class Solution:\n",
    "    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:\n",
    "        cycle = bike = head\n",
    "        \n",
    "        while bike and bike.next:\n",
    "            cycle = cycle.next\n",
    "            bike = bike.next.next\n",
    "            \n",
    "        return cycle\n",
    "            "
   ]
  }
 ],
 "metadata": {
  "language_info": {
   "name": "python"
  },
  "orig_nbformat": 4
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
