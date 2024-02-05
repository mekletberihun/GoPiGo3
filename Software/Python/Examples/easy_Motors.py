# import the time library for the sleep function
import time
# import the GoPiGo3 drivers
from easygopigo3 import EasyGoPiGo3

# Create an instance of the GoPiGo3 class.
# GPG will be the GoPiGo3 object.
gpg = EasyGoPiGo3()

#Chapter 3.1

print("Move the motors forward freely for 1 second.")
gpg.forward() #This moves the robot forward
time.sleep(1) #The motors will stop for 1 second
gpg.stop()

#time.sleep just adds delay to program

print("Stop the motors for 1 second.")
time.sleep(1) #Stops the motors for 1 second

print("Drive the motors 50 cm and then stop.")
gpg.drive_cm(50, True) #Drives for 50 cm so parameters are cm, boolean ?
time.sleep(1)

print("Turn right 1 second.")
gpg.right() #Makes wheels turn right for 1 second
time.sleep(1)

print("Turn left 1 second.")
gpg.left() #Makes wheels turn left for 1 second
time.sleep(1)

print("Stop!")
gpg.stop()
print("Done!")


#Chapter 3.1
length = 30


#Making a Square
for i in range(4):
  gpg.drive_cm(length) # drive forward for length cm
  gpg.turn_degrees(90) # rotate 90 degrees to the right


#Draw half circles
gpg.orbit(180, 50) # draw half a circle
gpg.turn_degrees(180) # rotate the GoPiGo3 around
gpg.orbit(-180, 50) # return on the initial path
gpg.turn_degrees(180) # and put it in the initial position


#Draw an infinity shape
gpg.orbit(-270, radius) # to rotate to the left
gpg.drive_cm(radius * 2) # move forward
gpg.orbit(270, radius) # to rotate to the right
gpg.drive_cm(radius * 2) # move forward


#Goes forward while increasing speed (acceleration)
# setting speed to lowest value and
# calculating the step increase in speed
current_speed = 50
end_speed = 400
step = (end_speed - current_speed) / 20
gpg.set_speed(current_speed)

# start moving the robot at an ever increasing speed
gpg.forward()
while current_speed <= end_speed:
  sleep(0.1)
  gpg.set_speed(current_speed)
  current_speed += step

# and then stop it
gpg.stop()
