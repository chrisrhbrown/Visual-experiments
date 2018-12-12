/*************************** 
 * Letterrsvp_Commond Test *
 ***************************/

import { PsychoJS } from './lib/core-3.0.0b11.js';
import * as core from './lib/core-3.0.0b11.js';
import { TrialHandler } from './lib/data-3.0.0b11.js';
import { Scheduler } from './lib/util-3.0.0b11.js';
import * as util from './lib/util-3.0.0b11.js';
import * as visual from './lib/visual-3.0.0b11.js';

// init psychoJS:
var psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([(- 1), (- 1), (- 1)]),
  units: 'pix'
});

// store info about the experiment session:
let expName = 'LetterRSVP_commonD';  // from the Builder filename that created this script
let expInfo = {'participant': '', 'session': '001'};

// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
const trialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trialsLoopBegin, trialsLoopScheduler);
flowScheduler.add(trialsLoopScheduler);
flowScheduler.add(trialsLoopEnd);
flowScheduler.add(quitPsychoJS, true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, false);

psychoJS.start({configURL: 'config.json', expInfo: expInfo});

var frameDur;
function updateInfo() {
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;

  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0/Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0/60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  psychoJS.setRedirectUrls('completedURL', 'incompleteURL');
  return Scheduler.Event.NEXT;
}

var trialClock;
var fixation;
var P1;
var P2;
var P3;
var P4;
var P5;
var P6;
var P7;
var P8;
var P9;
var P10;
var P11;
var P12;
var P13;
var P14;
var P15;
var ResponseWindow;
var LeftDistractor;
var RightDistractor;
var globalClock;
var routineTimer;
function experimentInit() {
  // Initialize components for Routine "trial"
  trialClock = new util.Clock();
  
  fixation = new visual.TextStim({
    win : psychoJS.window,
    name : 'fixation',
    text : '+',
    font : 'Arial',
    pos : [0, 0], height : 20,  wrapWidth : undefined, ori: 0,
    color : new util.Color('black'),  opacity : 1,
    depth : -1.0 
  });
  
  P1 = new visual.TextStim({
    win : psychoJS.window,
    name : 'P1',
    text : None,
    font : 'Arial',
    pos : [0, 0], height : None,  wrapWidth : undefined, ori: 0,
    color : new util.Color(None),  opacity : 1,
    depth : -2.0 
  });
  
  P2 = new visual.TextStim({
    win : psychoJS.window,
    name : 'P2',
    text : None,
    font : 'Arial',
    pos : [0, 0], height : None,  wrapWidth : undefined, ori: 0,
    color : new util.Color(None),  opacity : 1,
    depth : -3.0 
  });
  
  P3 = new visual.TextStim({
    win : psychoJS.window,
    name : 'P3',
    text : None,
    font : 'Arial',
    pos : [0, 0], height : None,  wrapWidth : undefined, ori: 0,
    color : new util.Color(None),  opacity : 1,
    depth : -4.0 
  });
  
  P4 = new visual.TextStim({
    win : psychoJS.window,
    name : 'P4',
    text : None,
    font : 'Arial',
    pos : [0, 0], height : None,  wrapWidth : undefined, ori: 0,
    color : new util.Color(None),  opacity : 1,
    depth : -5.0 
  });
  
  P5 = new visual.TextStim({
    win : psychoJS.window,
    name : 'P5',
    text : None,
    font : 'Arial',
    pos : [0, 0], height : None,  wrapWidth : undefined, ori: 0,
    color : new util.Color(None),  opacity : 1,
    depth : -6.0 
  });
  
  P6 = new visual.TextStim({
    win : psychoJS.window,
    name : 'P6',
    text : None,
    font : 'Arial',
    pos : [0, 0], height : None,  wrapWidth : undefined, ori: 0,
    color : new util.Color(None),  opacity : 1,
    depth : -7.0 
  });
  
  P7 = new visual.TextStim({
    win : psychoJS.window,
    name : 'P7',
    text : None,
    font : 'Arial',
    pos : [0, 0], height : None,  wrapWidth : undefined, ori: 0,
    color : new util.Color(None),  opacity : 1,
    depth : -8.0 
  });
  
  P8 = new visual.TextStim({
    win : psychoJS.window,
    name : 'P8',
    text : None,
    font : 'Arial',
    pos : [0, 0], height : None,  wrapWidth : undefined, ori: 0,
    color : new util.Color(None),  opacity : 1,
    depth : -9.0 
  });
  
  P9 = new visual.TextStim({
    win : psychoJS.window,
    name : 'P9',
    text : None,
    font : 'Arial',
    pos : [0, 0], height : None,  wrapWidth : undefined, ori: 0,
    color : new util.Color(None),  opacity : 1,
    depth : -10.0 
  });
  
  P10 = new visual.TextStim({
    win : psychoJS.window,
    name : 'P10',
    text : None,
    font : 'Arial',
    pos : [0, 0], height : None,  wrapWidth : undefined, ori: 0,
    color : new util.Color(None),  opacity : 1,
    depth : -11.0 
  });
  
  P11 = new visual.TextStim({
    win : psychoJS.window,
    name : 'P11',
    text : None,
    font : 'Arial',
    pos : [0, 0], height : None,  wrapWidth : undefined, ori: 0,
    color : new util.Color(None),  opacity : 1,
    depth : -12.0 
  });
  
  P12 = new visual.TextStim({
    win : psychoJS.window,
    name : 'P12',
    text : None,
    font : 'Arial',
    pos : [0, 0], height : None,  wrapWidth : undefined, ori: 0,
    color : new util.Color(None),  opacity : 1,
    depth : -13.0 
  });
  
  P13 = new visual.TextStim({
    win : psychoJS.window,
    name : 'P13',
    text : None,
    font : 'Arial',
    pos : [0, 0], height : None,  wrapWidth : undefined, ori: 0,
    color : new util.Color(None),  opacity : 1,
    depth : -14.0 
  });
  
  P14 = new visual.TextStim({
    win : psychoJS.window,
    name : 'P14',
    text : None,
    font : 'Arial',
    pos : [0, 0], height : None,  wrapWidth : undefined, ori: 0,
    color : new util.Color(None),  opacity : 1,
    depth : -15.0 
  });
  
  P15 = new visual.TextStim({
    win : psychoJS.window,
    name : 'P15',
    text : None,
    font : 'Arial',
    pos : [0, 0], height : None,  wrapWidth : undefined, ori: 0,
    color : new util.Color(None),  opacity : 1,
    depth : -16.0 
  });
  
  ResponseWindow = new visual.TextStim({
    win : psychoJS.window,
    name : 'ResponseWindow',
    text : '?',
    font : 'Arial',
    pos : [0, 0], height : 20,  wrapWidth : undefined, ori: 0,
    color : new util.Color('white'),  opacity : 1,
    depth : -17.0 
  });
  
  LeftDistractor = new visual.ImageStim({
    win : psychoJS.window,
    name : 'LeftDistractor', 
    image : undefined, mask : undefined,
    ori : 0, pos : [(- 80), 0], size : [100, 150],
    color : new util.Color ([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -19.0 
  });
  RightDistractor = new visual.ImageStim({
    win : psychoJS.window,
    name : 'RightDistractor', 
    image : undefined, mask : undefined,
    ori : 0, pos : [80, 0], size : [100, 150],
    color : new util.Color ([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -20.0 
  });
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}

var trials;
function trialsLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  trials = new TrialHandler({
    psychoJS,
    nReps: 1, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'RSVPtrials_common.csv',
    seed: undefined, name: 'trials'});
  psychoJS.experiment.addLoop(trials); // add the loop to the experiment

  // Schedule all the trials in the trialList:
  for (const thisTrial of trials) {
    thisScheduler.add(importConditions(trials));
    thisScheduler.add(trialRoutineBegin);
    thisScheduler.add(trialRoutineEachFrame);
    thisScheduler.add(trialRoutineEnd);
    thisScheduler.add(endLoopIteration(thisTrial));
  }

  return Scheduler.Event.NEXT;
}


function trialsLoopEnd() {
  psychoJS.experiment.removeLoop(trials);

  return Scheduler.Event.NEXT;
}

var t;
var frameN;
var response;
var trialComponents;
function trialRoutineBegin() {
  //------Prepare to start Routine 'trial'-------
  t = 0;
  trialClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  
  response = new core.BuilderKeyResponse(psychoJS);
  LeftDistractor.setImage(D_L);
  RightDistractor.setImage(D_R);
  // keep track of which components have finished
  trialComponents = [];
  trialComponents.push(fixation);
  trialComponents.push(P1);
  trialComponents.push(P2);
  trialComponents.push(P3);
  trialComponents.push(P4);
  trialComponents.push(P5);
  trialComponents.push(P6);
  trialComponents.push(P7);
  trialComponents.push(P8);
  trialComponents.push(P9);
  trialComponents.push(P10);
  trialComponents.push(P11);
  trialComponents.push(P12);
  trialComponents.push(P13);
  trialComponents.push(P14);
  trialComponents.push(P15);
  trialComponents.push(ResponseWindow);
  trialComponents.push(response);
  trialComponents.push(LeftDistractor);
  trialComponents.push(RightDistractor);
  
  for (const thisComponent of trialComponents)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}

var continueRoutine;
function trialRoutineEachFrame() {
  //------Loop for each frame of Routine 'trial'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = trialClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  
  // *fixation* updates
  if (frameN >= 0.0 && fixation.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    fixation.tStart = t;  // (not accounting for frame time here)
    fixation.frameNStart = frameN;  // exact frame index
    fixation.setAutoDraw(true);
  }
  if (fixation.status === PsychoJS.Status.STARTED && frameN >= (fixation.frameNStart + 12)) {
    fixation.setAutoDraw(false);
  }
  
  // *P1* updates
  if (frameN >= startFrame1 && P1.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    P1.tStart = t;  // (not accounting for frame time here)
    P1.frameNStart = frameN;  // exact frame index
    P1.setAutoDraw(true);
  }
  if (P1.status === PsychoJS.Status.STARTED && frameN >= (P1.frameNStart + 3)) {
    P1.setAutoDraw(false);
  }
  
  // *P2* updates
  if (frameN >= startFrame2 && P2.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    P2.tStart = t;  // (not accounting for frame time here)
    P2.frameNStart = frameN;  // exact frame index
    P2.setAutoDraw(true);
  }
  if (P2.status === PsychoJS.Status.STARTED && frameN >= (P2.frameNStart + 3)) {
    P2.setAutoDraw(false);
  }
  
  // *P3* updates
  if (frameN >= startFrame3 && P3.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    P3.tStart = t;  // (not accounting for frame time here)
    P3.frameNStart = frameN;  // exact frame index
    P3.setAutoDraw(true);
  }
  if (P3.status === PsychoJS.Status.STARTED && frameN >= (P3.frameNStart + 3)) {
    P3.setAutoDraw(false);
  }
  
  // *P4* updates
  if (frameN >= startFrame4 && P4.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    P4.tStart = t;  // (not accounting for frame time here)
    P4.frameNStart = frameN;  // exact frame index
    P4.setAutoDraw(true);
  }
  if (P4.status === PsychoJS.Status.STARTED && frameN >= (P4.frameNStart + 3)) {
    P4.setAutoDraw(false);
  }
  
  // *P5* updates
  if (frameN >= startFrame5 && P5.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    P5.tStart = t;  // (not accounting for frame time here)
    P5.frameNStart = frameN;  // exact frame index
    P5.setAutoDraw(true);
  }
  if (P5.status === PsychoJS.Status.STARTED && frameN >= (P5.frameNStart + 3)) {
    P5.setAutoDraw(false);
  }
  
  // *P6* updates
  if (frameN >= startFrame6 && P6.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    P6.tStart = t;  // (not accounting for frame time here)
    P6.frameNStart = frameN;  // exact frame index
    P6.setAutoDraw(true);
  }
  if (P6.status === PsychoJS.Status.STARTED && frameN >= (P6.frameNStart + 3)) {
    P6.setAutoDraw(false);
  }
  
  // *P7* updates
  if (frameN >= startFrame7 && P7.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    P7.tStart = t;  // (not accounting for frame time here)
    P7.frameNStart = frameN;  // exact frame index
    P7.setAutoDraw(true);
  }
  if (P7.status === PsychoJS.Status.STARTED && frameN >= (P7.frameNStart + 3)) {
    P7.setAutoDraw(false);
  }
  
  // *P8* updates
  if (frameN >= startFrame8 && P8.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    P8.tStart = t;  // (not accounting for frame time here)
    P8.frameNStart = frameN;  // exact frame index
    P8.setAutoDraw(true);
  }
  if (P8.status === PsychoJS.Status.STARTED && frameN >= (P8.frameNStart + 3)) {
    P8.setAutoDraw(false);
  }
  
  // *P9* updates
  if (frameN >= startFrame9 && P9.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    P9.tStart = t;  // (not accounting for frame time here)
    P9.frameNStart = frameN;  // exact frame index
    P9.setAutoDraw(true);
  }
  if (P9.status === PsychoJS.Status.STARTED && frameN >= (P9.frameNStart + 3)) {
    P9.setAutoDraw(false);
  }
  
  // *P10* updates
  if (frameN >= startFrame10 && P10.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    P10.tStart = t;  // (not accounting for frame time here)
    P10.frameNStart = frameN;  // exact frame index
    P10.setAutoDraw(true);
  }
  if (P10.status === PsychoJS.Status.STARTED && frameN >= (P10.frameNStart + 3)) {
    P10.setAutoDraw(false);
  }
  
  // *P11* updates
  if (frameN >= startFrame11 && P11.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    P11.tStart = t;  // (not accounting for frame time here)
    P11.frameNStart = frameN;  // exact frame index
    P11.setAutoDraw(true);
  }
  if (P11.status === PsychoJS.Status.STARTED && frameN >= (P11.frameNStart + 3)) {
    P11.setAutoDraw(false);
  }
  
  // *P12* updates
  if (frameN >= startFrame12 && P12.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    P12.tStart = t;  // (not accounting for frame time here)
    P12.frameNStart = frameN;  // exact frame index
    P12.setAutoDraw(true);
  }
  if (P12.status === PsychoJS.Status.STARTED && frameN >= (P12.frameNStart + 3)) {
    P12.setAutoDraw(false);
  }
  
  // *P13* updates
  if (frameN >= startFrame13 && P13.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    P13.tStart = t;  // (not accounting for frame time here)
    P13.frameNStart = frameN;  // exact frame index
    P13.setAutoDraw(true);
  }
  if (P13.status === PsychoJS.Status.STARTED && frameN >= (P13.frameNStart + 3)) {
    P13.setAutoDraw(false);
  }
  
  // *P14* updates
  if (frameN >= startFrame14 && P14.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    P14.tStart = t;  // (not accounting for frame time here)
    P14.frameNStart = frameN;  // exact frame index
    P14.setAutoDraw(true);
  }
  if (P14.status === PsychoJS.Status.STARTED && frameN >= (P14.frameNStart + 3)) {
    P14.setAutoDraw(false);
  }
  
  // *P15* updates
  if (frameN >= startFrame15 && P15.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    P15.tStart = t;  // (not accounting for frame time here)
    P15.frameNStart = frameN;  // exact frame index
    P15.setAutoDraw(true);
  }
  if (P15.status === PsychoJS.Status.STARTED && frameN >= (P15.frameNStart + 3)) {
    P15.setAutoDraw(false);
  }
  
  // *ResponseWindow* updates
  if (frameN >= RW && ResponseWindow.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    ResponseWindow.tStart = t;  // (not accounting for frame time here)
    ResponseWindow.frameNStart = frameN;  // exact frame index
    ResponseWindow.setAutoDraw(true);
  }
  
  // *response* updates
  if (frameN >= RW && response.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    response.tStart = t;  // (not accounting for frame time here)
    response.frameNStart = frameN;  // exact frame index
    response.status = PsychoJS.Status.STARTED;
    // keyboard checking is just starting
    psychoJS.window.callOnFlip(response.clock.reset) // t = 0 on screen flip
  }
  if (response.status === PsychoJS.Status.STARTED) {
    let theseKeys = psychoJS.eventManager.getKeys({keyList:['z', 'x', 'n', 'm']});
    
    // check for quit:
    if ("escape" in theseKeys) {
        psychoJS.experiment.experimentEnded = true;
    }
    if (theseKeys.length > 0) {  // at least one key was pressed
      response.keys = theseKeys[theseKeys.length-1]  // just the last key pressed
      response.rt = response.clock.getTime();
      // was this 'correct'?
      if (response.keys == correctresp) {
          response.corr = 1;
      } else {
          response.corr = 0;
      }
      // a response ends the routine
      continueRoutine = false;
    }
  }
  
  // *LeftDistractor* updates
  if (frameN >= LagFrame && LeftDistractor.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    LeftDistractor.tStart = t;  // (not accounting for frame time here)
    LeftDistractor.frameNStart = frameN;  // exact frame index
    LeftDistractor.setAutoDraw(true);
  }
  if (LeftDistractor.status === PsychoJS.Status.STARTED && frameN >= (LeftDistractor.frameNStart + 3)) {
    LeftDistractor.setAutoDraw(false);
  }
  
  // *RightDistractor* updates
  if (frameN >= LagFrame && RightDistractor.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    RightDistractor.tStart = t;  // (not accounting for frame time here)
    RightDistractor.frameNStart = frameN;  // exact frame index
    RightDistractor.setAutoDraw(true);
  }
  if (RightDistractor.status === PsychoJS.Status.STARTED && frameN >= (RightDistractor.frameNStart + 3)) {
    RightDistractor.setAutoDraw(false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  continueRoutine = false;// reverts to True if at least one component still running
  for (const thisComponent of trialComponents)
    if ('status' in thisComponent && thisComponent.status != PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  // check for quit (the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    psychoJS.quit('The [Escape] key was pressed. Goodbye!');
  }
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function trialRoutineEnd() {
  //------Ending Routine 'trial'-------
  for (const thisComponent of trialComponents) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  
  // check responses
  if (['', [], undefined].indexOf(response.keys) >= 0) {    // No response was made
      response.keys = undefined;
  }
  // was no response the correct answer?!
  if (response.keys == undefined) {
    if (psychoJS.str(correctresp).toLowerCase() == 'none') {
       response.corr = 1  // correct non-response
    } else {
       response.corr = 0  // failed to respond (incorrectly)
    }
  }
  // store data for thisExp (ExperimentHandler)
  psychoJS.experiment.addData('response.keys', response.keys);
  psychoJS.experiment.addData('response.corr', response.corr);
  if (response.keys != undefined) {  // we had a response
      psychoJS.experiment.addData('response.rt', response.rt);
      routineTimer.reset();
      }
  // the Routine "trial" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}


function endLoopIteration(thisTrial) {
  // ------Prepare for next entry------
  return function () {
    if (typeof thisTrial === 'undefined' || !('isTrials' in thisTrial) || thisTrial.isTrials) {
      psychoJS.experiment.nextEntry();
    }
  return Scheduler.Event.NEXT;
  };
}


function importConditions(loop) {
  const trialIndex = loop.getTrialIndex();
  return function () {
    loop.setTrialIndex(trialIndex);
    psychoJS.importAttributes(loop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


function quitPsychoJS(isCompleted) {
  psychoJS.window.close();
  psychoJS.quit({isCompleted});

  return Scheduler.Event.QUIT;
}
