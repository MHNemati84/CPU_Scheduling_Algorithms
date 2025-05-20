from utils import FCFS,SJF,RR
from models import Process
if __name__ == '__main__':
    """
        Process format : (PID,AT,BT,RT)  
        
        PID := Process ID
        AT := Arrival Time
        BT := Burst Time
        RT := Remaining Time(For RR)

       
        Output Format : (avg RT , avg. WT , avg. TAT)

        RT := Response Time
        WT := Waiting Time
        TAT := Turn-around Time

        
        All the outputs shown here have been tested manually.

    """

    # TestCase 1
    P1 = Process(1,0,10,10)
    P2 = Process(2,1,5,5)
    P3 = Process(3,2,8,8)

    print("FCFS for test 1: ",FCFS([P1,P2,P3]))
    print("SJF for test 1: ",SJF([P1,P2,P3]))
    print("RR for test 1: ",RR([P1,P2,P3],4))
    print()

    # TestCase 2
    P1 = Process(1,2,6,6)
    P2 = Process(2,5,2,2)
    P3 = Process(3,8,4,4)

    print("FCFS for test 2: ",FCFS([P1,P2,P3]))
    print("SJF for test 2: ",SJF([P1,P2,P3]))
    print("RR for test 2: ",RR([P1,P2,P3],2))
    print()

    # TestCase 3
    P1 = Process(1,0,4,4)
    P2 = Process(2,1,3,3)
    P3 = Process(3,2,1,1)
    P4 = Process(4,3,2,2)

    print("FCFS for test 3: ", FCFS([P1,P2,P3,P4]))
    print("SJF for test 3: ", SJF([P1,P2,P3,P4]))
    print("RR for test 3: ", RR([P1,P2,P3,P4],2))
    print()

    # TestCase 4
    P1 = Process(1,0,3,3)
    P2 = Process(2,2,6,6)
    P3 = Process(3,4,4,4)
    P4 = Process(4,6,5,5)
    P5 = Process(5,8,2,2)

    print("FCFS for test 4: ",FCFS([P1,P2,P3,P4,P5]))
    print("SJF for test 4: ",SJF([P1,P2,P3,P4,P5]))
    print("RR for test 4: ",RR([P1,P2,P3,P4,P5],3))
    print()

    # TestCase 5
    P1 = Process(1,0,5,5)
    print("FCFS for test 5: ",FCFS([P1]))
    print("SJF for test 5: ",SJF([P1]))
    print("RR for test 5: ",RR([P1],2))
    print()


    # TestCase 6
    P1 = Process(1,0,4,4)
    P2 = Process(2,0,6,6)
    print("FCFS for test 6: ",FCFS([P1,P2]))
    print("SJF for test 6: ",SJF([P1,P2]))
    print("RR for test 6: ",RR([P1,P2],2))
    print()

    # TestCase 7
    P1 = Process(1,0,8,8)
    P2 = Process(2,1,4,4)
    P3 = Process(3,2,9,9)
    P4 = Process(4,3,5,5)
    print("FCFS for test 7: ",FCFS([P1,P2,P3,P4]))
    print("SJF for test 7: ",SJF([P1,P2,P3,P4]))
    print("RR for test 7: ",RR([P1,P2,P3,P4],3))
    print()


    # TestCase 8
    P1 = Process(1,0,10,10)
    P2 = Process(2,2,3,3)
    P3 = Process(3,4,7,7)
    P4 = Process(4,6,5,5)
    P5 = Process(5,7,2,2)
    P6 = Process(6,9,8,8)

    print("FCFS for test 8: ",FCFS([P1,P2,P3,P4,P5,P6]))
    print("SJF for test 8: ",SJF([P1,P2,P3,P4,P5,P6]))
    print("RR for test 8: ",RR([P1,P2,P3,P4,P5,P6],4))
    print()





