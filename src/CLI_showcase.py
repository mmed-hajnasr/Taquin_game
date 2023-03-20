import lib.node_class as mine

initial_node = mine.node()
#- the DFS algorithm is set on default to switch to BFS change the paramater BFS of method solution to True
#- to set a limit to the depth searched change the paramater limit to the chosen limit 
#- if you don't want to set a limit set the paramater limit to -1
#- if solution not found the method will return an empty list
result=initial_node.solution(BFS=False,limit=4)
if result==[]:
    print("the solution was not found")
else:
    print("the solution can be accomplished in "+str(len(result)-1)+" moves")
print("the number of nodes expored was "+str(len(mine.node.explored_states)))