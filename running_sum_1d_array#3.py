{
 "cells": [
  
  
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "class Solution:\n",
    "    def runningSum(self, nums: List[int]) -> List[int]:\n",
    "        for i in range(1,len(nums)):\n",
    "            nums[i]+=nums[i-1]\n",
    "        return nums\n",
    "        "
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
