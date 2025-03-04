def tower_hanoi(n, start, end): 
    # n >= 1
    # 1 <= start <= 3
    # 1 <= end <= 3
    # start != end
    """
    Prints the list of steps required to move n disks from the start rod to the end rod
    """
    if n == 1:
        pm(start, end)  
        
    else:
        other = 6 - (start + end)
        tower_hanoi(n - 1, start, other)
        pm(start, end)
        tower_hanoi(n - 1, other, end)
     
     
     
def pm(start, end):
    """
    Prints a move in the correct format
    """
    print(start, '-->', end)
    
    

tower_hanoi(2, 1, 2)