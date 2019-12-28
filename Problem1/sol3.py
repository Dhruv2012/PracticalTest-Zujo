#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 16:24:06 2019

@author: dhruv
"""

import xml.etree.ElementTree as ET
import csv
import os
INPUT_DIR = '/home/dhruv/PracTest_Zujo/Problem1'
# INPUT DIRECTORY OF ALL XML FILES
import pandas as pd
import numpy as np

def xmltocsv(input_path,output_path):
    tree = ET.parse(input_path)
    root = tree.getroot()
    frame_data1 =  open(output_path, 'w')
    csvwriter = csv.writer(frame_data1)
    label_head = []
    count =0
    for member in root.findall('track'):
        #print(member.attrib)
        
        for sub in member:
            #print(sub.attrib)
            fr = []
            if(count==0):
                label_head.append('frame')       
                label_head.append('id')
                label_head.append('xtl')
                label_head.append('ytl')
                label_head.append('xbr')
                label_head.append('ybr')
                label_head.append('label')
                label_head.append('complexity')
                csvwriter.writerow(label_head)
                count = count + 1
            FRAME = sub.attrib['frame']
            fr.append(FRAME)
            ID = member.attrib['id'] 
            fr.append(ID)
            XTL = sub.attrib['xtl']
            fr.append(XTL)
            YTL = sub.attrib['ytl']
            fr.append(YTL)
            XBR = sub.attrib['xbr']
            fr.append(XBR)
            YBR = sub.attrib['ybr']
            fr.append(YBR)
            LABEL = member.attrib['label']
            fr.append(LABEL)
            for subsub in sub:
                COMPLEXITY = subsub.text
            fr.append(COMPLEXITY)
            csvwriter.writerow(fr)
    frame_data1.close()
print(" ")
print("CSV Files created:")
for filename in os.listdir(INPUT_DIR):
    if not filename.endswith('.xml'): continue
    input_fullname = os.path.join(INPUT_DIR, filename)
    output_fullname = os.path.splitext(input_fullname)[0] + '_csv.csv'
    print(output_fullname)
    xmltocsv(input_fullname,output_fullname)
print(" ")


# READING CSV FILES
output1 = [] 
output2 = []
for filename in os.listdir(INPUT_DIR):
    if not filename.endswith('.csv'): continue
    count = 0
    input_fullname = os.path.join(INPUT_DIR, filename)
    df = pd.read_csv(input_fullname)
    x = []
    x = df[df['complexity']>=0.5]
    y = []
    y = df[df['complexity']>0.5]
    if(x.shape[0]==0):
        output1.append(os.path.splitext(filename)[0])
    if(y.shape[0]==0):
        output2.append(os.path.splitext(filename)[0])
        
# SHOWS CSV FILES WITH COMPLEXITY IS LESS THAN 0.5 
if(len(output1)==0):
    print("THERE ARE NO CSV FILES WITH COMPLEXITY < 0.5 IN ALL THE FRAMES.")
else:
    print("Files with complexity < 0.5 in all the frames are:")
    print(output1)    
print(" ")
if(len(output2)==0):
    print("THERE ARE NO CSV FILES WITH COMPLEXITY <=0.5")
else:
    print("Files with complexity <= 0.5 in all the frames are:")
    print(output2)

