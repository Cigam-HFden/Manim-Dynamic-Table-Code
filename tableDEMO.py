######
# ---Credit---
# Code made for SoME3 video presentation:
# Divide Even By 2 Until Odd
# Cigam
# 202307
# ---Notes---
# Demo for table code functions I wrote for the presentation
# ---Utils---
# Manim Community Edition v0.17.3
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

# from codeBase import const #custom constants used as default values
# from codeBase import dep #custom functions that are dependencies
from codeBase import act #custom functions that are actionable

from manim import *

######
# Main Class:
######

class tableDEMO(Scene):
	def construct(self) -> None:

		#add background color to see table easier
		background :Rectangle= Rectangle(
			width = config.frame_width,
			height = config.frame_height,
			stroke_width = 0,
			fill_color = [PURPLE_E, BLACK],
			fill_opacity = 1,
			sheen_direction = DOWN,
			z_index = -10,
		)
		self.add(background)

		# create base table with column and rows defined
		allValues :list= act.makeBaseTable(6,6)

		# create a list to be the table values and make it
		tableValList :list= []
		for i in range(allValues[0]*allValues[1]):
			tableValList.append(i)
		allValues = act.makeTableList(
			allValues,
			tableValList,
			True,
			False,
		)[1]

		# print out some of the values to see them
		act.printt([
			allValues[0],
			allValues[1],
			allValues[2],
			allValues[3],
			allValues[4],
			],"\n\n")

		# display the table
		displayVgr :VGroup= act.makeVgroup(allValues[4])
		displayVgr.to_edge(UL)
		act.writeVgroup(self,displayVgr)

		# insert list of values into columns
		insertList :list= [
			[0,["Col",1,"A","B","C","D"],False],
			[0,["Col",2,"A","B","C","D"],True],
			[3,["Col",3,"A","B","C","D"],True],
			[3,["Col",4,"A","B","C","D"],None],
			[6,["Col",5,"A","B","C","D"],True],
			[6,["Col",6,"A","B","C","D"],False],
		]
		allValues = act.insertTableListLines(
			self,allValues,insertList,True
		)
		# insert list of values into rows
		insertList :list= [
			[0,["Row",1,0,0,0,0,0,0,0,0,0,1],False],
			[0,["Row",2,0,0,0,0,0,0,0,0,0,2],True],
			[3,["Row",3,0,0,0,0,0,0,0,0,0,3],True],
			[3,["Row",4,0,0,0,0,0,0,0,0,0,4],None],
			[6,["Row",5,0,0,0,0,0,0,0,0,0,5],True],
			[6,["Row",6,0,0,0,0,0,0,0,0,0,6],False],
		]
		allValues = act.insertTableListLines(
			self,allValues,insertList,False
		)

		# replace lines in columns
		allValues = act.replaceTableListLines(
			self,allValues,
			[
				[1,["RepCol",0,1,2,3,4,5,4,3,2,1,0,],False],
				[1,["RepCol",0,1,2,3,4,5,4,3,2,1,0,],None],
				[5,["RepCol",0,1,2,3,4,5,4,3,2,1,0,],None],
				[5,["RepCol",0,1,2,3,4,5,4,3,2,1,0,],False],
			],
			True,
		)
		# replace lines in rows
		allValues = act.replaceTableListLines(
			self,allValues,
			[
				[1,["RepRow",0,1,2,3,4,5,4,3,2,1,0,8,9],False],
				[1,["RepRow",0,1,2,3,4,5,4,3,2,1,0,8,9],None],
				[5,["RepRow",0,1,2,3,4,5,4,3,2,1,0,8,9],None],
				[5,["RepRow",0,1,2,3,4,5,4,3,2,1,0,8,9],False],
			],
			False,
		)

		# rescale to fix insert problems
		allValues = act.scaleTableFontSize(
			self,allValues,True,allValues[7],None
		)

		#TODO broken here for some reason not sure why
		# delete line columns
		allValues = act.deleteTableListLines(
			self,allValues,[2,5,6],
		)
		# delete line rows
		allValues = act.deleteTableListLines(
			self,allValues,[0,4,5,6,allValues[1]-1],False
		)

		# rescale after delete to fix size
		allValues = act.scaleTableFontSize(
			self,allValues,True,allValues[7],None
		)
		#recale to 1.5 times the size
		allValues = act.scaleTableFontSize(
			self,allValues,False,1.75,None
		)

		# shimmer betwen different highlight styles
		allValues = act.shimmerStyleTable(
			self,allValues,None
		)
		allValues = act.shimmerStyleTable(
			self,allValues,False
		)
		allValues = act.shimmerStyleTable(
			self,allValues,True
		)

		# change the style of lines and cells
		allValues = act.shimmerStyleSelected(
			self,allValues,
			[
				[True,6,None],
				[False,6,None],
				[3,3,None],
				[1,2,None],
			],
			True,
		)

		# remove the table
		displayVgr = act.makeVgroup(allValues[4])
		act.writeVgroup(self,displayVgr,False)

		pass
