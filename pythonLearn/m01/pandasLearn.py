import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

workout_dict = {
    "stockcode":[128111,127007,113013],
    "volumu":[30000,50000,60000],
    "type":["szse","szse","sse"]
}

workout = pd.DataFrame(workout_dict)
print(workout)
