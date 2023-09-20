def cleanstr(raw_str):
    """
    Removes unbalanced parentheses from a string.
    
    Args:
        raw_str (str): Input string containing parentheses.
        
    Returns:
        str: A new string with balanced parentheses.
    """
    stack = []
    removeQ = []
    resultstr = ""
    
    for i in range(len(raw_str)):
        c = raw_str[i]
        if c == "(":
            stack.append(i)
        elif c == ")":
            try:
                stack.pop()
            except IndexError:
                removeQ.append(i)
    
    print(f"Remove Queue: {removeQ}")
    print(f"Stack: {stack}")
    
    for i, c in enumerate(raw_str):
        if i in (removeQ + stack):
            continue
        resultstr += c

    return resultstr


def test_cleanstr():
    # Test Case 1: No unbalanced parentheses
    input_str_1 = "hg(*)(*())"
    assert cleanstr(input_str_1) == input_str_1

    # Test Case 2: Unbalanced parentheses
    input_str_2 = "h(2))1((()(232(1)"
    assert cleanstr(input_str_2) == 'h(2)1()232(1)'

    # Test Case 3: Empty string
    input_str_3 = ""
    assert cleanstr(input_str_3) == ""

    # Test Case 4: No parentheses
    input_str_4 = "Hello, world!"
    assert cleanstr(input_str_4) == input_str_4

    # Test Case 5: Only unbalanced parentheses
    input_str_5 = ")(()))))()("
    assert cleanstr(input_str_5) == ""
    
    print("All test cases passed!")

test_cleanstr()
