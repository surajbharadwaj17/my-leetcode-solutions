#
# @lc app=leetcode id=721 lang=python3
#
# [721] Accounts Merge
#

# @lc code=start
import collections
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        graph = collections.defaultdict(list)
        visited = [False for _ in range(len(accounts))]
        ret = []

        for i, acc in enumerate(accounts):
            for j in range(1, len(acc)):
                graph[acc[j]].append(i)     # { "email" : [0,2 <User index>]}

        def dfs(i, emails):
            # Base case - Already visited node
            if visited[i] : return
            
            # Mark as visited
            visited[i] = True
            for j in range(1, len(accounts[i])):
                email = accounts[i][j]
                emails.add(email)

                # Visit all the neighbors
                for nei in graph[email]:
                    dfs(nei, emails)
        
        for i,acc in enumerate(accounts):
            if not visited[i]:
                name, emails = acc[0], set()
                dfs(i, emails)
                ret.append([name] + sorted(emails))

        return ret


        
# @lc code=end

