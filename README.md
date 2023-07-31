# SoME3 Divide Even By 2 Until Odd
Code I wrote for my SoME3 Presentation about division of numbers. Specifically I made it for how many times an Even number can be divided by 2 until it reaches Odd.

# Presentation
WIP

# Table Demo
This code is provided as-is, if you want to use it or improve upon it then feel free. I wound up writing this table code since the base Manim code did not seem to have the functions I wanted to do with a table. If someone would like to implement this or something like this into Manim itself that might be helpful to others. For now though if anyone has a need of it, this at least mostly works.

This is to show off the table code I wrote. It has various issues and limitations. I have a TODO in one spot where I could fix the inserts, but is not needed for what it is. The concepts of what is being done is a rectangle with a lower stroked text and a non stroked text above it. I also have a separate VMobject to represent whether the whole thing is highlighted or not. It was a quick fix to add that rather than rewrite code I already had.

The textboxes are made from a list of values. All of the appropriate values are stored in an allValues list. That variable is then passed to the functions to do whatever is needed from there. I put typed variables in almost every spot. I am used to doing that in godot gdscript, and since that is similar to python did the same here. It may not be correct but should be close.

The tableDEMO.py shows the main functions that will be used. There will be others that I will make for the presentation, but these are the base functions for insert/delete/highlight/rescale etc.

In the codeBase folder is the code itself. Act.py is where the main functions that will be called are in. Dep.py is most of the dependant functions that are used by act.py and lastly const.py is some default variables I use for the allValues base table.

https://github.com/CigamPower/SoME3-Divide-Even-By-2-Until-Odd/assets/43964088/06146fa5-a44b-4fc6-8cd7-0ab287237d01


