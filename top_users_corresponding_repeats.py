"""
A website named "All for Five", sells many products to registered clients that cost all the same (5 dollars, the price is not relevant). Every user receives an alphanumeric id code, like D085. The page tracks all the purchases, that the clients do. For each purchase of a certain client, his/her id user will be registered once.

You will be given an uncertain number of arrays that contains strings (the id code users). Each array will represent the purchases that the users do in a month. You should find the total number of purchases of the users that have bought in all the given months (the clients that their id code are present in all the arrays). e.g.:

a1 = ['A042', 'B004', 'A025', 'A042', 'C025']
a2 = ['B009', 'B040', 'B004', 'A042', 'A025', 'A042']
a3 = ['A042', 'A025', 'B004']
The result will be:

'A042'---> 5 times
'A025'---> 3 times
'B004'---> 3 times
It may be that not even a single user has purchased in all the months

a1 = ['A043', 'B004', 'A025', 'A042', 'C025']
a2 = ['B009', 'B040', 'B003', 'A042', 'A027', 'A044']
a3 = ['A041', 'A026', 'B005']
Even though '0042' is present in two arrays, is not present in all the arrays.

The function that solves this challenge will be called as: id_best_users().

The entries of the function and the output for the cases above will be:

a1 = ['A042', 'B004', 'A025', 'A042', 'C025']
a2 = ['B009', 'B040', 'B004', 'A042', 'A025', 'A042']
a3 = ['A042', 'A025', 'B004']
id_best_users(a1, a2, a3) == [[5, ['A042']], [3, ['A025', 'B004']]]

a1 = ['A043', 'B004', 'A025', 'A042', 'C025']
a2 = ['B009', 'B040', 'B003', 'A042', 'A027', 'A044']
a3 = ['A041', 'A026', 'B005']
id_best_users(a1, a2, a3) == []
As you can see the output will have the total number of purchases in decreasing order. If two users have the same amount of total purchases, they will be sorted by their id user string value.

"""
def id_best_users(*args):
    num_args = len(args)
    repeated_arg = []
    repeated_arg_dict = {}
    repeated_arg_set = []
    key_value_list = []
    result_arr = []
    
    for arg in args:
        for element in arg:
            repeated_arg.append(element)
            
    for arg in args:
        for i in set(arg):
            repeated_arg_set.append(i)

    
    print(f"repeated_arg_set = {repeated_arg_set}")
        

        
    for i in repeated_arg_set:
        
        i_frequency = repeated_arg.count(i)
        
        print(f"i_frequency = {i_frequency}")
        
        if (i_frequency >= num_args) and (i_frequency not in repeated_arg_dict) :
            repeated_arg_dict[i_frequency] = [i]
            
            while i in repeated_arg_set:
                repeated_arg_set.remove(i)
                
        elif (i_frequency >= num_args) and (i_frequency in repeated_arg_dict):
            repeated_arg_dict[i_frequency] += [i]
            while i in repeated_arg_set:
                repeated_arg_set.remove(i)
    
    print(repeated_arg_dict)    
    
    
    for i in repeated_arg_dict:
        key_value_list.append(i)
            
    key_value_list.sort(reverse = True)
    
    print(f"key_value_list = {key_value_list}")
     

    for i in key_value_list:
        result_arr.append([ i, sorted(repeated_arg_dict[i])] )
    return result_arr
        

        
