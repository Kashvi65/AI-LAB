import math

# --------------------------------------------
# Define the game tree structure
# --------------------------------------------
game_tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['L1', 'L2'],
    'E': ['L3', 'L4'],
    'F': ['L5', 'L6'],
    'G': ['L7', 'L8'],
    'L1': 10,
    'L2': 9,
    'L3': 14,
    'L4': 18,
    'L5': 5,
    'L6': 4,
    'L7': 50,
    'L8': 3
}

# --------------------------------------------
# Pretty print the game tree as ASCII art
# --------------------------------------------
def print_tree():
    print("\n================ GAME TREE STRUCTURE ================\n")
    print("                     A (MAX)")
    print("                 /            \\")
    print("             B (MIN)           C (MIN)")
    print("           /       \\         /       \\")
    print("      D (MAX)     E (MAX)  F (MAX)   G (MAX)")
    print("     /    \\      /    \\    /    \\    /    \\")
    print("   10     9    14    18   5     4   50     3")
    print("\n=====================================================\n")

# --------------------------------------------
# Alpha-Beta Pruning Implementation (with detailed trace)
# --------------------------------------------
def alphabeta(node, depth, alpha, beta, maximizing_player):
    indent = "  " * depth  # indentation for readability

    # Base case: Leaf node
    if isinstance(game_tree[node], int):
        print(f"{indent}Reached leaf {node} with value = {game_tree[node]}")
        return game_tree[node]

    # MAX Node
    if maximizing_player:
        print(f"{indent}→ MAX node {node} (depth={depth}) | α={alpha:.2f}, β={beta:.2f}")
        max_eval = -math.inf
        for child in game_tree[node]:
            print(f"{indent}  Exploring child {child} of {node} ...")
            eval_value = alphabeta(child, depth + 1, alpha, beta, False)
            max_eval = max(max_eval, eval_value)
            alpha = max(alpha, eval_value)
            print(f"{indent}  Updated {node}: value={max_eval}, α={alpha:.2f}, β={beta:.2f}")
            if beta <= alpha:
                print(f"{indent}  ⚠️  Pruning remaining children of {node} (β={beta:.2f} ≤ α={alpha:.2f})")
                break
        return max_eval

    # MIN Node
    else:
        print(f"{indent}→ MIN node {node} (depth={depth}) | α={alpha:.2f}, β={beta:.2f}")
        min_eval = math.inf
        for child in game_tree[node]:
            print(f"{indent}  Exploring child {child} of {node} ...")
            eval_value = alphabeta(child, depth + 1, alpha, beta, True)
            min_eval = min(min_eval, eval_value)
            beta = min(beta, eval_value)
            print(f"{indent}  Updated {node}: value={min_eval}, α={alpha:.2f}, β={beta:.2f}")
            if beta <= alpha:
                print(f"{indent}  ⚠️  Pruning remaining children of {node} (β={beta:.2f} ≤ α={alpha:.2f})")
                break
        return min_eval


# --------------------------------------------
# Run the algorithm
# --------------------------------------------
print_tree()
print("Starting Alpha–Beta Pruning...\n")

best_value = alphabeta('A', 0, -math.inf, math.inf, True)

print("\n=====================================================")
print(f"✅ Best achievable value at root (A): {best_value}")
print("=====================================================")
