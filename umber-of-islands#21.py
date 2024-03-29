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
    "    def numIslands(self, grid: List[List[str]]) -> int:\n",
    "        count = 0\n",
    "        m = len(grid)\n",
    "        n = len(grid[0])\n",
    "\t\t# here marking all the islands as false visited\n",
    "        visited = [[False for i in range(n)] for j in range(m)]\n",
    "\t\t\n",
    "        # This method will mark the island cell as visited as well as call all the neighbor\n",
    "        def neighbor(g,v,i,j):\n",
    "            if g[i][j] == \"0\" or v[i][j] == True:\n",
    "                return\n",
    "            v[i][j] = True\n",
    "            if j-1 >= 0:\n",
    "                neighbor(g,v,i,j-1)\n",
    "            if j+1 < n:\n",
    "                neighbor(g,v,i,j+1)\n",
    "            if i-1 >= 0:\n",
    "                neighbor(g,v,i-1,j)\n",
    "            if i+1 < m:\n",
    "                neighbor(g,v,i+1,j)\n",
    "\t\t\n",
    "\t\t# Now just loop on all the cell if visited then continue else send it to \n",
    "        for i in range(m):\n",
    "            for j in range(n):\n",
    "                if grid[i][j] == \"1\" and visited[i][j] == False:\n",
    "                    neighbor(grid,visited,i,j)\n",
    "                    count += 1\n",
    "      return count"
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
