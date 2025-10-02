def is_valid_naive(n):
    n_str = str(n)
    l= len(n_str)
    if l==4:
        return True 
    else:
        return False# for 4 digit password"



def is_valid(n):
    result = True
    n_str=str(n)
    if len(n_str)!=4:
        return False
        return result
    n_list= list(n_str)
    n_set=set(n_list)
    if len(n_set)==1:
        result= False
        return result

    for d in range(len(n_list)):
       if int(n_list[d]) in int(n_list[i+i])+1:
            break
            result=False
    return False

    for d in range(len(n_list)):
       if int(n_list[d]) in int(n_list[i+i])-1:
            break
            result=False
    return False

return True

print(is_valid(2222))