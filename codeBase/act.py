
######
# Includes:
######

from codeBase import const #custom constants used as default values
from codeBase import dep #custom functions that are dependencies

from manim import *
from manim.utils.color import Colors
from copy import deepcopy

######
# Custom Functions: Actionable
######

## special print to add tab or delim to a list of values
def printt(
	valList :list= [],
	delimStr :str= "\t",
) -> None:
	tempStr :str= ""
	for i in range(len(valList)):
		tempStr += str(valList[i]) + delimStr
	print(tempStr)
	pass

## get how many decimal places there are in float
def getDecimalCount(
	numFloat :float,
) -> int:
	numPlace :int= 0
	numSplit :str= str(numFloat).split(".")
	if len(numSplit) > 1:
		numPlace = len(numSplit[1])
	return numPlace
	pass

## convert a float by moving decimal into number
def floatAsNoDecimalInt(
	numFloat :float,
	numPlace :int,
) -> int:
	numMulti :int= pow(10,numPlace)
	numAdder :float= 0.5 / numMulti
	numCalc :int= int((numFloat + numAdder) * numMulti)
	return numCalc
	pass

## better float add / multiply without random offset errors
def floatAddorMulAsInt(
	numFloat :float,
	addFloat :float,
	doAddorMul :bool= True, #True = Add, False = Multiply
) -> float:
	placeOne :int= getDecimalCount(numFloat)
	floatOne :int= floatAsNoDecimalInt(numFloat,placeOne)
	placeTwo :int= getDecimalCount(addFloat)
	floatTwo :int= floatAsNoDecimalInt(addFloat,placeTwo)
	twoLarge :bool= placeTwo > placeOne
	newPlace :int= 0
	difPlace :int= 0
	numMulti :int= 0
	numCalc :int= 0
	newFloat :float= 0
	if doAddorMul:
		if twoLarge:
			difPlace = placeTwo - placeOne
			newPlace = placeTwo
			numMulti = pow(10,difPlace)
			floatOne *= numMulti
		else:
			difPlace = placeOne - placeTwo
			newPlace = placeOne
			numMulti = pow(10,difPlace)
			floatTwo *= numMulti
		numCalc = floatOne + floatTwo
		numMulti = pow(10,newPlace)
		newFloat = float(numCalc / numMulti)
		newFloat = roundFloatPlaces(newFloat,newPlace)
	else:
		numCalc = numFloat * addFloat
		newPlace = placeOne + placeTwo
		newFloat = roundFloatPlaces(numCalc,newPlace)
	return newFloat
	pass

## round floats nicely based on a set number of places
def roundFloatPlaces(
	numFloat :float,
	numPlace :int,
) -> float:
	numMulti :int= pow(10,numPlace)
	numAdder :float= 0.5 / numMulti
	numCalc :int= int((numFloat + numAdder) * numMulti)
	newFloat :float= (numCalc / numMulti)
	numWhole :int= int(newFloat)
	numDecim :int= int((newFloat - numWhole) * numMulti)
	if numDecim == 0:
		newFloat = numWhole
	return newFloat
	pass

## make a barebone list with all elements needed for table
def makeBaseTable(
	numCol :int= 1,
	numRow :int= 1,
	tableList :list= [],
	colrowSize :list= [],
	tableVgrList :list= [],
	#base
	timeRun :float= const.TimeRun,
	timeWait :float= const.TimeWait,
	txtSize :float= const.TxtSize,
	#normal
	colorTxt :Colors= const.ColorTxt,
	colorRec :Colors= const.ColorRec,
	colorStrokeTxt :Colors= const.ColorStrokeTxt,
	colorStrokeRec :Colors= const.ColorStrokeRec,
	#highlight
	highColorTxt :Colors= const.HighColorTxt,
	highColorRec :Colors= const.HighColorRec,
	highColorStrokeTxt :Colors= const.HighColorStrokeTxt,
	highColorStrokeRec :Colors= const.HighColorStrokeRec,
	#other
	opacityTxt :float= const.OpacityTxt,
	opacityRec :float= const.OpacityRec,
	strokeWidthTxt :float= const.StrokeWidthTxt,
	strokeWidthRec :float= const.StrokeWidthRec,
	#box
	recWidth :float= const.RecWidth,
	recHeight :float= const.RecHeight,
	padWidth :float= const.PadWidth,
	padHeight :float= const.PadHeight,
) -> list:
	allValues :list= []
	allValues.append(numCol)
	allValues.append(numRow)
	allValues.append(tableList)
	allValues.append(colrowSize)
	allValues.append(tableVgrList)
	allValues.append(timeRun)
	allValues.append(timeWait)
	allValues.append(txtSize)
	allValues.append(colorTxt)
	allValues.append(colorRec)
	allValues.append(colorStrokeTxt)
	allValues.append(colorStrokeRec)
	allValues.append(highColorTxt)
	allValues.append(highColorRec)
	allValues.append(highColorStrokeTxt)
	allValues.append(highColorStrokeRec)
	allValues.append(opacityTxt)
	allValues.append(opacityRec)
	allValues.append(strokeWidthTxt)
	allValues.append(strokeWidthRec)
	allValues.append(recWidth)
	allValues.append(recHeight)
	allValues.append(padWidth)
	allValues.append(padHeight)
	return allValues
	pass

## makes a table of textbox VGroups
def makeTableList(
	allValues :list,
	tableValues :list,
	saveOver :bool= False,
	doHighlight :bool= False,
	doColumn :bool= None,
) -> list:
	#values
	numCol :int= allValues[0]
	numRow :int= allValues[1]
	tableList :list= allValues[2]
	colrowSize :list= allValues[3]
	tableVgrList :list= allValues[4]
	#base
	timeRun :float= allValues[5]
	timeWait :float= allValues[6]
	txtSize :float= allValues[7]
	#normal
	colorTxt :Colors= allValues[8]
	colorRec :Colors= allValues[9]
	colorStrokeTxt :Colors= allValues[10]
	colorStrokeRec :Colors= allValues[11]
	#highlight
	highColorTxt :Colors= allValues[12]
	highColorRec :Colors= allValues[13]
	highColorStrokeTxt :Colors= allValues[14]
	highColorStrokeRec :Colors= allValues[15]
	#other
	opacityTxt :float= allValues[16]
	opacityRec :float= allValues[17]
	strokeWidthTxt :float= allValues[18]
	strokeWidthRec :float= allValues[19]
	#box
	recWidth :float= allValues[20]
	recHeight :float= allValues[21]
	padWidth :float= allValues[22]
	padHeight :float= allValues[23]

	newVgrList = []

	useTableVal :list= []
	if tableValues == []:
		useTableVal = tableList
	else:
		useTableVal = tableValues
	
	# checkNumCol :int= numCol
	# checkNumRow :int= numRow
	checkNumCol :int= 0
	checkNumRow :int= 0
	if saveOver:
		checkNumCol = numCol
		checkNumRow = numRow
	else:
		if doColumn != None:
			checkNumCol = 1 if doColumn else len(tableValues)
			checkNumRow = len(tableValues) if doColumn else 1
		else:
			checkNumCol = numCol
			checkNumRow = numRow

	checkSize = dep.getColWidthRowHeight(
		useTableVal,checkNumCol,checkNumRow,txtSize,strokeWidthTxt
	)
	colrowSize = checkSize if colrowSize == [] else colrowSize
	arrIdx :int= 0
	preVgr :VGroup= None
	
	# prePoint :np.ndarray= UL if doColumn else UL
	# posPoint :np.ndarray= UR if doColumn else DL
	alignToCol0 :np.ndarray
	for r in range(checkNumRow):
		for c in range(checkNumCol):
			recWidth :float= checkSize[0][c] if doColumn == True else colrowSize[0][c]
			recHeight :float= checkSize[1][r] if doColumn == False else colrowSize[1][r]
			newVgr :VGroup= dep.makeTextBox(
				str(useTableVal[arrIdx]),
				txtSize,
				doHighlight,
				highColorTxt if doHighlight else colorTxt,
				highColorRec if doHighlight else colorRec,
				highColorStrokeTxt if doHighlight else colorStrokeTxt,
				highColorStrokeRec if doHighlight else colorStrokeRec,
				opacityTxt,
				opacityRec,
				strokeWidthTxt,
				strokeWidthRec,
				recWidth,
				recHeight,
				padWidth,
				padHeight,
			)
			if preVgr != None:
				alignTo :np.ndarray
				if c == 0:
					newVgr.move_to(alignToCol0, aligned_edge=UL)
					alignToCol0 = newVgr.get_critical_point(DL)
				else:
					alignTo = preVgr.get_critical_point(UR)
					newVgr.move_to(alignTo, aligned_edge=UL)
			else:
				alignToCol0 = newVgr.get_critical_point(DL)
			preVgr = newVgr
			newVgrList.append(newVgr)
			arrIdx += 1
	# print(newVgrList)
	return [
		[
		checkSize,
		newVgrList,
		],
		[
		#values
		numCol,
		numRow,
		tableValues if saveOver else tableList,
		checkSize if saveOver else colrowSize,
		newVgrList if saveOver else tableVgrList,
		#base
		timeRun,
		timeWait,
		txtSize,
		#normal
		colorTxt,
		colorRec,
		colorStrokeTxt,
		colorStrokeRec,
		#highlight
		highColorTxt,
		highColorRec,
		highColorStrokeTxt,
		highColorStrokeRec,
		#other
		opacityTxt,
		opacityRec,
		strokeWidthTxt,
		strokeWidthRec,
		#box
		recWidth,
		recHeight,
		padWidth,
		padHeight,
		],
	]
	pass

## makes one VGroup from a list of VGroups
def makeVgroup(
	vgrList :list,
) -> VGroup:
	newList :VGroup= VGroup()
	for i in range(len(vgrList)):
		newList.add(vgrList[i])
	return newList
	pass

## writes or unwrites a VGroup with wait
def writeVgroup(
	argSelf,
	theVGr :VGroup,
	doWrite :bool= True,
	timeRun :float= const.TimeRun,
	timeWait :float= const.TimeWait,
	doReverse :bool= False,
) -> None:
	if doWrite:
		argSelf.play(
			Write(theVGr),
			reverse = doReverse,
			run_time = timeRun,
		)
	else:
		argSelf.play(
			Unwrite(theVGr),
			reverse = doReverse,
			run_time = timeRun,
		)
	argSelf.wait(timeWait)
	pass

## transforms one VGroup into another with wait
def transformVgroup(
	argSelf,
	vgrFrom :VGroup,
	vgrTo :VGroup,
	timeRun :float= const.TimeRun,
	timeWait :float= const.TimeWait,
) -> None:
	argSelf.play(
		Transform(vgrFrom, vgrTo),
		run_time = timeRun,
	)
	argSelf.wait(timeWait)
	pass

## delete all specified index col/row in the table
def deleteTableListLines(
	argSelf,
	allValues :list,
	deleteIdx :list[int],
	doColumn :bool= True,
	timeDiv :int= 2,
	doTimeWait :bool= True,
):
	#values
	numCol :int= allValues[0]
	numRow :int= allValues[1]
	tableList :list= allValues[2]
	colrowSize :list= allValues[3]
	tableVgrList :list= allValues[4]
	#base
	timeRun :float= allValues[5]
	timeWait :float= allValues[6]
	txtSize :float= allValues[7]
	#normal
	colorTxt :Colors= allValues[8]
	colorRec :Colors= allValues[9]
	colorStrokeTxt :Colors= allValues[10]
	colorStrokeRec :Colors= allValues[11]
	#highlight
	highColorTxt :Colors= allValues[12]
	highColorRec :Colors= allValues[13]
	highColorStrokeTxt :Colors= allValues[14]
	highColorStrokeRec :Colors= allValues[15]
	#other
	opacityTxt :float= allValues[16]
	opacityRec :float= allValues[17]
	strokeWidthTxt :float= allValues[18]
	strokeWidthRec :float= allValues[19]
	#box
	recWidth :float= allValues[20]
	recHeight :float= allValues[21]
	padWidth :float= allValues[22]
	padHeight :float= allValues[23]

	delLen :int= len(deleteIdx)
	delCol :int= delLen if doColumn else 0
	delRow :int= 0 if doColumn else delLen

	keepColRow :list= dep.getMultiSplitList(
		colrowSize[0] if doColumn else colrowSize[1],
		deleteIdx,True,
	)

	splitTable :list= dep.splitListTable(
		tableList,numCol,numRow,doColumn
	)
	keepList :list= dep.getMultiSplitList(
		splitTable,deleteIdx,True,
	)

	splitVgrTable :list= dep.splitListTable(
		tableVgrList,numCol,numRow,doColumn
	)
	nullVgrList :list= dep.getMultiSplitList(
		splitVgrTable,deleteIdx,False,
	)
	keepVgrList :list= dep.getMultiSplitList(
		splitVgrTable,deleteIdx,True,
	)

	vgrNullLines :list= []
	for i in range(len(nullVgrList)):
		vgrNullLines.append(makeVgroup(nullVgrList[i]))
	vgrKeepLines :list= []
	for i in range(len(keepVgrList)):
		vgrKeepLines.append(makeVgroup(keepVgrList[i]))
	prePoint :np.ndarray= UL if doColumn else UL
	posPoint :np.ndarray= UR if doColumn else DL
	basePoint :np.ndarray= []
	if deleteIdx[0] == 0:
		basePoint = vgrNullLines[0].get_critical_point(prePoint)
	else:
		basePoint = vgrKeepLines[0].get_critical_point(prePoint)
	alignTo :np.ndarray= basePoint

	playRemove :list= []
	playMovers :list= []
	for i in range(len(vgrNullLines)):
		vgrNullLines[i].set_z_index(-1)
		playRemove.append(Unwrite(vgrNullLines[i]))
	for i in range(len(vgrKeepLines),):
		playMovers.append(
			vgrKeepLines[i].animate.move_to(alignTo, aligned_edge=prePoint),
		)
		alignTo = dep.getMovedPoint(
			vgrKeepLines[i],alignTo,prePoint,posPoint
		)
	argSelf.play(
		*playRemove,
		reverse = False,
		run_time = timeRun/timeDiv,
	)
	argSelf.play(
		*playMovers,
		reverse = False,
		run_time = timeRun/timeDiv,
	)
	if doTimeWait:
		argSelf.wait(timeWait)

	colrowNew :list= colrowSize
	colrowNew[0 if doColumn else 1] = keepColRow
	return [
		#values
		numCol - delCol,
		numRow - delRow,
		dep.mergeSplitTable(keepList,doColumn),
		colrowNew,
		dep.mergeSplitTable(keepVgrList,doColumn),
		#base
		timeRun,
		timeWait,
		txtSize,
		#normal
		colorTxt,
		colorRec,
		colorStrokeTxt,
		colorStrokeRec,
		#highlight
		highColorTxt,
		highColorRec,
		highColorStrokeTxt,
		highColorStrokeRec,
		#other
		opacityTxt,
		opacityRec,
		strokeWidthTxt,
		strokeWidthRec,
		#box
		recWidth,
		recHeight,
		padWidth,
		padHeight,
	]
	pass

#TODO does not resize if the insert is bigger/smaller than
# the current col/row size. Can use the scale afterwards
## delete all specified index col/row in the table
def insertTableListLines(
	argSelf,
	allValues :list,
	insertVal :list[list[int,list,bool]],
	doColumn :bool= True,
	timeDiv :int= 2,
	doTimeWait :bool= True,
):
	#values
	numCol :int= allValues[0]
	numRow :int= allValues[1]
	tableList :list= allValues[2]
	colrowSize :list= allValues[3]
	tableVgrList :list= allValues[4]
	#base
	timeRun :float= allValues[5]
	timeWait :float= allValues[6]
	txtSize :float= allValues[7]
	#normal
	colorTxt :Colors= allValues[8]
	colorRec :Colors= allValues[9]
	colorStrokeTxt :Colors= allValues[10]
	colorStrokeRec :Colors= allValues[11]
	#highlight
	highColorTxt :Colors= allValues[12]
	highColorRec :Colors= allValues[13]
	highColorStrokeTxt :Colors= allValues[14]
	highColorStrokeRec :Colors= allValues[15]
	#other
	opacityTxt :float= allValues[16]
	opacityRec :float= allValues[17]
	strokeWidthTxt :float= allValues[18]
	strokeWidthRec :float= allValues[19]
	#box
	recWidth :float= allValues[20]
	recHeight :float= allValues[21]
	padWidth :float= allValues[22]
	padHeight :float= allValues[23]

	insLen :int= len(insertVal)
	insCol :int= insLen if doColumn else 0
	insRow :int= 0 if doColumn else insLen

	splitTable :list= dep.splitListTable(
		tableList,numCol,numRow,doColumn
	)
	keepList :list= dep.insertMultiIntoList(
		splitTable,insertVal
	)

	splitVgrTable :list= dep.splitListTable(
		tableVgrList,numCol,numRow,doColumn
	)
	newColRowInsert :list= []
	newVgrInsert :list= []
	for i in range(len(insertVal)):
		tempNewVgr :list= makeTableList(
			allValues,
			insertVal[i][1],False,
			insertVal[i][2],doColumn,
		)[0]

		styleList :list= dep.getStyleList(allValues)
		if insertVal[i][2] == None:
			styleIdx :int= 0 + insertVal[i][0]
			if doColumn:
				if styleIdx > numCol-1:
					styleIdx = numCol-1
			else:
				if styleIdx > numRow-1:
					styleIdx = numRow-1
			tempNewVgr[1] = dep.styleCopyList(
				splitVgrTable[styleIdx],
				tempNewVgr[1],
				styleList,
			)

		newColRowInsert.append([
			insertVal[i][0],
			tempNewVgr[0][0 if doColumn else 1][0]
			])
		newVgrInsert.append([
			insertVal[i][0],tempNewVgr[1]
		])

	keepVgrList :list= dep.insertMultiIntoList(
		splitVgrTable,newVgrInsert
	)
	posListIdx :list= dep.getLocateIdxList(insertVal,[0])
	vgrGroupSplit :list= dep.getListGroupAfterInsert(
		keepVgrList,posListIdx
	)

	keepColRow :list= dep.insertMultiIntoList(
		colrowSize[0 if doColumn else 1],
		newColRowInsert
	)
	
	oriGroup :list= vgrGroupSplit[0]
	insGroup :list= vgrGroupSplit[1]
	preAdd :bool= vgrGroupSplit[2]
	posAdd :bool= vgrGroupSplit[3]

	insGroupSplit :list= []
	for i in range(len(insGroup)):
		for s in range(len(insGroup[i])):
			insGroupSplit.append(insGroup[i][s])

	prePoint :np.ndarray= UL if doColumn else UL
	posPoint :np.ndarray= UR if doColumn else DL
	alignTo :np.ndarray= []

	insGroupFixAlign :VGroup= []
	for i in range(len(insGroupSplit)):
		insGroupFixAlign.append(makeVgroup(insGroupSplit[i]))
	for i in range(1,len(insGroupFixAlign)):
		if insertVal[i-1][0] == insertVal[i][0]:
			insGroupFixAlign[i].move_to(
				insGroupFixAlign[i-1].get_critical_point(posPoint),
				aligned_edge=prePoint
			)

	for i in range(len(oriGroup)):
		oriGroup[i] = dep.mergeSplitTable(
			oriGroup[i],doColumn
		)
	for i in range(len(insGroup)):
		insGroup[i] = dep.mergeSplitTable(
			insGroup[i],doColumn
		)

	oriVgrGroup :list= []
	for i in range(len(oriGroup)):
		oriVgrGroup.append(makeVgroup(oriGroup[i]))
	insVgrGroup :list= []
	for i in range(len(insGroup)):
		insVgrGroup.append(makeVgroup(insGroup[i]))
	
	playInsert :list= []
	playMovers :list= []

	if preAdd:
		insVgrGroup[0].set_z_index(-1)
		insVgrGroup[0].move_to(
			oriVgrGroup[0].get_critical_point(prePoint),
			aligned_edge=prePoint
		)
		playInsert.append(Write(insVgrGroup[0]))
		alignTo = insVgrGroup[0].get_critical_point(posPoint)
		playMovers.append(
			oriVgrGroup[0].animate.move_to(
			alignTo,aligned_edge=prePoint
		))
	
	insLen :int= len(insVgrGroup)
	oriLen :int= len(oriVgrGroup)
	insDifOri :int= insLen - oriLen
	pairLen :int= 0
	if insDifOri == 0:
		pairLen = insLen
	else:
		pairLen = oriLen
	
	for i in range(1 if preAdd else 0,pairLen):
		if i == 0:
			alignTo = oriVgrGroup[0].get_critical_point(prePoint)
			
		if i > 0:
			alignTo = dep.getMovedPoint(
				oriVgrGroup[i-1],alignTo,prePoint,posPoint
			)
			insVgrGroup[i-(1-preAdd)].set_z_index(-1)
			insVgrGroup[i-(1-preAdd)].move_to(
				alignTo,aligned_edge=prePoint
			)
			playInsert.append(Write(insVgrGroup[i-(1-preAdd)]))
			alignTo = insVgrGroup[i-(1-preAdd)].get_critical_point(posPoint)

		playMovers.append(
			oriVgrGroup[i].animate.move_to(
			alignTo,aligned_edge=prePoint
		))
	
	if posAdd:
		alignTo = dep.getMovedPoint(
			oriVgrGroup[oriLen-1],alignTo,prePoint,posPoint
		)
		insVgrGroup[insLen-1].set_z_index(-1)
		insVgrGroup[insLen-1].move_to(
			alignTo,aligned_edge=prePoint
		)
		playInsert.append(Write(insVgrGroup[insLen-1]))

	argSelf.play(
		*playMovers,
		reverse = False,
		run_time = timeRun/timeDiv,
	)
	argSelf.play(
		*playInsert,
		reverse = False,
		run_time = timeRun/timeDiv,
	)
	for i in range(insLen):
		insVgrGroup[i].set_z_index(0)
	if doTimeWait:
		argSelf.wait(timeWait)

	colrowNew :list= colrowSize
	colrowNew[0 if doColumn else 1] = keepColRow
	return [
		#values
		numCol + insCol,
		numRow + insRow,
		dep.mergeSplitTable(keepList,doColumn),
		colrowNew,
		dep.mergeSplitTable(keepVgrList,doColumn),
		#base
		timeRun,
		timeWait,
		txtSize,
		#normal
		colorTxt,
		colorRec,
		colorStrokeTxt,
		colorStrokeRec,
		#highlight
		highColorTxt,
		highColorRec,
		highColorStrokeTxt,
		highColorStrokeRec,
		#other
		opacityTxt,
		opacityRec,
		strokeWidthTxt,
		strokeWidthRec,
		#box
		recWidth,
		recHeight,
		padWidth,
		padHeight,
	]
	pass

## play anim from one list to another
def playShimmerList(
	argSelf,
	oldVgrList :list, #allValues[4]
	newVgrList :list,
	timeRun :float, #allValues[5]
	timeWait :float, #allValues[6]
) -> None:
	oldGroup :VGroup= makeVgroup(oldVgrList)
	newGroup :VGroup= makeVgroup(newVgrList)
	newGroup.move_to(
		oldGroup.get_critical_point(UL),
		aligned_edge=UL,
	)
	argSelf.play(
		Unwrite(oldGroup),
		Write(newGroup),
		reverse = False,
		run_time = timeRun,
	)
	argSelf.wait(timeWait)
	pass

## play and change the style of the whole table
def shimmerStyleTable(
	argSelf,
	allValues :list,
	doHighlight :bool,
) -> list:
	oldVgrList :list= allValues[4]
	timeRun :float= allValues[5]
	timeWait :float= allValues[6]
	styleList :list= dep.getStyleList(allValues)
	newVgrList :list= dep.styleSetList(
		oldVgrList,styleList,doHighlight
	)
	playShimmerList(
		argSelf,oldVgrList,newVgrList,timeRun,timeWait
	)
	allValues[4] = newVgrList
	return allValues
	pass

## play and change style for selected columns, rows, or cells
## [int, int, doHighlight] for cell [col, row]
## [True, int, doHighlight] for col
## [False, int, doHighlight] for row
def shimmerStyleSelected(
	argSelf,
	allValues :list,
	cellSelect :list,
	doIncrement :bool= False,
) -> list:
	numCol :int= allValues[0]
	numRow :int= allValues[1]
	tableVgrList :list= allValues[4]
	timeRun :float= allValues[5]
	timeWait :float= allValues[6]
	selectLen :int= len(cellSelect)
	styleList :list= dep.getStyleList(allValues)
	oldList :list= []
	newList :list= []

	dcVgrList :list= deepcopy(tableVgrList)
	listIdxVal :list= dep.getCellIndexList(
		cellSelect,numCol,numRow
	)
	noDupList :list= dep.getNoDuplicateIdxList(listIdxVal)
	idxCount :list= []
	if doIncrement:
		idxCount = listIdxVal
	else:
		idxCount = noDupList
	
	for i in range(selectLen):
		for v in range(len(idxCount[i])):
			dcVgrList[idxCount[i][v]] = dep.styleSetCell(
				dcVgrList[idxCount[i][v]],
				styleList,
				cellSelect[i][2],
			)
	oldList = dep.getOneListFromSubList(
		dep.getValListFromIdxSubList(
			tableVgrList,noDupList,
		)
	)
	newList = dep.getOneListFromSubList(
		dep.getValListFromIdxSubList(
			dcVgrList,noDupList,
		)
	)
	playShimmerList(
		argSelf,oldList,newList,timeRun,timeWait
	)
	for i in range(len(allValues[4])):
		argSelf.remove(allValues[4][i])
	allValues[4] = dcVgrList
	return allValues
	pass

## replaces a list of table lines
def replaceTableListLines(
	argSelf,
	allValues :list,
	insertVal :list[list[int,list,bool]],
	doColumn :bool= True,
) -> list:
	allValues = insertTableListLines(
		argSelf,allValues,insertVal,doColumn,4,False
	)
	delIdxList :list= dep.getLocateIdxList(insertVal,[0])
	delIdxList = dep.getListInsertCount(delIdxList)
	delIdxList = dep.getListInsertOffset(delIdxList)
	delIdxList = dep.getLocateIdxList(delIdxList,[1])
	allValues = deleteTableListLines(
		argSelf,allValues,delIdxList,doColumn,4,
	)
	return allValues
	pass

#TODO I think this is broken somehow in the copy not sure
## scale the table by new font size or overall scale
def scaleTableFontSize(
	argSelf,
	allValues :list,
	doFontOrScale :bool,
	changeSize :float,
	doHighlight :bool,
) -> list:
	styleList :list= dep.getStyleList(allValues)
	txtSize :float= allValues[7]
	newSize :float= changeSize if doFontOrScale else (
		floatAddorMulAsInt(txtSize,changeSize,False)
	)
	oldVgrList :list= allValues[4]
	oldVgroup :VGroup= makeVgroup(oldVgrList)
	allValues[3] = []
	allValues[4] = []
	allValues[7] = newSize
	allValues = makeTableList(
		allValues,
		allValues[2],
		True,
		doHighlight,
	)[1]
	newVgrList :list= allValues[4]
	allValues[4] = []
	if doHighlight == None:
		for i in range(len(oldVgrList)):
			allValues[4].append(dep.styleCopyCell(
				oldVgrList[i],newVgrList[i],styleList
			))
	newStyleVgroup = makeVgroup(allValues[4])
	alignTo :np.ndarray= oldVgroup.get_critical_point(UL)
	newStyleVgroup.move_to(alignTo, aligned_edge=UL)
	transformVgroup(
		argSelf,
		oldVgroup,
		newStyleVgroup,
	)
	argSelf.remove(oldVgroup)
	return allValues
	pass