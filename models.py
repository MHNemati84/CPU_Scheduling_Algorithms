from typing import List

class Process:
    def __init__(self,pid,arrival_time,burst_time,remaining_time=None):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.remaining_time = remaining_time

    def __str__(self):
        return f"Process {self.pid}"
            
    