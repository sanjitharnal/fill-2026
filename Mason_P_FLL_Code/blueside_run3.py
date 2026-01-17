from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port,Direction
from pybricks.robotics import DriveBase
from pybricks.tools import multitask, run_task


hub = PrimeHub()
leftWheel   = Motor(Port.A, Direction.COUNTERCLOCKWISE)
rightWheel  = Motor(Port.C, Direction.CLOCKWISE)
wheelsize   = 62.4
axletrackwidth = 110
#robot and robot initial settings
robot = DriveBase(leftWheel,rightWheel,wheelsize,axletrackwidth)
robot.settings(straight_speed=600,straight_acceleration=200,turn_rate=400,turn_acceleration=200 )

#left attachment motor
LAM = Motor(Port.E, Direction.COUNTERCLOCKWISE)
#right attachment motor
RAM = Motor(Port.B,Direction.COUNTERCLOCKWISE)

#Turn on Gyro Sensor if the hub is good, turn off if it is bad
robot.use_gyro(True)
hub.imu.reset_heading(0)

async def main():
   if hub.imu.ready():
        # Mission 8 (Silo)
        await robot.straight(400)
        ## Slam hammer around 5 times
        for x in range(5):
            await RAM.run_angle(-1000,80)
            await RAM.run_angle(1000,80)
        await robot.straight(-1300)
        
run_task(main())
