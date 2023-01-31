# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 09:41:34 2023

@author: Administrator
"""

import tkinter as tk
from tkinter import messagebox



class Ordinary_input:
    def __init__(self, master):
        self.master = master
        self.master.title('New Model Training Tool-General Settings')
        self.master.geometry('1000x700')
        
        #Frames, different packing ways
        self.frm_left = tk.Frame(self.master)
        self.frm_right = tk.Frame(self.master)
        self.frm_bottom = tk.Frame(self.master)
        
        self.btn_advSet = tk.Button(self.frm_bottom, text = 'Advanced settings', width = 25, command = self.new_window)
        self.btn_advSet.pack()
        
        self.btn_conf = tk.Button(self.frm_bottom, text = 'Advanced settings', width = 25, command = self.new_window)
        
        self.frm_left.pack(side='left')
        self.frm_right.pack(side='right')
        self.frm_bottom.pack(side='bottom')
        
        return

    def new_window(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = Additional_input(self.newWindow)
        return
    
    def confirm_ord(self):
        
        return
        
        

class Additional_input:
    def __init__(self, master):
        self.master = master
        
        self.frm_left = tk.Frame(self.master)
        self.frm_right = tk.Frame(self.master)
        self.frm_bottom = tk.Frame(self.master)
        
        self.master.title('New Model Training Tool-Advanced Settings')
        
        self.frm_left.pack(side='left')
        self.frm_right.pack(side='right')
        self.frm_bottom.pack(side='bottom')
        
        #Default values of additional input
        dft_e_1 = tk.StringVar(self.frm_right, value='1')#SF average days
        dft_e_2 = tk.StringVar(self.frm_right, value='6')#SF average days
        
        
        #LEFT, labels
        var_L_00 = tk.StringVar()
        var_L_00.set('Parameter Names')
        self.Lab_00 = tk.Label(self.frm_left, textvariable=var_L_00, bg='white', font=('Times New Roman', 12), height=2).pack()
        #1. SF average days
        var_L_1 = tk.StringVar()
        var_L_1.set('Spring freshet average days:')
        self.Lab_1 = tk.Label(self.frm_left, textvariable=var_L_1, bg='white', font=('Times New Roman', 12), height=1).pack()
        #2. Flow/concentration average days
        var_L_2 = tk.StringVar()
        var_L_2.set('Flow rate & concentration average days:')
        self.Lab_2 = tk.Label(self.frm_left, textvariable=var_L_2, bg='white', font=('Times New Roman', 12), height=1).pack()
        
        
        #RIGHT, entries
        var_L_01 = tk.StringVar()
        var_L_01.set('Parameter Values')
        self.Lab_01 = tk.Label(self.frm_right, textvariable=var_L_01, bg='white', font=('Times New Roman', 12), height=2).pack()
        #1. SF average days
        self.e_1 = tk.Entry(self.frm_right, show="", width=10, font=6, textvariable=dft_e_1).pack()
        #2. Flow/concentration average days
        self.e_2 = tk.Entry(self.frm_right, show="", width=10, font=6, textvariable=dft_e_2).pack()
        
        
        #Bottom
        self.btn_quit = tk.Button(self.frm_bottom, text = 'Quit', width = 25, command = self.close_windows)
        self.btn_quit.pack()
        
        return

    def update_adv(self):
        
        return
    
    def close_windows(self):
        self.master.destroy()
        return

def main(): 
    root = tk.Tk()
    
    
    
    
    
    Ordinary_input(root)
    root.mainloop()
    
    return

if __name__ == '__main__':
    main()