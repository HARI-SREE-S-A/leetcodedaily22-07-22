{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "hellow world\n"
     ]
    } 
   ],
   "source": [
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Definition for a binary tree node.\n",
    "# class TreeNode:\n",
    "#     def __init__(self, val=0, left=None, right=None):\n",
    "#         self.val = val\n",
    "#         self.left = left\n",
    "#         self.right = right\n",
    "class Solution:\n",
    "    def isValidBST(self, root: Optional[TreeNode]) -> bool:\n",
    "        def check_valid(node, max_left, max_right):\n",
    "            if not node: return True\n",
    "            if node.val <= max_left or node.val >= max_right: return False\n",
    "            return check_valid(node.left, max_left, node.val) and check_valid(node.right, node.val, max_right)\n",
    "        return check_valid(root, -float('inf'), float('inf'))"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3.10.4 64-bit",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.4"
  },
  "orig_nbformat": 4,
  "vscode": {
   "interpreter": {
    "hash": "3a1f4c369d64c01a82ffa09783598b9a02f96933d26a870e3e0a06bbbe91dde6"
   }
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
