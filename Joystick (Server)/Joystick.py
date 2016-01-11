import pygame
import ZMQCommunication
import LowPassFilter

Pub=ZMQCommunication.Publisher()
LPF=LowPassFilter.LowPassFilter()

pygame.init()
pygame.joystick.init()
# Used to manage how fast the screen updates
clock = pygame.time.Clock() 

class Joystick():
	def __init__(self, done=0):
		self.done=False

	def mainRoutine(self):

		# -------- Main Program Loop -----------
		while self.done==False:
    		# EVENT PROCESSING STEP
    			for event in pygame.event.get(): # User did something
        			if event.type == pygame.QUIT: # If user clicked close
            				self.done=True # Flag that we are done so we exit this loop

    			for i in range(1):
        			joystick = pygame.joystick.Joystick(0)
        			joystick.init()
    
        			# Get the name from the OS for the controller/joystick
        			name = joystick.get_name()

        			axis1 = joystick.get_axis( 1 )
        			axis2 = joystick.get_axis( 2 )

        			directionForwardReverse=float(axis1)
        			directionLeftTRight=float(axis2)

        			FilteredValuesFR=LPF.lowPassFilterFR(-directionForwardReverse)
        			FilteredValuesLR=LPF.lowPassFilterLR(-directionLeftTRight)
    			
        			Publisher=Pub.publisher('joystick', FilteredValuesFR, FilteredValuesLR)
		    		
				# Limit to 20 frames per second
        			clock.tick(20)
		pygame.quit ()

		
	def main(self):
		Joystick.mainRoutine()

if __name__ == '__main__':
    Joystick = Joystick()
    Joystick.main()