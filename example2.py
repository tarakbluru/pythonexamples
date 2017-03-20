# 
# ********************************************************************************
# The MIT License (MIT)
# Copyright (c) 2016 Tarakeshwar NC 
# Permission is hereby granted, free of charge, to any person obtaining a copy of 
# this software and associated documentation files (the "Software"), to deal in 
# the Software without restriction, including without limitation the rights to 
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of 
# the Software, and to permit persons to whom the Software is furnished to do so, 
# subject to the following conditions:
# The above copyright notice and this permission notice shall be included in all 
# copies or substantial portions of the Software.
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR 
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE 
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER 
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, 
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE 
# SOFTWARE.
# *******************************************************************************
#
#
# *******************************************************************************
# getquote.py - Gets OHLC data from server  
# Note: Date in DD/MM/YEAR format
# *******************************************************************************
# 
#!/usr/bin/python
import numpy as np
import pandas as pd
import matplotlib

import matplotlib.pyplot as plt
import get_quote

plt.ion()


def process_symbol (line) :
    #data=get_quote.get_quote("AUROPHARMA.NS",'1/1/2005', '18/3/2017')
    #data=get_quote.get_quote("INFY.NS",'1/1/2010', '18/3/2017')
    #data=get_quote.get_quote("GOLDBEES.NS",'1/1/2005', '18/3/2017')
    data=get_quote.get_quote(line,'1/1/2005', '18/3/2017')
    
    #data['Close'].plot(grid=True, figsize=(8, 5))
    
    data['42d'] = np.round(pd.rolling_mean(data['Close'], window=42), 2)
    data['252d'] = np.round(pd.rolling_mean(data['Close'], window=252), 2)
    data[['Close', '42d', '252d']].tail()
    #data[['Close', '42d', '252d']].plot(grid=True, figsize=(8, 5))
    
    data['42-252'] = data['42d'] - data['252d']
    data['42-252'].tail()
    SD = 20
    data['Regime'] = np.where(data['42-252'] > SD, 1, 0)
    data['Regime'] = np.where(data['42-252'] < -SD, -1, data['Regime'])
    data['Regime'].value_counts()

    figura = plt.figure(1)    
    data['Regime'].plot(lw=1.5)
    plt.ylim([-1.1, 1.1])
    plt.xlim(['1/1/2005', '1/12/2018'])
#    while True:
#        if plt.waitforbuttonpress():
#            break
    while True:
       if plt.waitforbuttonpress():
            break  
    plt.close(figura)
    #==============================================================================
    # data['Market'] = np.log(data['Close'] / data['Close'].shift(1))
    # data['Strategy'] = data['Regime'].shift(1) * data['Market']
    # data[['Market', 'Strategy']].cumsum().apply(np.exp).plot(grid=True,figsize=(8, 5))
    #==============================================================================
    return

skip = True

with open('nifty_50.txt') as f:
    for line in f:
        print "Read..", line
        if ('#' in line) :
            continue
        line = line.rstrip('\n')
        if line == "MARICO" :
            skip = False
        if skip :
            print "skipping ", line, "\n"
            continue
        line += ".NS"
        print "Processing", line
        process_symbol (line)
        


