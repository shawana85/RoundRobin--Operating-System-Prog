#importing Queue module
import queue
from inputs import processes_fcfs, burst_time_fcfs

def findWaitingTime(queue_data, n, bt, wt):

    # first process is 0 
    wt[0] = 0

    for i in range(1, n ):
        wt[i] = (bt[i - 1] + wt[i - 1])

# Function to calculate turn around time
def findTurnAroundTime(queue_data, n, bt, wt, tat):

    for i in range(n):
        tat.put(bt[i] + wt[i])

# Function to calculate average time
def findavgTime(queue_data, n, bt):

    wt = [0] * n
    tat = queue.Queue(maxsize=n)
    total_wt = 0
    total_tat = 0

    findWaitingTime(queue_data, n, bt, wt)

    findTurnAroundTime(queue_data, n, bt, wt, tat)

    print( "Processes Burst time " +
                " Waiting time " +
                " Turn around time" + "   Response Time ")

    # Calculate total waiting time and total turn around time
    for i in range(n):
            tat_ref = tat.get()
            total_wt = total_wt + wt[i]
            total_tat = total_tat + tat_ref
            print(" " + str(i + 1) + "\t\t\t" +
                  str(bt[i]) + "\t\t\t " +
                  str(wt[i]) + "\t\t\t " +
                  str(tat_ref) + "\t\t\t\t\t " + str(wt[i]))
            if i == n-1 :
                print( "Average waiting time = "+str(total_wt / n))
                print("Average turn around time = "+str(total_tat / n))

# Driver code
if __name__ =="__main__":
    
        processes = processes_fcfs
        burst_time = burst_time_fcfs
        queue_data = queue.Queue(maxsize=6)
        for i in processes:
                queue_data.put(i)
        n = queue_data.qsize()
        findavgTime(queue_data, n, burst_time)
