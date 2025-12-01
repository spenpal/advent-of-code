def parse(data: str) -> dict[int, tuple]:
    t_map = data.strip().splitlines()
    trans_t_map = list(zip(*t_map, strict=False))
    visible_trees = ((len(t_map) - 2) + len(t_map[0])) * 2

    return {1: (t_map, trans_t_map, visible_trees), 2: (t_map, trans_t_map, visible_trees)}


def visible(t_map, trans_t_map, i, j):
    max_up_tree = max(map(int, trans_t_map[j][:i]))
    max_down_tree = max(map(int, trans_t_map[j][i + 1 :]))
    max_left_tree = max(map(int, t_map[i][:j]))
    max_right_tree = max(map(int, t_map[i][j + 1 :]))
    tree_h = int(t_map[i][j])

    return any(max_tree < tree_h for max_tree in (max_up_tree, max_down_tree, max_left_tree, max_right_tree))


def part1(t_map, trans_t_map, visible_trees):
    def visible(t_map, trans_t_map, i, j):
        max_up_tree = max(map(int, trans_t_map[j][:i]))
        max_down_tree = max(map(int, trans_t_map[j][i + 1 :]))
        max_left_tree = max(map(int, t_map[i][:j]))
        max_right_tree = max(map(int, t_map[i][j + 1 :]))
        tree_h = int(t_map[i][j])

        return any(max_tree < tree_h for max_tree in (max_up_tree, max_down_tree, max_left_tree, max_right_tree))

    for i in range(1, len(t_map) - 1):
        for j in range(1, len(t_map[0]) - 1):
            visible_trees += visible(t_map, trans_t_map, i, j)
    return visible_trees


def part2(t_map, trans_t_map, visible_trees):
    def block_index(tree_row, tree_h):
        for i, tree in enumerate(tree_row):
            if tree >= tree_h:
                return i + 1
        return i + 1

    def scenic_score(t_map, trans_t_map, i, j):
        tree_h = t_map[i][j]
        up_view = block_index(trans_t_map[j][:i][::-1], tree_h)
        down_view = block_index(trans_t_map[j][i + 1 :], tree_h)
        left_view = block_index(t_map[i][:j][::-1], tree_h)
        right_view = block_index(t_map[i][j + 1 :], tree_h)

        return up_view * down_view * left_view * right_view

    trans_t_map = ["".join(tree_row) for tree_row in zip(*t_map, strict=False)]
    return max(
        scenic_score(t_map, trans_t_map, i, j) for i in range(1, len(t_map) - 1) for j in range(1, len(t_map[0]) - 1)
    )
