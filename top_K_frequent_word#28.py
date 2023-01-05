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
    "\n",
    "  class Solution:\n",
    "    def topKFrequent(self, words: List[str], k: int) -> List[str]:\n",
    "        freqs = {}\n",
    "        for w in words:\n",
    "            if w in freqs:\n",
    "                freqs[w] += 1\n",
    "            else:\n",
    "                freqs[w] = 1\n",
    "        output = []\n",
    "        for w in sorted(freqs.keys(), key=lambda x: (-freqs[x], x))[:k]:\n",
    "            output.append(w)\n",
    "        return output"
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
