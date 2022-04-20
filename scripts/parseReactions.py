import xml.etree.ElementTree as ET

#Gets the strings with the kinetics file and the reaction names file

def parseReactions(dataKinetics,dataNames):
    #Parse the file
    tree = ET.parse(dataNames)
    root = tree.getroot()
    #Now we get the reaction-names
    reactions=str.splitlines(root[1].text)
    #We eliminate the first element as it is a blank space
    reactions.pop(0)

    #Once we have the names, now get the info from the kinetics file. First lnA
    tree = ET.parse(dataKinetics)
    root = tree.getroot()
    lnAString=str.splitlines(root[9][15][0][0].text)[:-1]
    lnAString.pop(0)
    lnAString.pop(0)
    lnA=[]
    i=0
    for row in lnAString:
        lnA.insert(i,float(row))
        i=i+1

    #then beta values
    betaString=str.splitlines(root[9][15][0][2].text)[:-1]
    betaString.pop(0)
    betaString.pop(0)
    beta=[]
    i=0
    for row in betaString:
        beta.insert(i,float(row))
        i=i+1

    #now eOverR
    eOverRString=str.splitlines(root[9][15][0][3].text)[:-1]
    eOverRString.pop(0)
    eOverRString.pop(0)
    eOverR=[]
    i=0
    for row in eOverRString:
        eOverR.insert(i,float(row))
        i=i+1
    
    #Now we get the indexes of the threebody reactions
    list=str.splitlines(root[9][5].text)
    list.pop(0)
    list.pop(0)
    i=0
    threeBodyList=[]
    for e in list:
        aux=e.split(' ')[:-1]
        for number in aux:
            threeBodyList.insert(i,int(float(number)))
            i=i+1
    
    #Now we take the parameters of the threebody reactions. 
    listOfThreebody=root[9][15][1]
    listOfParameters=[]
    i=0
    for row in listOfThreebody:
        list=str.splitlines(row.text)[1:]
        speciesIndex=list[0].split()[1:]
        speciesNumber=list[1].split()[1:]
        speciesN=[float(x) for x in speciesNumber]
        listDict=dict(zip(speciesIndex,speciesN))
        listOfParameters.insert(i,listDict)
        i=i+1
    #It is a dictionary of dictionaries. Each ThreeBody reaction has a dict associated
    #with its species and values in it
    threeBodyDict=dict(zip(threeBodyList,listOfParameters))


    #Now we get the indexes of the falloff reactions to create the dictionaries
    list=str.splitlines(root[9][6].text)
    list.pop(0)
    list.pop(0)
    i=0
    falloffList=[]
    for e in list:
        aux=e.split(' ')[:-1]
        for number in aux:
            falloffList.insert(i,int(float(number)))
            i=i+1
    
    #Now we get the threebody parameters for the falloff reactions in the same way we did with threebody reactions
    threeBodyFallOff=root[9][15][2][3]
    listOfParameters=[]
    i=0
    for row in threeBodyFallOff:
        list=str.splitlines(row.text)[2:]
        speciesIndex=list[1].split()[1:]
        speciesNumber=list[2].split()[1:]
        speciesN=[float(x) for x in speciesNumber]
        listDict=dict(zip(speciesIndex,speciesN))
        listOfParameters.insert(i,listDict)
        i=i+1
    #It is a dictionary of dictionaries. Each ThreeBody reaction has a dict associated
    #with its species and values in it
    fallOffThreeBodyDict=dict(zip(falloffList,listOfParameters))


    #Now we get the indexes of the lindemann(falloff) reactions
    list=str.splitlines(root[9][6][0].text)
    list.pop(0)
    list.pop(0)
    i=0
    lindList=[]
    for e in list:
        aux=e.split(' ')[:-1]
        for number in aux:
            lindList.insert(i,int(float(number)))
            i=i+1
    
    #Now we get the indexes of the troe(falloff) reactions
    list=str.splitlines(root[9][6][1].text)
    list.pop(0)
    list.pop(0)
    i=0
    troeList=[]
    for e in list:
        aux=e.split(' ')[:-1]
        for number in aux:
            troeList.insert(i,int(float(number)))
            i=i+1
    
    #We get the parameters specific for the TROE reactions
    list=root[9][15][2][3]
    listOfParameters=[]
    i=0
    for row in threeBodyFallOff:
        line=str.splitlines(row.text)[1]
        name=line.split(" ")[0]
        if(name=="troe"):
            values=line.split(" ")[2:-1]
            valuesN=[float(x) for x in values]
            listOfParameters.insert(i,valuesN)
            i=i+1
    #It is a dictionary of dictionaries. Each ThreeBody reaction has a dict associated
    #with its species and values in it
    troeCoefList=dict(zip(troeList,listOfParameters))
    
    #Now we get the indexes of the pressureLog reactions
    list=str.splitlines(root[9][9].text)
    list.pop(0)
    list.pop(0)
    i=0
    pressLogList=[]
    for e in list:
        aux=e.split(' ')[:-1]
        for number in aux:
            pressLogList.insert(i,int(float(number)))
            i=i+1

    #Now we will get the parameters for the pressurelog
    pressLogString=str.splitlines(root[9][15][3].text)
    pressLogString.pop(0)
    pressLogString=pressLogString[1::2]
    pressLogParam=[]
    i=0
    for row in pressLogString:
        values=row.split(' ')[:-1]
        valuesN=[float(x) for x in values]
        pressLogParam.insert(i,valuesN)
        i=i+1
    pressLogDict = dict(zip(pressLogList,pressLogParam))

    #Now get the specific parameters for fallOff reactions
    lnafallOffString=str.splitlines(root[9][15][2][0].text)[-1]
    lnafallOffString=lnafallOffString.split(' ')[:-1]
    lnafallOffParam=[float(x) for x in lnafallOffString]
    lnaFallOffDict=dict(zip(falloffList,lnafallOffParam))

    betafallOffString=str.splitlines(root[9][15][2][1].text)[-1]
    betafallOffString=betafallOffString.split(' ')[:-1]
    betafallOffParam=[float(x) for x in betafallOffString]
    betaFallOffDict=dict(zip(falloffList,betafallOffParam))

    eOverRfallOffString=str.splitlines(root[9][15][2][2].text)[-1]
    eOverRfallOffString=eOverRfallOffString.split(' ')[:-1]
    eOverRfallOffParam=[float(x) for x in eOverRfallOffString]
    eOverRFallOffDict=dict(zip(falloffList,eOverRfallOffParam))


    return reactions,lnA,beta,eOverR,threeBodyList,lindList,troeList,pressLogList,pressLogDict,lnaFallOffDict,betaFallOffDict,eOverRFallOffDict,threeBodyDict,fallOffThreeBodyDict,troeCoefList