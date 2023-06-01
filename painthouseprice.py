costs = [[17,2,17],[16,16,5],[14,3,19]]
costs2 = [1,2,3,4]

def minCost(costs):
    




# def minCost(costs): WRONG BRUH because this takes into account taking the minimum of each
#house, but thasts not necessarily true
#     minValue = 0
#     tempIndex = 0
#     for i in range(len(costs)):
#         if i == 0:
#             minValue += min(costs[i])
#             tempIndex = costs[i].index(min(costs[i]))
#             print("tempIndex: ", tempIndex)
#         else:
#             if costs[i].index(min(costs[i])) != tempIndex:
#                 minValue += min(costs[i])
#                 tempIndex = costs[i].index(min(costs[i]))
#             else:
#                 costs[i].remove(min(costs[i]))
#                 minValue += min(costs[i])
#                 tempIndex = costs[i].index(min(costs[i]))
#     return minValue
def main():
    print(minCost(costs2))
if __name__ == "__main__":
    main()
