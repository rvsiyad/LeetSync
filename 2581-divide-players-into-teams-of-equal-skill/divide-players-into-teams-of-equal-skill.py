class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()

        L = 0
        R = len(skill) - 1

        perTeamSum = skill[L] + skill[R]
        teams = []

        while L < R:
            currSum = skill[L] + skill[R]

            if currSum != perTeamSum:
                return -1

            teams.append((skill[L], skill[R]))

            L += 1
            R -= 1
        
        res = 0

        for t in teams:
            num1, num2 = t

            res += (num1 * num2)

        
        return res