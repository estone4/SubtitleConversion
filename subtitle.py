# -*- coding:utf-8 -*-

"""
Subtitle converter

Corrects improper Turkish characters.
"""

# IMPORTS
# --------------------------------------------------------
# import glob
# --------------------------------------------------------

# VARIABLES
# --------------------------------------------------------
# fileDict = {}
# fileContents = []
data = ""
# --------------------------------------------------------

# MAIN PROGRAM
# --------------------------------------------------------
# for file in glob.glob('*.srt'):

f = open("a-walk-to-remember_turkish-22705.srt", "r", encoding="ISO-8859-9")
# print("Test")		#DEBUG PRINT
data = f.read()
f.close()
# print(data)		# DEBUG PRINT

f = open("SubtitleTest.srt", "w", encoding="utf-8")
f.write(data)
f.close()
# print(data)		#DEBUG PRINT

# print(type(data))	#DEBUG PRINT
# --------------------------------------------------------
