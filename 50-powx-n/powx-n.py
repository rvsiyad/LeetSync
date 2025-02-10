class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Use recursion
        isNegative = n < 0

        def helper(x, n, cache):
            if n in cache:
                return cache[n]
            
            if n == 0:
                return 1

            if n == 1:
                return x
            

            cache[n] = helper(x, n // 2, cache) * helper(x, n // 2, cache) * (x if n % 2 else 1)
    
            return cache[n]
        
        result = helper(x, abs(n), {})
        
        return  1 / result if isNegative  else result
            
