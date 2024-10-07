def strobo(string):
    dict = {
        "0": "0",
        "1": "1",
        "8": "8",
        "6": "9",
        "9": "6"
    }
    
    left = 0
    right = len(string) - 1
    
    if left == right:
        return string
        
    while left <= right:
        if string[left] in dict:
            if dict[string[left]] == string[right]:
                left += 1
                right -= 1
        else:
            return False
    
    return True
    
    
    
print(strobo("69"))
    