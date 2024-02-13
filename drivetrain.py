import wpilib
import wpilib.drive as wpiDrive
import wpimath.kinematics as Kinematics

import ctre

import commands2 as Commands


class Drivetrain(Commands.SubsystemBase):
    def __init__(self, l_ports, r_ports, invert_right=False, invert_left=False) -> None:
        super().__init__()

        self.l_front_motor = ctre.WPI_VictorSPX(l_ports[0])
        self.l_back_motor = ctre.WPI_VictorSPX(l_ports[1])
        self.l_motor_group = wpilib.MotorControllerGroup(self.l_front_motor, self.l_back_motor)
        self.l_motor_group.setInverted(invert_left)

        self.r_front_motor = ctre.WPI_VictorSPX(r_ports[0])
        self.r_back_motor = ctre.WPI_VictorSPX(r_ports[1])
        self.r_motor_group = wpilib.MotorControllerGroup(self.r_front_motor, self.r_back_motor)
        self.r_motor_group.setInverted(invert_right)

        self.drive = wpiDrive.DifferentialDrive(self.l_motor_group, self.r_front_motor)

        #NOTE: not a clue what those arguments are
        '''self.left_encoder = wpilib.Encoder(0,1)
        self.right_encoder = wpilib.Encoder(2,3)'''

        #TODO: find actual track width
        self.kinematics = Kinematics.DifferentialDriveKinematics(20)
        '''self.odemetry = Kinematics.DifferentialDriveOdometry(
            self.gyro.getRotation2d(),
            self.left_encoder.getDistance(),
            self.right_encoder.getDistance()
        )'''

    def tank_drive(self, left_speed, right_speed):
        self.drive.tankDrive(left_speed, right_speed)
    def arcade_drive(self, x_speed, z_rot):
        self.drive.arcadeDrive(x_speed, z_rot)
    
    def periodic(self):
        '''self.odemetry.update(
            self.gyro.getRotation2d(), 
            self.left_encoder.getDistance(), 
            self.right_encoder.getDistance()
        )'''
    def sumulationPeriodic(self): pass
