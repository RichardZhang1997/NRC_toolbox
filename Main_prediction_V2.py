# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 09:41:34 2023

@author: Administrator
"""

import tkinter as tk
from tkinter import messagebox
from datetime import date, timedelta, datetime

import os
import numpy as np
import pandas as pd
#import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

from sklearn.impute import SimpleImputer

#from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import MinMaxScaler

# Constructing a RNN
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM, GRU
from tensorflow.keras.constraints import max_norm
import tensorflow as tf

#from tensorflow.keras.wrappers.scikit_learn import KerasRegressor
from tensorflow.keras.callbacks import ModelCheckpoint

class Ordinary_input:
    def __init__(self, master, param_dict):
        self.master = master
        self.master.title('RNN Model Training Tool-General Settings')
        self.master.geometry('1000x700')
        
        self.param_dict = param_dict
        
        #Frames, different packing ways
        self.frm_left = tk.Frame(self.master)
        self.frm_right = tk.Frame(self.master)
        self.frm_bottom = tk.Frame(self.master)
        
        e_font = 12
        
        #Initializing values of entries
        dft_e_1 = tk.StringVar(value=self.param_dict['dir_features'])#1. Address of input features
        dft_e_2 = tk.StringVar(value=self.param_dict['dir_tar_flow'])#2. Address of the flow rate target
        dft_e_3 = tk.StringVar(value=self.param_dict['use_col_features'])#3. Features use columns, exclude date column
        dft_e_4 = tk.StringVar(value=self.param_dict['use_col_flow'])#4. Target use column, exclude date column
        dft_e_5 = tk.StringVar(value=self.param_dict['use_col_fea_date'])#5. Datetime column of features
        dft_e_6 = tk.StringVar(value=self.param_dict['use_col_flow_date'])#6. Datetime column of target
        #dft_e_7 = tk.StringVar(value=self.param_dict['flowrate_threshold'])#7. Flow rate threshold for spring freshet
        dft_e_7 = tk.StringVar(value=self.param_dict['train_startDate'])#9. Date when test set starts
        dft_e_8 = tk.StringVar(value=self.param_dict['train_endDate'])#8. Date when training set starts 
        dft_e_9 = tk.StringVar(value=self.param_dict['test_startDate'])#9. Date when test set starts
        dft_e_10 = tk.StringVar(value=self.param_dict['test_endDate'])#10. Date when test set ends
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
        
        #9. Date when test set starts
        var_L_7 = tk.StringVar()
        var_L_7.set('7. Date when training set starts:')
        self.Lab_7 = tk.Label(self.frm_left, textvariable=var_L_7, bg='white', 
                              font=('Times New Roman', 12), height=1).pack()
        self.e_7 = tk.Entry(self.frm_left, show="", width=10, font=e_font, textvariable=dft_e_7)
        self.e_7.pack()
            
        #9. Date when test set starts
        var_L_9 = tk.StringVar()
        var_L_9.set('9. Date when the predicting range starts:')
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
            
    
        
        #Right
        #2. Address of the target feature
        var_L_2 = tk.StringVar()
        var_L_2.set('2. File address of the  target:')
        self.Lab_2 = tk.Label(self.frm_right, textvariable=var_L_2, bg='white', 
                              font=('Times New Roman', 12), height=1).pack()
        self.e_2 = tk.Entry(self.frm_right, show="", width=40, font=e_font, textvariable=dft_e_2)
        self.e_2.pack()
        
        #4. Target use column
        var_L_4 = tk.StringVar()
        var_L_4.set('4. The number of column of the target (exclude date column):')
        self.Lab_4 = tk.Label(self.frm_right, textvariable=var_L_4, bg='white', 
                              font=('Times New Roman', 12), height=1).pack()
        self.e_4 = tk.Entry(self.frm_right, show="", width=10, font=e_font, textvariable=dft_e_4)
        self.e_4.pack()
        
        #6. Datetime column of target
        var_L_6 = tk.StringVar()
        var_L_6.set('6. The number of date column of the target:')
        self.Lab_6 = tk.Label(self.frm_right, textvariable=var_L_6, bg='white', 
                              font=('Times New Roman', 12), height=1).pack()
        self.e_6 = tk.Entry(self.frm_right, show="", width=10, font=e_font, textvariable=dft_e_6)
        self.e_6.pack()
        
        #8. Date when training set start 
        var_L_8 = tk.StringVar()
        var_L_8.set('8. Date when training set ends:')
        self.Lab_8 = tk.Label(self.frm_right, textvariable=var_L_8, bg='white', 
                              font=('Times New Roman', 12), height=1).pack()
        self.e_8 = tk.Entry(self.frm_right, show="", width=10, font=e_font, textvariable=dft_e_8)
        self.e_8.pack()
               
        #10. Date when test set ends
        var_L_10 = tk.StringVar()
        var_L_10.set('10. Date when the predicting range ends:')
        self.Lab_10 = tk.Label(self.frm_right, textvariable=var_L_10, bg='white', 
                              font=('Times New Roman', 12), height=1).pack()
        self.e_10 = tk.Entry(self.frm_right, show="", width=10, font=e_font, textvariable=dft_e_10)
        self.e_10.pack()
        
        #12. Training model selection: automatic (0) VS manual (1)
        
        self.var_L_12 = tk.StringVar()
        self.var_L_12.set('12. Training model selection (Manual mode):')
        self.Lab_12 = tk.Label(self.frm_right, textvariable=self.var_L_12, bg='white', 
                              font=('Times New Roman', 12), height=1).pack()
        self.r_12_1 = tk.Radiobutton(self.frm_right, text='Automatic', variable=self.dft_r_12, value=0,
                    command=self.print_r_12_selection)#.place(x=130, y=705, anchor='nw')
        self.r_12_2 = tk.Radiobutton(self.frm_right, text='Manual', variable=self.dft_r_12, value=1,
                    command=self.print_r_12_selection)#.place(x=190, y=705, anchor='nw')
        self.r_12_1.pack()
        self.r_12_2.pack()
        
        #13. Station name
        var_L_13 = tk.StringVar()
        var_L_13.set('12. Please type in a name of the station/trail:')
        self.Lab_13 = tk.Label(self.frm_right, textvariable=var_L_13, bg='white', 
                              font=('Times New Roman', 12), height=1).pack()
        self.e_13 = tk.Entry(self.frm_right, show="", width=20, font=e_font, textvariable=dft_e_13)
        self.e_13.pack()
        
        #Bottom
        self.btn_advSet = tk.Button(self.frm_bottom, text = 'Advanced Settings', 
                                    width = 25, command = self.new_window_add).pack()
        
        self.btn_conf = tk.Button(self.frm_bottom, text = 'Confirm & Run', 
                                  width = 25, command = self.confirm_btn).pack()
        
        self.btn_loadRst = tk.Button(self.frm_bottom, text = 'Load Previous Training Results', 
                                  width = 25, command = self.new_window_load).pack()
        
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
    
    def new_window_add(self):
        newWindow = tk.Toplevel(self.master)
        self.app = Additional_input(newWindow, self.param_dict)
        return
    
    def new_window_load(self):
        newWindow = tk.Toplevel(self.master)
        self.app = Load_model_results(newWindow, 1, self.param_dict)#temp
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
            #self.param_dict['flowrate_threshold'] = float(self.e_7.get())
            
            #3. Features use columns, exclude date column
            use_col_fea = []
            str_use_col_fea = str(self.e_3.get())
            str_use_col_fea = str_use_col_fea.split(sep=',')
            
            for num in str_use_col_fea:
                use_col_fea.append(int(num.strip()))
            use_col_fea = list(set(use_col_fea))#Deduplication
            
            self.param_dict['use_col_features'] = use_col_fea
            
            #8-11
            self.param_dict['train_startDate'] = datetime.strptime(self.e_7.get(), '%Y/%m/%d').strftime('%Y/%m/%d')
            self.param_dict['train_endDate'] = datetime.strptime(self.e_8.get(), '%Y/%m/%d').strftime('%Y/%m/%d')
            self.param_dict['test_startDate'] = datetime.strptime(self.e_9.get(), '%Y/%m/%d').strftime('%Y/%m/%d')
            self.param_dict['test_endDate'] = datetime.strptime(self.e_10.get(), '%Y/%m/%d').strftime('%Y/%m/%d')
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
            
            self.app = Model_main(self.master, self.param_dict)
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
        
        self.master.title('RNN Model Training Tool-Advanced Settings')
        self.master.geometry('580x800')
        
        self.frm_left.pack(side='left')
        self.frm_right.pack(side='right')
        self.frm_bottom.pack(side='bottom')
        
        #Default values of additional input
        #common
        #dft_e_1 = tk.IntVar(value=self.param_dict['tree_avg_days'])#SF average days
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
        var_L_00.set('*Hyperparameters of the neural network*')
        self.Lab_00 = tk.Label(self.frm_left, textvariable=var_L_00, bg='white', 
                               font=('Times New Roman', 12), height=2).pack()
        e_font = 12
        '''
        #1. SF average days
        var_L_1 = tk.StringVar()
        var_L_1.set('1. Spring freshet average days:')
        self.Lab_1 = tk.Label(self.frm_left, textvariable=var_L_1, bg='white', 
                              font=('Times New Roman', 12), height=1).pack()
        self.e_1 = tk.Entry(self.frm_left, show="", width=10, font=e_font, textvariable=dft_e_1)
        self.e_1.pack()
        '''
        #2. Flow/concentration average days
        var_L_2 = tk.StringVar()
        var_L_2.set('1. Flow rate average days:')
        self.Lab_2 = tk.Label(self.frm_left, textvariable=var_L_2, bg='white', 
                              font=('Times New Roman', 12), height=1).pack()
        self.e_2 = tk.Entry(self.frm_left, show="", width=10, font=e_font, textvariable=dft_e_2)
        self.e_2.pack()
        
        #3. Time step
        var_L_3 = tk.StringVar()
        var_L_3.set('2. Time step for the recurrent neural network (RNN):')
        self.Lab_3 = tk.Label(self.frm_left, textvariable=var_L_3, bg='white', 
                              font=('Times New Roman', 12), height=1).pack()
        self.e_3 = tk.Entry(self.frm_left, show="", width=10, font=e_font, textvariable=dft_e_3)
        self.e_3.pack()
        
        #4. Gap days
        var_L_4 = tk.StringVar()
        var_L_4.set('3. Gap days between the end of input and the target date:')
        self.Lab_4 = tk.Label(self.frm_left, textvariable=var_L_4, bg='white', 
                              font=('Times New Roman', 12), height=1).pack()
        self.e_4 = tk.Entry(self.frm_left, show="", width=10, font=e_font, textvariable=dft_e_4)
        self.e_4.pack()
        
        #5. Random seed
        var_L_5 = tk.StringVar()
        var_L_5.set('4. The seed to generate random numbers:')
        self.Lab_5 = tk.Label(self.frm_left, textvariable=var_L_5, bg='white', 
                              font=('Times New Roman', 12), height=1).pack()
        self.e_5 = tk.Entry(self.frm_left, show="", width=10, font=e_font, textvariable=dft_e_5)
        self.e_5.pack()
        
        #6. Learning rate in Adam optimizer
        var_L_6 = tk.StringVar()
        var_L_6.set('5. Learning rate in Adam optimizer for training RNNs:')
        self.Lab_6 = tk.Label(self.frm_left, textvariable=var_L_6, bg='white', 
                              font=('Times New Roman', 12), height=1).pack()
        self.e_6 = tk.Entry(self.frm_left, show="", width=10, font=e_font, textvariable=dft_e_6)
        self.e_6.pack()
        
        #8. No. of hidden states
        var_L_8 = tk.StringVar()
        var_L_8.set('6. No. of hidden states in the fully connected layer of RNNs:')
        self.Lab_8 = tk.Label(self.frm_left, textvariable=var_L_8, bg='white', 
                              font=('Times New Roman', 12), height=1).pack()
        self.e_8 = tk.Entry(self.frm_left, show="", width=10, font=e_font, textvariable=dft_e_8)
        self.e_8.pack()
        
        #9. Recurrent dropout rate
        var_L_9 = tk.StringVar()
        var_L_9.set('7. Recurrent dropout rate:')
        self.Lab_9 = tk.Label(self.frm_left, textvariable=var_L_9, bg='white', 
                              font=('Times New Roman', 12), height=1).pack()
        self.e_9 = tk.Entry(self.frm_left, show="", width=10, font=e_font, textvariable=dft_e_9)
        self.e_9.pack()
        
        #10. Max_norm constraint
        var_L_10 = tk.StringVar()
        var_L_10.set('8. Max_norm constraint:')
        self.Lab_10 = tk.Label(self.frm_left, textvariable=var_L_10, bg='white', 
                               font=('Times New Roman', 12), height=1).pack()
        self.e_10 = tk.Entry(self.frm_left, show="", width=10, font=e_font, textvariable=dft_e_10)
        self.e_10.pack()
        
        #11. Batch size
        var_L_11 = tk.StringVar()
        var_L_11.set('9. Batch size:')
        self.Lab_11 = tk.Label(self.frm_left, textvariable=var_L_11, bg='white', 
                               font=('Times New Roman', 12), height=1).pack()
        self.e_11 = tk.Entry(self.frm_left, show="", width=10, font=e_font, textvariable=dft_e_11)
        self.e_11.pack()
        
        #12. Max epoches
        var_L_12 = tk.StringVar()
        var_L_12.set('10. Maximum No. of epochs:')
        self.Lab_12 = tk.Label(self.frm_left, textvariable=var_L_12, bg='white', 
                               font=('Times New Roman', 12), height=1).pack()
        self.e_12 = tk.Entry(self.frm_left, show="", width=10, font=e_font, textvariable=dft_e_12)
        self.e_12.pack()
        
        #13. Validation frequency
        var_L_13 = tk.StringVar()
        var_L_13.set('11. Validation frequency (validate after how many epochs):')
        self.Lab_13 = tk.Label(self.frm_left, textvariable=var_L_13, bg='white', 
                               font=('Times New Roman', 12), height=1).pack()
        self.e_13 = tk.Entry(self.frm_left, show="", width=10, font=e_font, textvariable=dft_e_13)
        self.e_13.pack()
        
        #7. Recurrent type
        self.var_L_7 = tk.StringVar()
        self.var_L_7.set('12. RNN type (LSTM selected):')
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
            #self.param_dict['tree_avg_days'] = int(self.e_1.get())
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


class Additional_input_min:
    def __init__(self, master, param_dict):
        self.master = master
        self.param_dict = param_dict
        
        self.frm_left = tk.Frame(self.master)
        self.frm_right = tk.Frame(self.master)
        self.frm_bottom = tk.Frame(self.master)
        
        self.master.title('RNN Model Training Tool-Advanced Settings')
        self.master.geometry('580x800')
        
        self.frm_left.pack(side='left')
        self.frm_right.pack(side='right')
        self.frm_bottom.pack(side='bottom')
        
        #Default values of additional input
        #common
        #dft_e_1 = tk.IntVar(value=self.param_dict['tree_avg_days'])#SF average days
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
        #dft_e_8 = tk.IntVar(value=self.param_dict['hidden_states_flow'])#No. of hidden states
        #dft_e_9 = tk.StringVar(value=str(self.param_dict['dropout_rate_flow']))#Recurrent dropout rate
        #dft_e_10 = tk.IntVar(value=self.param_dict['constraint_flow'])#Max_norm constraint
        dft_e_11 = tk.IntVar(value=self.param_dict['batch_size_flow'])#Batch size
        dft_e_12 = tk.IntVar(value=self.param_dict['max_epochs_flow'])#Max epoches
        
        #LEFT, labels
        var_L_00 = tk.StringVar()
        var_L_00.set('*Hyperparameters of the neural network*')
        self.Lab_00 = tk.Label(self.frm_left, textvariable=var_L_00, bg='white', 
                               font=('Times New Roman', 12), height=2).pack()
        e_font = 12
        '''
        #1. SF average days
        var_L_1 = tk.StringVar()
        var_L_1.set('1. Spring freshet average days:')
        self.Lab_1 = tk.Label(self.frm_left, textvariable=var_L_1, bg='white', 
                              font=('Times New Roman', 12), height=1).pack()
        self.e_1 = tk.Entry(self.frm_left, show="", width=10, font=e_font, textvariable=dft_e_1)
        self.e_1.pack()
        '''
        #2. Flow/concentration average days
        var_L_2 = tk.StringVar()
        var_L_2.set('1. Flow rate average days:')
        self.Lab_2 = tk.Label(self.frm_left, textvariable=var_L_2, bg='white', 
                              font=('Times New Roman', 12), height=1).pack()
        self.e_2 = tk.Entry(self.frm_left, show="", width=10, font=e_font, textvariable=dft_e_2)
        self.e_2.pack()
        
        #3. Time step
        var_L_3 = tk.StringVar()
        var_L_3.set('2. Time step for the recurrent neural network (RNN):')
        self.Lab_3 = tk.Label(self.frm_left, textvariable=var_L_3, bg='white', 
                              font=('Times New Roman', 12), height=1).pack()
        self.e_3 = tk.Entry(self.frm_left, show="", width=10, font=e_font, textvariable=dft_e_3)
        self.e_3.pack()
        
        #4. Gap days
        var_L_4 = tk.StringVar()
        var_L_4.set('3. Gap days between the end of input and the target date:')
        self.Lab_4 = tk.Label(self.frm_left, textvariable=var_L_4, bg='white', 
                              font=('Times New Roman', 12), height=1).pack()
        self.e_4 = tk.Entry(self.frm_left, show="", width=10, font=e_font, textvariable=dft_e_4)
        self.e_4.pack()
        
        #5. Random seed
        var_L_5 = tk.StringVar()
        var_L_5.set('4. The seed to generate random numbers:')
        self.Lab_5 = tk.Label(self.frm_left, textvariable=var_L_5, bg='white', 
                              font=('Times New Roman', 12), height=1).pack()
        self.e_5 = tk.Entry(self.frm_left, show="", width=10, font=e_font, textvariable=dft_e_5)
        self.e_5.pack()
        
        #6. Learning rate in Adam optimizer
        var_L_6 = tk.StringVar()
        var_L_6.set('5. Learning rate in Adam optimizer for training RNNs:')
        self.Lab_6 = tk.Label(self.frm_left, textvariable=var_L_6, bg='white', 
                              font=('Times New Roman', 12), height=1).pack()
        self.e_6 = tk.Entry(self.frm_left, show="", width=10, font=e_font, textvariable=dft_e_6)
        self.e_6.pack()
        
        #11. Batch size
        var_L_11 = tk.StringVar()
        var_L_11.set('9. Batch size:')
        self.Lab_11 = tk.Label(self.frm_left, textvariable=var_L_11, bg='white', 
                               font=('Times New Roman', 12), height=1).pack()
        self.e_11 = tk.Entry(self.frm_left, show="", width=10, font=e_font, textvariable=dft_e_11)
        self.e_11.pack()
        
        #12. Max epoches
        var_L_12 = tk.StringVar()
        var_L_12.set('10. Maximum No. of epochs:')
        self.Lab_12 = tk.Label(self.frm_left, textvariable=var_L_12, bg='white', 
                               font=('Times New Roman', 12), height=1).pack()
        self.e_12 = tk.Entry(self.frm_left, show="", width=10, font=e_font, textvariable=dft_e_12)
        self.e_12.pack()
        
        #13. Validation frequency
        var_L_13 = tk.StringVar()
        var_L_13.set('11. Validation frequency (validate after how many epochs):')
        self.Lab_13 = tk.Label(self.frm_left, textvariable=var_L_13, bg='white', 
                               font=('Times New Roman', 12), height=1).pack()
        self.e_13 = tk.Entry(self.frm_left, show="", width=10, font=e_font, textvariable=dft_e_13)
        self.e_13.pack()
        
        #7. Recurrent type
        self.var_L_7 = tk.StringVar()
        self.var_L_7.set('12. RNN type (LSTM selected):')
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
            self.param_dict['batch_size_flow'] = int(self.e_11.get())
            self.param_dict['max_epochs_flow'] = int(self.e_12.get())
            #print(self.param_dict)
            
            #common
            #self.param_dict['tree_avg_days'] = int(self.e_1.get())
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
    

class Model_main:
    def __init__(self, master, param_dict):
        self.master = master
        self.param_dict = param_dict
        
        #print(self.param_dict)
        #messagebox.showinfo(title='Test', message='All parameters have been updated successfully.')
        #print(self.param_dict['station'])
        #self.test()
        
        try:
            self.run_RNN()
            
            #self.get_dir
        except Exception as ex:
            messagebox.showerror(title='Failed to run the RNN model', message=ex)
            return
       
    def run_RNN(self):#To be done: make run_RNN a class instead of a function
        #print('run_flow')
        
        # =============================================================================
        # Loading parameters
        # =============================================================================
        #common
        station = self.param_dict['station']
        #tree_avg_days = self.param_dict['tree_avg_days']#here is the average days for decision tree input
        seed = self.param_dict['seed']#seed gave the best prediction result for FRO KC1 station, keep it
        #flowrate_threshold = self.param_dict['flowrate_threshold']#1.2, 1.7, and 0.7 for FRO_KC1, FRO_HC1, and EVO_HC1
        
        dir_tar = self.param_dict['dir_tar_flow']
        use_col_date = self.param_dict['use_col_flow_date']
        use_col = self.param_dict['use_col_flow']
        dir_output = self.param_dict['dir_output']

        train_startDate = self.param_dict['train_startDate']
        train_endDate = self.param_dict['train_endDate']
        test_startDate = self.param_dict['test_startDate']
        test_endDate = self.param_dict['test_endDate']
        
        #flow
        RNN_avg_days = self.param_dict['RNN_avg_days_flow']#average days for LSTM input
        time_step = self.param_dict['time_step_flow']
        gap_days = self.param_dict['gap_days_flow']#No. of days between the last day of input and the predict date
        recurrent_type = self.param_dict['recurrent_type_flow']#choose 'LSTM' OR 'GRU'
        use_col_features = self.param_dict['use_col_features']
        dir_features = self.param_dict['dir_features']
        use_col_fea_date = self.param_dict['use_col_fea_date']
        
        #Model hyperparameters
        learning_rate = self.param_dict['learning_rate_flow']
        max_epochs = self.param_dict['max_epochs_flow']
        batch_size = self.param_dict['batch_size_flow']
        hidden_states = self.param_dict['hidden_states_flow']
        dropout_rate = self.param_dict['dropout_rate_flow']
        constraint = self.param_dict['constraint_flow']
        validation_freq = self.param_dict['validation_freq']
        
        self.param_dict['best_epoch'] = self.param_dict['max_epochs_flow']
        #best_epoch = self.param_dict['best_epoch']
        
        # =============================================================================
        #Read flow rate file
        try:
            print(dir_tar)
            flowrate = pd.read_csv(filepath_or_buffer=dir_tar, 
                        usecols=[use_col_date-1])
            flowrate.columns = ['Datetime']
            
            flowrate['flow'] = np.array(pd.read_csv(filepath_or_buffer=dir_tar, 
                        usecols=[use_col-1]))
            
            # Converting date string to datetime
            flowrate['Datetime'] = pd.to_datetime(flowrate['Datetime'], format='%Y/%m/%d')
            #flowrate = flowrate.drop('sample_date', 1)
            flowrate.dropna(inplace=True)
            
            print('Target:\n', flowrate)#for testing
            path_prep = self.createFolder_ifNotExist(folder_name='Target', 
                                                     dir_output=dir_output+'\\Pre-processed Data')
            flowrate.to_csv(path_or_buf = path_prep+'\\'+station+'_target_'+'.csv',
                            index=False)
        except Exception as ex:
            messagebox.showerror(title='Failed to read the target file', message=ex)
            return
        
        #print(flowrate.describe())
        # =============================================================================
        # Generate Weather_avg_ data
        # =============================================================================
        for i in range(0,len(use_col_features)):#index from 0
            use_col_features[i] -= 1
        try:
            weather_avg = pd.read_csv(filepath_or_buffer=dir_features, 
                        usecols=use_col_features)
            weather_org = weather_avg.copy()
            
            weather_datetime = pd.read_csv(filepath_or_buffer=dir_features, 
                        usecols=[use_col_fea_date - 1])
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
                    if i < RNN_avg_days-1:
                        weather_avg.loc[i, col+'_avg'] = sum(weather_avg[col].loc[0:i])/(i+1)
                    else:
                        weather_avg.loc[i, col+'_avg'] = sum(weather_avg[col].loc[i-RNN_avg_days+1:i])/RNN_avg_days
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
            
            weather_merge.drop('Month', 1, inplace=True)

            #print('dir_output: ', dir_output)
            path_prep = self.createFolder_ifNotExist(folder_name="Features", 
                                         dir_output=dir_output+'\\Pre-processed Data')
            weather_merge.to_csv(path_or_buf = path_prep+'\\'+station+'_features_filled_avg_'+
                                 str(RNN_avg_days)+'.csv',
                                 index=False)
            
            print('Weather_merge:', weather_merge)
        except Exception as ex:
            messagebox.showerror(title='Failed to generate the monthly averaged features', message=ex)
            return
        
        #Merge
        merged_data = pd.merge(weather_merge, flowrate, on=('Datetime'), how='left')
        merged_data.index = merged_data['Datetime']
        
        #train/test separation
        train = merged_data.loc[train_startDate : train_endDate].drop('Datetime', 1)
        test = merged_data.loc[test_startDate : test_endDate].drop('Datetime', 1)
        
        #Datetime string for train and test set
        datetime_train = merged_data.loc[train_startDate : train_endDate].index[:].strftime('%Y-%m-%d')
        datetime_test = merged_data.loc[test_startDate : test_endDate].index[:].strftime('%Y-%m-%d')
        
        #Data scaling
        scaler = MinMaxScaler(feature_range=(0, 1), copy=True)
        scaled_train = scaler.fit_transform(train)
        scaled_test = scaler.transform(test)
        
        scaled = np.r_[scaled_train, scaled_test]
        original = np.r_[train, test]
        datetime = np.r_[datetime_train, datetime_test]
        
        #construct 3-D input matrix
        No_of_fea = len(fea_lst)
        No_of_tar = len(merged_data.columns)-No_of_fea-1#'-1' because of 'datetime' column
        
        print('Below are results for time_step:', time_step)
        X_scaled, y_scaled, y_not_scaled= [], [], []
        datetime_deNull = []#target deNull
        for i in range(time_step, len(scaled)):
            sample_input = []
            for j in range(0, time_step):
                sample_input.append(scaled[i-gap_days-(time_step-1-j)*RNN_avg_days, :-No_of_tar])
            X_scaled.append(sample_input)
            y_scaled.append(scaled[i, -No_of_tar:])
            y_not_scaled.append(original[i, -No_of_tar:])
            datetime_deNull.append(datetime[i])
        X_scaled, y_scaled, y_not_scaled = np.array(X_scaled), np.array(y_scaled), np.array(y_not_scaled)
        datetime_deNull = np.array(datetime_deNull)
        
        test_size = len(pd.DataFrame(test).dropna())#Number of valid test size
        
        #train/test separation again
        X_train = X_scaled[:len(X_scaled)-test_size, :, :]
        y_train = y_scaled[:len(X_scaled)-test_size]
        y_train_not_scaled = y_not_scaled[:len(X_scaled)-test_size]
        datetime_train_deNull = datetime_deNull[:len(X_scaled)-test_size]
        
        X_test = X_scaled[len(X_scaled)-test_size:, :, :]
        y_test = y_scaled[len(X_scaled)-test_size:]
        y_test_not_scaled = y_not_scaled[len(X_scaled)-test_size:]
        datetime_test_deNull = datetime_deNull[len(X_scaled)-test_size:]
        
        # =============================================================================
        # Constructing RNN
        # =============================================================================
        #print(tf.__version__)
        tf.keras.backend.clear_session()
        tf.random.set_seed(seed)
        
        opt = tf.keras.optimizers.Adam(learning_rate=learning_rate)#default lr=0.001
        
        print('The training will at most stop at epoch:', max_epochs)
        #print('Training the LSTM without monitoring the validation set...')
        
        path_rst_stn = self.createFolder_ifNotExist(folder_name=station, 
                                                    dir_output=dir_output+'\\Model Training Results')
        
        #create LSTM/GRU
        if recurrent_type == 'LSTM':
            print('Creating LSTM...')
            regressor = self.create_LSTM(optimizer=opt, neurons=hidden_states,
                                    dropoutRate=dropout_rate,
                                    constraints=constraint)
            
            checkpoint = ModelCheckpoint(path_rst_stn+'\\LSTM_weights_at_epoch_{epoch:2d}', #to be fixed
                                         monitor='val_loss', verbose=1, 
                                         save_best_only=False, save_weights_only=True, 
                                         mode='auto', save_freq='epoch')
        elif recurrent_type == 'GRU':
            print('Creating GRU...')
            regressor = self.create_GRU(optimizer=opt, neurons=hidden_states,
                                    dropoutRate=dropout_rate,
                                    constraints=constraint)
        
            checkpoint = ModelCheckpoint(path_rst_stn+'\\GRU_weights_at_epoch_{epoch:2d}', 
                                         monitor='val_loss', verbose=1, 
                                         save_best_only=False, save_weights_only=True, 
                                         mode='auto', save_freq='epoch')
        else:
            print('Wrong recurrent type, go with LSTM anyway.')
            regressor = self.create_LSTM(optimizer=opt, neurons=hidden_states,
                                    dropoutRate=dropout_rate,
                                    constraints=constraint)
            
            checkpoint = ModelCheckpoint(path_rst_stn+'\\LSTM_weights_at_epoch_{epoch:2d}', 
                                         monitor='val_loss', verbose=1, 
                                         save_best_only=False, save_weights_only=True, 
                                         mode='auto', save_freq='epoch')
        
        r = regressor.fit(X_train, y_train, epochs=max_epochs, batch_size=batch_size, 
                          validation_data=(X_test, y_test), 
                          validation_freq=validation_freq, callbacks=[checkpoint])
        regressor.summary()
        #choose LSTM or GRU save history loss
        path_loss = self.createFolder_ifNotExist(folder_name="Train Loss History", 
                                dir_output=dir_output) 
        
        loss_history = pd.DataFrame(np.c_[range(1,max_epochs+1), r.history['loss'], r.history['val_loss']],
                                    columns = ['epoch', 'train_loss', 'validation_loss'])
        
        if recurrent_type == 'GRU':
            loss_history.to_csv(path_or_buf = path_loss+'\\'+station+'_GRU_loss_history.csv',
                                 index=False)
        else:
            loss_history.to_csv(path_or_buf = path_loss+'\\'+station+'_LSTM_loss_history.csv',
                                 index=False)

        print(loss_history)
        print('Traning and validation loss has been saved.')
        
        #Find the best_epoch, which has the lowest validation_loss and pass it to param_dict
        min_loss = loss_history.loc[0,'validation_loss']
        best_epoch = 1
        for i in range(1, len(loss_history)):
            #print(i)
            if loss_history.loc[i,'validation_loss'] < min_loss:
                min_loss = loss_history.loc[i,'validation_loss']
                best_epoch = int(loss_history.loc[i,'epoch'])
        
        self.param_dict['best_epoch'] = best_epoch
        print('The best epoch is: ', best_epoch)
        
        #Load the best epoch to predict
        try:
            if recurrent_type == 'GRU':
                regressor.load_weights(path_rst_stn+'\\GRU_weights_at_epoch_ '+
                                       str(best_epoch))#Skip compiling and fitting process
                print('GRU loaded successfully.')
            else:
                regressor.load_weights(path_rst_stn+'\\LSTM_weights_at_epoch_ '+
                                       str(best_epoch))#Skip compiling and fitting process
                print('LSTM loaded successfully.')
        except Exception as ex:
            messagebox.showerror(title='Failed to load the best model training results at epoch: '+str(best_epoch), message=ex)
            return

        sc_flow = MinMaxScaler(feature_range=(0, 1), copy=True)
        sc_flow.fit_transform(np.array(y_train_not_scaled).reshape(-1, 1))
        
        y_pred_scaled = regressor.predict(X_test)
        y_pred_test = sc_flow.inverse_transform(y_pred_scaled)
        
        y_pred_scaled_train = regressor.predict(X_train)
        y_pred_train = sc_flow.inverse_transform(y_pred_scaled_train)
        
        path_pred = self.createFolder_ifNotExist(folder_name=station, 
                                dir_output=dir_output+'\\Model Predictions') 
        
        # Saving prediction on train set
        pred_train = pd.DataFrame(np.c_[datetime_train_deNull,y_train_not_scaled,y_pred_train],
                                  columns = ['Datetime','Target_train_real','Target_train_pred'])
        pred_train.to_csv(path_or_buf = path_pred+'\\Train_Data.csv',
                                 index=False)

        # Saving prediction on test set
        pred_test = pd.DataFrame(np.c_[datetime_test_deNull,y_test_not_scaled,y_pred_test],
                                  columns = ['Datetime','Target_test_real','Target_test_pred'])
        pred_test.to_csv(path_or_buf = path_pred+'\\Test_Data.csv',
                                 index=False)
        
        print('RMSE on training set:')
        self.rootMSE(y_test=y_train_not_scaled, y_pred=y_pred_train)
        
        print('RMSE on test set:')
        self.rootMSE(y_test=y_test_not_scaled, y_pred=y_pred_test)

        messagebox.showinfo(title='Model Training Finished Successfully', 
                            message='Training results for station '+station+
                            ' have been saved at the folder: '+path_pred)
        # =============================================================================
        # Plotting
        # =============================================================================
        # Create a new Tkinter window to display figures
        newWindow = tk.Toplevel(self.master)
        newWindow.title("Matplotlib with Tkinter")
        
        # Create a new matplotlib figure and plot some data
        #1. train loss plot
        fig_1 = Figure(figsize=(8, 6), dpi=100)
        ax_1 = fig_1.add_subplot(111)
        
        ax_1.plot(range(1,max_epochs+1), r.history['loss'], label='loss')
        ax_1.plot(np.linspace(0,max_epochs,
                             int(max_epochs/validation_freq)+1,endpoint=True)[1:int(int(max_epochs/validation_freq)+1)], 
                 r.history['val_loss'], label='val_loss')
        ax_1.set_title('Train MSE Loss')
        ax_1.set_xlabel('No. of epoches')
        ax_1.set_ylabel('Mean square error')
        ax_1.legend()
        
        canvas_1 = FigureCanvasTkAgg(fig_1, master=newWindow)
        canvas_1.draw()
        
        #2. prediction results on training set
        fig_2 = Figure(figsize=(8, 6), dpi=100)
        ax_2 = fig_2.add_subplot(111)
        
        ax_2.plot(datetime_train_deNull, y_train_not_scaled, label='Monitored data-training set')
        ax_2.plot(datetime_train_deNull, y_pred_train, label='Predicted data-training set')
        ax_2.plot(datetime_test_deNull, y_test_not_scaled, label='Monitored data-testing set')
        ax_2.plot(datetime_test_deNull, y_pred_test, label='Predicted data-testing set')
        
        ax_2.set_title('Monitored and predicted data')
        ax_2.set_xlabel('Date')
        ax_2.set_ylabel('Target')
        ax_2.legend()
        
        canvas_2 = FigureCanvasTkAgg(fig_2, master=newWindow)
        canvas_2.draw()

        canvas_1.get_tk_widget().pack(side=tk.LEFT)
        canvas_2.get_tk_widget().pack(side=tk.LEFT)

        return#return to run_flow
    

    # =============================================================================
    # Other functions
    # =============================================================================
    def rootMSE(self, y_test, y_pred):
        import math
        from sklearn.metrics import mean_squared_error
        rmse = math.sqrt(mean_squared_error(y_test, y_pred))
        print('RMSE = %2.2f' % rmse)
        print('Predicted results length:', y_pred.shape)
        y_test = np.array(y_test).reshape(-1, 1)
        print('Real results length:', y_test.shape)
        return rmse
    
    def createFolder_ifNotExist(self, folder_name, dir_output):
        try:
            folder_name = str(folder_name)
            path = os.path.join(dir_output, folder_name)
            if not os.path.exists(path):
                os.makedirs(path)
                print(f"Folder '{folder_name}' created successfully.")
            else:
                print(f"Folder '{folder_name}' already exists.")
            return path
        except Exception as ex:
            messagebox.showerror(title='Failed to create the folder: '+folder_name, message=ex)
            return
        
    #@tf.function
    def create_LSTM(self, optimizer, neurons, dropoutRate, constraints):
        # Ignore the WARNING here, numpy version problem
        
        # Initializing the RNN
        regressor = Sequential()
        #regressor.add(Dropout(rate=0.2))

        # Adding the last LSTM layer and some Dropout regulariazation
        regressor.add(LSTM(units=neurons, return_sequences=False, recurrent_dropout=dropoutRate,
                           kernel_constraint=max_norm(constraints), recurrent_constraint=max_norm(constraints)))

        # Adding output layer
        regressor.add(Dense(units=1, kernel_initializer='random_normal', activation='relu'))# Output layer do not need specify the activation function
        
        # Compiling the RNN by usign right optimizer and right loss function
        regressor.compile(loss='mean_squared_error', optimizer=optimizer, metrics=['mse'])#adam to be changed
        return regressor
    
    def create_GRU(self, optimizer, neurons, dropoutRate, constraints):
        # Ignore the WARNING here, numpy version problem
        
        # Initializing the RNN
        regressor = Sequential()
        #regressor.add(Dropout(rate=0.2))

        # Adding the last GRU layer and some Dropout regulariazation
        regressor.add(GRU(units=neurons, return_sequences=False, recurrent_dropout=dropoutRate,
                           kernel_constraint=max_norm(constraints), recurrent_constraint=max_norm(constraints)))

        # Adding output layer
        regressor.add(Dense(units=1, kernel_initializer='random_normal', activation='relu'))# Output layer do not need specify the activation function
        
        # Compiling the RNN by usign right optimizer and right loss function
        regressor.compile(loss='mean_squared_error', optimizer=optimizer, metrics=['mse'])#adam to be changed
        return regressor

class Load_model_results():#To be finished
    def __init__(self, master, load_model, param_dict):
        self.master = master
        self.param_dict = param_dict
        #self.load_model = load_model#0 means new model; 1 means load previous training results
        
        #If did not record the best_epoch from run_RNN
        if self.param_dict['best_epoch'] == 0:
            self.param_dict['best_epoch'] = self.param_dict['max_epochs_flow']

        self.frm_left = tk.Frame(self.master)
        self.frm_right = tk.Frame(self.master)
        self.frm_top = tk.Frame(self.master)
        self.frm_bottom = tk.Frame(self.master)
        
        self.master.title('RNN Model Training Tool-Model Settings')
        self.master.geometry('800x300')
        
        self.frm_left.pack(side='left')
        self.frm_right.pack(side='right')
        self.frm_top.pack(side='top')
        self.frm_bottom.pack(side='bottom')
        
        e_font = 12
        
        # =============================================================================
        # Default values of results loading
        # =============================================================================
        if self.param_dict['recurrent_type_flow'] == 'GRU':#RNN type; 0 for LSTM and 1 for GRU; by default: 0
            self.dft_r_7 = tk.IntVar(value=1)
        else:
            self.dft_r_7 = tk.IntVar(value=0)
        
        dft_e_11 = tk.StringVar(value=self.param_dict['model_weight_dir'])#11. Output file directory
        
        dft_e_13 = tk.StringVar(value=self.param_dict['station'])#13. Station name
        
        # =============================================================================
        # Construct labels and entries 
        # =============================================================================
        #13. Station name
        var_L_13 = tk.StringVar()
        var_L_13.set('1. Please type in a name of the station/trail:')
        self.Lab_13 = tk.Label(self.frm_top, textvariable=var_L_13, bg='white', 
                              font=('Times New Roman', 12), height=1).pack()
        self.e_13 = tk.Entry(self.frm_top, show="", width=20, font=e_font, textvariable=dft_e_13)
        self.e_13.pack()

        #2. Hyperparameters
        #print(self.param_dict['train_mode_flow'])
        if self.param_dict['train_mode_flow'] == 'manual' or load_model == 1:
            self.btn_advSet = tk.Button(self.frm_bottom, text = 'Hyperparameters', 
                                        width = 25, command = self.new_window_add).pack()
        #1. Update
        self.btn_updateRst = tk.Button(self.frm_bottom, text = 'Load', width = 25, 
                                  command = self.load_weight).pack()
        #Quit
        self.btn_quit = tk.Button(self.frm_bottom, text = 'Quit', width = 25, 
                                  command = self.close_windows).pack()
        
        if load_model == 1:
            #11. Output file directory
            var_L_11 = tk.StringVar()
            var_L_11.set('2. Model weight directory:')
            self.Lab_11 = tk.Label(self.frm_top, textvariable=var_L_11, bg='white', 
                                font=('Times New Roman', 12), height=1).pack()
            self.e_11 = tk.Entry(self.frm_top, show="", width=80, font=e_font, textvariable=dft_e_11)
            self.e_11.pack()
        
        
        
        
        
        return
    
    
    def load_weight(self):
        try:
            #self.param_dict['RNN_avg_days_flow'] = int(self.e_2.get())
            
                        
            messagebox.showinfo(title='Previous Training Results Loaded', 
                                message='All advanced parameters have been updated successfully.')
            self.master.destroy()
        except Exception as ex:
            messagebox.showerror(title='Failed to load model training results', message=ex)
            return
        
        return
    
    def new_window_add(self):
        newWindow = tk.Toplevel(self.master)
        self.app = Additional_input(newWindow, self.param_dict)
        return
    
    def close_windows(self):
        self.master.destroy()
        return

class Start_menu:
    #confirm_data = False
    #confirm_model = False
    def __init__(self, master, param_dict):
        self.master = master
        self.param_dict = param_dict
        
        self.frm_left = tk.Frame(self.master)
        self.frm_right = tk.Frame(self.master)
        self.frm_top = tk.Frame(self.master)
        self.frm_bottom = tk.Frame(self.master)
        
        self.master.title('RNN Model Training Tool-Start Menu')
        self.master.geometry('1000x400')
        
        self.frm_left.pack(side='left')
        self.frm_right.pack(side='right')
        self.frm_top.pack(side='top')
        self.frm_bottom.pack(side='bottom')
        
        #Initializing values of entries
        #1. Data source selection
        if self.param_dict['data_source'] == 'raw':
            self.dft_r_1 = tk.IntVar(value=0)
        elif self.param_dict['data_source'] == 'preporcessed':
            self.dft_r_1 = tk.IntVar(value=1)
        
        #2. Model source selection
        if self.param_dict['model_source'] == 'new':
            self.dft_r_2 = tk.IntVar(value=0)
        elif self.param_dict['model_source'] == 'trained':
            self.dft_r_2 = tk.IntVar(value=1)
        
        #3. Training model selection: automatic (0) VS manual (1)
        if self.param_dict['train_mode_flow'] == 'manual':
            self.dft_r_3 = tk.IntVar(value=1)
        elif self.param_dict['train_mode_flow'] == 'automatic':
            self.dft_r_3 = tk.IntVar(value=0)
        
        #Top
        #Feature file directory
        self.var_L_3 = tk.StringVar()
        self.var_L_3.set('*Features file directory:*\n'+self.param_dict['dir_features'])
        
        self.Lab_3 = tk.Label(self.frm_top, textvariable=self.var_L_3, bg='white', 
                              font=('Times New Roman', 12), height=2).pack()
        
        #Target file directory
        self.var_L_4 = tk.StringVar()
        self.var_L_4.set('*Target file directory:*\n'+self.param_dict['dir_tar_flow'])
        
        self.Lab_4 = tk.Label(self.frm_top, textvariable=self.var_L_4, bg='white', 
                              font=('Times New Roman', 12), height=2).pack()
        
        #Target file directory
        self.var_L_5 = tk.StringVar()
        self.var_L_5.set('*Trained model directory:*\nNone')
        
        self.Lab_5 = tk.Label(self.frm_top, textvariable=self.var_L_5, bg='white', 
                              font=('Times New Roman', 12), height=2).pack()
        
        #Left
        #1. Data source selection
        self.var_L_1 = tk.StringVar()
        self.var_L_1.set('1. Please select the data source\n(raw data):')
        
        self.Lab_1 = tk.Label(self.frm_left, textvariable=self.var_L_1, bg='white', 
                              font=('Times New Roman', 12), height=2).pack()
        
        self.r_1_1 = tk.Radiobutton(self.frm_left, text='Start with raw data', 
                                    variable=self.dft_r_1, value=0,
                    command=self.print_r_1_selection)#.place(x=130, y=705, anchor='nw')
        self.r_1_2 = tk.Radiobutton(self.frm_left, text='Load pre-processed data', 
                                    variable=self.dft_r_1, value=1,
                    command=self.print_r_1_selection)#.place(x=190, y=705, anchor='nw')
        self.r_1_1.pack()
        self.r_1_2.pack()

        #confrim data button
        self.btn_conf_data = tk.Button(self.frm_left, text = 'Update Data Source', 
                                  width = 25, command = self.confirmData_btn).pack()
        
        #Right
        #2. Model source selection
        self.var_L_2 = tk.StringVar()
        self.var_L_2.set('2. Please select the model option\n(new model):')

        self.Lab_2 = tk.Label(self.frm_left, textvariable=self.var_L_2, bg='white', 
                              font=('Times New Roman', 12), height=2).pack()
        
        self.r_2_1 = tk.Radiobutton(self.frm_left, text='Train a new RNN', 
                                    variable=self.dft_r_2, value=0,
                    command=self.print_r_2_selection)#.place(x=130, y=705, anchor='nw')
        self.r_2_2 = tk.Radiobutton(self.frm_left, text='Load a previously trained RNN', 
                                    variable=self.dft_r_2, value=1,
                    command=self.print_r_2_selection)#.place(x=190, y=705, anchor='nw')
        self.r_2_1.pack()
        self.r_2_2.pack()
                
        #3. Training model selection: automatic (0) VS manual (1)
        
        self.var_L_6 = tk.StringVar()
        self.var_L_6.set('3. Training model selection (Manual mode):')
        self.Lab_6 = tk.Label(self.frm_left, textvariable=self.var_L_6, bg='white', 
                              font=('Times New Roman', 12), height=1).pack()
        self.r_3_1 = tk.Radiobutton(self.frm_left, text='Automatic', variable=self.dft_r_3, value=0,
                    command=self.print_r_3_selection)#.place(x=130, y=705, anchor='nw')
        self.r_3_2 = tk.Radiobutton(self.frm_left, text='Manual', variable=self.dft_r_3, value=1,
                    command=self.print_r_3_selection)#.place(x=190, y=705, anchor='nw')
        self.r_3_2.pack()
        self.r_3_1.pack()
        

        #confrim model button
        self.btn_conf_model = tk.Button(self.frm_left, text = 'Update Model Source', 
                                  width = 25, command = self.confirmModel_btn).pack()

        #Bottom
        #Run model button
        self.btn_conf_model = tk.Button(self.frm_right, text = 'Run Model', 
                                  width = 25, command = self.runModel_btn).pack()
        
        self.btn_quit = tk.Button(self.frm_right, text = 'Quit', width = 25, 
                                  command = self.close_windows).pack()

        #3. Training model selection: automatic (0) VS manual (1)
        if self.dft_r_3 == 0:
            self.param_dict['train_mode_flow'] = 'automatic'
        elif self.dft_r_3 == 1:
            self.param_dict['train_mode_flow'] = 'manual'

    def print_r_1_selection(self):
        if self.dft_r_1.get() == 0:
            str_print = '1. Please select the data source\n(raw data):'
        
        elif self.dft_r_1.get() == 1:
            str_print = '1. Please select the data source\n(pre-processed data):'
        
        self.var_L_1.set(str_print)
        return
    
    def print_r_2_selection(self):
        if self.dft_r_2.get() == 0:
            str_print = '2. Please select the model option\n(new model):'
        
        elif self.dft_r_2.get() == 1:
            str_print = '2. Please select the model option\n(trained model):'
        
        self.var_L_2.set(str_print)
        return
    
    def print_r_3_selection(self):
        if self.dft_r_3.get() == 0:
            str_print = '3. Training model selection (Automatic mode):'
            messagebox.showinfo(title='Automatic mode selected', 
                                message=
            '''            By selecting automatic mode, it is about 
            to take much longer time to find the best 
            combination of hyperparameters. If you already 
            know the best combination of them, please 
            input them into 'advanced settings' and switch to 
            'Manual' to save time.''')
        
        elif self.dft_r_3.get() == 1:
            str_print = '3. Training model selection (Manual mode):'
        
        self.var_L_6.set(str_print)
        return
    
    def confirmData_btn(self):
        print('confirmData_btn')
        if self.dft_r_1.get() == 0:
            print('Raw dataset window')
            
        elif self.dft_r_1.get() == 1:
            print('Pre-processed dataset window')
        
        self.param_dict['confirm_data'] = True
        
        #display a label
        self.var_L_3.set('Features file directory:\n'+self.param_dict['dir_features'])
        self.var_L_4.set('Target file directory:\n'+self.param_dict['dir_tar_flow'])
        return
    
    def confirmModel_btn(self):
        print('confirmModel_btn')
        newWindow = tk.Toplevel(self.master)
        if self.dft_r_2.get() == 0:
            print('Training new model window')
            self.app = Load_model_results(newWindow, self.dft_r_2.get(), self.param_dict)
        
        elif self.dft_r_2.get() == 1:
            print('Loading previously trained model window')
           
            #newWindow = tk.Toplevel(self.master)
            self.app = Load_model_results(newWindow, self.dft_r_2.get(), self.param_dict)
            
            self.var_L_5.set('Trained model directory:\n'+self.param_dict['model_weight_dir'])
        
        self.param_dict['confirm_model'] = True
        return
    
    def runModel_btn(self):
        print('runModel_btn')
        if self.param_dict['confirm_data'] and self.param_dict['confirm_model']:
            print('Running the RNN model with loaded data and model information...')
            
            
            
        else:
            messagebox.showerror(title='Data and/or model information missing', 
            message='''Please confirm the check to confirm both data and model before running the model.''')
            
        return

    def close_windows(self):
        self.master.destroy()
        return




def main(): 
    #Default values for ordinary/advanced parameters settings
    '''
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
        
        #Start menu
        'data_source': 'raw',#'raw' or 'preporcessed'
        'model_source': 'new',#'new' or 'trained'
        'confirm_data': False, #confirm if data is loaded
        'confirm_model': False, #confirm if the model is loaded
        'model_weight_dir': '',
                  }
    '''
    #for testing
    param_dict = {
        #Ordinary parameters
        #flow
        'dir_tar_flow': 'D:\\Study\\PhD_Project\\NRC_toolbox\\Testing\\Input\\Flowrate_test.csv',#2. Address of the flow rate target 
        'use_col_flow': 4,#4. Flowrate use column, exclude date column
        'use_col_flow_date': 3,#6. Datetime column of target
        #conc
        #'dir_tar_conc': 'D:\\MyFile\\MineDataConc.csv',#*. Address of the concentration target
        #'use_col_conc': 2,#4. Target use column, exclude date column
        #'use_col_conc_date': 1,#6. Datetime column of target
        
        #common
        'dir_features': 'D:\\Study\\PhD_Project\\NRC_toolbox\\Testing\\Input\\Weather_test.csv',#1. Address of input features
        'use_col_features': '5,6,7,8,9',#3. Features use columns, exclude date column, should be a list[] 
        'use_col_fea_date': 1,#5. Datetime column of features
        #'flowrate_threshold': 1.8,#7. Flow rate threshold for spring freshet
        'train_startDate': '1997/01/01',#8. Date when training set starts 
        'train_endDate': '1997/10/31',#8. Date when training set ends
        'test_startDate': '1997/10/31',#9. Date when test set starts
        'test_endDate': '1997/12/31',#10. Date when test set ends
        'dir_output': 'D:\\Study\\PhD_Project\\NRC_toolbox\\Testing\\Results',#11. Output file directory
        'train_mode_flow': 'manual',#12. Training model selection: automatic (0) VS manual (1)
        'station': 'APP_test_1',#13. Station name
        
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
        'max_epochs_flow': 5, #Max epoches
        'best_epoch': 0, #0 as initial value
        
        #common
        'validation_freq': 1,#Validation frequency
        #'tree_avg_days': 1, #SF average days
        'seed': 29,#Random seed
        
        #Start menu
        'data_source': 'raw',#'raw' or 'preporcessed'
        'model_source': 'new',#'new' or 'trained'
        'confirm_data': False, #confirm if data is loaded
        'confirm_model': False, #confirm if the model is loaded
        'model_weight_dir': 'D:\\Study\\PhD_Project\\NRC_toolbox\\Testing\\Results\\Model Training Results\\APP_test_1\\GRU_weights_at_epoch_ 1.data-00000-of-00001',
                  }
    #'''
    root = tk.Tk()
    
    #Ordinary_input(root, param_dict)
    Start_menu(root, param_dict)
    
    root.mainloop()
    
    return

if __name__ == '__main__':
    main()