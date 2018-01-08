import json
import xlrd

wbAcute = xlrd.open_workbook('../data/AcuteGlucose 2014 11 13 Diagnoses and care episodes Rg Kbg 2.xlsx')
#wbDiabetes = xlrd.open_workbook('../data/AcuteGlucose  Diabetes Diagnoses 2005_201406 Rg Kbg 3.xlsx')
wbLab = xlrd.open_workbook('../data/AcuteGlucose Lab values 20140710 Rg Kbg 1.xlsx')

sheetAcute = wbAcute.sheet_by_index(1)          # ~25.000 entries
#sheetDiabetes = wbDiabetes.sheet_by_index(0)    # ~331.000 entries
sheetLab = wbLab.sheet_by_index(0)              # ~59.000 entries

diagnosisAttrs = {}

def getPIDs(diagnosis):
    pIDs = []
    for row in range(2, sheetAcute.nrows):
        if sheetAcute.row(row)[7].value == diagnosis:
            pIDs.append(sheetAcute.row(row)[0].value)
    #sprint(pIDs)
    return pIDs
    


def getGenderDistribution(diagnosis, pIDs):
    hitCounter = 0
    for pID in pIDs:
        for row in range(9,sheetLab.nrows):
            if sheetLab.row(row)[4].value == pID:
                if sheetLab.row(row)[5].value == 'M':
                    hitCounter += 1
                    break
        print(hitCounter)
    return {
        'male': hitCounter,
        'female': len(pIDs) - hitCounter,
        'malePercent': 1.0*hitCounter/len(pIDs)*100,
        'femalePercent': 100 - 1.0*hitCounter/len(pIDs)*100
    }





def initDiagnosisAttrs():

    for row in range(2, sheetAcute.nrows):
    
        diagnosis = sheetAcute.row(row)[7].value
        
        if not diagnosisAttrs.get(diagnosis):
            diagnosisAttrs[diagnosis] = {
                'lifeStatus':{'dead':0,'alive':0,'deadPercent':0,'alivePercent':0},
                'gender':{'male':0,'female':0,'malePercent':0,'femalePercent':0},
                'diabetes':0
            }
        
        if sheetAcute.row(row)[11].value == 'Avliden':
            diagnosisAttrs[diagnosis]['lifeStatus']['dead'] += 1
        else:
            diagnosisAttrs[diagnosis]['lifeStatus']['alive'] += 1
            
        diagnosisAttrs[diagnosis]['lifeStatus']['deadPercent'] = 1.0*diagnosisAttrs[diagnosis]['lifeStatus']['dead']/(diagnosisAttrs[diagnosis]['lifeStatus']['dead']+diagnosisAttrs[diagnosis]['lifeStatus']['alive'])*100
        diagnosisAttrs[diagnosis]['lifeStatus']['alivePercent'] = 100 - diagnosisAttrs[diagnosis]['lifeStatus']['deadPercent']
                
        print(diagnosisAttrs[diagnosis]['lifeStatus'])

initDiagnosisAttrs()

                
# getting annotation data for each diagnosis
for k,v in diagnosisAttrs.items(): 
    print(k,v)
    pIDs = getPIDs(k)
    diagnosisAttrs[k]['gender'] = getGenderDistribution(k,pIDs)

    
  

def getDiabetesPatients(diagnosis):
    pIDs = getPIDs(diagnosis)
    hitCounter = 0
    for pID in pIDs:
        for row in range(1,sheetDiabetes.nrows):
            if sheetDiabetes.row(row)[0].value == pID:
                hitCounter += 1
                break
        print(pID,hitCounter)
    print(len(pIDs,hitCounter))
    
#getDiabetesPatients('I109')

        
      
    