t = int(input())


for i in range(t):
    n, b = input().strip().split()
    b = int(b)
    counter = 0
    n_b = 0
    b_arr = []
    one_case = False
    if b == 1:
        n_b = 10
        b_arr = [0,1,2,3,4,5,6,7,8,9]
        one_case = True
        print(n)
    elif b == 2:
        n_b = 5
        b_arr = [0,2,4,6,8]
    elif b == 3:
        n_b = 4
        b_arr = [0,3,6,9]
    elif b == 4:
        n_b = 3
        b_arr = [0,4,8]
    elif b < 10:
        n_b = 2
        b_arr = [0,b]
    else:
        print(0)
    cur_tree_level = 1
    greater_flag = False
    equals_final_len = False
    base_case = True
    for char in n:
        if greater_flag or equals_final_len:
            break
        gigachad_flag = False
        for i in range(len(b_arr)):
            if int(char) < b_arr[i]:
                counter += i*n_b**(len(n) - cur_tree_level)
                greater_flag = True
                base_case = False
                gigachad_flag = True
                break
            elif int(char) == b_arr[i]:
                base_case = False
                for j in range(0,i):
                    counter += n_b**(len(n) - cur_tree_level)
                if cur_tree_level == len(n):
                    counter += 1
                    equals_final_len = True
                cur_tree_level += 1
                gigachad_flag = True
                break
        if cur_tree_level > 1 and not gigachad_flag:
            counter += n_b**(len(n) - cur_tree_level + 1)
            greater_flag = True
        if base_case:
            counter = n_b**(len(n))
            break
    if not one_case: 
        print(counter-1)