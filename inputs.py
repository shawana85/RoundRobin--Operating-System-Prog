

#Input for First Come First Serve Scheduling 
processes_fcfs = [1,2,3,4]
burst_time_fcfs = [5, 3, 8, 6]

#Input for Shortest Job First Scheduling ([process],[AT],[BT])
ain_sjf = [[1,1,21,4], 
           [2,2,3,4], 
           [3,3,6,4],
           [4,4,2,4]]

for i in range(4):
    ain_sjf.append([0]*len(ain_sjf[1]))
    

#Input for Round Robin Scheduling 
process_rrb = [1,2,3,4]
burst_time_rrb = [5, 4, 2, 1] 



#Input for Priority Round Robin Scheduling 
#              (P,BT,Priority)
process_prr = [[1, 4, 3],
               [2, 5, 2],
               [3, 8, 2],
               [4, 7, 1],
               [5, 3, 3]]







