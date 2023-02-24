# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 11:07:09 2023

@author: Administrator
"""

from datetime import date
from datetime import datetime as dt
# =============================================================================
# Initialization
# =============================================================================
#Flow
dir_tar = 'D:\\Study\\PhD_Project\\NRC_toolbox\\Testing\\Input\\Flowrate_test.csv'
use_col_date = 3
use_col = 4
seed = 29

#Features
use_col_features=[5,6,7,8,9]
dir_features = 'D:\\Study\\PhD_Project\\NRC_toolbox\\Testing\\Input\\Weather_test.csv'
use_col_fea_date = 1

#Output
dir_output='D:\\Study\\PhD_Project\\NRC_toolbox\\Testing\\Results'

#Model parameters
RNN_avg_days = 6
time_step = 10
gap_days = 0
learning_rate = 2e-4
max_epochs = 10
batch_size = 4
validation_freq = 1
hidden_states = 50
dropout_rate = 0.1
constraint = 99
recurrent_type = 'LSTM'

today = date.today()
station = 'Test_'+dt.now().strftime("%Y-%m-%d %H-%M-%S")
train_startDate = '1997-01-01'
train_endDate = '1997-11-30'
test_startDate = '1997-12-01'
test_endDate = '1997-12-31'



