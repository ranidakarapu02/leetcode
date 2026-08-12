class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        sol = []

        def backtrack(x):
            if len(sol) == k:
                res.append(sol[:])
                return

            if x < 1:
                return

            # Don't choose x
            backtrack(x - 1)

            # Choose x
            sol.append(x)
            backtrack(x - 1)
            sol.pop()

        backtrack(n)
        return res