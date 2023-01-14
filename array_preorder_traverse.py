{
 "cells": [
  {
   "cell_type": "code",
   
   
   
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "class Solution:\n",
    "\tdef preorder(self, root: 'Node') -> List[int]:\n",
    "\t\tif root is None:\n",
    "\t\t\treturn root\n",
    "\t\tnodestack=[]\n",
    "\t\tnodestack.append(root)\n",
    "\t\tans=[]\n",
    "\t\twhile len(nodestack):\n",
    "\t\t\tcurr=nodestack[0]\n",
    "\t\t\tnodestack.pop(0)\n",
    "\t\t\tans.append(curr.val)\n",
    "\t\t\tfor it in range(len(curr.children)-1,-1,-1): \n",
    "\t\t\t\tnodestack.insert(0,curr.children[it])\n",
    "      \n",
    "\t\treturn ans"
    
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
