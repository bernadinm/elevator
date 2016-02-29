# Miguel Bernadin
# Mesosphere Challenge

import uuid
import Queue
import time

class Elevator(object):
	def __init__(self):
		self.currentFloor = 0
		self.id = uuid.uuid4()
		self.upwardDestinationFloors = Queue.PriorityQueue()
		self.downwardDestinationFloors = Queue.PriorityQueue()
		self.direction = 0 # -1 = Downward, 0 = no direction, 1 = upward direction
		self.express = False # Used to enable or disable direct stops

class Floor(object):
	def __init__(self, floorNumber):
		self.upward = False
		self.downward = False
		self.level = floorNumber
		self.riders = list()
		self.ridersGoingUp = list()
		self.ridersGoingDown = list()
	def setUp(self):
		if self.upward == True:
			print "Elevator is already called to go up on floor %d" % self.level
		else:
			self.upward = True
	def setDown(self):
		if self.downward == True:
			print "Elevator is already called to go up on floor %d" % self.level
		else:
			self.downward = True
	def getUpStatus(self):
		return self.upward
	def getDownStatus(self):
		return self.downward
	def clearDown(self):
		self.upward = False
	def clearUp(self):
		self.downward = False
	def getRiders(self):
		return self.riders
	def addPerson(self, person):
		self.riders.add(person)
		if person.destinationFloor > self.level:
			self.ridersGoingUp.add(person)
			setUp()
		elif person.destinationFloor < self.level:
			self.ridersGoingDown.add(person)
			setDown()
	def removePerson(self, direction):
		for person in self.riders:
			if person.destinationFloor > person.currentFloor and direction == 1:
				self.riders.remove(person)
				clearUp()
			elif person.destinationFloor < person.currentFloor and direction == -1:
				self.riders.remove(person)
				clearDown()
	def getRidersGoingUp(self, elevator):
		ridersEnteringElevators = self.ridersGoingUp
		self.ridersGoingUp = []
		self.clearUp()
		for person in ridersEnteringElevators:
			elevator.upwardDestinationFloors.put(person.destinationFloor)
			elevator.direction = 1
	def getRidersGoingDown(self, elevator):
		ridersEnteringElevators = self.ridersGoingDown
		self.ridersGoingDown = []
		self.clearDown()
		for person in ridersEnteringElevators:
			elevator.downwardDestinationFloors.put((-person.destinationFloor, person.destinationFloor))
			elevator.direction = -1		


class Person(object):
	def __init__(self, floor, destinationFloor):
		self.destinationFloor = destinationFloor
		self.currentFloor = floor
	def direction(self):
		if self.destinationFloor > self.currentFloor: 
			return 1 
		elif self.destinationFloor < self.currentFloor:
			return -1
		else:
		 	return 0



class ElevatorControlSystem(object):
	def __init__(self, total_elevators, total_floors, floorsNameSpace):
		self.requestOnFloor = set()
		self.managedElevators = [Elevator() for x in range(total_elevators)]
		self.numberOfElevators = total_elevators
		self.maxfloors = total_floors
		self.floors = floorsNameSpace
	def update(self, elevator):
		""" Update status of the elevator. i.e, passenger sets destination to a floor
		"""
		# TODO Fix the elevator direction 0 issue which takes all riders.
		#Check if the elevator is going the same direction

		if elevator.direction == 1 and self.floors[elevator.currentFloor].ridersGoingUp: self.floors[elevator.currentFloor].getRidersGoingUp(elevator)
		if elevator.direction == -1 and self.floors[elevator.currentFloor].ridersGoingDown: self.floors[elevator.currentFloor].getRidersGoingDown(elevator)
		if elevator.direction == 0 and self.floors[elevator.currentFloor].ridersGoingUp:
			self.floors[elevator.currentFloor].getRidersGoingUp(elevator)
		if elevator.direction == 0 and self.floors[elevator.currentFloor].ridersGoingDown:
			self.floors[elevator.currentFloor].getRidersGoingDown(elevator)		
	def step(self):
		""" Loop through all elevators to evaluate their step
		"""
		for selectedElevator in self.managedElevators:
			if selectedElevator.upwardDestinationFloors.empty() and selectedElevator.downwardDestinationFloors.empty(): # If no request, set direction to 0
				selectedElevator.direction = 0 #
				print "Elevator id:%s is remaining idle on floor %d" % (selectedElevator.id, selectedElevator.currentFloor) 
				self.update(selectedElevator)
			else: # If we do have a request head to that direction
				if (selectedElevator.direction == 1 and not selectedElevator.upwardDestinationFloors.empty()) or (selectedElevator.direction == -1 and selectedElevator.downwardDestinationFloors.empty() and not selectedElevator.upwardDestinationFloors.empty()):
					selectedElevator.direction == 1 # Ensure correct direction 					
					stopToRemember = selectedElevator.upwardDestinationFloors.get()
					if selectedElevator.currentFloor < stopToRemember:
						selectedElevator.currentFloor = selectedElevator.currentFloor + 1
						print "Elevator id:%s moving past floor %d to floor %d" % (selectedElevator.id, selectedElevator.currentFloor-1,  selectedElevator.currentFloor) 
						selectedElevator.upwardDestinationFloors.put(stopToRemember)
					if selectedElevator.currentFloor == stopToRemember:
						print "Elevator id:%s says door is now open on floor %d" % (selectedElevator.id, selectedElevator.currentFloor)
						if selectedElevator.express == True: selectedElevator.express = False
						###Call update elevators with new passenger function 
						self.update(selectedElevator)	
				elif (selectedElevator.direction == -1 and not selectedElevator.downwardDestinationFloors.empty()) or (selectedElevator.direction == 1 and selectedElevator.upwardDestinationFloors.empty() and not selectedElevator.downwardDestinationFloors.empty()):
					selectedElevator.direction == -1 # Ensure correct direction  
					stopToRemember = selectedElevator.downwardDestinationFloors.get()[1]
					if selectedElevator.currentFloor > stopToRemember:
						selectedElevator.currentFloor = selectedElevator.currentFloor - 1
						print "Elevator id:%s moving past floor %d to floor %d" % (selectedElevator.id, selectedElevator.currentFloor+1,  selectedElevator.currentFloor) 
						selectedElevator.downwardDestinationFloors.put((-stopToRemember,stopToRemember))
					if selectedElevator.currentFloor == stopToRemember:
						print "Elevator id:%s says door is now open on floor %d" % (selectedElevator.id, selectedElevator.currentFloor)
						if selectedElevator.express == True: selectedElevator.express = False 
						###Call update elevators with new passenger function 
						self.update(selectedElevator)
	def status(self):
		""" Print The status of all the elevators
		"""
		print [( selectedElevator.id, selectedElevator.currentFloor, selectedElevator.upwardDestinationFloors) for selectedElevator in self.managedElevators]
	def pickup(self, floorNumber, direction):
		""" Passenger request an elevator
		""" 
		for selectedElevator in self.managedElevators:	
			""" Find closest unused elevator or default to the  first elevator """ 
			closestElevator = self.managedElevators[0]
			for selectedElevator in self.managedElevators:	
				if selectedElevator.direction == 0:
					if selectedElevator == self.managedElevators[0]:
					 	closestElevator = selectedElevator
					elif abs(selectedElevator.currentFloor - floorNumber) < abs(closestElevator.currentFloor - floorNumber):
					 	closestElevator = selectedElevator
			if closestElevator.currentFloor > floorNumber:
				closestElevator.direction = -1
				closestElevator.downwardDestinationFloors.put((-floorNumber,floorNumber))
				closestElevator.express = True
				print "ECS sent elevator id:%s to floor %d" % (closestElevator.id, floorNumber)
			elif closestElevator.currentFloor < floorNumber:
				closestElevator.direction = 1
				closestElevator.upwardDestinationFloors.put(floorNumber)
				closestElevator.express = True
				print "ECS sent elevator id:%s to floor %d" % (closestElevator.id, floorNumber)
			else:
				closestElevator.direction = 0
				closestElevator.express = False
				print "ECS opened elevator id:%s door for a person on floor %d" % (closestElevator.id, floorNumber)
				return


class Building(object):
	def __init__(self, TOTAL_FLOORS, TOTAL_ELEVATORS):
		self.floors = [Floor(i) for i in range(TOTAL_FLOORS)]
		self.ecs = ElevatorControlSystem(TOTAL_ELEVATORS, TOTAL_FLOORS, self.floors)
	def addPersonToFloor(self, person):
		self.floors[person.currentFloor].riders.append(person)
		if person.direction() == 1: 
			self.floors[person.currentFloor].ridersGoingUp.append(person)
			self.floors[person.currentFloor].setUp()
			self.ecs.pickup(person.currentFloor, person.direction())
		if person.direction() == -1: 
			self.floors[person.currentFloor].ridersGoingDown.append(person)
			self.floors[person.currentFloor].setDown()
			self.ecs.pickup(person.currentFloor, person.direction())

	def run(self):
		while True:
		    self.ecs.step()
		    time.sleep(1)  # Delay for 1 second


def main():
	TOTAL_ELEVATORS = 3
	TOTAL_FLOORS = 8

	building = Building(TOTAL_FLOORS, TOTAL_ELEVATORS)

	Mary = Person(0, 3)
	Jack = Person(4, 0)
	Susy = Person(3, 1)
	John = Person(1, 3)
	Joe = Person(4, 3)
	Mike = Person(2, 1)
	Frank = Person(7,3)

	building.addPersonToFloor(Mary)
	building.addPersonToFloor(Jack)
	building.addPersonToFloor(Susy)  
	building.addPersonToFloor(John)
	building.addPersonToFloor(Joe)
	building.addPersonToFloor(Mike)
	building.addPersonToFloor(Frank)

	building.run()

if __name__ == '__main__':
	main()

# ecs.managedElevators[1].upwardDestinationFloors.add(8)
# ecs = elevatorControlSystem(3)

#Rules are:
#Elevators may stop at any floor as long as the floor is in the direction of travel
#Elevators may change direction as long as there is no passenger.
