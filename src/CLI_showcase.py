from lib.node_class import node

initial_node = node()
#- the DFS algorithm is set on default to switch to BFS change the paramater BFS of method solution to True
#- to set a limit to the depth searched change the paramater limit to the chosen limit 
#- if you don't want to set a limit set the paramater limit to -1
#- if solution not found the method will return an empty list
result,nb=initial_node.solution(BFS=True,limit=5)
if result==[]:
    print("the solution was not found")
else:
    print("the solution can be accomplished in "+str(len(result)-1)+" moves")
print("the number of nodes explored was "+str(len(node.explored_states)))
print("the number of nodes generated was "+str(len(node.explored_states)+nb))
for state in result:
    state.show()