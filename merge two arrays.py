def merge(arr1, arr2):
    final = []
    i = 0
    j = 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            final.append(arr1[i])
            i = i+1
        else:
            final.append(arr2[j])
            j = j+1
            
    while i < len(arr1):
        final.append(arr1[i])
        i = i+1
        
    while j < len(arr2):
        final.append(arr2[j])
        j = j+1
            
    return final
   
print(merge([0,2],[1])) 

            
    
        