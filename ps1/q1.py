def longest_valid_paranthesis(str):
    """
    Given a string containing just the characters '(' and ')',
    find the length of the longest valid (well-formed) parentheses substring.

    Constraints:

    0 <= s.length <= 3 * 104
    s[i] is '(', or ')'.

    >>> s_1 = "(()"
    >>> result_1 = longest_valid_paranthesis(s_1)
    >>> result_1
    2
    >>> s_2 = ")()())"
    >>> result_2 = longest_valid_paranthesis(s_1)
    >>> result_2
    4
    >>> s_3 = ""

    >>> result_3 = longest_valid_paranthesis(s_1)
    >>> result_3
    0
    """
    n = len(str)

    # Create an empty list
    stack_list = []
    stack_list.append(-1)

    # initialise count
    count = 0

    for i in range(n):
        if str[i] == '(':
            stack_list.append(i)
        else:
            if len(stack_list) != 0:
                stack_list.pop() # delete the previous unmatched parenthesis
            if len(stack_list) != 0:
                count = max(count, i - stack_list[len(stack_list) - 1])
            else:
                stack_list.append(i)

    return count
