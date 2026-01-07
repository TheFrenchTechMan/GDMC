def tuples_to_dict(l):
    return {k: v for k, v in list(zip(l[::2], l[1::2]))}
    #return list(zip(l[::2], l[1::2]))