from collections import namedtuple

def is_balanced_binary(bin_tree):
    BalancedAndHeight = nt('BalancedAndHeight', 'balanced height')
    def check_balanced(tree):
        if not tree:                            #if leaf
            return BalancedAndHeight(True, -1)

        left_result = check_balanced(tree.left)
        if not left_result.balanced:
            return BalancedAndHeight(False, 0)

        right_result = check_balanced(tree.right)
        if not right_result.balanced:
            return BalancedAndHeight(False, 0)

        is_balanced = abs(left_result.height - right_result.height) <= 1
        height = max(left_result.height, right_result.height) + 1
        return BalancedAndHeight(is_balanced, height)
    return check_balanced(bin_tree).balanced
