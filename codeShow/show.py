
######
# Includes:
######

from codeBase import const #custom constants used as default values
from codeBase import dep #custom functions that are dependencies
from codeBase import act #custom functions that are actionable

from manim import *
# from manim.utils.color import Colors
from manim_voiceover.services.gtts import GTTSService
# from manim_voiceover.services.recorder import RecorderService
# from copy import deepcopy

######
# Custom Functions: Specific for my SoME3 presentation
######

## calls the TTS voiceover with a function and wait
def voiceOverCall(
	argSelf,
	voWait :float,
	voText :str,
	voSubT :str,
	funcCall,
	*funcArgs,
) -> list:
	valList :list= []
	with argSelf.voiceover(
		text=voText,
		subcaption=voText if voSubT == "" else voSubT,
	) as tracker:
		valList = funcCall(*funcArgs)
		argSelf.wait(tracker.get_remaining_duration(buff=-1))
		argSelf.wait(voWait)
	return valList
	
## set speech settings for voiceover
def setSpeechSettings(
	argSelf,
) -> None:
	argSelf.set_speech_service(GTTSService())
	# argSelf.set_speech_service(RecorderService())
	pass

## create the background for the presentation
def createBackground(
	argSelf,
) -> None:
	background :Rectangle= Rectangle(
		width = config.frame_width,
		height = config.frame_height,
		stroke_width = 0,
		fill_color = [PURPLE_E, BLACK],
		fill_opacity = 1,
		sheen_direction = DOWN,
		z_index = -10,
	)
	argSelf.add(background)
	argSelf.wait(const.TimeWait)
	pass

## the Manim logo display
def makeManimBanner(
	argSelf,
	runTime :float= 1,
) -> None:
	banner = ManimBanner().scale(0.5)
	argSelf.play(
		banner.create(),
		reverse = False,
		run_time = runTime,
	)
	argSelf.play(
		banner.expand(),
		reverse = False,
		run_time = runTime,
	)
	argSelf.play(
		FadeOut(banner),
		reverse = False,
		run_time = runTime,
	)
	pass

## make the intro title, author, and formula
def makeIntroTitle(
	argSelf,
	runTime :float= const.TimeRun,
) -> list:
	title = Tex("Divide Even by 2 Until Odd", font_size=72)
	maker = Tex("Cigam", font_size=54)
	equat = MathTex(r"\lceil \log_{D} (\gcd ( { D^{\lfloor\log_{D}N\rfloor} }, {N} ) ) \rceil")
	VGroup(title, maker, equat).arrange(DOWN)
	argSelf.play(
		Write(title),
		FadeIn(maker, shift=DOWN),
		Write(equat),
		reverse = False,
		run_time = runTime,
	)
	return [title, maker, equat]
	pass

## transition from the into title to slide name
def makeTitleToName(
	argSelf,
	valList :list,
	newName :str,
	runTime :float= const.TimeRun,
) -> list:
	newString :str= "<span underline='single'>"
	newString += newName
	newString += "</span>"
	newTitle = MarkupText(
		newString,
		font_size=50,
	)
	newTitle.to_edge(UR)
	argSelf.play(
		Transform(valList[0], newTitle),
		LaggedStart(*[FadeOut(obj, shift=DOWN) for obj in [valList[1], valList[2]]]),
		reverse = False,
		run_time = runTime,
	)
	return [act.makeVgroup(valList[0])]
	pass

## make the slide name that is in the upper right
def makeSlideName(
	argSelf,
	oldName :list,
	newName :str,
	runTime :float= const.TimeRun,
) -> list:
	newString :str= "<span underline='single'>"
	newString += newName
	newString += "</span>"
	newTitle = MarkupText(
		newString,
		font_size=50,
	)
	newTitle.to_edge(UR)
	newVgrName = act.makeVgroup(newTitle)
	if oldName == []:
		argSelf.play(
			Write(newVgrName),
			reverse = False,
			run_time = runTime,
		)
		return [newVgrName]
	else:
		argSelf.play(
			# Transform(oldName[0], newVgrName),
			Unwrite(oldName[0]),
			Write(newVgrName),
			reverse = False,
			run_time = runTime,
		)
		# return [oldName[0]]
		argSelf.remove(oldName[0])
		return [newVgrName]
	pass

## show and change the info text on the screen
def makeInfoDescription(
	argSelf,
	oldInfo :list,
	newText :list,
	fontSize :int= 30,
	perWidth :float= 0.6,
	runTime :float= const.TimeRun,
) -> list:
	doBold :bool= True
	newMTList :list= []
	preString :list= ["\t","<b>"]
	posString :list= ["","</b>"]
	newPerWidth = perWidth
	newAdjWidth = (perWidth+0.1) * config.frame_width
	newAdjWidth = config.frame_width - newAdjWidth
	for i in range(len(newText)):
		newString :str= ""
		newString += preString[doBold]
		newString += newText[i]
		newString += posString[doBold]
		newFontSize = fontSize if doBold else fontSize * 4.5
		textInfo = MarkupText(
			newString,
			font_size= newFontSize,
		)
		if doBold == False:
			textInfo.width = newAdjWidth
		if i == 0:
			textInfo.to_edge(UL)
			textInfo.shift([
				newPerWidth * config.frame_width,
				-0.1 * config.frame_height,
				0,
			])
		else:
			alignTo :np.ndarray= newMTList[i-1].get_critical_point(DL)
			textInfo.move_to(
				alignTo,
				aligned_edge=UL,
			)
			textInfo.shift([
				0,
				-0.25,
				0,
			])
		newMTList.append(textInfo)
		doBold = 1-doBold
	
	doBold = True
	for i in range(len(newText)):
		if doBold == False:
			newMTList[i].shift([
				0.5,
				0,
				0,
			])
		doBold = 1-doBold
	newInfo = act.makeVgroup(newMTList)
	if oldInfo == []:
		argSelf.play(
			Write(newInfo),
			reverse = False,
			run_time = runTime,
		)
		return [newInfo]
	else:
		argSelf.play(
			# Transform(oldInfo[0], newInfo),
			Unwrite(oldInfo[0]),
			Write(newInfo),
			reverse = False,
			run_time = runTime,
		)
		# return [oldInfo[0]]
		argSelf.remove(oldInfo[0])
		return [newInfo]
	pass

######
# Custom Functions: Used with actions
######

## get the index of a matching value
def getMatchIndex(
	scanList :list,
	scanVal,
) -> int:
	retVal :int= -1
	for i in range(len(scanList)):
		if scanList[i] == scanVal:
			retVal = i
			break
	return retVal
	pass

#TODO would like to find a formula way for this instead
## determine the steps to skip to not have repeats in table
def calcSkipStepsForDivTable(
	numStart :float= 1,
	numMulti :float= 2,
	numIncre :float= 2,
) -> list:
	skipStarter :int= 0
	skipRepeats :int= 0
	#TODO temp fix to prevent infinite loops
	if numIncre <= numMulti and numIncre <= numStart:
		skipStarter = -1
		colAdd :list= []
		colMul :list= []
		curNum :float= numStart
		curIdx :int= 0
		while skipStarter == -1:
			colAdd.append(curNum)
			skipStarter = getMatchIndex(colMul,curNum)
			colMul.append(
				act.floatAddorMulAsInt(
					curNum,numMulti,False,
				)
			)
			if skipStarter > -1:
				skipStarter = curIdx
				break
			else:
				curIdx += 1
				curNum = act.floatAddorMulAsInt(
					curNum,numIncre,
				)
		skipRepeats = -1
		while skipRepeats == -1:
			curNum = act.floatAddorMulAsInt(
				curNum,numIncre,
			)
			colAdd.append(curNum)
			skipRepeats = getMatchIndex(colMul,curNum)
			colMul.append(
				act.floatAddorMulAsInt(
					colAdd[curIdx],numMulti,False,
				)
			)
			if skipRepeats > -1:
				skipRepeats = curIdx - skipStarter
				break
			else:
				curIdx += 1
	return [skipStarter, skipRepeats]
	pass

## make the odd even list I needed that shows the divisions
def makeDivisionTableList(
	listTitle :str= "Num",
	numCol :int= 6,
	numRow :int= 14,
	numStart :float= 1,
	numMulti :float= 2,
	numIncre :float= 2,
) -> list:
	arrValues :list= []
	skipSteps :list= calcSkipStepsForDivTable(
		numStart,numMulti,numIncre
	)
	skipCount :int= 1
	skipStop :int= skipSteps[0]
	doStarter :bool= True
	beginIncre :float= 0 + numIncre
	beginNum :float= 0 + numStart
	priorNum :float= 0
	for r in range(numRow):
		if r > 1:
			if skipCount == skipStop:
				if doStarter:
					doStarter = False
					skipStop = skipSteps[1]
				beginNum = act.floatAddorMulAsInt(
					beginNum,beginIncre
				)
				beginNum = act.floatAddorMulAsInt(
					beginNum,beginIncre
				)
				skipCount = 1
			else:
				skipCount += 1
				beginNum = act.floatAddorMulAsInt(
					beginNum,beginIncre
				)
		for c in range(numCol):
			if r == 0:
				if c == 0:
					arrValues.append(listTitle)
				else:
					arrValues.append(c)
			else:
				if c == 0:
					arrValues.append(r)
				else:
					if c == 1:
						priorNum = 0 + beginNum
						arrValues.append(priorNum)
					else:
						priorNum = act.floatAddorMulAsInt(
							priorNum,numMulti,False
						)
						arrValues.append(priorNum)
	return arrValues
	pass

## make a list based on the difference of prior cell values
def makeTableDifList(
	allValues :list,
	doColumn :bool= True,
	doHighlight :bool= False,
) -> list:
	numCol :int= allValues[0]
	numRow :int= allValues[1]
	tableList :list= allValues[2]
	splitTable :list= dep.splitListTable(
		tableList,numCol,numRow,doColumn
	)
	difValList :list= []
	for i in range(1,numCol if doColumn else numRow):
		difValList.append([
			i+1,
			makeDifList(splitTable[i]),
			doHighlight,
		])
	return difValList
	pass

## make a list of difference values from numbers in table list
def makeDifList(
	listValue :list[float]= [],
	listTitle :str= "Dif",
	numSkip :int= 1,
) -> list:
	retList :list= []
	retList.append(listTitle)
	for i in range(numSkip):
		retList.append("")
	for i in range(numSkip+1,len(listValue)):
		numPlaces :int= act.getDecimalCount(listValue)
		numDif :float= listValue[i]-listValue[i-1]
		numDif = act.roundFloatPlaces(numDif,numPlaces)
		retList.append(numDif)
	return retList
	pass

## make a list of repeated values
def makeRepeatList(
	listValue,
	listTitle :str= "Rep",
	maxVals :int= 3,
	numSkip :int= 1,
) -> list:
	retList :list= []
	retList.append(listTitle)
	for i in range(numSkip):
		retList.append("")
	for i in range(maxVals-(1+numSkip)):
		retList.append(listValue)
	return retList
	pass
