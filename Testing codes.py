# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 11:07:09 2023

@author: Administrator
"""

from datetime import date,timedelta
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

today = date.today()
param_dict = {
        #Ordinary parameters
        #flow
        'dir_tar_flow': 'D:\\MyFile\\MineDataFlow.csv',#2. Address of the flow rate target 
        'use_col_flow': 2,#4. Flowrate use column, exclude date column
        'use_col_flow_date': 1,#6. Datetime column of target
        #conc
        #'dir_tar_conc': 'D:\\MyFile\\MineDataConc.csv',#*. Address of the concentration target
        #'use_col_conc': 2,#4. Target use column, exclude date column
        #'use_col_conc_date': 1,#6. Datetime column of target
        
        #common
        'dir_features': 'D:\\MyFile\\MineDataFeatures.csv',#1. Address of input features
        'use_col_features': '2, 3, 4',#3. Features use columns, exclude date column, should be a list[] 
        'use_col_fea_date': 1,#5. Datetime column of features
        #'flowrate_threshold': 1.8,#7. Flow rate threshold for spring freshet
        'train_startDate': (today-timedelta(days=365)).strftime('%Y/%m/%d'),#8. Date when training set starts 
        'train_endDate': (today-timedelta(days=30)).strftime('%Y/%m/%d'),#8. Date when training set ends
        'test_startDate': (today-timedelta(days=30)).strftime('%Y/%m/%d'),#9. Date when test set starts
        'test_endDate': today.strftime('%Y/%m/%d'),#10. Date when test set ends
        'dir_output': 'D:\\MyFile\\MineData\\Output',#11. Output file directory
        'train_mode_flow': 'manual',#12. Training model selection: automatic (0) VS manual (1)
        'station': 'Station_1_trial_1',#13. Station name
        
        #Advanced parameters
        #flow
        'RNN_avg_days_flow': 6, #Flow rate/concentration average days
        'time_step_flow': 10, #Time step for LSTM/GRU
        'gap_days_flow': 0, #gap days between the end of input date and the target date
        'learning_rate_flow': 2e-4, #Learning rate in Adam optimizer
        'recurrent_type_flow': 'LSTM', #RNN type; 0 for LSTM and 1 for GRU; by default: 0
        'hidden_states_flow': 50, #No. of hidden states
        'dropout_rate_flow': 0.1, #Recurrent dropout rate
        'constraint_flow': 99, #Max_norm constraint
        'batch_size_flow': 4, #Batch size
        'max_epochs_flow': 100, #Max epoches
        'best_epoch': 0, #0 as initial value
        #conc
        
        
        #common
        'validation_freq': 1,#Validation frequency
        #'tree_avg_days': 1, #SF average days
        'seed': 29#Random seed
        }

class test_class:
    x=0
    def __init__(self):
        self.x += 1
        print(self.x)
    
    def test_func(self):
        self.x += 1
        print(self.x)
        return self.x

class test_class_2(test_class):
    x = 100
    def __init__(self):
        temp = self.test_func()
        print(temp)