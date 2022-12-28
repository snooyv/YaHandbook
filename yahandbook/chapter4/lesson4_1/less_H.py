# А роза упала на лапу Азора 7.0

def is_palindrome(any_obj):
    if get_instance(any_obj):
        return is_list_or_tuple(any_obj)

    return is_num_or_string(any_obj)


def get_instance(any_obj):
    if isinstance(any_obj, list) or isinstance(any_obj, tuple):
        return True

    return False


def is_list_or_tuple(any_obj):

    return True if any_obj == any_obj[::-1] else False


def is_num_or_string(any_obj):

    return True if str(any_obj) == str(any_obj)[::-1] else False


# result = is_palindrome(123)
# result1 = is_palindrome('121')
# result2 = is_palindrome([1, 2, 1, 2, 1])
# result3 = is_palindrome("mama")

# print(result)
# print(result1)
# print(result2)
# print(result3)



