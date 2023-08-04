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
			" I started with odds as the base line, since they cannot be divided by 2, and still be a whole number. With even numbers becoming the starting numbers.",
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
			"The first column is odd numbers. Each following column is 2 times the previous. The first row is the powers of 2. The column number equals how many times that number can be divided by 2, plus 1.",
			"",
			act.writeVgroup,
			self,displayVgr,
		)

		listInfoText = show.voiceOverCall(
			self,0,
			"The difference between the rows of each column are all powers of 2.",
			"",
			show.makeInfoDescription,
			self,listInfoText,[
				"Row Differences:",
				"Each difference is 2 raised to the column number\n\tThis gives a persistent number to make the formula from",
				"Calculate Input:",
				"Using the row and column numbers we can ensure we get the proper value",
			],
		)

		insertList :list= show.makeTableDifList(
			allValues,True,True,
		)
		allValues = show.voiceOverCall(
			self,voWait,
			"2 raised to the column number, gives a persistent number to make a formula from. Using the row and column numbers we can ensure we get the proper value.",
			"",
			act.insertTableListLines,
			self,allValues,insertList,True,
		)
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
				[True,6,False],
				[5,0,True],
				[0,9,True],
				[5,9,True],
			],
			False,
		)

		# allValues = act.replaceTableListLines(
		# 	self,allValues,[
		# 		[1,
		# 		act.makeRepeatList("=","Rep",allValues[1],),
		# 		False,],
		# 	],True
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
