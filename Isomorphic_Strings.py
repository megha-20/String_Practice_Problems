# Find if X and Y are Isomorphic or not
def IsIsomorphic(X,Y):

    # if X and Y have different lengths, they cannot be Isomorphic
    if len(X) != len(Y):
        return False
    
    # use dict to store mapping from characters of X to Y
    dict = {}
    
    # use set to store pool of already mapped characters
    s = set()

    
    for i in range(len(X)):
        x = X[i]
        y = Y[i]
        
        # if x is seen before
        if x in dict:

            # return false if first occurrence of x is mapped to different character
            if dict[x] != y:
                return False

        # if x is seen for the first time (i.e. it is not mapped yet)
        else:
            # return false if y is already mapped to some other in X
            if y in s:
                return False
            
            # dict y to x and mark it mapped
            dict[x] = y
            s.add(y)

    return True

    
if __name__ == '__main__':
    
    X = 'ACAB'
    Y = 'XCXY'

    if IsIsomorphic(X,Y):
        print(X,"and",Y,"are Isomorphic Strings")

    else:
        print(X,"and",Y,"are not Isomorphic Strings")

        

    
