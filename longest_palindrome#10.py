{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    
    "class Solution:\n",
    "    def longestPalindrome(self, s: str) -> int:\n",
    "        counter = 0\n",
    "        containsOdds = False\n",
    "        hashtbl = {}\n",
    "        \n",
    "        for i in range(len(s)):\n",
    "            if s[i] in hashtbl.keys():\n",
    "                hashtbl[s[i]] += 1 \n",
    "            else:\n",
    "                hashtbl[s[i]] = 1\n",
    "        \n",
    "        for value in hashtbl.values():\n",
    "            if value % 2 == 0:\n",
    "                counter += value\n",
    "            else:\n",
    "                containsOdds = True\n",
    "                counter += value - 1\n",
    "        \n",
    "        if containsOdds:\n",
    "            counter += 1\n",
    "\n",
    "        return counter"
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
