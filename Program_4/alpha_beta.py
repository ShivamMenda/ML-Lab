class Tree:
    def __init__(self,value,children=[]):
        self.value=value
        self.children=children

game_tree=Tree(0,
[
    Tree(0,
    [Tree(3),Tree(12)]
    ),
    Tree(0,
    [Tree(8),Tree(2)]
    ),
])

def minmax(tree,depth,alpha,beta,max_player):
    if(depth==0 or not tree.children):
        return tree.value,[tree.value]
    if(max_player):
        max_value=float("-inf")
        max_path=[]
        for child in tree.children:
            child_value,child_path=minmax(child,depth-1,alpha,beta,False)
            if(child_value>max_value):
                max_value=child_value
                max_path=[tree.value]+child_path
            alpha=max(alpha,max_value)
            if(alpha>=beta):
                break
        return max_value,max_path
    else:
        min_value = float("inf")
        min_path = []
        for child_node in tree.children:
            child_value, child_path = minmax(child_node, depth - 1, alpha, beta, True)
            if child_value < min_value:
                min_value = child_value
                min_path = [tree.value] + child_path
            beta = min(beta, min_value)
            if alpha >= beta:
                break
        return min_value, min_path

optimal_value, optimal_path = minmax(game_tree, 2, float("-inf"), float("inf"), True)
print("Optimal value:", optimal_value)
print("Optimal path:", optimal_path)
