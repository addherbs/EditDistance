"""
Evaluate Division

Solution
You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single variable.

You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer for Cj / Dj = ?.

Return the answers to all queries. If a single answer cannot be determined, return -1.0.

Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.

 

Example 1:

Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
Explanation: 
Given: a / b = 2.0, b / c = 3.0
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
return: [6.0, 0.5, -1.0, 1.0, -1.0 ]
Example 2:

Input: equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
Output: [3.75000,0.40000,5.00000,0.20000]
Example 3:

Input: equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
Output: [0.50000,2.00000,-1.00000,-1.00000]
 

Constraints:

1 <= equations.length <= 20
equations[i].length == 2
1 <= Ai.length, Bi.length <= 5
values.length == equations.length
0.0 < values[i] <= 20.0
1 <= queries.length <= 20
queries[i].length == 2
1 <= Cj.length, Dj.length <= 5
Ai, Bi, Cj, Dj consist of lower case English letters and digits.

"""


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        nodes = dict()
        count = 0
        rev = {}
        for n1, n2 in equations:
            if n1 not in nodes:
                nodes[n1] = count
                rev[count] = n1
                count += 1
            if n2 not in nodes:
                rev[count] = n2
                nodes[n2] = count
                count += 1
        
        adj_list = [[0 for _ in range(len(nodes))] for i in range(len(nodes))]
        
        for i, eq in enumerate(equations):
            n1, n2 = eq
            adj_list[nodes[n1]][nodes[n2]] = values[i]
            adj_list[nodes[n2]][nodes[n1]] = 1 / values[i]
        
        # print(adj_list)
        answer = []
        for start, end in queries:
            if start not in nodes or end not in nodes: 
                answer.append(-1.0)
                continue
                
            visited = set()
            stack = [[start, 1]]
            ans = -1.0
            
            while stack:
                # print(stack)
                cur, val = stack.pop()
                if cur == end:
                    ans = val
                    break

                visited.add(cur)
                
                for i, elem in enumerate(adj_list[nodes[cur]]):
                    if not elem: continue
                    if rev[i] in visited: continue
                    stack.append([rev[i], val * elem])
        
            answer.append(ans)
        
        return answer
        