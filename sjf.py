import queue
from inputs import ain_sjf

def arrangeArrival(n, array):
    for i in range(0, n):
        for j in range(i, n-i-1):
            if array[1][j] > array[1][j+1]:
                for k in range(0, n):
                    array[k][j], array[k][j+1] = array[k][j+1], array[k][j]
  
  
def CompletionTime(n, array):
    value = 0
    array[3][0] = array[1][0] + array[2][0]
    array[5][0] = array[3][0] - array[1][0]
    array[4][0] = array[5][0] - array[2][0]
    for i in range(1, n):
        temp = array[3][i-1]
        mini = array[2][i]
        for j in range(i, n):
            if temp >= array[1][j] and mini >= array[2][j]:
                mini = array[2][j]
                value = j
        array[3][value] = temp + array[2][value]
        array[5][value] = array[3][value] - array[1][value]
        array[4][value] = array[5][value] - array[2][value]
        for k in range(0, 6):
            array[k][value], array[k][i] = array[k][i], array[k][value]
  
  
if __name__ == '__main__':
    n = 4
    arr = ain_sjf
    arrangeArrival(n, arr)
    CompletionTime(n, arr)
    print ("{:<8}   {:<15}  {:<15}{:<15}{:<15}{:<15}".format('Processes','Arrival','Burst','Completion','Waiting','Turnaround'))
    
    waitingtime = 0
    turaroundtime = 0
    for i in range(0, n):
        print ("{:<15}{:<15}{:<15}{:<15}{:<15}{:<15}".format(arr[0][i],arr[1][i],arr[2][i],
               arr[3][i],arr[4][i],arr[5][i]))
        waitingtime += arr[4][i]
        turaroundtime += arr[5][i]
    print("Average waiting time is ", (waitingtime/n))
    print("Average Turnaround Time is  ", (turaroundtime/n))