
######
# Includes:
######

from codeBase import const #custom constants used as default values

from manim import *
from manim.utils.color import Colors
from copy import deepcopy

######
# Custom Functions: Local Dependencies
######

## sort whole list or to particular index by another index
def sortListByIndex(
	fromList :list,
	sortByIdx :int= 0,
	sortToIdx :int= -1,
) -> list:
	sortList :list= deepcopy(fromList)
	if sortToIdx == -1:
		sortList.sort(key=lambda x: x[sortByIdx])
	else:
		sortList[sortToIdx].sort(key=lambda x: x[sortByIdx])
	return sortList
	pass

## calculates the default stroke width based on text size
def calcStrokeWidth(
	txtSize :float= const.TxtSize,
) -> float:
	return txtSize / 5
	pass

## calculates the default padding width based on text size
def calcPadWidth(
	txtSize :float= const.TxtSize,
) -> float:
	return txtSize / 100
	pass

## gets either a column or row from a single array of values
def getListTableLine(
	tableList :list,
	numCol :int,
	numRow :int,
	getIdx :int,
	doColumn :bool= True,
) -> list:
	newLine :list= []
	getThis :int= getIdx if doColumn else getIdx * numCol
	numRange :int= numRow if doColumn else numCol
	numAdder :int= numCol if doColumn else 1
	for i in range(numRange):
		newLine.append(tableList[getThis])
		getThis += numAdder
	return newLine
	pass

## splits list at multiple index
def getListRange(
	arrList :list,
	startIdx :int,
	enderIdx :int,
	# deleteIdx :bool= False,
) -> list:
	arrLen :int= len(arrList)
	splitList :list= []
	preIdx :int= 0 if startIdx < 0 else startIdx
	posIdx :int= arrLen if enderIdx > arrLen else enderIdx
	splitList = arrList[preIdx:posIdx]
	return splitList[0]
	pass

## get new list with insert position and repeats
def getListInsertCount(
	locList :list,
) -> list:
	locLen :int= len(locList)
	retList :list= []
	cntList :int= 1
	for i in range(1,locLen):
		if locList[i] == locList[i-1]:
			cntList += 1
		elif locList[i] > locList[i-1]:
			retList.append([locList[i-1],cntList])
			cntList = 1
	retList.append([locList[locLen-1],cntList])
	return retList
	pass

## change insert count list into correct offset for new list
def getListInsertOffset(
	newLocList :list,
) -> list:
	retList :list= []
	adderTo :int= 0
	for i in range(len(newLocList)):
		retList.append([
			newLocList[i][0]+adderTo,
			newLocList[i][0]+adderTo+newLocList[i][1]
			])
		adderTo += newLocList[i][1]
	return retList
	pass

## copy the style from one vgr cell to another
def styleCopyCell(
	fromVgr :VGroup,
	toVgr :VGroup,
	styleList :list,
) -> VGroup:
	cellHighlight :bool= bool(fromVgr[3].get_fill_opacity())
	styleVgr :VGroup= styleSetCell(
		toVgr,styleList,cellHighlight
	)
	return styleVgr
	pass

## calculate the single list index of the col row index
def cellNumFromColRow(
	listColRow :list, #[col, row]
	numCol :int, #allValues[0]
) -> int:
	cellNum :int= (numCol * listColRow[1]) + listColRow[0]
	return cellNum
	pass

######
# Custom Functions: Action Dependencies
######

## makes a text and rectanlge box VGroup
def makeTextBox(
	txtString :str= "",
	txtSize :float= const.TxtSize,
	doHighlight :bool= False,
	colorTxt :Colors= const.ColorTxt,
	colorRec :Colors= const.ColorRec,
	colorStrokeTxt :Colors= const.ColorStrokeTxt,
	colorStrokeRec :Colors= const.ColorStrokeRec,
	opacityTxt :float= const.OpacityTxt,
	opacityRec :float= const.OpacityRec,
	strokeWidthTxt :float= const.StrokeWidthTxt,
	strokeWidthRec :float= const.StrokeWidthRec,
	recWidth :float= const.RecWidth,
	recHeight :float= const.RecHeight,
	padWidth :float= const.PadWidth,
	padHeight :float= const.PadHeight,
) -> VGroup:
	newVgr :VGroup= VGroup()
	defStroke :float= calcStrokeWidth(txtSize)
	defPad :float= calcPadWidth(txtSize)
	if strokeWidthTxt == -1:
		strokeWidthTxt = defStroke
	newTxtStroke :Text= Text(
		text = txtString,
		fill_opacity = opacityTxt,
		stroke_width = strokeWidthTxt,
		stroke_color = colorStrokeTxt,
		fill_color = colorStrokeTxt,
		font_size = txtSize,
		z_index = 1,
		)
	newTxt :Text= Text(
		text = txtString,
		fill_opacity = opacityTxt,
		fill_color = colorTxt,
		font_size = txtSize,
		z_index = 2,
		)
	if recHeight == -1:
		recHeight = newTxtStroke.height
	if recWidth == -1:
		recWidth = newTxtStroke.width
	if strokeWidthRec == -1:
		strokeWidthRec = defStroke
	if padHeight == -1:
		padHeight = defPad
	if padWidth == -1:
		padWidth = defPad
	newRec :Rectangle= Rectangle(
		height = recHeight + padHeight,
		width = recWidth + padWidth,
		fill_color = colorRec,
		fill_opacity = opacityRec,
		stroke_width = strokeWidthRec,
		stroke_color = colorStrokeRec,
		z_index = 0,
		)
	vmHighlight :VMobject= VMobject()
	vmHighlight.set_fill(opacity=doHighlight,family=False)
	newVgr.add(
		newRec,
		newTxtStroke,
	    newTxt,
		vmHighlight,
	)
	newVgr.set_z_index(0)
	return newVgr
	pass

## merges a split column or row array into a single array
def mergeSplitTable(
	splitList :list,
	doColumn :bool= True,
) -> list:
	newList :list= []
	numCol :int= len(splitList) if doColumn else len(splitList[0])
	numRow :int= len(splitList[0]) if doColumn else len(splitList)
	for r in range(numRow):
		for c in range(numCol):
			if doColumn:
				newList.append(splitList[c][r])
			else:
				newList.append(splitList[r][c])
	return newList
	pass

## splits a single array of values into a list of columns or rows
def splitListTable(
	tableList :list,
	numCol :int,
	numRow :int,
	doColumn :bool= True,
) -> list:
	newList :list= []
	numRange :int= numCol if doColumn else numRow
	for i in range(numRange):
		newList.append(getListTableLine(
			tableList,numCol,numRow,i,doColumn)
		)
	return newList
	pass

## calculates the max height and width for cells in a table
def getColWidthRowHeight(
	tableList :list,
	numCol :int,
	numRow :int,
	txtSize :float= const.TxtSize,
	strokeWidthTxt :float= const.StrokeWidthTxt,
) -> list:
	listColWidth :list= [0] * numCol
	listRowHeight :list= [0] * numRow
	arrIdx :int= 0
	defStroke :float= calcStrokeWidth(txtSize)
	if strokeWidthTxt == -1:
		strokeWidthTxt = defStroke
	for r in range(numRow):
		for c in range(numCol):
			txtString :str= str(tableList[arrIdx])
			newTxtStroke :Text= Text(
				text = txtString,
				fill_opacity = 1,
				stroke_width = strokeWidthTxt,
				stroke_color = BLACK,
				fill_color = BLACK,
				font_size = txtSize,
				)
			colWidth :float= newTxtStroke.width
			rowHeight :float= newTxtStroke.height
			if colWidth > listColWidth[c]:
				listColWidth[c] = colWidth
			if rowHeight > listRowHeight[r]:
				listRowHeight[r] = rowHeight
			arrIdx += 1
	return [listColWidth, listRowHeight]
	pass

## get many lists based on a list of index
def getMultiSplitList(
	splitList :list,
	multiIdx :list[int],
	getInvert :bool= False,
) -> list:
	lenMulti :int= len(multiIdx)
	arrLen :int= len(splitList) if getInvert else lenMulti
	multiList :list= []
	checkIdx :int= 0
	for i in range(arrLen):
		if getInvert:
			if checkIdx < lenMulti and i == multiIdx[checkIdx]:
				checkIdx += 1
			else:
				multiList.append(
					getListRange(
						splitList,
						i,
						i+1,
					)
				)
		else:
			multiList.append(
				getListRange(
					splitList,
					multiIdx[i],
					multiIdx[i]+1,
				)
			)
	return multiList
	pass

## get what critical point when the vgroup is moved
def getMovedPoint(
	theVgroup :VGroup,
	moveToPos :np.ndarray,
	prePoint :np.ndarray,
	posPoint :np.ndarray,
) -> np.ndarray:
	origAlign :np.ndarray= []
	newToPos :np.ndarray= []
	origAlign = theVgroup.get_critical_point(prePoint)
	theVgroup.move_to(moveToPos, aligned_edge=prePoint)
	newToPos = theVgroup.get_critical_point(posPoint)
	theVgroup.move_to(origAlign, aligned_edge=prePoint)
	return newToPos
	pass

## inserts values at idx in reverse order
def insertMultiIntoList(
	startList :list,
	insertVal :list[int,list],
):
	retList :list= startList
	for i in range(len(insertVal)-1,-1,-1):
		retList.insert(insertVal[i][0],insertVal[i][1])
	return retList
	pass

## get new list from list of sub index path from another list
def getLocateIdxList(
	locateList :list,
	posIsolate :list[int],
) -> list:
	retList :list= []
	tmpList :list= []
	locLen :int= len(locateList)
	posLen :int= len(posIsolate)
	for l in range(locLen):
		tmpList = locateList[l]
		for p in range(posLen):
			if type(tmpList) == list:
				tmpList = tmpList[posIsolate[p]]
			else:
				break
		retList.append(tmpList)
	return retList
	pass

## separate new list into the groups of original and inserted
def getListGroupAfterInsert(
	finalList :list,
	locateIdx :list[int],
) -> list:
	finLen :int= len(finalList)
	locLen :int= len(locateIdx)
	oriLen :int= finLen - locLen
	oriList :list= []
	insList :list= []
	newLoc :list= getListInsertCount(locateIdx)
	newLen :int= len(newLoc)
	preAdd :bool= True if newLoc[0][0] == 0 else False
	posAdd :bool= True if newLoc[newLen-1][0] >= oriLen else False
	offLoc :list= getListInsertOffset(newLoc)
	offLen :int= len(offLoc)

	for i in range(offLen):
		insList.append(finalList[
			offLoc[i][0]:offLoc[i][1]
		])
	
	if preAdd == False:
		oriList.append(finalList[
			0:offLoc[0][0]
		])
	for i in range(offLen-1):
		oriList.append(finalList[
			offLoc[i][1]:offLoc[i+1][0]
		])
	if posAdd == False:
		oriList.append(finalList[
			offLoc[offLen-1][1]:finLen
		])

	return [oriList,insList,preAdd,posAdd]
	pass

## get the array to use with changing the style of cells
def getStyleList(
	allValues :list,
) -> list:
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

	styleList :list= [
		[
		colorTxt,
		colorRec,
		colorStrokeTxt,
		colorStrokeRec,
		],
		[
		highColorTxt,
		highColorRec,
		highColorStrokeTxt,
		highColorStrokeRec,
		],
	]
	return styleList
	pass

## copy the style from a list of vgr cells to another
def styleCopyList(
	fromVgr :list,
	toVgr :list,
	styleList :list,
) -> list:
	styleVgr :list= []
	for i in range(len(fromVgr)):
		styleVgr.append(styleCopyCell(
			fromVgr[i],
			toVgr[i],
			styleList,
		))
	return styleVgr
	pass

## change the style for a single vgr cell
def styleSetCell(
	fromVgr :VGroup,
	styleList :list,
	doHighlight :bool,
) -> VGroup:
	styleVgr :VGroup= deepcopy(fromVgr)
	cellHighlight :bool= bool(fromVgr[3].get_fill_opacity())
	if doHighlight == None:
		doHighlight :bool= bool(1-cellHighlight)
	styleVgr[0].set_fill_color(styleList[doHighlight][1])
	styleVgr[0].set_stroke_color(styleList[doHighlight][3])
	styleVgr[1].set_fill_color(styleList[doHighlight][2])
	styleVgr[1].set_stroke_color(styleList[doHighlight][2])
	styleVgr[2].set_fill_color(styleList[doHighlight][0])
	styleVgr[3].set_fill(opacity=doHighlight,family=False)
	return styleVgr
	pass

## change the style for a list of vgr cells
def styleSetList(
	vgrList :list,
	styleList :list,
	doHighlight :bool,
) -> list:
	newVgrList :list= []
	for i in range(len(vgrList)):
		newVgrList.append(styleSetCell(
			vgrList[i],styleList,doHighlight
		))
	return newVgrList
	pass

## get a single list from sub lists
def getOneListFromSubList(
	subList :list,
) -> list:
	oneList :list= []
	for i in range(len(subList)):
		for v in range(len(subList[i])):
			oneList.append(subList[i][v])
	return oneList
	pass

## get a value from one list using the index from a sub list
def getValListFromIdxSubList(
	optionList :list,
	idxSubList :list,
) -> list:
	valList :list= []
	for i in range(len(idxSubList)):
		tempList :list= []
		for s in range(len(idxSubList[i])):
			tempList.append(optionList[idxSubList[i][s]])
		valList.append(tempList)
	return valList
	pass

## set a value from one list using the index from a sub list
def setValListFromIdxSubList(
	argSelf,
	fromList :list,
	toList :list,
	idxSubList :list,
) -> list:
	setList :list= fromList
	for i in range(len(idxSubList)):
		for s in range(len(idxSubList[i])):
			remList :list= setList[idxSubList[i][s]]
			setList[idxSubList[i][s]] = toList[idxSubList[i][s]]
			argSelf.remove(remList)
	return setList
	pass

## get the single list index for each sub list insert col row
def getCellIndexList(
	cellSelect :list,
	numCol :int, #allValues[0]
	numRow :int, #allValues[1]
) -> list:
	numStart :int= 0
	numAdder :int= 0
	numTotal :int= 0
	listIdxVal :list= []
	for i in range(len(cellSelect)):
		doColRow :bool= type(cellSelect[i][0]) == bool
		tempList :list= []
		if doColRow:
			if cellSelect[i][0] == True:
				numStart = cellSelect[i][1]
				numAdder = numCol
				numTotal = numRow
			elif cellSelect[i][0] == False:
				numStart = numCol * cellSelect[i][1]
				numAdder = 1
				numTotal = numCol
		else:
			numStart = cellNumFromColRow(cellSelect[i],numCol)
			numAdder = 0
			numTotal = 1
		for v in range(numTotal):
			tempList.append(numStart)
			numStart += numAdder
		listIdxVal.append(tempList)
	return listIdxVal
	pass

## remove duplicates of the insert sub index list
def getNoDuplicateIdxList(
	listIdxVal :list,
) -> list:
	noDupList :list= []
	for i in range(len(listIdxVal)):
		tempList :list= []
		for v in range(len(listIdxVal[i])):
			noMatch :bool= True
			for d in range(len(noDupList)):
				for x in range(len(noDupList[d])):
					if listIdxVal[i][v] == noDupList[d][x]:
						noMatch = False
						break
			if noMatch:
				tempList.append(listIdxVal[i][v])
		noDupList.append(tempList)
	return noDupList
	pass
