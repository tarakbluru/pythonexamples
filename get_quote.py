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
import time
from datetime import date, timedelta
import pandas_datareader.data as web

def get_quote (symbol="INFY.NS", start='1/1/2017', end='2/1/2017', server='yahoo') :
    ohlcdata = web.DataReader (symbol, server, start, end)
    return ohlcdata;

def get_today_quote (symbol="INFY.NS", server='yahoo') :
    stoday = time.strftime("%d/%m/%Y")
    yesterday = date.today() - timedelta(1)
    syesterday = yesterday.strftime('%m%d%y')
    ohlcdata = get_quote (symbol, syesterday, stoday, server)
    return ohlcdata;

data = get_quote ("NTPC.NS", '1/1/2017', '17/3/2017', 'yahoo')
tdata = get_today_quote("NTPC.NS", 'yahoo')
tdata.info()

