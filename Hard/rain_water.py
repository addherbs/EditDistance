class Solution (object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        ans = 0;
        lmax = 0;
        rmax = 0
        l = 0;
        r = len (height) - 1

        if (r <= 1): return 0

        while (l < r):
            # print (l, r, lmax, rmax, ans)

            if (height[l] < height[r]):
                if (height[l] >= lmax):
                    lmax = height[l]
                else:
                    ans += (lmax - height[l])
                l += 1
            else:
                if (height[r] >= rmax):
                    rmax = height[r]
                else:
                    ans += (rmax - height[r])
                r -= 1

        print (ans)
        return ans