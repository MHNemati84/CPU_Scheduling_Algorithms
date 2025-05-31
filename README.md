# CPU Scheduling Algorithms 

In this Mini-Project , Three of the most common CPU Scheduling Algorithms - namely, **FCFS** (First-Come First-Serve)
,**SJF**(Shortest Job First) and **Round-Robin** have been implemented along with their associated performance metrics
such as **Avg. Response Time**, **Avg. Waiting Time** and **Avg. Turn-around Time** so that each of the schedulers returns
a tuple `(avg_rt,avg_wt,avg_tat)` indicating the performance of the scheduler for a given Workload.

To see the output associated with each testcase in the `main.py`, Simply run `python3 main.py` or `python main.py` on the console.

**Note: The outputs produced for the 8 testcases have all been manually tested**

**Example.**
```In:
# TestCase 2
P1 = Process(1,2,6,6)
P2 = Process(2,5,2,2)
P3 = Process(3,8,4,4)
```

```Out:
FCFS for test 2 : (1.67,1.67,5.67)
SJF for test 2 : (1.67,1.67,5.67)
RR for test 2 : (1.0,1.67,5.67)
```
