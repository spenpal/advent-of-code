# FUNCTIONS
def visible(t_map, trans_t_map, i, j):
    max_up_tree = max(map(int, trans_t_map[j][:i]))
    max_down_tree = max(map(int, trans_t_map[j][i+1:]))
    max_left_tree = max(map(int, t_map[i][:j]))
    max_right_tree = max(map(int, t_map[i][j+1:]))
    tree_h = int(t_map[i][j])
    
    return any(max_tree < tree_h 
               for max_tree in (max_up_tree, max_down_tree, max_left_tree, max_right_tree))


# MAIN
with open("input.txt") as f:
    t_map = f.read().splitlines()
    trans_t_map = list(zip(*t_map))
    visible_trees = ((len(t_map)-2) + len(t_map[0])) * 2
    
for i in range(1, len(t_map) - 1):
    for j in range(1, len(t_map[0]) - 1):
        visible_trees += visible(t_map, trans_t_map, i, j)
    
print(visible_trees)