# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 09:41:34 2023

@author: Administrator
"""

import tkinter as tk
from tkinter import messagebox
from datetime import date, timedelta, datetime

#import os
import numpy as np
import pandas as pd
#import matplotlib.pyplot as plt
from sklearn.impute import SimpleImputer

#from sklearn.model_selection import GridSearchCV
#from sklearn.preprocessing import MinMaxScaler

# Constructing a RNN
#from tensorflow.keras.models import Sequential
#from tensorflow.keras.layers import Dense, LSTM, GRU
#from tensorflow.keras.constraints import max_norm
#import tensorflow as tf

#from tensorflow.keras.wrappers.scikit_learn import KerasRegressor
#from tensorflow.keras.callbacks import ModelCheckpoint

class Ordinary_input:
    def __init__(self, master, param_dict):
        self.master = master
        self.master.title('New Model Training Tool-General Settings')
        self.master.geometry('1000x700')
        
        self.param_dict = param_dict
        
        #Frames, different packing ways
        self.frm_left = tk.Frame(self.master)
        self.frm_right = tk.Frame(self.master)
        self.frm_bottom = tk.Frame(self.master)
        
        e_font = 12
        
        dft_e_1 = tk.StringVar(value=self.param_dict['dir_features'])#1. Address of input features
        dft_e_2 = tk.StringVar(value=self.param_dict['dir_tar_flow'])#2. Address of the flow rate target
        dft_e_3 = tk.StringVar(value=self.param_dict['use_col_features'])#3. Features use columns, exclude date column
        dft_e_4 = tk.StringVar(value=self.param_dict['use_col_flow'])#4. Target use column, exclude date column
        dft_e_5 = tk.StringVar(value=self.param_dict['use_col_fea_date'])#5. Datetime column of features
        dft_e_6 = tk.StringVar(value=self.param_dict['use_col_flow_date'])#6. Datetime column of target
        dft_e_7 = tk.StringVar(value=self.param_dict['flowrate_threshold'])#7. Flow rate threshold for spring freshet
        dft_e_8 = tk.StringVar(value=self.param_dict['train_startDate'])#8. Date when training set starts 
        dft_e_9 = tk.StringVar(value=self.param_dict['test_startDate'])#9. Date when test set starts
        dft_e_10 = tk.StringVar(value=self.param_dict['endDate'])#10. Date when test set ends
        dft_e_11 = tk.StringVar(value=self.param_dict['dir_output'])#11. Output file directory
        
        #12. Training model selection: automatic (0) VS manual (1)
        if self.param_dict['train_mode_flow'] == 'manual':
            self.dft_r_12 = tk.IntVar(value=1)
        elif self.param_dict['train_mode_flow'] == 'automatic':
            self.dft_r_12 = tk.IntVar(value=0)
        
        dft_e_13 = tk.StringVar(value=self.param_dict['station'])#13. Station name
        
        #Left
        #1. Address of input features
        var_L_1 = tk.StringVar()
        var_L_1.set('1. File address of input features:')
        self.Lab_1 = tk.Label(self.frm_left, textvariable=var_L_1, bg='white', 
                              font=('Times New Roman', 12), height=1).pack()
        self.e_1 = tk.Entry(self.frm_left, show="", width=40, font=e_font, textvariable=dft_e_1)
        self.e_1.pack()
        
        #3. Features use columns
        var_L_3 = tk.StringVar()
        var_L_3.set('3. The number of columns of input features (exclude date column):')
        self.Lab_3 = tk.Label(self.frm_left, textvariable=var_L_3, bg='white', 
                              font=('Times New Roman', 12), height=1).pack()
        self.e_3 = tk.Entry(self.frm_left, show="", width=20, font=e_font, textvariable=dft_e_3)
        self.e_3.pack()
        
        #5. Datetime column of features
        var_L_5 = tk.StringVar()
        var_L_5.set('5. The number of date column of input features:')
        self.Lab_5 = tk.Label(self.frm_left, textvariable=var_L_5, bg='white', 
                              font=('Times New Roman', 12), height=1).pack()
        self.e_5 = tk.Entry(self.frm_left, show="", width=10, font=e_font, textvariable=dft_e_5)
        self.e_5.pack()
        
        #7. Flow rate threshold for spring freshet
        var_L_7 = tk.StringVar()
        var_L_7.set('7. Flow rate threshold for spring freshet:')
        self.Lab_7 = tk.Label(self.frm_left, textvariable=var_L_7, bg='white', 
                              font=('Times New Roman', 12), height=1).pack()
        self.e_7 = tk.Entry(self.frm_left, show="", width=10, font=e_font, textvariable=dft_e_7)
        self.e_7.pack()
        
        #9. Date when test set starts
        var_L_9 = tk.StringVar()
        var_L_9.set('9. Date when test set starts:')
        self.Lab_9 = tk.Label(self.frm_left, textvariable=var_L_9, bg='white', 
                              font=('Times New Roman', 12), height=1).pack()
        self.e_9 = tk.Entry(self.frm_left, show="", width=10, font=e_font, textvariable=dft_e_9)
        self.e_9.pack()
        
        #11. Output file directory
        var_L_11 = tk.StringVar()
        var_L_11.set('11. Output file directory:')
        self.Lab_11 = tk.Label(self.frm_left, textvariable=var_L_11, bg='white', 
                              font=('Times New Roman', 12), height=1).pack()
        self.e_11 = tk.Entry(self.frm_left, show="", width=40, font=e_font, textvariable=dft_e_11)
        self.e_11.pack()
        
        #13. Station name
        var_L_13 = tk.StringVar()
        var_L_13.set('13. Please type in a name of the station/trail:')
        self.Lab_13 = tk.Label(self.frm_left, textvariable=var_L_13, bg='white', 
                              font=('Times New Roman', 12), height=1).pack()
        self.e_13 = tk.Entry(self.frm_left, show="", width=20, font=e_font, textvariable=dft_e_13)
        self.e_13.pack()
        
        
        
        #Right
        #2. Address of the target feature
        var_L_2 = tk.StringVar()
        var_L_2.set('2. File address of the flow rate target:')
        self.Lab_2 = tk.Label(self.frm_right, textvariable=var_L_2, bg='white', 
                              font=('Times New Roman', 12), height=1).pack()
        self.e_2 = tk.Entry(self.frm_right, show="", width=40, font=e_font, textvariable=dft_e_2)
        self.e_2.pack()
        
        #4. Target use column
        var_L_4 = tk.StringVar()
        var_L_4.set('4. The number of column of the flow rate target (exclude date column):')
        self.Lab_4 = tk.Label(self.frm_right, textvariable=var_L_4, bg='white', 
                              font=('Times New Roman', 12), height=1).pack()
        self.e_4 = tk.Entry(self.frm_right, show="", width=10, font=e_font, textvariable=dft_e_4)
        self.e_4.pack()
        
        #6. Datetime column of target
        var_L_6 = tk.StringVar()
        var_L_6.set('6. The number of date column of the flow rate target:')
        self.Lab_6 = tk.Label(self.frm_right, textvariable=var_L_6, bg='white', 
                              font=('Times New Roman', 12), height=1).pack()
        self.e_6 = tk.Entry(self.frm_right, show="", width=10, font=e_font, textvariable=dft_e_6)
        self.e_6.pack()
        
        #8. Date when training set start 
        var_L_8 = tk.StringVar()
        var_L_8.set('8. Date when training set starts:')
        self.Lab_8 = tk.Label(self.frm_right, textvariable=var_L_8, bg='white', 
                              font=('Times New Roman', 12), height=1).pack()
        self.e_8 = tk.Entry(self.frm_right, show="", width=10, font=e_font, textvariable=dft_e_8)
        self.e_8.pack()
        
        #10. Date when test set ends
        var_L_10 = tk.StringVar()
        var_L_10.set('10. Date when test set ends:')
        self.Lab_10 = tk.Label(self.frm_right, textvariable=var_L_10, bg='white', 
                              font=('Times New Roman', 12), height=1).pack()
        self.e_10 = tk.Entry(self.frm_right, show="", width=10, font=e_font, textvariable=dft_e_10)
        self.e_10.pack()
        
        #12. Training model selection: automatic (0) VS manual (1)
        self.var_L_12 = tk.StringVar()
        self.var_L_12.set('12. Training model selection: ')
        self.Lab_12 = tk.Label(self.frm_right, textvariable=self.var_L_12, bg='white', 
                              font=('Times New Roman', 12), height=1).pack()
        self.r_12_1 = tk.Radiobutton(self.frm_right, text='Automatic', variable=self.dft_r_12, value=0,
                    command=self.print_r_12_selection)#.place(x=130, y=705, anchor='nw')
        self.r_12_2 = tk.Radiobutton(self.frm_right, text='Manual', variable=self.dft_r_12, value=1,
                    command=self.print_r_12_selection)#.place(x=190, y=705, anchor='nw')
        self.r_12_1.pack()
        self.r_12_2.pack()
        
        
        
        #Bottom
        self.btn_advSet = tk.Button(self.frm_bottom, text = 'Advanced Settings', 
                                    width = 25, command = self.new_window).pack()
        
        self.btn_conf = tk.Button(self.frm_bottom, text = 'Confirm & Run', 
                                  width = 25, command = self.confirm_btn).pack()
        self.btn_quit = tk.Button(self.frm_bottom, text = 'Quit', width = 25, 
                                  command = self.close_windows).pack()
        
        self.frm_left.pack(side='left')
        self.frm_right.pack(side='right')
        self.frm_bottom.pack(side='bottom')
        
        return
    
    def print_r_12_selection(self):
        if self.dft_r_12.get() == 0:
            str_print = '12. Training model selection (Automatic mode):'
            messagebox.showinfo(title='Automatic mode selected', 
                                message=
'''By selecting automatic mode, it is about 
to take much longer time to find the best 
combination of hyperparameters. If you already 
know the best combination of them, please 
input them into 'advanced settings' and switch to 
'Manual' to save time.''')
        
        elif self.dft_r_12.get() == 1:
            str_print = '12. Training model selection (Manual mode):'
        
        self.var_L_12.set(str_print)
        return
    
    def new_window(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = Additional_input(self.newWindow, self.param_dict)
        return
    
    def confirm_btn(self):
        try:
            #load data to param_dict
            #flow
            self.param_dict['dir_tar_flow'] = str(self.e_2.get())
            self.param_dict['use_col_flow'] = int(self.e_4.get())
            self.param_dict['use_col_flow_date'] = int(self.e_6.get())
            
            #common
            self.param_dict['dir_features'] = str(self.e_1.get())
            self.param_dict['use_col_fea_date'] = int(self.e_5.get())
            self.param_dict['flowrate_threshold'] = float(self.e_7.get())
            
            #3. Features use columns, exclude date column
            use_col_fea = []
            str_use_col_fea = str(self.e_3.get())
            str_use_col_fea = str_use_col_fea.split(sep=',')
            
            for num in str_use_col_fea:
                use_col_fea.append(int(num.strip()))
            use_col_fea = list(set(use_col_fea))#Deduplication
            
            self.param_dict['use_col_features'] = use_col_fea
            
            #8-11
            self.param_dict['train_startDate'] = datetime.strptime(self.e_8.get(), '%Y/%m/%d').strftime('%Y/%m/%d')
            self.param_dict['test_startDate'] = datetime.strptime(self.e_9.get(), '%Y/%m/%d').strftime('%Y/%m/%d')
            self.param_dict['endDate'] = datetime.strptime(self.e_10.get(), '%Y/%m/%d').strftime('%Y/%m/%d')
            self.param_dict['dir_output'] = str(self.e_11.get())
            
            #12. Training model selection: automatic (0) VS manual (1)
            if self.dft_r_12 == 0:
                self.param_dict['train_mode_flow'] = 'auto'
            else:
                self.param_dict['train_mode_flow'] = 'manual'
            
            #13. Station name
            self.param_dict['station'] = str(self.e_13.get())
            
            messagebox.showinfo(title='All parameters updated', 
                                message='All parameters have been updated successfully.')
            
            self.app = model_main(self.param_dict)
        except Exception as ex:
            messagebox.showerror(title='Failed to update ordinary parameters', message=ex)
            return
        return
    
    def close_windows(self):
        self.master.destroy()
        return

class Additional_input:
    def __init__(self, master, param_dict):
        self.master = master
        self.param_dict = param_dict
        
        self.frm_left = tk.Frame(self.master)
        self.frm_right = tk.Frame(self.master)
        self.frm_bottom = tk.Frame(self.master)
        
        self.master.title('New Model Training Tool-Advanced Settings')
        self.master.geometry('580x800')
        
        self.frm_left.pack(side='left')
        self.frm_right.pack(side='right')
        self.frm_bottom.pack(side='bottom')
        
        #Default values of additional input
        #common
        dft_e_1 = tk.IntVar(value=self.param_dict['tree_avg_days'])#SF average days
        dft_e_5 = tk.IntVar(value=self.param_dict['seed'])#Random seed
        dft_e_13 = tk.IntVar(value=self.param_dict['validation_freq'])#Validation frequency
        
        #flow
        dft_e_2 = tk.IntVar(value=self.param_dict['RNN_avg_days_flow'])#Flow rate/concentration average days
        dft_e_3 = tk.IntVar(value=self.param_dict['time_step_flow'])#Time step for LSTM/GRU
        dft_e_4 = tk.IntVar(value=self.param_dict['gap_days_flow'])#gap days between the end of input date and the target date
        dft_e_6 = tk.StringVar(value=str(self.param_dict['learning_rate_flow']))#Learning rate in Adam optimizer
        if self.param_dict['recurrent_type_flow'] == 'GRU':#RNN type; 0 for LSTM and 1 for GRU; by default: 0
            self.dft_r_7 = tk.IntVar(value=1)
        else:
            self.dft_r_7 = tk.IntVar(value=0)
        dft_e_8 = tk.IntVar(value=self.param_dict['hidden_states_flow'])#No. of hidden states
        dft_e_9 = tk.StringVar(value=str(self.param_dict['dropout_rate_flow']))#Recurrent dropout rate
        dft_e_10 = tk.IntVar(value=self.param_dict['constraint_flow'])#Max_norm constraint
        dft_e_11 = tk.IntVar(value=self.param_dict['batch_size_flow'])#Batch size
        dft_e_12 = tk.IntVar(value=self.param_dict['max_epochs_flow'])#Max epoches
        
        
        
        #LEFT, labels
        var_L_00 = tk.StringVar()
        var_L_00.set('*Flowrate Model Parameters*')
        self.Lab_00 = tk.Label(self.frm_left, textvariable=var_L_00, bg='white', 
                               font=('Times New Roman', 12), height=2).pack()
        e_font = 12
        
        #1. SF average days
        var_L_1 = tk.StringVar()
        var_L_1.set('1. Spring freshet average days:')
        self.Lab_1 = tk.Label(self.frm_left, textvariable=var_L_1, bg='white', 
                              font=('Times New Roman', 12), height=1).pack()
        self.e_1 = tk.Entry(self.frm_left, show="", width=10, font=e_font, textvariable=dft_e_1)
        self.e_1.pack()
        
        #2. Flow/concentration average days
        var_L_2 = tk.StringVar()
        var_L_2.set('2. Flow rate average days:')
        self.Lab_2 = tk.Label(self.frm_left, textvariable=var_L_2, bg='white', 
                              font=('Times New Roman', 12), height=1).pack()
        self.e_2 = tk.Entry(self.frm_left, show="", width=10, font=e_font, textvariable=dft_e_2)
        self.e_2.pack()
        
        #3. Time step
        var_L_3 = tk.StringVar()
        var_L_3.set('3. Time step for the recurrent neural network (RNN):')
        self.Lab_3 = tk.Label(self.frm_left, textvariable=var_L_3, bg='white', 
                              font=('Times New Roman', 12), height=1).pack()
        self.e_3 = tk.Entry(self.frm_left, show="", width=10, font=e_font, textvariable=dft_e_3)
        self.e_3.pack()
        
        #4. Gap days
        var_L_4 = tk.StringVar()
        var_L_4.set('4. Gap days between the end of input and the target date:')
        self.Lab_4 = tk.Label(self.frm_left, textvariable=var_L_4, bg='white', 
                              font=('Times New Roman', 12), height=1).pack()
        self.e_4 = tk.Entry(self.frm_left, show="", width=10, font=e_font, textvariable=dft_e_4)
        self.e_4.pack()
        
        #5. Random seed
        var_L_5 = tk.StringVar()
        var_L_5.set('5. The seed to generate random numbers:')
        self.Lab_5 = tk.Label(self.frm_left, textvariable=var_L_5, bg='white', 
                              font=('Times New Roman', 12), height=1).pack()
        self.e_5 = tk.Entry(self.frm_left, show="", width=10, font=e_font, textvariable=dft_e_5)
        self.e_5.pack()
        
        #6. Learning rate in Adam optimizer
        var_L_6 = tk.StringVar()
        var_L_6.set('6. Learning rate in Adam optimizer for training RNNs:')
        self.Lab_6 = tk.Label(self.frm_left, textvariable=var_L_6, bg='white', 
                              font=('Times New Roman', 12), height=1).pack()
        self.e_6 = tk.Entry(self.frm_left, show="", width=10, font=e_font, textvariable=dft_e_6)
        self.e_6.pack()
        
        #8. No. of hidden states
        var_L_8 = tk.StringVar()
        var_L_8.set('7. No. of hidden states in the fully connected layer of RNNs:')
        self.Lab_8 = tk.Label(self.frm_left, textvariable=var_L_8, bg='white', 
                              font=('Times New Roman', 12), height=1).pack()
        self.e_8 = tk.Entry(self.frm_left, show="", width=10, font=e_font, textvariable=dft_e_8)
        self.e_8.pack()
        
        #9. Recurrent dropout rate
        var_L_9 = tk.StringVar()
        var_L_9.set('8. Recurrent dropout rate:')
        self.Lab_9 = tk.Label(self.frm_left, textvariable=var_L_9, bg='white', 
                              font=('Times New Roman', 12), height=1).pack()
        self.e_9 = tk.Entry(self.frm_left, show="", width=10, font=e_font, textvariable=dft_e_9)
        self.e_9.pack()
        
        #10. Max_norm constraint
        var_L_10 = tk.StringVar()
        var_L_10.set('9. Max_norm constraint:')
        self.Lab_10 = tk.Label(self.frm_left, textvariable=var_L_10, bg='white', 
                               font=('Times New Roman', 12), height=1).pack()
        self.e_10 = tk.Entry(self.frm_left, show="", width=10, font=e_font, textvariable=dft_e_10)
        self.e_10.pack()
        
        #11. Batch size
        var_L_11 = tk.StringVar()
        var_L_11.set('10. Batch size:')
        self.Lab_11 = tk.Label(self.frm_left, textvariable=var_L_11, bg='white', 
                               font=('Times New Roman', 12), height=1).pack()
        self.e_11 = tk.Entry(self.frm_left, show="", width=10, font=e_font, textvariable=dft_e_11)
        self.e_11.pack()
        
        #12. Max epoches
        var_L_12 = tk.StringVar()
        var_L_12.set('11. Maximum No. of epochs:')
        self.Lab_12 = tk.Label(self.frm_left, textvariable=var_L_12, bg='white', 
                               font=('Times New Roman', 12), height=1).pack()
        self.e_12 = tk.Entry(self.frm_left, show="", width=10, font=e_font, textvariable=dft_e_12)
        self.e_12.pack()
        
        #13. Validation frequency
        var_L_13 = tk.StringVar()
        var_L_13.set('12. Validation frequency (validate after how many epochs):')
        self.Lab_13 = tk.Label(self.frm_left, textvariable=var_L_13, bg='white', 
                               font=('Times New Roman', 12), height=1).pack()
        self.e_13 = tk.Entry(self.frm_left, show="", width=10, font=e_font, textvariable=dft_e_13)
        self.e_13.pack()
        
        #7. Recurrent type
        self.var_L_7 = tk.StringVar()
        self.var_L_7.set('13. RNN type:')
        self.Lab_7 = tk.Label(self.frm_left, textvariable=self.var_L_7, bg='white', 
                              font=('Times New Roman', 12), height=1).pack()
        self.r_7_1 = tk.Radiobutton(self.frm_left, text='LSTM', variable=self.dft_r_7, value=0,
                    command=self.print_r_7_selection)#.place(x=130, y=705, anchor='nw')
        self.r_7_2 = tk.Radiobutton(self.frm_left, text='GRU', variable=self.dft_r_7, value=1,
                    command=self.print_r_7_selection)#.place(x=190, y=705, anchor='nw')
        self.r_7_1.pack()
        self.r_7_2.pack()

        #Bottom
        #1. Update
        self.btn_update = tk.Button(self.frm_right, text = 'Update', width = 25, 
                                  command = self.update_adv).pack()
        #2. Quit
        self.btn_quit = tk.Button(self.frm_right, text = 'Quit', width = 25, 
                                  command = self.close_windows).pack()
        return
    
    def print_r_7_selection(self):
        if self.dft_r_7.get() == 0:
            str_print = '13. RNN type (LSTM selected):'
        elif self.dft_r_7.get() == 1:
            str_print = '13. RNN type (GRU selected):'
        
        self.var_L_7.set(str_print)
        return
    
    def update_adv(self):
        try:
            self.param_dict['RNN_avg_days_flow'] = int(self.e_2.get())
            self.param_dict['time_step_flow'] = int(self.e_3.get())
            self.param_dict['gap_days_flow'] = int(self.e_4.get())
            self.param_dict['learning_rate_flow'] = float(self.e_6.get())
            if self.dft_r_7.get() == 1:#RNN type; 0 for LSTM and 1 for GRU; by default: 0
                self.param_dict['recurrent_type_flow'] = 'GRU'
            else:
                self.param_dict['recurrent_type_flow'] = 'LSTM'
            #print(self.param_dict['recurrent_type'])
            self.param_dict['hidden_states_flow'] = int(self.e_8.get())
            self.param_dict['dropout_rate_flow'] = float(self.e_9.get())
            self.param_dict['constraint_flow'] = int(self.e_10.get())
            self.param_dict['batch_size_flow'] = int(self.e_11.get())
            self.param_dict['max_epochs_flow'] = int(self.e_12.get())
            #print(self.param_dict)
            
            #common
            self.param_dict['tree_avg_days'] = int(self.e_1.get())
            self.param_dict['seed'] = int(self.e_5.get())
            self.param_dict['validation_freq'] = int(self.e_13.get())
            
            messagebox.showinfo(title='Advanced parameters updated', 
                                message='All advanced parameters have been updated successfully.')
        except Exception as ex:
            messagebox.showerror(title='Failed to update advanced parameters', message=ex)
            return
        
        return
    
    def close_windows(self):
        self.master.destroy()
        return
    
class model_main:
    def __init__(self, param_dict):
        self.param_dict = param_dict
        
        #print(self.param_dict)
        #messagebox.showinfo(title='Test', message='All parameters have been updated successfully.')
        #print(self.param_dict['station'])
        #self.test()
        
        try:
            self.run_RNN()
            #self.get_dir
        except Exception as ex:
            messagebox.showerror(title='Failed to run the flow rate model', message=ex)
            return
        '''
        try:
            self.run_conc()
        except Exception as ex:
            messagebox.showerror(title='Failed to run the concentration model', message=ex)
            return
        
        return
        '''
        

    def run_RNN(self):
        #print('run_flow')
        
        # =============================================================================
        # Loading parameters
        # =============================================================================
        #common
        station = self.param_dict['station']
        #tree_avg_days = self.param_dict['tree_avg_days']#here is the average days for decision tree input
        seed = self.param_dict['seed']#seed gave the best prediction result for FRO KC1 station, keep it
        #flowrate_threshold = self.param_dict['flowrate_threshold']#1.2, 1.7, and 0.7 for FRO_KC1, FRO_HC1, and EVO_HC1
        
        train_startDate = self.param_dict['train_startDate']
        test_startDate = self.param_dict['test_startDate']
        endDate = self.param_dict['endDate']
        
        #flow
        RNN_avg_days_flow = self.param_dict['RNN_avg_days_flow']#average days for LSTM input
        time_step_flow = self.param_dict['time_step_flow']
        gap_days_flow = self.param_dict['gap_days_flow']#No. of days between the last day of input and the predict date
        recurrent_type_flow = self.param_dict['recurrent_type_flow']#choose 'LSTM' OR 'GRU'

        # =============================================================================
        
        #Read flow rate file
        try:
            flowrate = pd.read_csv(filepath_or_buffer=self.param_dict['dir_tar_flow'], 
                        usecols=[self.param_dict['use_col_flow_date']-1])
            flowrate.columns = ['Datetime']
            
            flowrate['flow'] = np.array(pd.read_csv(filepath_or_buffer=self.param_dict['dir_tar_flow'], 
                        usecols=[self.param_dict['use_col_flow']-1]))
            
            # Converting date string to datetime
            flowrate['Datetime'] = pd.to_datetime(flowrate['Datetime'], format='%Y/%m/%d')
            #flowrate = flowrate.drop('sample_date', 1)
            
            #print('Flow rate:\n', flowrate)#for testing
        except Exception as ex:
            messagebox.showerror(title='Failed to read the flow rate file', message=ex)
            return
        
        #print(flowrate.describe())
        # =============================================================================
        # Generate Weather_avg_ data
        # =============================================================================
        use_col_features = self.param_dict['use_col_features']
        
        for i in range(0,len(use_col_features)):#index from 0
            use_col_features[i] -= 1
        try:
            weather_avg = pd.read_csv(filepath_or_buffer=self.param_dict['dir_features'], 
                        usecols=use_col_features)
            weather_org = weather_avg.copy()
            
            weather_datetime = pd.read_csv(filepath_or_buffer=self.param_dict['dir_features'], 
                        usecols=[self.param_dict['use_col_fea_date'] - 1])
            weather_datetime.columns = ['Datetime']
            weather_datetime.loc[:,'Datetime'] = pd.to_datetime(weather_datetime['Datetime'], format='%Y/%m/%d')
            
            #print(weather_avg)
            fea_lst = []
            for col in weather_avg.columns:
                #print(col)
                fea_lst.append(col)
                #f_col = interp1d(self.timestampToNum(weather_datetime['Datetime']), weather_avg[col])
                imp = SimpleImputer(missing_values=np.nan, strategy='mean')
                weather_avg[col] = imp.fit_transform(np.c_[np.array(weather_avg.index), np.array(weather_avg[col])])[:,1]
                
                weather_avg.loc[:,col+'_avg'] = weather_avg.loc[:,col]
                for i in range(0, len(weather_avg)):
                    if i < RNN_avg_days_flow-1:
                        weather_avg.loc[i, col+'_avg'] = sum(weather_avg[col].loc[0:i])/(i+1)
                    else:
                        weather_avg.loc[i, col+'_avg'] = sum(weather_avg[col].loc[i-RNN_avg_days_flow+1:i])/RNN_avg_days_flow
                weather_avg.loc[:,col] = weather_avg.loc[:,col+'_avg']
                weather_avg.drop(col+'_avg', 1, inplace=True)
            

            # Converting date string to datetime
            weather_avg.loc[:,'Datetime'] = weather_datetime['Datetime']
            
            month_weather_avg = []
            for day in weather_avg['Datetime']:
                month_weather_avg.append(day.month)
            weather_avg['Month'] = np.array(month_weather_avg)
            
            #print('Input variables:\n', weather_avg)#for testing
        except Exception as ex:
            messagebox.showerror(title='''Failed to read or process the input variable file.''', message=ex)
            return
        

        # =============================================================================
        # Missing weather data filling (average weather input enabled)
        # =============================================================================
        try:
            monthly_mean = pd.DataFrame()
            for col in fea_lst:
                monthly_mean.loc[:,col+'_avg'] = weather_avg.groupby('Month')[col].mean()
            monthly_mean['Month'] = monthly_mean.index
            monthly_mean.index = np.array(monthly_mean.index)#remove the name of index
            
            weather_merge = pd.merge(weather_avg, monthly_mean, on=('Month'), how='left')
            
            for col in fea_lst:
                for i in range(0, len(weather_avg)):
                    if weather_org[col].isnull()[i]:
                        weather_merge.loc[i, col] = weather_merge[col+'_avg'][i]
                weather_merge.drop(col+'_avg', 1, inplace=True)
            
            #print('dir_output: ', self.param_dict['dir_output'])
            #to be done: create a new folder to save the file
            weather_merge.to_csv(self.param_dict['dir_output']+'\\'+
                                 station+'features_filled_avg_'+
                                 str(RNN_avg_days_flow)+'.csv',index=True)
            
            
        except Exception as ex:
            messagebox.showerror(title='Failed to generate the monthly averaged features', message=ex)
            return

        
        
        
        
        
        
        
        
        return#return to run_flow
    
    '''
    def run_conc(self):
        print('run_conc')
        return#return to run_conc
    '''
    # =============================================================================
    # Other functions
    # =============================================================================
    def predict_test(X_scaled_test, classifier, y_test):
        y_pred = classifier.predict(X_scaled_test)
        print(np.concatenate((y_pred.reshape(len(y_pred), 1), (y_test.reshape(len(y_test), 1))), 1))
        return y_pred
    
    def accuracy_print_conf(y_test, y_pred):
        from sklearn.metrics import confusion_matrix, accuracy_score
        conf_matrix = confusion_matrix(y_test.astype('int'), y_pred.astype('int'))
        #separately print out confusion matrix
        #tn, fp, fn, tp = confusion_matrix(y_test.astype('int'), y_pred.astype('int')).ravel()
        print('The confusion matrix is:\n', conf_matrix)
        accuracy = accuracy_score(y_test.astype('int'), y_pred.astype('int'))
        print('The accuracy is: %2.2f' % accuracy)
        return accuracy
    
    def rootMSE(y_test, y_pred):
        import math
        from sklearn.metrics import mean_squared_error
        rmse = math.sqrt(mean_squared_error(y_test, y_pred))
        print('RMSE = %2.2f' % rmse)
        print('Predicted results length:', y_pred.shape)
        y_test = np.array(y_test).reshape(-1, 1)
        print('Real results length:', y_test.shape)
        return rmse
    

    # =============================================================================
    
def main(): 
    #Default values for ordinary/advanced parameters settings
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
        'flowrate_threshold': 1.8,#7. Flow rate threshold for spring freshet
        'train_startDate': (today-timedelta(days=365)).strftime('%Y/%m/%d'),#8. Date when training set starts 
        'test_startDate': (today-timedelta(days=31)).strftime('%Y/%m/%d'),#9. Date when test set starts
        'endDate': today.strftime('%Y/%m/%d'),#10. Date when test set ends
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
        #conc
        
        
        #common
        'validation_freq': 1,#Validation frequency
        'tree_avg_days': 1, #SF average days
        'seed': 29#Random seed
                  }
    
    root = tk.Tk()
    
    Ordinary_input(root, param_dict)
    root.mainloop()
    
    return

if __name__ == '__main__':
    main()