def balanceCheck(string):
    # first check the length of the string
    if len(string) % 2 != 0:
        return False

    # opening set
    openig_set = set('({[')
    # matching set
    matching_pair = set([('(', ')'), ('{', '}'), ('[', ']')])
    # define stack
    stack = []
    # lets travel through the string
    for i in string:
        # now push opening to the stack
        if i in openig_set:
            # Append to the stack
            stack.append(i)

        else:
            # check the length of stack(if not matching to the opening )
            if len(stack) == 0:
                return False
            # now initialize a variable for check,which will pop until find the the match pair

            last_check = stack.pop()

            '''
            #make sure parameter will be (last check,i)
            because it pop then )
            '''

            if (last_check, i) not in matching_pair:
                return False
    # now going to return stack length 0
    return len(stack) == 0


a = '( ()'
# pass to the function
print(balanceCheck(a))
