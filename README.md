# Pomodoro Timer

The [Pomodoro Technique](https://cirillocompany.de/pages/pomodoro-technique) is a simple time-management technique developed by Francesco Cirillo in the 1980s. The core of the technique, as described on the website, is as follows:

* Decide on a task to complete
* Set a timer for 25 minutes and focus on the task during that time
* When the timer is done, take a break for 5 minutes
* After 4 pomodoros, take a longer break of 15 to 30 minutes

This app implements a version of the Pomodoro Technique customized for logging one's activities throughout the day.

When the app first starts, the user is presented with a blank task and a timer set for 25 minutes. The user can set a task, or pomo, and start the timer by clicking "GO!". If no pomos have been completed yet, the app will ask when the user arrived at work and what they've been doing since then. It will then count down for 25 minutes and notify the user by maximizing the window when finished. The pomo is then added to a running list displayed to the user. At the start of each pomo after the first one and on closing the app, a dialog asks the user to describe what they've been doing since the last pomo. The app also allows users to prematurely end a pomo, as distractions and interruptions are a common office event.

On closing the app, a *.csv file, log.csv, is created in the app directory and all activities are recorded. For each activity, the app records the date, start/end times, description, and type. Types can be "initial," "pomodoro," "break," or "final."
