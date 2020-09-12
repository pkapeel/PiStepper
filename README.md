# PiStepper
Python script allowing the control of a stepper motor drive with a Raspberry Pi.
The intention of this program is to allow remote control of the focuser of a Dobsonian telescope.

Tested on Raspberry Pi 4  Model B.
Stepper motor is a NEMA 17 bipolar motor made by STEPPERONLINE.
Stepper motor is driven by a DM542T unit made by STEPPERONLINE.
The Pi output pins control the motor driver.
The Pi has two (2) input pins controlled by a momentary DPDT toggle switch.
This toggle switch controls the direction of the motor (clockwise or counterclockwise).
The center position of the toggle switch causes the motor to idle with no holding torque (coils de-energized).
