from math import log 
def calcShonnonEnt(dataSet):
    numEntries = len(dataSet)
    labelCounts = {}
    shannonEnt = 0.0
    for featVec in dataSet:
        currentLabel = featVec[-1]
        if currentLabel not in labelCounts.keys():
	    labelCounts[currentLabel]=1
	else:
	    labelCounts[currentLabel]+=1
    shannonEnt = 0.0
    for key in labelCounts:
        prob = float(labelCounts[key])/numEntries
        shannonEnt -= prob * log(prob,2)
    return shannonEnt
def creatDataSet():
    dataSet = [[1,1,'yes'],[1,1,'yes'],[1,0,'no'],[0,0,'no'],[0,0,'no']]
    labels =['no surfacing','flippers']
    return dataSet,labels
#myDat,labels = creatDataSet()
#var = calcShonnonEnt(myDat)
#print "%r" %var
def splitDataSet(dataSet,axis,value):
    returnDataSet = []
    for dataVec in dataSet:
        if dataVec[axis] == value:
            tmp = dataVec[:axis]
            tmp.extend(dataVec[axis+1:])
            returnDataSet.append(tmp)
    return returnDataSet
myDat,labels = creatDataSet()
#ret = splitDataSet(myDat,0,1)
#print"%r" %ret
def chooseBestFeatureToSplit(dataSet):
    numOfFeatures = len(dataSet[0])-1
    bestInfoGain = 0.0
    baseEntropy = calcShonnonEnt(dataSet)
    selectfeat = -1;
    for num in range(numOfFeatures):
        feat = [example[num] for example in dataSet]
        featSet = set(feat)
        newEntropy = 0.0
        for value in featSet:
            subDataSet = splitDataSet(dataSet,num,value)
            prob = len(subDataSet)/float(len(dataSet))
            newEntropy += prob * calcShonnonEnt(subDataSet)
        infoGain = baseEntropy - newEntropy
        if(infoGain > bestInfoGain):
            selectfeat = num
            bestInfoGain = infoGain
    return selectfeat
best = chooseBestFeatureToSplit(myDat)
print "%r" %best