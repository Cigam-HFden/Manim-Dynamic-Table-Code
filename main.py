######
# ---Credit---
# Code made for SoME3 video presentation:
# Divide Even By 2 Until Odd
# Cigam
# 202307
# ---Notes---
# This is the code for the main SoME3 presenation
# ---Utils---
# Manim Community Edition v0.17.3
# Manim Voiceover v0.3.3.post0
# MikTex v23.4
# ffmpeg v4.2.3
# python v3.11.4
# ---Links---
# SoME3 discord project post:
# https://discord.com/channels/834837272234426438/1125156889408307250
# Manim CE discord help post:
# https://discord.com/channels/581738731934056449/1127278550853111949
# Code for video in SoME3:
# https://github.com/CigamPower/SoME3-Divide-Even-By-2-Until-Odd
# Youtube video for SoME3:
# TBD
######

######
# Includes:
######

from codeBase import const #custom constants used as default values
# from codeBase import dep #custom functions that are dependencies
from codeBase import act #custom functions that are actionable
from codeShow import show #custom functions that are specific to show the presentation

from manim import *
from manim_voiceover import VoiceoverScene
# from manim_voiceover.services.gtts import GTTSService
# from manim.utils.color import Colors
# from copy import deepcopy

######
# Main Class:
######

class main(VoiceoverScene):
	def construct(self) -> None:

		show.setSpeechSettings(self)
		show.createBackground(self)

		voWait :float= const.TimeWait

		# intro
		listIntro :list= show.voiceOverCall(
			self,voWait,
			"Divide Even By 2 Until Odd. By Kegam.",
			"Divide Even By 2 Until Odd. By Cigam.",
			show.makeIntroTitle,
			self,
		)
		listSlideName :list= show.voiceOverCall(
			self,0,
			"This formula was created when I was testing some ideas of binary and primes.",
			"",
			show.makeTitleToName,
			self,listIntro,"Task:",
		)

		# Info on how it started
		listInfoText :list= show.voiceOverCall(
			self,0,
			"I was needing to solve how many times a number could be divided by 2 until it divides into a decimal. My tests were done in a spreadsheet app, so the limitation was fitting it into one cell.",
			"",
			show.makeInfoDescription,
			self,[],[
				"Solve:",
				"How many times an even number can be divided by 2 until reaching an odd number",
				"Requirements:",
				"Fit formula into a single cell of a spreadsheet",
			],
		)
		listInfoText = show.voiceOverCall(
			self,0,
			"Manually dividing would not work, and doing the binary count conversion was limited to only 1024.",
			"",
			show.makeInfoDescription,
			self,listInfoText,[
				"Not usable options:",
				"Manually divide (takes more than one cell)\n\tBinary 0 count (is limited to 10 bits in app)",
				"Base Line:",
				"Odd numbers cannot be divided by 2 without going into decimals.\n\tEvens therefore are the starting numbers to divide from.",
			],
		)

		listSlideName = show.voiceOverCall(
			self,0,
			"I started with odds as the base line, since they cannot be divided by 2, and still be a whole number. With even numbers becoming the starting numbers.",
			"",
			show.makeSlideName,
			self,listSlideName,"Table:",
		)
		listInfoText = show.voiceOverCall(
			self,0,
			"Here is the table I created to start my tests.",
			"",
			show.makeInfoDescription,
			self,listInfoText,[
				"Columns:",
				"First column is odds\n\tEach following column is 2 times the previous",
				"Rows:",
				"First row is the power of 2 binary values",
				"Column Number:",
				"Number of times it can be divided by 2 + 1",
			],
		)

		# start of table showing
		allValues :list= act.makeBaseTable(6,14)
		allValues = act.makeTableList(
			allValues,
			show.makeDivisionTableList(
				"Num",allValues[0],allValues[1],
				1,2,2
			),
			True,
			False,
		)[1]
		displayVgr :VGroup= act.makeVgroup(allValues[4])
		displayVgr.to_edge(UL)
		show.voiceOverCall(
			self,voWait,
			"The first column is odd numbers. Each following column is 2 times the previous. The first row is the powers of 2. The column number equals how many times that number can be divided by 2 + 1.",
			"",
			act.writeVgroup,
			self,displayVgr,
		)

		# difference values
		insertList :list= show.makeTableDifList(
			allValues,True,True,
		)
		allValues = show.voiceOverCall(
			self,0,
			"The difference between the rows of each column are all powers of 2.",
			"",
			act.insertTableListLines,
			self,allValues,insertList,True,
		)
		listInfoText = show.voiceOverCall(
			self,voWait,
			"2 raised to the column number, gives a persistent number to make a formula from. Using the row and column numbers we can verify we get the proper value.",
			"",
			show.makeInfoDescription,
			self,listInfoText,[
				"Row Differences:",
				"Each difference is 2 raised to the column number\n\tThis gives a persistent number to make the formula from",
				"Calculate Input:",
				"Using the row and column numbers we can verify we get the proper value",
			],
		)

		# number from col and row
		allValues = show.voiceOverCall(
			self,0,
			"For now we will focus on just column 5.",
			"",
			act.deleteTableListLines,
			self,allValues,[2,4,6,8],
		)
		allValues = show.voiceOverCall(
			self,0,
			"Column 5, row 9, has a value of 272.",
			"",
			act.shimmerStyleSelected,
			self,allValues,
			[
				[5,0,True],
				[0,9,True],
				[5,9,True],
				[True,6,False],
			],
			False,
		)
		listSlideName = show.voiceOverCall(
			self,0,
			"Now let us calculate the input.",
			"",
			show.makeSlideName,
			self,listSlideName,"Calculate Input:",
		)
		listInfoText = show.voiceOverCall(
			self,voWait,
			"I worked out two formulas to get the input number from the column, row, and the divisor numbers.",
			"",
			show.makeInfoDescription,
			self,listInfoText,[
				"Variables:",
				"C = Col = 5\n\tR = Row = 9\n\tD = Divisor = 2\n\tN = Input = 272",
				"Formulas:",
				"((D*R)-1)*(D^(C-1))\n\tor\n\t((D^C)*R)-(D^C-1))",
			],
		)

		# ceiling log decimal
		allValues = show.voiceOverCall(
			self,0,
			"Division decimal.",
			"",
			act.deleteTableListLines,
			self,allValues,[2,3,4,6],
		)
		listSlideName = show.voiceOverCall(
			self,0,
			"Now.",
			"",
			show.makeSlideName,
			self,listSlideName,"Decimal Col:",
		)
		insertList = [
			[3,["CeLoD",4,6,7,7,8,8,8,8,9,9,9,9,9],False],
			[3,["PowD",16,64,128,128,256,256,256,256,512,512,512,512,512],False],
			[3,["Num/PowD",1,0.75,0.625,0.875,0.5625,0.6875,0.8125,0.9375,0.53125,0.59375,0.65625,0.71875,0.78125],True],
		]
		allValues = show.voiceOverCall(
			self,0,
			"Ceiling Log 2.",
			"",
			act.insertTableListLines,
			self,allValues,insertList,True,
		)
		allValues = show.voiceOverCall(
			self,0,
			"Something.",
			"",
			act.shimmerStyleSelected,
			self,allValues,
			[
				[2,0,False],
				[0,9,False],
				[2,9,False],
			],
			False,
		)

		# length to column
		insertList = [
			[6,["Len",0,2,3,3,4,4,4,4,5,5,5,5,5],False],
			[6,["Col",5,5,5,5,5,5,5,5,5,5,5,5,5],False],
		]
		allValues = show.voiceOverCall(
			self,0,
			"Column from decimal length.",
			"",
			act.insertTableListLines,
			self,allValues,insertList,True,
		)
		allValues = show.voiceOverCall(
			self,0,
			"Something.",
			"",
			act.shimmerStyleSelected,
			self,allValues,
			[
				[True,5,False],
				[True,6,True],
			],
			False,
		)

		# view as fraction
		allValues = act.replaceTableListLines(
			self,allValues,[
				[7,
				["Frac",1,"3/4","5/8","7/8","9/16","11/16","13/16","15/16","17/32","19/32","21/32","23/32","25/32"],
				True,],
			],True
		)

		# LCM fraction
		allValues = show.voiceOverCall(
			self,0,
			"LCM fraction.",
			"",
			act.deleteTableListLines,
			self,allValues,[5,6,7],
		)
		insertList = [
			[5,["LCM",16,96,320,448,1152,1408,1664,1920,4352,4864,5376,5888,6400],False],
			[5,["Nmr",1,3,5,7,9,11,13,15,17,19,21,23,25],True],
			[5,["Dnm",1,4,8,8,16,16,16,16,32,32,32,32,32],False],
			[5,["Nmr/Dnm",1,0.75,0.625,0.875,0.5625,0.6875,0.8125,0.9375,0.53125,0.59375,0.65625,0.71875,0.78125],False],
		]
		allValues = show.voiceOverCall(
			self,0,
			"Numerator and Denominator.",
			"",
			act.insertTableListLines,
			self,allValues,insertList,True,
		)
		allValues = show.voiceOverCall(
			self,0,
			"Something.",
			"",
			act.shimmerStyleSelected,
			self,allValues,
			[
				[True,1,True],
			],
			False,
		)
		
		# using floor log 2
		allValues = act.replaceTableListLines(
			self,allValues,[
				[3,
				["FlLoD",4,5,6,6,7,7,7,7,8,8,8,8,8],
				False,],
				[7,["Dnm",1,2,4,4,8,8,8,8,16,16,16,16,16],False],
				[8,["Nmr/Dnm",1,1.5,1.25,1.75,1.125,1.375,1.625,1.875,1.0625,1.1875,1.3125,1.4375,1.5625],False],
			],True
		)
		allValues = show.voiceOverCall(
			self,0,
			"Something.",
			"",
			act.shimmerStyleSelected,
			self,allValues,
			[
				[True,1,False],
				[True,6,False],
				[True,0,True],
				[True,7,True],
			],
			False,
		)
		
		# relation to row
		allValues = act.replaceTableListLines(
			self,allValues,[
				[8,["CLRow",0,1,2,2,3,3,3,3,4,4,4,4,4],False],
				[8,["Pow",1,2,4,4,8,8,8,8,16,16,16,16,16],True],
			],True
		)
		allValues = show.voiceOverCall(
			self,0,
			"Something.",
			"",
			act.shimmerStyleSelected,
			self,allValues,
			[
				[True,0,False],
				[True,7,False],
				[True,9,False],
			],
			False,
		)

		# show 3 tables
		displayVgr = act.makeVgroup(allValues[4])
		displayVgr.save_state()
		act.writeVgroup(self,displayVgr,False)

		table1 :list= act.makeBaseTable(6,14)
		table1 = act.makeTableList(
			table1,
			show.makeDivisionTableList(
				"Num",table1[0],table1[1],
				1,2,2
			),
			True,
			False,
		)[1]
		displayTable1 :VGroup= act.makeVgroup(table1[4])
		displayTable1.to_edge(DL)

		table2 :list= act.makeBaseTable(6,14)
		table2 = act.makeTableList(
			table2,
			[
				"Numrs",1,2,3,4,5,
				1,1,1,1,1,1,
				2,3,3,3,3,3,
				3,5,5,5,5,5,
				4,7,7,7,7,7,
				5,9,9,9,9,9,
				6,11,11,11,11,11,
				7,13,13,13,13,13,
				8,15,15,15,15,15,
				9,17,17,17,17,17,
				10,19,19,19,19,19,
				11,21,21,21,21,21,
				12,23,23,23,23,23,
				13,25,25,25,25,25,
			],
			True,
			False,
		)[1]
		displayTable2 :VGroup= act.makeVgroup(table2[4])
		alignTo :np.ndarray= displayTable1.get_critical_point(UR)
		displayTable2.move_to(alignTo,aligned_edge=UL,)

		table3 :list= act.makeBaseTable(6,14)
		table3 = act.makeTableList(
			table3,
			[
				"Dnms",1,2,3,4,5,
				1,1,1,1,1,1,
				2,2,2,2,2,2,
				3,4,4,4,4,4,
				4,4,4,4,4,4,
				5,8,8,8,8,8,
				6,8,8,8,8,8,
				7,8,8,8,8,8,
				8,8,8,8,8,8,
				9,16,16,16,16,16,
				10,16,16,16,16,16,
				11,16,16,16,16,16,
				12,16,16,16,16,16,
				13,16,16,16,16,16,
			],
			True,
			False,
		)[1]
		displayTable3 :VGroup= act.makeVgroup(table3[4])
		alignTo :np.ndarray= displayTable2.get_critical_point(UR)
		displayTable3.move_to(alignTo,aligned_edge=UL,)

		display3Tables :VGroup= act.makeVgroup([
			displayTable1,displayTable2,displayTable3
		])
		act.writeVgroup(self,display3Tables)
		act.writeVgroup(self,display3Tables,False)

		self.play(
			Restore(displayVgr),
			reverse = False,
			run_time = const.TimeWait
		)
		# act.writeVgroup(self,displayVgr)


		# allValues = show.voiceOverCall(
		# 	self,0,
		# 	"Something.",
		# 	"",
		# 	act.deleteTableListLines,
		# 	self,allValues,[7,8],
		# )

		# allValues = act.deleteTableListLines(
		# 	self,allValues,[0,2],
		# )
		# allValues = act.deleteTableListLines(
		# 	self,allValues,[1,2],
		# )
		# allValues = act.deleteTableListLines(
		# 	self,allValues,[0,1,3,5,7,8,9],False,
		# )

		# insertList :list= [
		# 	[0,
		# 	act.makeRepeatList("A","Pre",allValues[0],),
		# 	False,],
		# 	[0,
		# 	act.makeRepeatList("A","Pre",allValues[0],),
		# 	True,],
		# 	[2,
		# 	act.makeRepeatList("B","Mid",allValues[0],),
		# 	None,],
		# 	[2,
		# 	act.makeRepeatList("B","Mid",allValues[0],),
		# 	None,],
		# 	[3,
		# 	act.makeRepeatList("C","Mid",allValues[0],),
		# 	None,],
		# 	[3,
		# 	act.makeRepeatList("C","Mid",allValues[0],),
		# 	None,],
		# 	[allValues[1],
		# 	act.makeRepeatList("D","Pos",allValues[0],),
		# 	True,],
		# 	[allValues[1],
		# 	act.makeRepeatList("D","Pos",allValues[0],),
		# 	False,],
		# ]

		# allValues = act.insertTableListLines(
		# 	self,allValues,insertList,False
		# )

		# allValues = act.shimmerStyleTable(
		# 	self,allValues,None
		# )
		# allValues = act.shimmerStyleTable(
		# 	self,allValues,False
		# )
		# allValues = act.shimmerStyleTable(
		# 	self,allValues,True
		# )

		# allValues = act.shimmerStyleSelected(
		# 	self,allValues,
		# 	[
		# 		[True,6,None],
		# 		[False,6,None],
		# 		[3,3,None],
		# 	],
		# 	True,
		# )

		displayVgr = act.makeVgroup(allValues[4])
		act.writeVgroup(self,displayVgr,False)

		show.voiceOverCall(
			self,voWait,
			"Created with Manim Community Edition.",
			"",
			show.makeManimBanner,
			self,
		)

		pass
