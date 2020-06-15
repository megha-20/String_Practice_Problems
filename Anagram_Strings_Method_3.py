# Function to check if X and Y are anagrams or not
def isAnagram(X,Y):

    # if X's length is not same as Y's, they can't be anagram
    if len(X) != len(Y):
        return False

    # create an empty dict for X and Y
    freqx = {}
    freqy = {}

    # maintain count of each character of X in the dict
    for i in range(len(X)):
        freqx[X[i]] = freqx.get(X[i],0)+1

    # maintain count of each character of Y in the dict
    for i in range(len(Y)):
        freqy[Y[i]] = freqy.get(Y[i],0)+1

    # return true if both dict has same content
    return freqx == freqy
        


if __name__ == '__main__':

    X = input()
    Y = input()

    if isAnagram(X,Y):
        print("Anagram")

    else:
        print("Not an Anagram")
