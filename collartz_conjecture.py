print('collartz conjecture')

def collartz_conjecture(arr,number):
    num = number
    
    arr.append(num)
    if number == 1:
        print(arr)
        return 
    if number % 2 == 0:
        num = int(number / 2)
        collartz_conjecture(arr,num)
    else:
        num = (number * 3) + 1      
        collartz_conjecture(arr,num)
    
        
        
collartz_conjecture([],100)