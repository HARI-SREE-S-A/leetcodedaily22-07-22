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
    "class Solution:\n",
    "    def climbStairs(self, n: int) -> int:        \n",
    "        if n == 1:\n",
    "            return 1\n",
    "\t\t\t\n",
    "        res = [0 for x in range(n)]\n",
    "        res[0] = 1 #base case n =1 -> 1\n",
    "        res[1] = 2 #base case n =2 -> 2\n",
    "\t\t\n",
    "        for i in range(2, n):\n",
    "            res[i] = res[i-1] + res[i-2]\n",
    "\t\t\t\n",
    "        return res[n-1]\n",
    "def climbStairs(self, n: int) -> int:\n",
    "         dp = {}\n",
    "        \n",
    "         def fib(n):\n",
    "             if n == 1:\n",
    "                 return 1\n",
    "             if n == 2:\n",
    "                 return 2\n",
    "             if n in dp:\n",
    "                 return dp[n]\n",
    "             else:\n",
    "                 res = fib(n-1) + fib(n-2)\n",
    "                 dp[n] = res\n",
    "                 return res\n",
    "         return fib(n)"
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
