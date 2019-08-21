def mean(num_list):
    assert isinstance(num_list,list)
    try:
        return sum(num_list)/len(num_list)
    except ZeroDivisionError as detail:
        msg = ("The algebraic mean of an empty list is undefined. Please provide a list of numbers")

        raise ZeroDivisionError(detail.__str__() + "\n" + msg)
