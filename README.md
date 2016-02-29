# elevator
Mesosphere's Elevator Control System Challange


##Challenge Question
Design and implement an elevator control system. What data structures, interfaces and algorithms will you need? Your elevator control system should be able to handle a few elevators — up to 16.

You can use the language of your choice to implement an elevator control system. In the end, your control system should provide an interface for:

  * Querying the state of the elevators (what floor are they on and where they
    are going),

  * receiving an update about the status of an elevator,

  * receiving a pickup request,

  * time-stepping the simulation.

## Solution

This current program allows a user to specify the number of elevators, floors and how many people are going to which floors. The challenge only listed a FCFS solution which would be a elevator you wouldn't want to ride. Our algorithm bypasses this limitation and implements a priority queue for each elevator. This allows a user to share an elevator with another person and skip floors that are not going the same direction. This solution is modeled by a realistic elevator system. It will also pick up people going the same direction without the need to call another elevator. This saves on resources allowing users to share the same elevator. 

## Requirements

 * Python 2.7
 
### Quick Start

1. Clone this repository  

    ```bash
    git clone http://github.com/bernadinm/elevator 
    ```

2.  Modify elevator.py's main function to add/remove the number of elevators, floors and people
    *( Or keep defaults, 3 elevator, 8 floors, 7 request )*

3. Begin elevator simulation

   ```bash
   python elevator.py 
   ```

### Example output

```
MacBook-Pro:elevator mingo$ python elevator.py
ECS opened elevator id:eb0ef2a8-b672-435a-b4d3-ef86a86e1c68 door for a person on floor 0
ECS sent elevator id:eb0ef2a8-b672-435a-b4d3-ef86a86e1c68 to floor 4
ECS sent elevator id:eb0ef2a8-b672-435a-b4d3-ef86a86e1c68 to floor 3
ECS sent elevator id:eb0ef2a8-b672-435a-b4d3-ef86a86e1c68 to floor 1
Elevator is already called to go up on floor 4
ECS sent elevator id:eb0ef2a8-b672-435a-b4d3-ef86a86e1c68 to floor 4
ECS sent elevator id:eb0ef2a8-b672-435a-b4d3-ef86a86e1c68 to floor 2
ECS sent elevator id:eb0ef2a8-b672-435a-b4d3-ef86a86e1c68 to floor 7
Elevator id:eb0ef2a8-b672-435a-b4d3-ef86a86e1c68 moving past floor 0 to floor 1
Elevator id:eb0ef2a8-b672-435a-b4d3-ef86a86e1c68 says door is now open on floor 1
Elevator id:eb0ef2a8-b672-435a-b4d3-ef86a86e1c68 says door is now open on floor 1
Elevator id:eb0ef2a8-b672-435a-b4d3-ef86a86e1c68 moving past floor 1 to floor 2
Elevator id:eb0ef2a8-b672-435a-b4d3-ef86a86e1c68 says door is now open on floor 2
Elevator id:eb0ef2a8-b672-435a-b4d3-ef86a86e1c68 says door is now open on floor 2
Elevator id:eb0ef2a8-b672-435a-b4d3-ef86a86e1c68 moving past floor 2 to floor 3
Elevator id:eb0ef2a8-b672-435a-b4d3-ef86a86e1c68 says door is now open on floor 3
Elevator id:eb0ef2a8-b672-435a-b4d3-ef86a86e1c68 says door is now open on floor 3
Elevator id:eb0ef2a8-b672-435a-b4d3-ef86a86e1c68 says door is now open on floor 3
Elevator id:eb0ef2a8-b672-435a-b4d3-ef86a86e1c68 moving past floor 3 to floor 4
Elevator id:eb0ef2a8-b672-435a-b4d3-ef86a86e1c68 says door is now open on floor 4
Elevator id:eb0ef2a8-b672-435a-b4d3-ef86a86e1c68 says door is now open on floor 4
Elevator id:eb0ef2a8-b672-435a-b4d3-ef86a86e1c68 says door is now open on floor 4
Elevator id:eb0ef2a8-b672-435a-b4d3-ef86a86e1c68 moving past floor 4 to floor 5
Elevator id:eb0ef2a8-b672-435a-b4d3-ef86a86e1c68 moving past floor 5 to floor 6
Elevator id:eb0ef2a8-b672-435a-b4d3-ef86a86e1c68 moving past floor 6 to floor 7
Elevator id:eb0ef2a8-b672-435a-b4d3-ef86a86e1c68 says door is now open on floor 7
Elevator id:eb0ef2a8-b672-435a-b4d3-ef86a86e1c68 says door is now open on floor 7
Elevator id: eb0ef2a8-b672-435a-b4d3-ef86a86e1c68 is remaining idle on floor 7
Elevator id:eb0ef2a8-b672-435a-b4d3-ef86a86e1c68 moving past floor 7 to floor 6
Elevator id:eb0ef2a8-b672-435a-b4d3-ef86a86e1c68 moving past floor 6 to floor 5
Elevator id:eb0ef2a8-b672-435a-b4d3-ef86a86e1c68 moving past floor 5 to floor 4
Elevator id:eb0ef2a8-b672-435a-b4d3-ef86a86e1c68 moving past floor 4 to floor 3
Elevator id:eb0ef2a8-b672-435a-b4d3-ef86a86e1c68 says door is now open on floor 3
Elevator id:eb0ef2a8-b672-435a-b4d3-ef86a86e1c68 says door is now open on floor 3
Elevator id:eb0ef2a8-b672-435a-b4d3-ef86a86e1c68 moving past floor 3 to floor 2
Elevator id:eb0ef2a8-b672-435a-b4d3-ef86a86e1c68 moving past floor 2 to floor 1
Elevator id:eb0ef2a8-b672-435a-b4d3-ef86a86e1c68 says door is now open on floor 1
Elevator id:eb0ef2a8-b672-435a-b4d3-ef86a86e1c68 says door is now open on floor 1
Elevator id: eb0ef2a8-b672-435a-b4d3-ef86a86e1c68 is remaining idle on floor 1
Elevator id: eb0ef2a8-b672-435a-b4d3-ef86a86e1c68 is remaining idle on floor 1
Elevator id: eb0ef2a8-b672-435a-b4d3-ef86a86e1c68 is remaining idle on floor 1
Elevator id: eb0ef2a8-b672-435a-b4d3-ef86a86e1c68 is remaining idle on floor 1
```
## Improvements

* ECS send an elevator to pick up a passenger to a floor going opposite direction. Currently this is allowed, but the user's required destination will be granted after all request going the same direction is served. You will see better results with mulitple elevators, but improvements will be fixed later.
