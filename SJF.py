def findWaitingTime(processes, n, bt, wt): 
    wt[0] = 0 
    for i in range(1, n ): 
        wt[i] = bt[i - 1] + wt[i - 1] 
 
def findTurnAroundTime(processes, n, bt, wt, tat): 
    for i in range(n): 
        tat[i] = bt[i] + wt[i] 

def findavgTime(processes, n, bt): 

    wt = [0] * n 
    tat = [0] * n 
    total_wt = 0
    total_tat = 0

    findWaitingTime(processes,  n, bt, wt) 
    findTurnAroundTime(processes, n,bt, wt, tat) 

    print( "Processes Burst time " +" Waiting time " +" Turn around time") 
    for i in range(n): 
        total_wt = total_wt + wt[i] 
        total_tat = total_tat + tat[i] 
        print(" " + str(i + 1) + "\t\t" +str(bt[i]) + "\t " +str(wt[i]) + "\t\t " +str(tat[i])) 

    print( "Average waiting time = "+str(total_wt / n)) 
    print("Average turn around time = "+str(total_tat / n)) 

# Main Fucntion 
if __name__ =="__main__": 
    print("Enter the number of processes: ")
    n=int(input())
    processes=[]
    burst_time=[]
    for i in range(n):
        processes.insert(i,i+1)
    print("Enter burst time of all processes (seperate inputs by a space): ")
    burst_time=list(map(int, input().split()))
    for i in range(n):
        for j in range(n-i-1):
            if(burst_time[j]>burst_time[j+1]):
                temp=burst_time[j]
                burst_time[j]=burst_time[j+1]
                burst_time[j+1]=temp

    findavgTime(processes, n, burst_time) 
