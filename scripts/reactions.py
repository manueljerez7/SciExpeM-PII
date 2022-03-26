from re import I
from species import Species
from species import findSpeciesByName

class Reaction:
    #__init__ for the standard reactions
    def __init__(self,i,name,species,lnA,beta,eOverR,threeBodyBool,lindBool,troeBool,pressBool,pressLogDict,lnaFallOffDict,betaFallOffDict,eOverRFallOffDict,threeBodyDict,fallOffThreeBodyDict,troeCoefList):
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
            self.reversability=False
        else:
            self.reversability=True

        if(threeBodyBool==True):
            keys=threeBodyDict[i].keys()
            mValuesDict=threeBodyDict[i]
            for e in list(keys):
                mValuesDict[species[int(e)-1].name] = mValuesDict.pop(e)
        if(troeBool==True):
            self.lnAFallOff=lnaFallOffDict[i]
            self.betaFallOff=betaFallOffDict[i]
            self.eOverRFallOff=eOverRFallOffDict[i]
            self.troeCoefficients=troeCoefList[i]

            #Now work on the threebody characteristics
            keys=fallOffThreeBodyDict[i].keys()
            mValuesDict=fallOffThreeBodyDict[i]
            for e in list(keys):
                mValuesDict[species[int(e)-1].name] = mValuesDict.pop(e)

        if(lindBool==True):
            self.lnAFallOff=lnaFallOffDict[i]
            self.betaFallOff=betaFallOffDict[i]
            self.eOverRFallOff=eOverRFallOffDict[i]

            #Now work on the threebody characteristics
            keys=fallOffThreeBodyDict[i].keys()
            mValuesDict=fallOffThreeBodyDict[i]
            for e in list(keys):
                mValuesDict[species[int(e)-1].name] = mValuesDict.pop(e)
            
        if(pressBool==True):
            self.pressureLogParam=pressLogDict[i]

        #Now we need to check that the reaction is neither a falloff or threebody reaction
        if(self.isLindemann==True or self.isTroe==True):
            name = name.replace("(+M)", "+M")
            self.name=name
        #Now we start with the parsing of the names
        #We need to check if it is or not reversible
        if(self.reversability==False):
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
        if(self.isThreeBody==True or self.isLindemann==True or self.isTroe==True):
            self.reactants['M']=mValuesDict
            self.products['M']=mValuesDict

        reactantList=[]
        i=0
        for e in list(self.reactants.keys()):
            if(e=='M'):
                pass
            else:
                obj=findSpeciesByName(e,species)
                reactantList.insert(i,obj)
                i=i+1
        self.reactantsObject=dict(zip(list(self.reactants.keys()),reactantList))
        productList=[]
        i=0
        for e in list(self.products.keys()):
            if(e=='M'):
                pass
            else:
                obj=findSpeciesByName(e,species)
                productList.insert(i,obj)
                i=i+1
        self.productsObject=dict(zip(list(self.products.keys()),productList))

        if(self.isThreeBody==True or self.isLindemann==True or self.isTroe==True):
            mSpeciesList=[]
            i=0
            for e in list(mValuesDict.keys()):
                obj=findSpeciesByName(e,species)
                mSpeciesList.insert(i,obj)
                i=i+1
            self.mSpeciesObject=dict(zip(list(mValuesDict.keys()),mSpeciesList))
