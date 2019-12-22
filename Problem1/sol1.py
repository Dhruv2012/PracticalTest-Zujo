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
    frame_head = []
    count = 0
    for member in root.findall('frames'):
        fr = []
        if count ==0:
            FRAME = member.find('frame').tag
            frame_head.append(FRAME)
            ID = member.find('id').tag
            frame_head.append(ID)
            XTL = member.find('xtl').tag
            frame_head.append(XTL)
            YTL = member.find('ytl').tag
            frame_head.append(YTL)
            XBR = member.find('xbr').tag
            frame_head.append(XBR)
            YBR = member.find('ybr').tag
            frame_head.append(YBR)
            LABEL = member.find('label').tag
            frame_head.append(LABEL)
            COMPLEXITY = member.find('complexity').tag
            frame_head.append(COMPLEXITY)
            csvwriter.writerow(frame_head)
            count = count+1
        FRAME = member.find('frame').text
        fr.append(FRAME)
        ID = member.find('id').text
        fr.append(ID)
        XTL = member.find('xtl').text
        fr.append(XTL)
        YTL = member.find('ytl').text
        fr.append(YTL)
        XBR = member.find('xbr').text
        fr.append(XBR)
        YBR = member.find('ybr').text
        fr.append(YBR)
        LABEL = member.find('label').text
        fr.append(LABEL)
        COMPLEXITY = member.find('complexity').text
        fr.append(COMPLEXITY)
        csvwriter.writerow(fr)
    frame_data1.close()
 
# XML TO CSV CONVERSION 
print(" ")
print("CSV Files created:")
for filename in os.listdir(INPUT_DIR):
    if not filename.endswith('.xml'): continue
    input_fullname = os.path.join(INPUT_DIR, filename)
    output_fullname = os.path.splitext(input_fullname)[0] + '_csv.csv'
    print(output_fullname)
    xmltocsv(input_fullname,output_fullname)
    
    