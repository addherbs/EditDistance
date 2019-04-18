def solution(total_money, total_damage, costs, damages):

    greedy = []
    for i,cost in enumerate(costs):
        greedy.append([damages[i] / cost , cost, damages[i]])
    greedy.sort(reverse = True, key = lambda x: x[0])

    for key in greedy:
        temp_cost = key[1]
        temp_dmg = key[2]
        if(total_money - temp_cost >= 0):
            total_damage -= temp_dmg
            total_money -= temp_cost

        if (total_damage<= 0): return True

    return True if (total_damage <= 0) else False

print(solution(5, 5, [1,2,4], [2,4,2]))