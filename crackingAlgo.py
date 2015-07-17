def compress(word):
    """
     Check if previous character is the same as current character. If so,
     incement counter. If not, add previous character and it's counter to
     the retval. At the end print last character and it's counter.
    """
    compressed = ''
    prev = ''
    counter = 1
    
    for i in range (1,len(word)):
        prev = word[i-1]
        if word[i] == prev:
            counter += 1
            
        else:
            compressed += prev
            compressed += str(counter)
            prev = word[i]
            counter = 1
            
    compressed += prev
    compressed += str(counter)
    
    return compressed
   

print compress('aaabbccccddd')