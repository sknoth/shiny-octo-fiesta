# -*- coding: utf-8 -*-
"""
Created on Sun Mar 04 17:09:06 2018

Create complete list of diagnosis Attributes that also contains part diagnoses

@author: Stefanie
"""

import json

dKeys = json.load(open('dKeys.json'))
diagnosisAttrs = json.load(open('diagnosisAttrs.json'))

dfa = diagnosisAttrs

for key in dKeys:  
    
    if key in diagnosisAttrs:
        continue
    
    else: 
        
        count = 0

        for k,v in diagnosisAttrs.items():
             
            if key.replace('+', '') in k:

                count += 1  
                
                if not key in dfa:
                    
                    dfa[key] = {
                        'lifeStatus': {'dead':0,'alive':0,'deadPercent':0,'alivePercent':0},
                        'gender': {'male':0,'female':0,'malePercent':0,'femalePercent':0},
                        'diabetes': {'yes':0,'no':0,'yesPercent':0,'noPercent':0},
                        'lengthOfStay': 0
                    }
                    
                else:                    
                    dfa[key]['lifeStatus']['dead'] += v['lifeStatus']['dead']
                    dfa[key]['lifeStatus']['alive'] += v['lifeStatus']['alive']
                    dfa[key]['diabetes']['no'] += v['diabetes']['no']
                    dfa[key]['diabetes']['yes'] += v['diabetes']['yes']
                    dfa[key]['gender']['male'] += v['gender']['male']
                    dfa[key]['gender']['female'] += v['gender']['female']
                    dfa[key]['lengthOfStay'] += v['lengthOfStay']
            
            if count > 0:
                
                if dfa[key]['lifeStatus']['dead']+dfa[key]['lifeStatus']['alive'] > 0:
                    dfa[key]['lifeStatus']['deadPercent'] = 1.0 * dfa[key]['lifeStatus']['dead'] / (dfa[key]['lifeStatus']['dead']+dfa[key]['lifeStatus']['alive']) * 100
                    dfa[key]['lifeStatus']['alivePercent'] = 100 - dfa[key]['lifeStatus']['deadPercent']
                if dfa[key]['diabetes']['no']+dfa[key]['diabetes']['yes'] > 0:                
                    dfa[key]['diabetes']['noPercent'] = 1.0 * dfa[key]['diabetes']['no'] / (dfa[key]['diabetes']['no']+dfa[key]['diabetes']['yes']) * 100
                    dfa[key]['diabetes']['yesPercent'] = 100 - dfa[key]['diabetes']['noPercent']
                if dfa[key]['gender']['female']+dfa[key]['gender']['male'] > 0:                
                    dfa[key]['gender']['malePercent'] = 1.0 * dfa[key]['gender']['male'] / (dfa[key]['gender']['female']+dfa[key]['gender']['male']) * 100
                    dfa[key]['gender']['femalePercent'] = 100 - dfa[key]['gender']['malePercent']           
                
                dfa[key]['lengthOfStay'] = v['lengthOfStay'] / count

count = 0   

dfa['diagnosis'] = {
    'lifeStatus': {'dead':0,'alive':0,'deadPercent':0,'alivePercent':0},
    'gender': {'male':0,'female':0,'malePercent':0,'femalePercent':0},
    'diabetes': {'yes':0,'no':0,'yesPercent':0,'noPercent':0},
    'lengthOfStay': 0
}     
        
for key in dKeys:

    if len(key) == 1:
        
        count += 1
        
        dfa['diagnosis']['lifeStatus']['dead'] += dfa[key]['lifeStatus']['dead']
        dfa['diagnosis']['lifeStatus']['alive'] += dfa[key]['lifeStatus']['alive']
        dfa['diagnosis']['diabetes']['no'] += dfa[key]['diabetes']['no']
        dfa['diagnosis']['diabetes']['yes'] += dfa[key]['diabetes']['yes']
        dfa['diagnosis']['gender']['male'] += dfa[key]['gender']['male']
        dfa['diagnosis']['gender']['female'] += dfa[key]['gender']['female']
        dfa['diagnosis']['lengthOfStay'] += dfa[key]['lengthOfStay']
        
if count > 0:
    
    if dfa['diagnosis']['lifeStatus']['dead']+dfa['diagnosis']['lifeStatus']['alive'] > 0:
        dfa['diagnosis']['lifeStatus']['deadPercent'] = 1.0 * dfa['diagnosis']['lifeStatus']['dead'] / (dfa['diagnosis']['lifeStatus']['dead']+dfa['diagnosis']['lifeStatus']['alive']) * 100
        dfa['diagnosis']['lifeStatus']['alivePercent'] = 100 - dfa['diagnosis']['lifeStatus']['deadPercent']
    if dfa['diagnosis']['diabetes']['no']+dfa['diagnosis']['diabetes']['yes'] > 0:                
        dfa['diagnosis']['diabetes']['noPercent'] = 1.0 * dfa['diagnosis']['diabetes']['no'] / (dfa['diagnosis']['diabetes']['no']+dfa['diagnosis']['diabetes']['yes']) * 100
        dfa['diagnosis']['diabetes']['yesPercent'] = 100 - dfa['diagnosis']['diabetes']['noPercent']
    if dfa['diagnosis']['gender']['female']+dfa['diagnosis']['gender']['male'] > 0:                
        dfa['diagnosis']['gender']['malePercent'] = 1.0 * dfa['diagnosis']['gender']['male'] / (dfa['diagnosis']['gender']['female']+dfa['diagnosis']['gender']['male']) * 100
        dfa['diagnosis']['gender']['femalePercent'] = 100 - dfa['diagnosis']['gender']['malePercent']           
    
    dfa['diagnosis']['lengthOfStay'] = v['lengthOfStay'] / count
        

with open('dfa.json', 'wb') as outfile:
    json.dump(dfa, outfile)