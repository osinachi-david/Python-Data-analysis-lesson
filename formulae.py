# function to calculate the median 
def calculateMedian(param):
    """ finds the middle number in the param"""
    noItems = len(param)
    sorted_items = sorted(param)
    midpoint = noItems // 2 # floor division 
    
    if noItems % 2 == 1:
        #if odd return the middle value
        return sorted_items[midpoint]
    else:
        #if even, return the average of the middle values 
        low = midpoint - 1
        high = midpoint
        return ( sorted_items[low] + sorted_items[high]) / 2

    
# function to calculate the mean 
def calculateMean(param):
    return sum(param) / len(param)
