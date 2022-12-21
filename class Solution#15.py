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
    "    def floodFill(self, image: List[List[int]], sr: int, sc: int, fillcolor: int) -> List[List[int]]:\n",
    "        from collections import deque\n",
    "        import numpy as np\n",
    "        m, n = len(image), len(image[0])\n",
    "        visited = np.full((m, n), False).tolist()\n",
    "        Q = deque([])\n",
    "        srccolor = image[sr][sc] \n",
    "        Q.append((sr, sc))\n",
    "        image[sr][sc] = fillcolor; visited[sr][sc] = True \n",
    "        directions = [(1, 0), (-1, 0), (0, 1), (0,-1)]\n",
    "        while Q:\n",
    "            (i,j) = Q.popleft()\n",
    "            for dx, dy in directions:\n",
    "                x, y = i+dx, j+dy\n",
    "                if (0 <= x < m) and (0 <= y < n):\n",
    "                    if (image[x][y] == srccolor) and (not visited[x][y]):\n",
    "                        image[x][y]= fillcolor\n",
    "                        Q.append((x,y))\n",
    "            visited[i][j] = True        \n",
    "        return image\n",
    "# 286 ms, 32.1 MB"
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
   "version": "3.10.4"
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
