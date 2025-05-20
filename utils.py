from typing import List
from models import Process

"""
    RT := Response Time
    WT := Waiting Time
    TAT := Turn-around Time
    
    Output := (avg. RT, avg. WT, avg. TAT)
"""


def FCFS(ready_queue : List[Process]) -> List[float]:
    """
    In FCFS, Processes are chosen from the ready queue
        based on their arrival time and in case of a tie,
        the process appearing first in the queue will be 
        chosen. 
        
        Since ready queue is a queue we do not need to loop through 
        its elements to find the one with the lowest arrival time.

        Turnaround Time = Waiting Time + Burst Time(In general)
        In FCFS : Waiting Time = Response Time
        So we do not need to keep a separate response time for the 
        processes.
                  
    """
    n = len(ready_queue)

    process_order = []
    waiting_time = []
    turnaround_time = []

    curr_time = 0
    while ready_queue:
        min_process = ready_queue[0]
        curr_time = max(curr_time,min_process.arrival_time)
    
        process_order.append(str(min_process))
        waiting_time.append(curr_time - min_process.arrival_time)
        turnaround_time.append(curr_time + min_process.burst_time - min_process.arrival_time)
        
        ready_queue.remove(min_process)

        curr_time += min_process.burst_time
        

    avg_wt = round(sum(waiting_time) / n,2)
    avg_rt = avg_wt
    avg_tat = round(sum(turnaround_time) / n,2)

    return (avg_wt,avg_rt,avg_tat)

def SJF(ready_queue : List[Process]) -> List[float]:
    """
    In SJF, processes are selected from the ready queue
        based on CPU burst. Processes with shorter CPU bursts
        are selected first. In case of a tie, we break ties with 
        Arrival Time.
        
        One thing to look out for in SJF is that the process with 
        shortest CPU burst should be selected among the arrived 
        processes.

        In non-preemptive SJF just like FCFS : Response Time = Waiting Time
    """
    n = len(ready_queue)
    process_order = []
    waiting_time = []
    turnaround_time = []

    curr_time = 0
    while ready_queue:
        min_arrival = ready_queue[0].arrival_time
        min_process = ready_queue[0]
        current_process = ready_queue[0]
        curr_time = max(curr_time,min_arrival)
        cnt = 0
        while ((current_process.arrival_time == min_arrival)
               and cnt < len(ready_queue) - 1):
            if current_process.burst_time < min_process.burst_time:
                    min_process = current_process
            cnt += 1
            current_process = ready_queue[cnt]

        process_order.append(str(min_process))
        waiting_time.append(curr_time - min_arrival)
        turnaround_time.append(curr_time + min_process.burst_time - min_arrival)

        ready_queue.remove(min_process)
        curr_time += min_process.burst_time


    avg_wt = round(sum(waiting_time) / n , 2)
    avg_rt = avg_wt
    avg_tat = round(sum(turnaround_time) / n , 2)

    return (avg_wt,avg_rt,avg_tat)



def RR(processes : List[Process], time_quantum : int) -> List[float]:
    
    n = len(processes)
    process_order = []
    running_time = {process : 0 for process in processes}
    waiting_time = []
    response_time = {str(process) : None for process in processes}
    turnaround_time = []

    ready_queue = [processes.pop(0)]
    curr_time = ready_queue[0].arrival_time

    while ready_queue:
        curr_process = ready_queue.pop(0)
        process_order.append(str(curr_process))
        if response_time[str(curr_process)] is None:
            response_time[str(curr_process)] = curr_time - curr_process.arrival_time
        if curr_process.remaining_time <= time_quantum:
            curr_time += curr_process.remaining_time
            running_time[curr_process] += curr_process.remaining_time
            curr_process.remaining_time = 0

            turnaround_time.append(curr_time - curr_process.arrival_time)
            waiting_time.append(curr_time - curr_process.arrival_time - running_time[curr_process])

            while processes and processes[0].arrival_time <= curr_time:
                ready_queue.append(processes.pop(0))
            
            
        else:
            curr_time += time_quantum
            curr_process.remaining_time -= time_quantum
            running_time[curr_process] += time_quantum

            while processes and processes[0].arrival_time <= curr_time:
                ready_queue.append(processes.pop(0))
            ready_queue.append(curr_process)
            
    
    avg_wt = round(sum(waiting_time) / n,2)
    avg_rt = round(sum(response_time.values()) / n,2)
    avg_tat = round(sum(turnaround_time) / n,2)

    return (avg_rt,avg_wt,avg_tat)

            

    