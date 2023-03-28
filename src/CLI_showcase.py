from lib.node_class import node

#- the DFS algorithm is set on default to switch to BFS change the paramater BFS of method solution to True
#- to set a limit to the depth searched change the paramater limit to the chosen limit 
#- if you don't want to set a limit set the paramater limit to -1
#- if solution not found the method will return an empty list
node.initial_state=[[1,2,3],[4,5,6],[7,8,0]]
node.final_state=[[1,4,7],[2,5,8],[3,6,0]]
initial_node = node()
result,nb=initial_node.solution(BFS=True)
if result==[]:
    print("the solution was not found")
else:
    print("the solution can be accomplished in "+str(len(result)-1)+" moves")
print("the number of nodes explored was "+str(len(node.explored_states)))
print("the number of nodes generated was "+str(len(node.explored_states)+nb))
for state in result:
    state.show()