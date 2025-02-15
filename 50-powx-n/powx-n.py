class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        def helper(x, n, cache):
            if n in cache:
                return cache[n]
            
            if n == 1:
                return x
            
            if n == 0:
                return 1
            
            cache[n] = helper(x, n // 2, cache) * helper(x, n // 2, cache) * (x if n % 2 != 0 else 1)

            return cache[n]
        
        if n >= 0:
            return helper(x, n, {})
        else:
            return 1 / helper(x, abs(n), {}) 