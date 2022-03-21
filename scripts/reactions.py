class Reaction:
    #__init__ for the standard reactions
    def __init__(self,i,name,species,lnA,beta,eOverR,threeBodyBool,lindBool,troeBool,pressBool,pressLogDict,lnaFallOffDict,betaFallOffDict,eOverRFallOffDict,threeBodyDict,fallOffThreeBodyDict):
        self.index=i
        self.name=name
        self.lnA = lnA
        self.beta = beta
        self.eOverR = eOverR
        self.isThreeBody=threeBodyBool
        self.isLindemann=lindBool
        self.isTroe=troeBool
        self.isPressureLog=pressBool

        #reversability=1 if reversible, 0 if irreversible
        if('=>' in name):
            self.reversability=0
        else:
            self.reversability=1

        if(threeBodyBool==1):
            keys=threeBodyDict[i].keys()
            mValuesDict=threeBodyDict[i]
            for e in list(keys):
                mValuesDict[species[int(e)-1].name] = mValuesDict.pop(e)
        if(troeBool==1):
            self.lnAFallOff=lnaFallOffDict[i]
            self.betaFallOff=betaFallOffDict[i]
            self.eOverRFallOff=eOverRFallOffDict[i]

            #Now work on the threebody characteristics
            keys=fallOffThreeBodyDict[i].keys()
            mValuesDict=fallOffThreeBodyDict[i]
            for e in list(keys):
                mValuesDict[species[int(e)-1].name] = mValuesDict.pop(e)

        if(lindBool==1):
            self.lnAFallOff=lnaFallOffDict[i]
            self.betaFallOff=betaFallOffDict[i]
            self.eOverRFallOff=eOverRFallOffDict[i]

            #Now work on the threebody characteristics
            keys=fallOffThreeBodyDict[i].keys()
            mValuesDict=fallOffThreeBodyDict[i]
            for e in list(keys):
                mValuesDict[species[int(e)-1].name] = mValuesDict.pop(e)
            
        if(pressBool==1):
            self.pressureLogParam=pressLogDict[i]

        #Now we need to check that the reaction is neither a falloff or threebody reaction
        if(self.isLindemann==1 or self.isTroe==1):
            name = name.replace("(+M)", "+M")
            self.name=name
        #Now we start with the parsing of the names
        #We need to check if it is or not reversible
        if(self.reversability==0):
            parsed=self.name.split("=>")
            reactantList=parsed[0]
            productList=parsed[1]
        else:
            parsed=self.name.split("=")
            reactantList=parsed[0]
            productList=parsed[1]
        
        reactants=reactantList.split('+')
        reactName=[]
        reactNum=[]
        numeric='0'
        i=0
        for e in reactants:
            flag=0
            j=0
            for char in e:
                if((char.isnumeric() or char=='.') and flag==0):
                    numeric = numeric + char
                else:
                    if(flag==0):
                        flag=1
                        reactName.insert(i,e[j:])
                        if(numeric=='0'):
                            numeric='1'
                        reactNum.insert(i,numeric)
                j=j+1
            i=i+1
        reactValues=[float(x) for x in reactNum]
        products=productList.split('+')
        prodName=[]
        prodNum=[]
        i=0
        for e in products:
            numeric='0'
            flag=0
            j=0
            for char in e:
                if((char.isnumeric() or char=='.') and flag==0):
                    numeric = numeric + char
                else:
                    if(flag==0):
                        flag=1
                        prodName.insert(i,e[j:])
                        if(numeric=='0'):
                            numeric='1'
                        prodNum.insert(i,numeric)
                j=j+1
            i=i+1
        prodValues=[float(x) for x in prodNum]
        self.reactants=dict(zip(reactName,reactValues))
        self.products=dict(zip(prodName,prodValues))
        #We change the value of the M key
        if(self.isThreeBody==1 or self.isLindemann==1 or self.isTroe==1):
            self.reactants['M']=mValuesDict
            self.products['M']=mValuesDict