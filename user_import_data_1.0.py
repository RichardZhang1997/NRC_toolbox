# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 12:59:35 2023

@author: Richa
"""

import tkinter as tk

#from tkinter import *
import os
import pandas as pd
#import math

#Acyclic parameter
No_line_conf = False#confirm that the no. of line has been got
No_col_conf = False#confirm that the no. of column has been got

#Main window of the input part
window_dir = tk.Tk()
window_dir.title('Data-importing Tool')
window_dir.geometry('1000x700')

#frm_main = tk.Frame(window_dir)
#frm_main.pack()

#frm_l = tk.Frame(frm_main)
#frm_l.pack(side='left')

# =============================================================================
# 1. File directory to get 'dir_string'
# =============================================================================
#Label for address
var_l_1 = tk.StringVar()
var_l_1.set('''1. Please input the file (.csv) directory like: "D:\\MyFile\\MineData.csv". ''')
l_1 = tk.Label(window_dir, textvariable=var_l_1, bg='white', font=('Times New Roman', 12), height=4)
l_1.place(x=0, y=0, anchor='nw')

#Entry for address
# e = tk.Entry(window, show="*")
e_1 = tk.Entry(window_dir, show="", width=40, font=5)#Input text window
e_1.place(x=500, y=30, anchor='nw')

#print(tk.messagebox.showinfo(title='Your directory is:', message=str(var)))

#t = tk.Text(window_dir, height=2)
#t.pack()

# =============================================================================
# 5. If line/column a feature to get use_col_conf.get()
# =============================================================================
def print_l_5_selection():
    #print(use_col_conf.get())
    if use_col_conf.get() == 1: 
        #tk.messagebox.showinfo(title='Testing line/col selection', 
        #                       message='4. Is each column or each line a feature? (Columns are features.)')
        str_print = '2. Is each line or each column a feature? (Columns are features.)'
    else:
        #tk.messagebox.showinfo(title='Testing line/col selection', 
        #                       message='4. Is each column or each line a feature? (Lines are features.)')
        str_print = '2. Is each line or each column a feature? (Lines are features.)'
    var_l_5.set(str_print)
    #return

#Label 
var_l_5 = tk.StringVar()
var_l_5.set('''2. Is each line or each column a feature? ''')

l_5 = tk.Label(window_dir, textvariable=var_l_5, bg='white', font=('Times New Roman', 12), height=4)
l_5.place(x=0, y=70, anchor='nw')#y+70 from last label

#If use column as feature
use_col_conf = tk.IntVar(value=1)#By default each column is a feature

r1 = tk.Radiobutton(window_dir, text='Each Column is a feature.',
                    variable=use_col_conf, value=1,
                    command=print_l_5_selection)
r1.place(x=700, y=105, anchor='nw')

r2 = tk.Radiobutton(window_dir, text='Each Line is a feature.',
                    variable=use_col_conf, value=0,
                    command=print_l_5_selection)
r2.place(x=500, y=105, anchor='nw')


# =============================================================================
# 2. Start line and column to get 'No_lin' & 'No_col'
# =============================================================================
var_l_2 = tk.StringVar()
#var_l_3 = tk.StringVar()

var_l_2.set('''3. Please input which line & column you want to start reading from: ''')
#var_l_3.set('''2. Please input which COLUMN you want to start reading from: ''')

l_2 = tk.Label(window_dir, textvariable=var_l_2, bg='white', font=('Times New Roman', 12), height=4)
l_2.place(x=0, y=140, anchor='nw')#y+70 from last label

#Entry for line and column
# e = tk.Entry(window, show="*")
e_2_1 = tk.Entry(window_dir, show="", width=10, font=5)#Input line window
e_2_1.place(x=500, y=170, anchor='nw')

e_2_2 = tk.Entry(window_dir, show="", width=10, font=5)#Input column window
e_2_2.place(x=700, y=170, anchor='nw')

# =============================================================================
# 3. Use columns list to get 'use_col'
# =============================================================================
#Label for use_col
var_l_3 = tk.StringVar()
var_l_3.set('''4. Please input which line/column of the features you want to read:
(e.g., if your features are in columns, [1, 2] means using the first 
and second columns in the origianl file.)
            ''')

l_3 = tk.Label(window_dir, textvariable=var_l_3, bg='white', font=('Times New Roman', 12), height=4)
l_3.place(x=0, y=210, anchor='nw')#y+70 from last label

#Entry for use_col
e_3 = tk.Entry(window_dir, show="", width=40, font=5)#Input line window
e_3.place(x=500, y=235, anchor='nw')

#Declare the target list 'use_col'
use_col = []

# =============================================================================
# 4. Choose which feature is Datetime to get date_col
# =============================================================================
#Label
var_l_4 = tk.StringVar()
var_l_4.set('5. Please input which column/line listed in Entry 4 is the datetime \n(YYYY-MM-DD): ')

l_4 = tk.Label(window_dir, textvariable=var_l_4, bg='white', font=('Times New Roman', 12), height=4)
l_4.place(x=0, y=280, anchor='nw')#y+70 from last label

#Entry
e_4 = tk.Entry(window_dir, show="", width=10, font=5)#Input line window
e_4.place(x=500, y=310, anchor='nw')

# =============================================================================
# 6. Output directory to get out_string
# =============================================================================
#Label 
var_l_6 = tk.StringVar()
var_l_6.set('''6. Please input the output directory like: "D:\\MyFile\\myMineData". ''')

l_6 = tk.Label(window_dir, textvariable=var_l_6, bg='white', font=('Times New Roman', 12), height=4)
l_6.place(x=0, y=350, anchor='nw')#y+70 from last label

#Entry for address
# e = tk.Entry(window, show="*")
e_6 = tk.Entry(window_dir, show="", width=40, font=5)#Input text window
e_6.place(x=500, y=385, anchor='nw')

# =============================================================================
# 7. Output file name to get get_out_name_string
# =============================================================================
#Label 
var_l_7 = tk.StringVar()
var_l_7.set('''6. Please input the file name: ''')

l_7 = tk.Label(window_dir, textvariable=var_l_7, bg='white', font=('Times New Roman', 12), height=4)
l_7.place(x=0, y=420, anchor='nw')#y+70 from last label

#Entry for address
# e = tk.Entry(window, show="*")
e_7 = tk.Entry(window_dir, show="", width=30, font=5)#Input text window
e_7.place(x=500, y=455, anchor='nw')

# =============================================================================
# Confirm button
# =============================================================================
def confm_button():
    from tkinter import messagebox
    global data, raw_data, dir_string, No_lin, No_line_conf, No_col, No_col_conf
    try:
        #Get directory
        dir_string = e_1.get()
        #t.insert('insert', var)
        #display_str = ''
        #tk.messagebox.showinfo(title='Input updated', 
        #                       message='Your file directory is:'+str(dir_string))
        var_l_1.set('1. Please input the file (.csv) directory like: "D:\\MyFile\\MineData.csv". \nFile directory received.')
        
        #Use column or line as feature ()
        if use_col_conf.get() == 1:
            use_col_boolen = True
        elif use_col_conf.get() == 0:
            use_col_boolen = False
        #print('If use columns as features:', use_col_boolen)
            
        #Get No. of line
        No_lin = int(e_2_1.get())
        #tk.messagebox.showinfo(title='Input updated', message='Read from the line of:'+str(No_lin))
        No_line_conf = True
        if No_col_conf:
            var_l_2.set('''3. Please input which line (Confirmed) & column (Confirmed) \nyou want to start reading from: ''')
        else:
            var_l_2.set('''3. Please input which line (Confirmed) & column \nyou want to start reading from: ''')
        #Get No. of col
        No_col = int(e_2_2.get())
        #tk.messagebox.showinfo(title='Input updated', message='Read from the column of:'+str(No_col))
        
        No_col_conf = True
        if No_line_conf:
            var_l_2.set('''3. Please input which line (Confirmed) & column (Confirmed) \nyou want to start reading from: ''')
        else:
            var_l_2.set('''3. Please input which line & column (Confirmed) \nyou want to start reading from: ''')
        
        #Read the file
        if use_col_boolen:#when use columns as features
            try:
                raw_data = pd.read_csv(filepath_or_buffer=dir_string, skiprows=No_lin-2,
                                       header=1)
                raw_data.index = range(0,len(raw_data))
                raw_data = raw_data.iloc[:,No_col-1:]
                
            except Exception as ex:
                messagebox.showerror(title='Failed to open the data file', message=ex)
                return
        else:#when use lines as features
            try:
                raw_data = pd.read_csv(filepath_or_buffer=dir_string).T
                raw_data.index = range(0,len(raw_data))
                raw_data = raw_data.iloc[No_col-1:,No_lin-2:]
                raw_data.columns = raw_data.iloc[0,:]
                raw_data = raw_data.iloc[1:,:]
                raw_data.index = range(0,len(raw_data))
            except Exception as ex:
                messagebox.showerror(title='Failed to open and read the data file', message=ex)
                return
        
        #Delete the lines and columns where all nans
        #raw_data.dropna(axis=1, how='all',inplace=True)
        #raw_data.dropna(axis=0, how='all',inplace=True)
        #raw_data.index = range(0,len(raw_data))
        
    except Exception as ex:
        #Directory 
        messagebox.showerror(title='Wrong directory', message=ex)
        
        #No. of line 
        if No_col_conf:
            var_l_2.set('''3. Please input which line & column (Confirmed) \nyou want to start reading from: ''')
        else:
            var_l_2.set('''3. Please input which line & column you want to start reading from: ''')
        #No. of col
        if No_line_conf:
            var_l_2.set('''3. Please input which line (Confirmed) & column \nyou want to start reading from: ''')
        else:
            var_l_2.set('''3. Please input which line & column you want to start reading from: ''')
        return
    #print('Raw data:\n', raw_data)
    
    #Feature selection
    global use_col, date_col
    try:
        use_col = []
        str_use_col = e_3.get()
        str_use_col = str_use_col.split(sep=',')
        
        for num in str_use_col:
            use_col.append(int(num.strip()))
        use_col = list(set(use_col))#Deduplication
        
        var_l_3.set('''4. Please input which line/column of the features you want to read (Confirmed): ''')
        messagebox.showinfo(title='Input updated', message='Use the column: '+str(use_col))
        
        use_col_names = []
        for val in use_col:
            if use_col_boolen:
                val -= No_col
            else:
                val -= No_lin
            use_col_names.append(raw_data.columns[val])
        
        #raw_data.dropna(axis=1, how='all',inplace=True)
        #raw_data.dropna(axis=0, how='all',inplace=True)
        #raw_data.index = range(0,len(raw_data))
        
        data = pd.DataFrame(raw_data.dropna(axis=0, how='all').dropna(axis=1, how='all'), 
                            columns=use_col_names)
        data.index = range(0,len(data))
        #print('Use data with selected features:\n', data)

        #Input datetime column
        if use_col_boolen:
            date_col = int(e_4.get())-No_col
        else:
            date_col = int(e_4.get())-No_lin
        
        data['Datetime'] = pd.to_datetime(data[raw_data.columns[date_col]], 
                              format='%Y-%m-%d')
        data.drop(raw_data.columns[date_col], 1, inplace=True)
        
        #print('Datetime column:\n', data['Datetime'])
        #tk.messagebox.showinfo(title='Input updated', message='Datetime is the column/line of:'+str(date_col+1))
        var_l_4.set('5. Please input which column/line listed in Entry 4 is the datetime \n(Confirmed): ')
        #print('Date column:', date_col)
        
    except Exception as ex:
        
        messagebox.showerror(title='Wrong No. of column', message=ex)
        return
    
    #Output and save file
    global out_dir_string, out_name_string
    
    try:
        #Get output directory
        out_dir_string = e_6.get()
        #t.insert('insert', var)
        #display_str = ''
        #tk.messagebox.showinfo(title='Input updated', message='Your output directory is:'+str(out_dir_string))
        var_l_6.set('6. Please input the output directory like: "D:\\MyFile\\myMineData". \nOutput directory received.')
        
        #Get output file name
        out_name_string = e_7.get()
        #t.insert('insert', var)
        #display_str = ''
        #tk.messagebox.showinfo(title='Input updated', message='Your output file name is:'+str(out_name_string))
        var_l_6.set('6. Please input the output directory like: "D:\\MyFile\\myMineData". \nOutput directory received.')
        
        #Save the file
        os.chdir(out_dir_string)
        #tk.messagebox.showinfo(title='Directory is fine', message='The output directory has been set')
        
        data.to_csv(path_or_buf=out_dir_string+'\\'+out_name_string+'.csv',index=False)
        messagebox.showinfo(title='Processed data saved', 
                               message='The processed data has been saved successfully.')

    except Exception as ex:
        messagebox.showerror(title='Failed to save the output file', message=ex)
        return

    return 

tk.Button(window_dir, text="Confirm", command=confm_button,
          width=20, height=2, font=4).pack(side='bottom') #button to close the window

window_dir.mainloop()
