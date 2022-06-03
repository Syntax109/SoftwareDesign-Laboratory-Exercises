def find_min_max(a_list):

    if a_list:
        head, *tail = a_list

        if tail:
            minimum, maximum = find_min_max(tail)

            return [head, minimum][minimum < head], [head, maximum][maximum > head]

        return head, head

    return a_list
a_list = [0,1,2,3,4,5,6,7,8,9,10,11,12]
print(find_min_max(a_list))
