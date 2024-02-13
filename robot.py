'''
from wpimath.estimator import *
from wpimath.filter import *
from wpimath.geometry import *
from wpimath.interpolation import *
from wpimath.spline import *
from wpimath.trajectory import *
from wpimath.units import *
from wpinet import *
from wpiutil import *

from cscore import *
from hal import *
from ntcore import *
from pyfrc import *
from robotpy_apriltag import *

from commands2.button import *
from commands2.cmd import *

from rev import *'''

import wpilib

from drivetrain import Drivetrain

class Robot(wpilib.TimedRobot):
    def robotInit(self): 
        #controller setup -- NOTE: change to x input when not on mac
        self.stick = wpilib.PS4Controller(0)

        #Tank Drive
        self.drive = Drivetrain((3,4), (1,2))

        #TODO: is correct channel?
        '''self.gyro = wpilib.AnalogGyro(0) 
        self.gyro.reset()'''

        #put Sendables on dashboard
        wpilib.SmartDashboard.putData('Drivetrain', self.drive)
        
    def robotPeriodic(self):pass

    def autonomousInit(self): pass
    def autonomousPeriodic(self): pass
    def autonomousExit(self): pass

    def teleopInit(self): pass
    def teleopPeriodic(self):
        #drive
        #self.drive.tank_drive(self.stick.getLeftY()*-1, self.stick.getRightY())
        self.drive.arcade_drive(self.stick.getLeftY(), self.stick.getLeftX())

        #Display Info
        wpilib.SmartDashboard.putNumber('left motor speed', self.drive.l_motor_group.get())
        wpilib.SmartDashboard.putNumber('right motor speed', self.drive.r_motor_group.get())

        #wpilib.SmartDashboard.putNumber('left encoder dist', self.drive.left_encoder.getDistance())        
        
    def teleopExit(self): pass

    def _simulationInit(self): pass
    def _simulationPeriodic(self): pass

    def disabledInit(self): pass
    def disabledPeriodic(self): pass
    def disabledExit(self): pass

if __name__ == '__main__':
    wpilib.run(Robot)