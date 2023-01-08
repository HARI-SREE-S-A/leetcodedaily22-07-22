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
    "    dp = dict()\n",
    "    def uniquePaths(self, m: int, n: int) -> int:\n",
    "        if m > n:\n",
    "            r = m\n",
    "            c = n\n",
    "        else:\n",
    "            r = n\n",
    "            c = m\n",
    "            \n",
    "        if r == 1 or c == 1:\n",
    "            return 1\n",
    "\n",
    "        if (r, c) not in self.dp:\n",
    "            self.dp[(r, c)] = self.uniquePaths(r - 1, c) + self.uniquePaths(r, c - 1)\n",
    "\n",
    "        return self.dp[(r,c)]"
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
