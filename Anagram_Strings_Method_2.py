# Function to check if X and Y are anagrams or not
def isAnagram(X,Y):

    # if X's length is not same as Y's, they can't be anagram
    if len(X) != len(Y):
        return False

    # create an empty dict
    freq = {}

    # maintain count of each character of X in the dict
    for i in range(len(X)):
        freq[X[i]] = freq.get(X[i],0)+1

    # do for each character of Y
    for i in range(len(Y)):

        # if y is found not in dict i.e. either y is not present
	# in X or has more occurrences in Y
        if Y[i] not in freq:
            return False

        # decrease the frequency of y in the dict
        freq[Y[i]] = freq[y[i]]-1

        # if its frequency become 0, erase it from dict
        if freq[Y[i]] == 0:
            del freq[y[i]]

    # return true if dict becomes empty
    return not freq


if __name__ == '__main__':

    X = input()
    Y = input()

    if isAnagram(X,Y):
        print("Anagram")

    else:
        print("Not an Anagram")
