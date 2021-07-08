import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv("data1.csv")
df.plot(x="Depth", y="Magnitude", kind="scatter")

