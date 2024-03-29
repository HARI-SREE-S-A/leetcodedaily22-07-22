{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
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
    "    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:\n",
    "        result = []\n",
    "        q = collections.deque()\n",
    "        q.append(root)\n",
    "        \n",
    "        while q:\n",
    "            level=[]\n",
    "            for i in range (len(q)):\n",
    "                node = q.popleft()\n",
    "                if node:\n",
    "                    level.append(node.val)\n",
    "                    q.append(node.left)\n",
    "                    q.append(node.right)\n",
    "            if level:\n",
    "                result.append(level)\n",
    "        return result"
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
