

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
    "class Solution(object):\n",
    "    def twoSum(self, nums, target):\n",
    "        \"\"\"\n",
    "        :type nums: List[int]\n",
    "        :type target: int\n",
    "        :rtype: List[int]\n",
    "        \"\"\"\n",
    "        for i in range(len(nums)):\n",
    "            to_find = target - nums[i]\n",
    "            for j in range(i+1,len(nums)):\n",
    "                if to_find == nums[j]:\n",
    "                    return [i,j]"
   ]
   
  }
 ],
 "metadata": {
  "kernelspec": {
 
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
   "version": "3.10.5"
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
