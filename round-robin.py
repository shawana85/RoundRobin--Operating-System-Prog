#importing Queue module
import queue
from inputs import process_rrb, burst_time_rrb

def process_wait_time(processes, n, burst_time, 
                         wait_time, quantum): 
  
    rem_bt = burst_time.copy()
    t = 0
    
    while(1):
        done = True
        for i in range(n):
            
            if (rem_bt[i] > 0) :
                done = False 
                  
                if (rem_bt[i] > quantum) :
                  
                    t += quantum 
                    rem_bt[i] -= quantum
                    
                else:

                    t = t + rem_bt[i] 
  
                    wait_time.put(t - burst_time[i])
  
                    rem_bt[i] = 0
                    
                  
        # If all processes are done 
        if (done == True):
            break
# Function to calculate turn around time
def process_turn_around_time(processes, n, burst_time,
                                wait_time, turn_arnd_time):
    # Calculating turnaround time 
    for i in range(n):

        wait_ref = wait_time.get()
        turn_arnd_time.put( burst_time[i] + wait_ref )
        wait_time.put(wait_ref)

def all_avg_time(processes, n, burst_time, quantum): 
    wait_time = queue.Queue(maxsize=n)
    turn_arnd_time = queue.Queue(maxsize=n)
    
  
    process_wait_time(processes, n, burst_time, wait_time, quantum) 
  
    process_turn_around_time(processes, n, burst_time, wait_time, turn_arnd_time) 
  
   # print("Processes    Burst Time     Waiting Time", 
    #                 "    Turn-Around Time     Response Time")
    print ("{:^15}{:^15}{:^15}{:^15} {:^15}".format('Processes','Burst Time','Waiting Time','Turn-Around_Time','Response Time'))
    total_wt = 0
    total_tat = 0
    resp_time = -2
    for i in range(n):
   
        wait_ref = wait_time.get()
        turn_ref = turn_arnd_time.get()
        
        total_wt = total_wt + wait_ref 
        total_tat = total_tat + turn_ref
        resp_time = resp_time + quantum
       # print(" ", i + 1, "\t\t", burst_time[i], 
        #      "\t\t\t\t", wait_ref, "\t\t\t\t\t", turn_ref, "\t\t\t\t\t", resp_time)
        print ("{:^15}{:^15}{:^15}{:^15}{:^15}".format( i + 1, burst_time[i],wait_ref,turn_ref,resp_time ))
        wait_time.put(wait_ref)
        turn_arnd_time.put(turn_ref)
  
    print("\nAverage waiting time = ",(total_wt /n) )
    print("Average turn around time = ", (total_tat / n)) 



if __name__ =="__main__":
      
    # Process id's 
    process = process_rrb
    n = len(process)
  
    # Burst time of all processes 
    burst_time = burst_time_rrb
  
    # Time quantum 
    quantum = 2; 
    all_avg_time(process, n, burst_time, quantum)








    
