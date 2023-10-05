
# Pizza Making Model (ACT-R)

This ACT-R model simulates the process of building two types of pizzas based on declarative memory.

## Overview

The model follows a sequence of rules to construct two varieties of pizzas:

1. **Marinara Pizza**: Crust -> Marinara -> Mozzarella -> Pepperoni -> Onion
2. **BBQ Pizza**: Crust -> BBQ -> Cheddar -> Bacon -> Onion

The process is guided by the current goal and the last added ingredient. At each step, the model retrieves the next ingredient from declarative memory, appends it to the pizza, and updates the goal for the subsequent step.

## Rules

- `marinara`: If the goal is to build a pizza and the crust is the base, this rule appends marinara sauce and sets the goal to add cheese.
- `bbq`: Similar to the marinara rule but appends BBQ sauce.
- `mozzarella`: Appends mozzarella cheese if the sauce is marinara and updates the goal to add meat.
- `cheddar`: Appends cheddar cheese if the sauce is BBQ.
- `pepperoni`: If mozzarella is the cheese, this rule adds pepperoni as the meat.
- `bacon`: If cheddar is the cheese, bacon is added.
- `cook_pizza_step`: Final rule to cook the pizza. It appends the last ingredient (onion) and finalizes the pizza-making process.

## Usage

To run the model, execute the script:

```bash
python pizza_dm.py
```

Ensure you have the required ACT-R environment and dependencies set up.

## Output

Upon successful execution, the model will display the constructed pizza:

```
Mmmmmm my crust_marinara_mozzarella_pepperoni_onion pizza is gooooood!
```
OR
```
Mmmmmm my crust_bbq_cheddar_bacon_onion pizza is gooooood!
```
---
## Vacuum Agent Simulator

### Overview

This model simulates adding dirty spots to the declarative memory and moving towards the spots to clean them. 

### Features


3. **Memory System**: The agent's declarative memory (DM) keeps track of the dirty spots in the environment. The agent is intended to move towards them to clean them, but I was not able to get this to work.
4. **Spiral Movement Pattern**: If the agent could move, it would first return to the green square and then proceed with the spiral pattern.

### Usage

To run the model, execute the script:

```bash
python vacuumAgent_dm.py
```

Ensure you have the required ACT-R environment and dependencies set up.
