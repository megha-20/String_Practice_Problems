# Function to check if X and Y are anagrams or not
def isAnagram(X,Y):

    # if X's length is not same as Y's, they can't be anagram
    if len(X) != len(Y):
        return False

    # sort the given strings X and Y 
    x1 = ''.join(sorted(X))
    y1 = ''.join(sorted(Y))

    # if the strings are equal after sorting, then they are anagrams 
    if x1 == y1:
        return True 
        
    else:
        return False
    
    
if __name__ == '__main__':
    
    X = input()
    Y = input()
    
    if isAnagram(X,Y):
        print("Anagram")
        
    else:
        print("Not an Anagram")
