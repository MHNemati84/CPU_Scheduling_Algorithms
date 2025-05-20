from utils import SJF,FCFS,RR
from CPU_Scheduling_Algorithms.models import Process
from typing import List

mapping = {
    "SJF":SJF,
    "FCFS":FCFS,
    "RR":RR
}

def test_alg(alg_name : str , processes : List[Process] 
             , expected_output : List[float]
             , time_quantum : int = 0):
    
    if alg_name == "RR":
        results = mapping[alg_name](processes,time_quantum)
    else:
        results = mapping[alg_name](processes)

    for res , expected in zip(results , expected_output):
        if res != expected:
            return False
    return True

def run_test_case(test_case:str,processes : List[Process]
                 ,expected_fcfs : List[float],expected_sjf : List[float]
                 ,expected_rr : List[float],time_quantum : int = 0):
    
    condition = (not test_alg("FCFS",processes,expected_fcfs)
                 or not test_alg("SJF",processes,expected_sjf)
                 or not test_alg("RR",processes,expected_rr,time_quantum))
    if condition :
        print(f"-->Test Case {test_case} failed")
    else:
        print(f"-->Test Case {test_case} Passed")

    
    
