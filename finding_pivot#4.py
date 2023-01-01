{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "class Solution:\n",
    "\tdef pivotIndex(self, nums: list[int]) -> int:\n",
    "        summ =  sum(nums)\n",
    "        right = 0        \n",
    "        for i in range (len(nums)):\n",
    "            left = summ - right - nums[i]\n",
    "            if left == right:\n",
    "                return i \n",
    "            left += nums[i]\n",
    "\n",
    "\n",
    "        return -1\n",
    "             \n",
    "             \n",
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
