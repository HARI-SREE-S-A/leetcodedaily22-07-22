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
    "    def findAnagrams(self, s: str, p: str) -> List[int]:        \n",
    "        result = list()\n",
    "        l, r = 0, len(p)-1\n",
    "        s_count, p_count = Counter(s[0:len(p)]), Counter(p)\n",
    "        \n",
    "        while True:\n",
    "\t\t\t# check if valid anagram, if so add leftmost index to result list.\n",
    "            if not len(p_count - s_count):\n",
    "                result.append(l)\n",
    "            \n",
    "            # decrease/remove leftmost char from hashmap and increase rightmost count.\n",
    "            if s[l] in s_count: s_count[s[l]] -= 1\n",
    "            r, l = r+1, l+1\n",
    "\n",
    "            if r >= len(s):\n",
    "                break\n",
    "                \n",
    "            s_count[s[r]] += 1\n",
    "        \n",
    "        return result"
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
