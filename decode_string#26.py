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
    "\tdef decodeString(self, s: str) -> str:\n",
    "\n",
    "\t\tst = []\n",
    "\n",
    "\t\tfor c in s:\n",
    "\t\t\tif c == ']':\n",
    "\t\t\t\ts = ''\n",
    "\t\t\t\twhile st[-1] != '[': s = st.pop() + s\n",
    "\t\t\t\tst.pop()\n",
    "\t\t\t\tk = ''\n",
    "\t\t\t\twhile st and st[-1].isdigit(): k = st.pop() + k\n",
    "\t\t\t\tk = int(k)\n",
    "\t\t\t\tst.append(s*k)\n",
    "\t\t\telse : st.append(c)\n",
    "\n",
    "\t\treturn ''.join(st)"
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
