#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.0.0b11),
    on December 12, 2018, at 12:29
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'untitled'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\chris\\OneDrive\\Desktop\\NEW EXPERIMENTS\\PsychoPy Perceptual load task\\RSVP TASK\\untitled_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1366, 768], fullscr=True, screen=0,
    allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[-1,-1,-1], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    units='pix')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "trial"
trialClock = core.Clock()
import random, subprocess
import os
import csv
import xlrd

directory = os.getcwd()
# randomise seed
random.seed()

#Filler letters
Letters = ["W", "E", "T","Y", "I", "A", "F", "H", "K", "L", "S", "V", "G", "J"]

#Target positions
Tpos = [7,8,9,10,11,12]



# green, blue, orange, yellow

FillCol = [(-1,1,-1), (-1,-1,1), (1,0.5,-1),(1,1,-1),(-1,1,-1), (-1,-1,1), (1,0.5,-1),(1,1,-1),(-1,1,-1), (-1,-1,1), (1,0.5,-1),(1,1,-1),(-1,1,-1), (-1,-1,1), (1,0.5,-1),(1,1,-1)]

h = 0.6

# Red counterbalanced
T_color = (1,-1,-1)

frameNs = [13,21,29,37,45,53,61,69,77,85,93,101,109,17,125]


startFrame1 = frameNs[0]
startFrame2 = frameNs[1]
startFrame3 = frameNs[2]
startFrame4 = frameNs[3]
startFrame5 = frameNs[4]
startFrame6 = frameNs[5]
startFrame7 = frameNs[6]
startFrame8 = frameNs[7]
startFrame9 = frameNs[8]
startFrame10 = frameNs[9]
startFrame11 = frameNs[10]
startFrame12 = frameNs[11]
startFrame13 = frameNs[12]
startFrame14 = frameNs[13]
startFrame15 = frameNs[14]

RW = (frameNs[14] + 3 + 3)
LagFrame = 0


#IMPORT DISTRACTOR IMAGES

import csv

FearLeft_trials = ['FEAR1.bmp','FEAR2.bmp','FEAR3.bmp','FEAR4.bmp','FEAR5.bmp','FEAR6.bmp','FEAR7.bmp','FEAR8.bmp','FEAR1.bmp','FEAR2.bmp','FEAR3.bmp','FEAR4.bmp','FEAR5.bmp','FEAR6.bmp','FEAR7.bmp','FEAR8.bmp']
FearRight_trials = ['FEAR1.bmp','FEAR2.bmp','FEAR3.bmp','FEAR4.bmp','FEAR5.bmp','FEAR6.bmp','FEAR7.bmp','FEAR8.bmp','FEAR1.bmp','FEAR2.bmp','FEAR3.bmp','FEAR4.bmp','FEAR5.bmp','FEAR6.bmp','FEAR7.bmp','FEAR8.bmp']
NeutralLeft_trials = ['NEUTRAL1.bmp','NEUTRAL2.bmp','NEUTRAL3.bmp','NEUTRAL4.bmp','NEUTRAL5.bmp','NEUTRAL6.bmp','NEUTRAL7.bmp','NEUTRAL8.bmp','NEUTRAL1.bmp','NEUTRAL2.bmp','NEUTRAL3.bmp','NEUTRAL4.bmp','NEUTRAL5.bmp','NEUTRAL6.bmp','NEUTRAL7.bmp','NEUTRAL8.bmp']
NeutralRight_trials = ['NEUTRAL1.bmp','NEUTRAL2.bmp','NEUTRAL3.bmp','NEUTRAL4.bmp','NEUTRAL5.bmp','NEUTRAL6.bmp','NEUTRAL7.bmp','NEUTRAL8.bmp','NEUTRAL1.bmp','NEUTRAL2.bmp','NEUTRAL3.bmp','NEUTRAL4.bmp','NEUTRAL5.bmp','NEUTRAL6.bmp','NEUTRAL7.bmp','NEUTRAL8.bmp']

#NUMBER OF DISTRACTOR IMAGES AND PRESENTATION
# 16 - 1
distractor_presentations = 15

FearLeft_marker = 0
FearRight_marker = 0
NeutralLeft_marker = 0
NeutralRight_marker = 0

random.shuffle(FearLeft_trials)
random.shuffle(FearRight_trials)
random.shuffle(NeutralLeft_trials)
random.shuffle(NeutralRight_trials)

fixation = visual.TextStim(win=win, name='fixation',
    text='+',
    font='Arial',
    pos=(0, 0), height=20, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
P1 = visual.TextStim(win=win, name='P1',
    text=None,
    font='Arial',
    pos=(0, 0), height=None, wrapWidth=None, ori=0, 
    color=None, colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
P2 = visual.TextStim(win=win, name='P2',
    text=None,
    font='Arial',
    pos=(0, 0), height=None, wrapWidth=None, ori=0, 
    color=None, colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
P3 = visual.TextStim(win=win, name='P3',
    text=None,
    font='Arial',
    pos=(0, 0), height=None, wrapWidth=None, ori=0, 
    color=None, colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
P4 = visual.TextStim(win=win, name='P4',
    text=None,
    font='Arial',
    pos=(0, 0), height=None, wrapWidth=None, ori=0, 
    color=None, colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
P5 = visual.TextStim(win=win, name='P5',
    text=None,
    font='Arial',
    pos=(0, 0), height=None, wrapWidth=None, ori=0, 
    color=None, colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
P6 = visual.TextStim(win=win, name='P6',
    text=None,
    font='Arial',
    pos=(0, 0), height=None, wrapWidth=None, ori=0, 
    color=None, colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);
P7 = visual.TextStim(win=win, name='P7',
    text=None,
    font='Arial',
    pos=(0, 0), height=None, wrapWidth=None, ori=0, 
    color=None, colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-8.0);
P8 = visual.TextStim(win=win, name='P8',
    text=None,
    font='Arial',
    pos=(0, 0), height=None, wrapWidth=None, ori=0, 
    color=None, colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-9.0);
P9 = visual.TextStim(win=win, name='P9',
    text=None,
    font='Arial',
    pos=(0, 0), height=None, wrapWidth=None, ori=0, 
    color=None, colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-10.0);
P10 = visual.TextStim(win=win, name='P10',
    text=None,
    font='Arial',
    pos=(0, 0), height=None, wrapWidth=None, ori=0, 
    color=None, colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-11.0);
P11 = visual.TextStim(win=win, name='P11',
    text=None,
    font='Arial',
    pos=(0, 0), height=None, wrapWidth=None, ori=0, 
    color=None, colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-12.0);
P12 = visual.TextStim(win=win, name='P12',
    text=None,
    font='Arial',
    pos=(0, 0), height=None, wrapWidth=None, ori=0, 
    color=None, colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-13.0);
P13 = visual.TextStim(win=win, name='P13',
    text=None,
    font='Arial',
    pos=(0, 0), height=None, wrapWidth=None, ori=0, 
    color=None, colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-14.0);
P14 = visual.TextStim(win=win, name='P14',
    text=None,
    font='Arial',
    pos=(0, 0), height=None, wrapWidth=None, ori=0, 
    color=None, colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-15.0);
P15 = visual.TextStim(win=win, name='P15',
    text=None,
    font='Arial',
    pos=(0, 0), height=None, wrapWidth=None, ori=0, 
    color=None, colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-16.0);
ResponseWindow = visual.TextStim(win=win, name='ResponseWindow',
    text='?',
    font='Arial',
    pos=(0, 0), height=20, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-17.0);
LeftDistractor = visual.ImageStim(
    win=win, name='LeftDistractor',
    image='sin', mask=None,
    ori=0, pos=(-80, 0), size=(100, 150),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-19.0)
RightDistractor = visual.ImageStim(
    win=win, name='RightDistractor',
    image='sin', mask=None,
    ori=0, pos=(80, 0), size=(100, 150),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-20.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('RSVPtrials_common.csv'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trial"-------
    t = 0
    trialClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    
    # randomise filler letters 
    random.shuffle(Letters)
    
    #randomise target position
    random.shuffle(Tpos)
    
    # select the RSVP stream letters and colours for each target position
    if Tpos[0] == 7:
        P1.setText(Letters[0])
        P2.setText(Letters[1])
        P3.setText(Letters[2])
        P4.setText(Letters[3])
        P5.setText(Letters[4])
        P6.setText(Letters[5])
        P7.setText(Target)
        P8.setText(Letters[6])
        P9.setText(Letters[7])
        P10.setText(Letters[8])
        P11.setText(Letters[9])
        P12.setText(Letters[10])
        P13.setText(Letters[11])
        P14.setText(Letters[12])
        P15.setText(Letters[13])
        
        P1.setColor(FillCol[0], 'rgb')
        P2.setColor(FillCol[1], 'rgb')
        P3.setColor(FillCol[2], 'rgb')
        P4.setColor(FillCol[3], 'rgb')
        P5.setColor(FillCol[4], 'rgb')
        P6.setColor(FillCol[5], 'rgb')
        P7.setColor(T_color, 'rgb')
        P8.setColor(FillCol[6], 'rgb')
        P9.setColor(FillCol[7], 'rgb')
        P10.setColor(FillCol[8], 'rgb')
        P11.setColor(FillCol[9], 'rgb')
        P12.setColor(FillCol[10], 'rgb')
        P13.setColor(FillCol[11], 'rgb')
        P14.setColor(FillCol[12], 'rgb')
        P15.setColor(FillCol[13], 'rgb')
    
    # set distractor lag in stream
        if Lag == 1:
            LagFrame = frameNs[5]
        elif Lag == 2:
            LagFrame = frameNs[4]
        elif Lag == 3:
            LagFrame = frameNs[3]
        elif Lag == 4:
            LagFrame = frameNs[2]
            
    elif Tpos[0] == 8:
        P1.setText(Letters[0])
        P2.setText(Letters[1])
        P3.setText(Letters[2])
        P4.setText(Letters[3])
        P5.setText(Letters[4])
        P6.setText(Letters[5])
        P7.setText(Letters[6])
        P8.setText(Target)
        P9.setText(Letters[7])
        P10.setText(Letters[8])
        P11.setText(Letters[9])
        P12.setText(Letters[10])
        P13.setText(Letters[11])
        P14.setText(Letters[12])
        P15.setText(Letters[13])
        
        P1.setColor(FillCol[0], 'rgb')
        P2.setColor(FillCol[1], 'rgb')
        P3.setColor(FillCol[2], 'rgb')
        P4.setColor(FillCol[3], 'rgb')
        P5.setColor(FillCol[4], 'rgb')
        P6.setColor(FillCol[5], 'rgb')
        P7.setColor(FillCol[6], 'rgb')
        P8.setColor(T_color, 'rgb')
        P9.setColor(FillCol[7], 'rgb')
        P10.setColor(FillCol[8], 'rgb')
        P11.setColor(FillCol[9], 'rgb')
        P12.setColor(FillCol[10], 'rgb')
        P13.setColor(FillCol[11], 'rgb')
        P14.setColor(FillCol[12], 'rgb')
        P15.setColor(FillCol[13], 'rgb')
    
    
        if Lag == 1:
            LagFrame = frameNs[6]
        elif Lag == 2:
            LagFrame = frameNs[5]
        elif Lag == 3:
            LagFrame = frameNs[4]
        elif Lag == 4:
            LagFrame = frameNs[3]
    
    elif Tpos[0] == 9:
        P1.setText(Letters[0])
        P2.setText(Letters[1])
        P3.setText(Letters[2])
        P4.setText(Letters[3])
        P5.setText(Letters[4])
        P6.setText(Letters[5])
        P7.setText(Letters[6])
        P8.setText(Letters[7])
        P9.setText(Target)
        P10.setText(Letters[8])
        P11.setText(Letters[9])
        P12.setText(Letters[10])
        P13.setText(Letters[11])
        P14.setText(Letters[12])
        P15.setText(Letters[13])
        
        P1.setColor(FillCol[0], 'rgb')
        P2.setColor(FillCol[1], 'rgb')
        P3.setColor(FillCol[2], 'rgb')
        P4.setColor(FillCol[3], 'rgb')
        P5.setColor(FillCol[4], 'rgb')
        P6.setColor(FillCol[5], 'rgb')
        P7.setColor(FillCol[6], 'rgb')
        P8.setColor(FillCol[7], 'rgb')
        P9.setColor(T_color, 'rgb')
        P10.setColor(FillCol[8], 'rgb')
        P11.setColor(FillCol[9], 'rgb')
        P12.setColor(FillCol[10], 'rgb')
        P13.setColor(FillCol[11], 'rgb')
        P14.setColor(FillCol[12], 'rgb')
        P15.setColor(FillCol[13], 'rgb')
    
        if Lag == 1:
            LagFrame = frameNs[7]
        elif Lag == 2:
            LagFrame = frameNs[6]
        elif Lag == 3:
            LagFrame = frameNs[5]
        elif Lag == 4:
            LagFrame = frameNs[4]
    
    
    elif Tpos[0] == 10:
        P1.setText(Letters[0])
        P2.setText(Letters[1])
        P3.setText(Letters[2])
        P4.setText(Letters[3])
        P5.setText(Letters[4])
        P6.setText(Letters[5])
        P7.setText(Letters[6])
        P8.setText(Letters[7])
        P9.setText(Letters[8])
        P10.setText(Target)
        P11.setText(Letters[9])
        P12.setText(Letters[10])
        P13.setText(Letters[11])
        P14.setText(Letters[12])
        P15.setText(Letters[13])
        
        P1.setColor(FillCol[0], 'rgb')
        P2.setColor(FillCol[1], 'rgb')
        P3.setColor(FillCol[2], 'rgb')
        P4.setColor(FillCol[3], 'rgb')
        P5.setColor(FillCol[4], 'rgb')
        P6.setColor(FillCol[5], 'rgb')
        P7.setColor(FillCol[6], 'rgb')
        P8.setColor(FillCol[7], 'rgb')
        P9.setColor(FillCol[8], 'rgb')
        P10.setColor(T_color, 'rgb')
        P11.setColor(FillCol[9], 'rgb')
        P12.setColor(FillCol[10], 'rgb')
        P13.setColor(FillCol[11], 'rgb')
        P14.setColor(FillCol[12], 'rgb')
        P15.setColor(FillCol[13], 'rgb')
    
        if Lag == 1:
            LagFrame = frameNs[8]
        elif Lag == 2:
            LagFrame = frameNs[7]
        elif Lag == 3:
            LagFrame = frameNs[6]
        elif Lag == 4:
            LagFrame = frameNs[5]
    
    
    
    elif Tpos[0] == 11:
        P1.setText(Letters[0])
        P2.setText(Letters[1])
        P3.setText(Letters[2])
        P4.setText(Letters[3])
        P5.setText(Letters[4])
        P6.setText(Letters[5])
        P7.setText(Letters[6])
        P8.setText(Letters[7])
        P9.setText(Letters[8])
        P10.setText(Letters[9])
        P11.setText(Target)
        P12.setText(Letters[10])
        P13.setText(Letters[11])
        P14.setText(Letters[12])
        P15.setText(Letters[13])
        
        P1.setColor(FillCol[0], 'rgb')
        P2.setColor(FillCol[1], 'rgb')
        P3.setColor(FillCol[2], 'rgb')
        P4.setColor(FillCol[3], 'rgb')
        P5.setColor(FillCol[4], 'rgb')
        P6.setColor(FillCol[5], 'rgb')
        P7.setColor(FillCol[6], 'rgb')
        P8.setColor(FillCol[7], 'rgb')
        P9.setColor(FillCol[8], 'rgb')
        P10.setColor(FillCol[9], 'rgb')
        P11.setColor(T_color, 'rgb')
        P12.setColor(FillCol[10], 'rgb')
        P13.setColor(FillCol[11], 'rgb')
        P14.setColor(FillCol[12], 'rgb')
        P15.setColor(FillCol[13], 'rgb')
    
        if Lag == 1:
            LagFrame = frameNs[9]
        elif Lag == 2:
            LagFrame = frameNs[8]
        elif Lag == 3:
            LagFrame = frameNs[7]
        elif Lag == 4:
            LagFrame = frameNs[6]
    
    
    elif Tpos[0] == 12:
        P1.setText(Letters[0])
        P2.setText(Letters[1])
        P3.setText(Letters[2])
        P4.setText(Letters[3])
        P5.setText(Letters[4])
        P6.setText(Letters[5])
        P7.setText(Letters[6])
        P8.setText(Letters[7])
        P9.setText(Letters[8])
        P10.setText(Letters[9])
        P11.setText(Letters[10])
        P12.setText(Target)
        P13.setText(Letters[11])
        P14.setText(Letters[12])
        P15.setText(Letters[13])
        
        P1.setColor(FillCol[0], 'rgb')
        P2.setColor(FillCol[1], 'rgb')
        P3.setColor(FillCol[2], 'rgb')
        P4.setColor(FillCol[3], 'rgb')
        P5.setColor(FillCol[4], 'rgb')
        P6.setColor(FillCol[5], 'rgb')
        P7.setColor(FillCol[6], 'rgb')
        P8.setColor(FillCol[7], 'rgb')
        P9.setColor(FillCol[8], 'rgb')
        P10.setColor(FillCol[9], 'rgb')
        P11.setColor(FillCol[10], 'rgb')
        P12.setColor(T_color, 'rgb')
        P13.setColor(FillCol[11], 'rgb')
        P14.setColor(FillCol[12], 'rgb')
        P15.setColor(FillCol[13], 'rgb')
    
        if Lag == 1:
            LagFrame = frameNs[10]
        elif Lag == 2:
            LagFrame = frameNs[9]
        elif Lag == 3:
            LagFrame = frameNs[8]
        elif Lag == 4:
            LagFrame = frameNs[7]
    
    
    
    random.shuffle(FearLeft_trials)
    random.shuffle(FearRight_trials)
    random.shuffle(NeutralLeft_trials)
    random.shuffle(NeutralRight_trials)
    
    if LeftD == "FEAR":
        D_R = "BLANK.bmp"
        D_L = FearLeft_trials[FearLeft_marker]
        FearLeft_marker += 1
    elif RightD == "FEAR":
        D_L = "BLANK.bmp"
        D_R = FearRight_trials[FearRight_marker]
        FearRight_marker += 1
    elif LeftD == "NEUTRAL":
        D_R = "BLANK.bmp"
        D_L = NeutralLeft_trials[NeutralLeft_marker]
        NeutralLeft_marker += 1
    elif RightD == "NEUTRAL":
        D_L = "BLANK.bmp"
        D_R =  NeutralRight_trials[NeutralRight_marker]
        NeutralRight_marker += 1
    else:
        D_L = "BLANK.bmp"
        D_R = "BLANK.bmp"
    
    FearLeft_trials[FearLeft_marker]
    FearRight_trials[FearRight_marker]
    NeutralLeft_trials[NeutralLeft_marker]
    NeutralRight_trials[NeutralRight_marker]
    
    
    
    
    
    response = event.BuilderKeyResponse()
    LeftDistractor.setImage(D_L)
    RightDistractor.setImage(D_R)
    # keep track of which components have finished
    trialComponents = [fixation, P1, P2, P3, P4, P5, P6, P7, P8, P9, P10, P11, P12, P13, P14, P15, ResponseWindow, response, LeftDistractor, RightDistractor]
    for thisComponent in trialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "trial"-------
    while continueRoutine:
        # get current time
        t = trialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # *fixation* updates
        if frameN >= 0.0 and fixation.status == NOT_STARTED:
            # keep track of start time/frame for later
            fixation.tStart = t
            fixation.frameNStart = frameN  # exact frame index
            fixation.setAutoDraw(True)
        if fixation.status == STARTED and frameN >= (fixation.frameNStart + 12):
            fixation.setAutoDraw(False)
        
        # *P1* updates
        if frameN >= startFrame1 and P1.status == NOT_STARTED:
            # keep track of start time/frame for later
            P1.tStart = t
            P1.frameNStart = frameN  # exact frame index
            P1.setAutoDraw(True)
        if P1.status == STARTED and frameN >= (P1.frameNStart + 3):
            P1.setAutoDraw(False)
        
        # *P2* updates
        if frameN >= startFrame2 and P2.status == NOT_STARTED:
            # keep track of start time/frame for later
            P2.tStart = t
            P2.frameNStart = frameN  # exact frame index
            P2.setAutoDraw(True)
        if P2.status == STARTED and frameN >= (P2.frameNStart + 3):
            P2.setAutoDraw(False)
        
        # *P3* updates
        if frameN >= startFrame3 and P3.status == NOT_STARTED:
            # keep track of start time/frame for later
            P3.tStart = t
            P3.frameNStart = frameN  # exact frame index
            P3.setAutoDraw(True)
        if P3.status == STARTED and frameN >= (P3.frameNStart + 3):
            P3.setAutoDraw(False)
        
        # *P4* updates
        if frameN >= startFrame4 and P4.status == NOT_STARTED:
            # keep track of start time/frame for later
            P4.tStart = t
            P4.frameNStart = frameN  # exact frame index
            P4.setAutoDraw(True)
        if P4.status == STARTED and frameN >= (P4.frameNStart + 3):
            P4.setAutoDraw(False)
        
        # *P5* updates
        if frameN >= startFrame5 and P5.status == NOT_STARTED:
            # keep track of start time/frame for later
            P5.tStart = t
            P5.frameNStart = frameN  # exact frame index
            P5.setAutoDraw(True)
        if P5.status == STARTED and frameN >= (P5.frameNStart + 3):
            P5.setAutoDraw(False)
        
        # *P6* updates
        if frameN >= startFrame6 and P6.status == NOT_STARTED:
            # keep track of start time/frame for later
            P6.tStart = t
            P6.frameNStart = frameN  # exact frame index
            P6.setAutoDraw(True)
        if P6.status == STARTED and frameN >= (P6.frameNStart + 3):
            P6.setAutoDraw(False)
        
        # *P7* updates
        if frameN >= startFrame7 and P7.status == NOT_STARTED:
            # keep track of start time/frame for later
            P7.tStart = t
            P7.frameNStart = frameN  # exact frame index
            P7.setAutoDraw(True)
        if P7.status == STARTED and frameN >= (P7.frameNStart + 3):
            P7.setAutoDraw(False)
        
        # *P8* updates
        if frameN >= startFrame8 and P8.status == NOT_STARTED:
            # keep track of start time/frame for later
            P8.tStart = t
            P8.frameNStart = frameN  # exact frame index
            P8.setAutoDraw(True)
        if P8.status == STARTED and frameN >= (P8.frameNStart + 3):
            P8.setAutoDraw(False)
        
        # *P9* updates
        if frameN >= startFrame9 and P9.status == NOT_STARTED:
            # keep track of start time/frame for later
            P9.tStart = t
            P9.frameNStart = frameN  # exact frame index
            P9.setAutoDraw(True)
        if P9.status == STARTED and frameN >= (P9.frameNStart + 3):
            P9.setAutoDraw(False)
        
        # *P10* updates
        if frameN >= startFrame10 and P10.status == NOT_STARTED:
            # keep track of start time/frame for later
            P10.tStart = t
            P10.frameNStart = frameN  # exact frame index
            P10.setAutoDraw(True)
        if P10.status == STARTED and frameN >= (P10.frameNStart + 3):
            P10.setAutoDraw(False)
        
        # *P11* updates
        if frameN >= startFrame11 and P11.status == NOT_STARTED:
            # keep track of start time/frame for later
            P11.tStart = t
            P11.frameNStart = frameN  # exact frame index
            P11.setAutoDraw(True)
        if P11.status == STARTED and frameN >= (P11.frameNStart + 3):
            P11.setAutoDraw(False)
        
        # *P12* updates
        if frameN >= startFrame12 and P12.status == NOT_STARTED:
            # keep track of start time/frame for later
            P12.tStart = t
            P12.frameNStart = frameN  # exact frame index
            P12.setAutoDraw(True)
        if P12.status == STARTED and frameN >= (P12.frameNStart + 3):
            P12.setAutoDraw(False)
        
        # *P13* updates
        if frameN >= startFrame13 and P13.status == NOT_STARTED:
            # keep track of start time/frame for later
            P13.tStart = t
            P13.frameNStart = frameN  # exact frame index
            P13.setAutoDraw(True)
        if P13.status == STARTED and frameN >= (P13.frameNStart + 3):
            P13.setAutoDraw(False)
        
        # *P14* updates
        if frameN >= startFrame14 and P14.status == NOT_STARTED:
            # keep track of start time/frame for later
            P14.tStart = t
            P14.frameNStart = frameN  # exact frame index
            P14.setAutoDraw(True)
        if P14.status == STARTED and frameN >= (P14.frameNStart + 3):
            P14.setAutoDraw(False)
        
        # *P15* updates
        if frameN >= startFrame15 and P15.status == NOT_STARTED:
            # keep track of start time/frame for later
            P15.tStart = t
            P15.frameNStart = frameN  # exact frame index
            P15.setAutoDraw(True)
        if P15.status == STARTED and frameN >= (P15.frameNStart + 3):
            P15.setAutoDraw(False)
        
        # *ResponseWindow* updates
        if frameN >= RW and ResponseWindow.status == NOT_STARTED:
            # keep track of start time/frame for later
            ResponseWindow.tStart = t
            ResponseWindow.frameNStart = frameN  # exact frame index
            ResponseWindow.setAutoDraw(True)
        
        # *response* updates
        if frameN >= RW and response.status == NOT_STARTED:
            # keep track of start time/frame for later
            response.tStart = t
            response.frameNStart = frameN  # exact frame index
            response.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(response.clock.reset)  # t=0 on next screen flip
        if response.status == STARTED:
            theseKeys = event.getKeys(keyList=['z', 'x', 'n', 'm'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                response.keys = theseKeys[-1]  # just the last key pressed
                response.rt = response.clock.getTime()
                # was this 'correct'?
                if (response.keys == str(correctresp)) or (response.keys == correctresp):
                    response.corr = 1
                else:
                    response.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # *LeftDistractor* updates
        if frameN >= LagFrame and LeftDistractor.status == NOT_STARTED:
            # keep track of start time/frame for later
            LeftDistractor.tStart = t
            LeftDistractor.frameNStart = frameN  # exact frame index
            LeftDistractor.setAutoDraw(True)
        if LeftDistractor.status == STARTED and frameN >= (LeftDistractor.frameNStart + 3):
            LeftDistractor.setAutoDraw(False)
        
        # *RightDistractor* updates
        if frameN >= LagFrame and RightDistractor.status == NOT_STARTED:
            # keep track of start time/frame for later
            RightDistractor.tStart = t
            RightDistractor.frameNStart = frameN  # exact frame index
            RightDistractor.setAutoDraw(True)
        if RightDistractor.status == STARTED and frameN >= (RightDistractor.frameNStart + 3):
            RightDistractor.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # check responses
    if response.keys in ['', [], None]:  # No response was made
        response.keys=None
        # was no response the correct answer?!
        if str(correctresp).lower() == 'none':
           response.corr = 1;  # correct non-response
        else:
           response.corr = 0;  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('response.keys',response.keys)
    trials.addData('response.corr', response.corr)
    if response.keys != None:  # we had a response
        trials.addData('response.rt', response.rt)
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials'

# get names of stimulus parameters
if trials.trialList in ([], [None], None):
    params = []
else:
    params = trials.trialList[0].keys()
# save data for this loop
trials.saveAsExcel(filename + '.xlsx', sheetName='trials',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
trials.saveAsText(filename + 'trials.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
