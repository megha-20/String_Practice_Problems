# Function to find all occurrences of a pattern of length m
# in given text of length n

def find(text,pattern):
    t = len(text)
    p = len(pattern)

    i = 0
    while i <= t-p:
        for j in range(len(p)):
            if text[i+j] is not pattern[j]:
                break

            if j == m-1:
                print("Pattern occurs with shift",i)

        i = i+1
                
# Program to demonstrate Naive Pattern Matching Algorithm in Python
text = "ABCABAABCABAC"
pattern = "CAB"

find(text,pattern)
