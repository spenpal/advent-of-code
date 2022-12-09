# FUNCTIONS
def block_index(tree_row, tree_h):
    for i, tree in enumerate(tree_row):
        if tree >= tree_h:
            return i + 1
    return i + 1


def scenic_score(t_map, trans_t_map, i, j):
    tree_h      = t_map[i][j]
    up_view     = block_index(trans_t_map[j][:i][::-1], tree_h)
    down_view   = block_index(trans_t_map[j][i+1:], tree_h)
    left_view   = block_index(t_map[i][:j][::-1], tree_h)
    right_view  = block_index(t_map[i][j+1:], tree_h)
    
    return up_view * down_view * left_view * right_view


# MAIN
with open("input.txt") as f:
    t_map = f.read().splitlines()
    trans_t_map = [''.join(tree_row) for tree_row in zip(*t_map)]
    visible_trees = ((len(t_map)-2) + len(t_map[0])) * 2
    
best_scenic_score = max(scenic_score(t_map, trans_t_map, i, j) 
                        for i in range(1, len(t_map) - 1) 
                        for j in range(1, len(t_map[0]) - 1))
print(best_scenic_score)