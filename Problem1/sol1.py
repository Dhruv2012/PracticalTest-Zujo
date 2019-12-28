#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 00:53:09 2019

@author: dhruv
"""

import xml.etree.ElementTree as ET
import csv
import os
INPUT_DIR = '/home/dhruv/PracTest_Zujo/Problem1'
# INPUT DIRECTORY OF ALL XML FILES


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

