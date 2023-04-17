import numpy as np
import pandas as pd

import matplotlib as mpl
import matplotlib.pyplot as plt 

import seaborn as sns
import seaborn.objects as so 

sns.set_theme(style="darkgrid")

data = pd.read_csv("./AISurvey.csv")
penguins = sns.load_dataset("penguins")

"""
fig, ax = plt.subplots()

sns.histplot(data, x="SentienceLimitA", discrete=True, color="blue", kde=True, ax=ax, label="Before")
sns.histplot(data, x="SentienceLimitB", discrete=True, color="red", kde=True, ax=ax, label="After")
"""



g = sns.JointGrid(data=data, x="DetrimentalB", y="AcceptedB")
g.plot_joint(sns.regplot)
g.plot_marginals(sns.boxplot)


#plt.legend()
plt.show()