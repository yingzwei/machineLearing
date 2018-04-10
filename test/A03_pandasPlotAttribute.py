'''
Created on 2018å¹?1æœ?15æ—?

@author: Administrator
'''
import pandas as pd
import pylab
import scipy.stats as sta


url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/undocumented/connectionist-bench/sonar/sonar.all-data'

data = pd.read_csv(url,header=None,prefix= 'V')
print(data.tail())
print(data.describe())  # ç»Ÿè®¡dataFrameä¸­å‡å€¼ã?æ ‡å‡†åå·®ã?æœ€å°å?¼ã??4ç™¾åˆ†ä½æ•°ã€æœ€å¤§å??
sta.probplot(data.iloc[:,3], dist='norm',plot =pylab)
pylab.show()