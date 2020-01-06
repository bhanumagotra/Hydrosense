import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
discharge = pd.read_csv('trial.csv')
print(discharge.head())
plt.plot(discharge.Date,discharge.Q)
plt.show()