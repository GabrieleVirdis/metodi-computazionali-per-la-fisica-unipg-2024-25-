import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class hit():

    def __init__(self, mod_id, det_id, hit_time):
        self.mod_id=mod_id
        self.det_id=det_id
        self.hit_time=hit_time

    def __lt__(self, other):
        return self.hit_time < other.hit_time

    def __sub__(self, other):
        return self.hit_time - other.hit_time

    def __repr__(self):
        return f"Hit(hit_time={self.hit_time})"

class Event():

    def __init__(self, num, t_1, t_2, dt, alls):
         self.num=num
         self.t_1=t_1
         self.t_2=t_2
         self.dt=dt
         self.alls=alls
