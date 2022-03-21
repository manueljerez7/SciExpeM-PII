from species import Species

def compareElements(el1,el2):
    equal = 1
    if(el1.elementComp == el2.elementComp):
        #They have same element composition, now compare other values
        #As we could have same values but disordered, we sort and compare
        if(sorted(el1.nasaCoef)==sorted(el2.nasaCoef) and sorted(el1.lennJones)==sorted(el2.lennJones)):
            pass
        else:
            equal=0
    else:
        equal=0
    return equal