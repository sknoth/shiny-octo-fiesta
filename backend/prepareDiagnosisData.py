# -*- coding: utf-8 -*-
import json
import xlrd

workbook = xlrd.open_workbook('../data/AcuteGlucose 2014 11 13 Diagnoses and care episodes Rg Kbg 2.xlsx')
sheet = workbook.sheet_by_index(1)

dDict = {}
dKeys = []

for row in range(2, sheet.nrows):
    
    diagnosis = sheet.row(row)[7].value
    
    s = []
    dLen = len(diagnosis)
    
    # prepare tree nodes
    i = 1
    while i <= dLen:
        s.append(diagnosis[0:i])
        i += 1      
     
    # added all part diagnosis keys for later referencing    
    dKeys.extend(s)

    # initialize tree stucture
    if not dDict.get(s[0]):
        dDict[s[0]] = {}
        
    if not dDict[s[0]].get(s[1]):
        dDict[s[0]][s[1]] = {}
        
    if not dDict[s[0]][s[1]].get(s[2]):
        dDict[s[0]][s[1]][s[2]] = {}
    
    if not dDict[s[0]][s[1]][s[2]].get(s[3]):
        dDict[s[0]][s[1]][s[2]][s[3]+'+'] = {}
        dDict[s[0]][s[1]][s[2]][s[3]] = 1
        dKeys.append(s[3]+'+')
        
    if dLen > 4 and not dDict[s[0]][s[1]][s[2]][s[3]+'+'].get(s[4]):
        dDict[s[0]][s[1]][s[2]][s[3]+'+'][s[4]] = 1
        
    # populate tree
    dDict[s[0]][s[1]][s[2]][s[3]] += 1
    
    if dLen > 4:
        dDict[s[0]][s[1]][s[2]][s[3]+'+'][s[4]] += 1
    

output = {
    'diagnosis': dDict
}

with open('result.json', 'w') as fp:
    json.dump(output, fp)
    
dKeys = list(set(dKeys))

with open('dKeys.json','w') as fp:
    json.dump(dKeys, fp)