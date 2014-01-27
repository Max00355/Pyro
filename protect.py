import hashlib

def protect(string):
    salt = "1asd;;|1::A21;'aASd11231aASdklkjllk1llk12l3jklff))DS001K1KL12askjk1l3123jj123jjl123jlj12j3j123klkjjkJj17&!&*!(#(*#%&%*#(%((#%(((||}|{}{}#%{}{}#{}{}#%{{}3"
    for x in range(100):
        string = hashlib.sha512(string+salt).hexdigest()

    return string
        
