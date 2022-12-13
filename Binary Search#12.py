{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "class Solution:\n",
    "    def search(self, nums: List[int], target: int) -> int:\n",
    "      i = 0  \n",
    "      for i in range (0,len(nums)-1):\n",
    "        if nums[i] == target:\n",
    "            return i\n",
    "            if nums[i] != target:\n",
    "                i += 1 \n",
    "          \n",
    "      
    "      return -1\n",
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
 "nbformat": 2
}
