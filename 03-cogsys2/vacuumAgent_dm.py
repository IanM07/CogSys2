##------
# Code last modified by Chris Dancy @ Penn State (2023-Sept)
#  from codebase written by Terry Stewart @ University of Waterloo
# Builds environment grid-like environment and creates a vacuum agent to clean up "mud"
##------


from AgentSupport import MotorModule, CleanSensorModule, MyCell
import AgentSupport
import python_actr
from python_actr.lib import grid
from python_actr.actr import *
from python_actr.actr.hdm import *
import random
import time

class VacuumAgent(python_actr.ACTR):
	goal = python_actr.Buffer()
	body = grid.Body()
	motorInst = MotorModule()
	cleanSensor = CleanSensorModule()
	retrieval = Buffer()
	#Finst number and time should be plenty for us to keep things simple (even if theoretically impractical!)
	DM_module = Memory(retrieval,finst_size=5,finst_time=10.0)

	def init():
		goal.set("start_recall_dirt")
		self.home = None
		#Inside of the memory, sets the locations of the dirty blocks to be cleaned
		DM_module.add("square:dirty location_x:4 location_y:4")
		DM_module.add("square:dirty location_x:2 location_y:4")
	#----ROOMBA----#

	def recall_dirty_spots_dm(goal="start_recall_dirt", DM_module="busy:False error:False"):
		goal.set("clean left")
		pass

	#----ROOMBA----#

	def clean_cell(cleanSensor="dirty:True", utility=0.6):
		motorInst.clean()

	def clean_left_square(goal="clean left", retrieval="square:dirty location_x:4 location_y:4"):
		#Intended to make the agent move to the dirty left block
		motorInst.go_towards(4,4)
		goal.set("clean right")
		DM_module.request("square:dirty location_x:2 location_y:4")

	def clean_right_square(goal="clean right", retrieval="square:dirty location_x:2 location_y:4"):
		#Intended to make the agent move to the dirty right block
		motorInst.go_towards(2,4)
		motorInst.go_towards(2,4)

	def forward_rsearch(goal="rsearch left ?dist ?num_turns ?curr_dist",				
		motorInst="busy:False", body="ahead_cell.wall:False"):
		motorInst.go_forward()
		print(body.ahead_cell.wall)
		curr_dist = str(int(curr_dist) - 1)
		goal.set("rsearch left ?dist ?num_turns ?curr_dist")

	def left_rsearch(goal="rsearch left ?dist ?num_turns 0", motorInst="busy:False",
					utility=0.1):
		motorInst.turn_left(2)
		num_turns = str(int(num_turns) + 1)
		goal.set("rsearch left ?dist ?num_turns ?dist")

		#Methods to handle agent's turning behavior. The agent spirals inwards, starting from the green square.
        #These methods help the agent decide when to turn based on its current position and how many turns it has made.
        #Each method corresponds to a specific turning point in the agent's path.
        
        #Below are the turn methods for the agent. Each method represents a specific turning point based on the current distance traveled and number of turns made.
        #After making a turn, the distances are reset and the number of turns is incremented.
        #This ensures the agent follows a spiral path.
	def turn0_rsearch(goal="rsearch left 7 0 7", motorInst="busy:False", utility=0.1):
		motorInst.turn_left(2)
		curr_dist = 0
		goal.set("rsearch left 0 1 0")
		
	def turn1_rsearch(goal="rsearch left 6 1 6", motorInst="busy:False", utility=0.1):
		motorInst.turn_left(2)
		curr_dist = 0
		goal.set("rsearch left 0 2 0")

	def turn2_rsearch(goal="rsearch left 7 2 7", motorInst="busy:False", utility=0.1):
		motorInst.turn_left(2)
		curr_dist = 0
		goal.set("rsearch left 0 3 0")
                                  
	def turn3_rsearch(goal="rsearch left 5 3 5", motorInst="busy:False", utility=0.1):
		motorInst.turn_left(2)
		curr_dist = 0
		goal.set("rsearch left 0 4 0")

	def turn4_rsearch(goal="rsearch left 6 4 6", motorInst="busy:False", utility=0.1):
		motorInst.turn_left(2)
		curr_dist = 0
		goal.set("rsearch left 0 5 0")

	def turn5_rsearch(goal="rsearch left 4 5 4", motorInst="busy:False", utility=0.1):
		motorInst.turn_left(2)
		curr_dist = 0
		goal.set("rsearch left 0 6 0")

	def turn6_rsearch(goal="rsearch left 5 6 5", motorInst="busy:False", utility=0.1):
		motorInst.turn_left(2)
		curr_dist = 0
		goal.set("rsearch left 0 7 0")
		
	def turn7_rsearch(goal="rsearch left 3 7 3", motorInst="busy:False", utility=0.1):
		motorInst.turn_left(2)
		curr_dist = 0
		goal.set("rsearch left 0 8 0")

	def turn8_rsearch(goal="rsearch left 4 8 4", motorInst="busy:False", utility=0.1):
		motorInst.turn_left(2)
		curr_dist = 0
		goal.set("rsearch left 0 9 0")

	def turn9_rsearch(goal="rsearch left 2 9 2", motorInst="busy:False", utility=0.1):
		motorInst.turn_left(2)
		curr_dist = 0
		goal.set("rsearch left 0 10 0")

	def turn10_rsearch(goal="rsearch left 3 10 3", motorInst="busy:False", utility=0.1):
		motorInst.turn_left(2)
		curr_dist = 0
		goal.set("rsearch left 0 11 0")

	def turn11_rsearch(goal="rsearch left 1 11 1", motorInst="busy:False", utility=0.1):
		motorInst.turn_left(2)
		curr_dist = 0
		goal.set("rsearch left 0 12 0")


rand_inst = random.Random()
rand_inst.seed(1)

world=grid.World(MyCell,map=AgentSupport.mymap)
agent=VacuumAgent()
agent.home=()
world.add(agent,5,5,dir=0,color="black")

python_actr.log_everything(agent, AgentSupport.my_log)
window = python_actr.display(world)
world.run()
time.sleep(1)
world.reset_map(MyCell,map=AgentSupport.mymap)
world.add(agent,5,5,dir=0,color="black")
world.run()
