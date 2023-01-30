# gains-calculator

Steps to Massive Gains Trainer

1. Input Desired Workout Category (Push/Pull/Legs)
2. Input Desired Workout Days for the Week (default 5 days)
3. Generate List of Workouts
	a. Each Exercise contains: Rep and Set Count, (Printed as 'Reps'x'Sets')
4. Workout list must be of a minimum set count +/-12 to max +/-16 

Backend:
1. Each Workout needs to target each applicable muscle group (ie. Push day should have at least one workout for Chest, Triceps, Shoulders) 
2. Excercises have the attributes: Major Muscle Group, Rep Count, Set Count)


# Algorithm for building schedule
Required stuffs are there
1. For each uncovered muscle group,
2.   randomly pick 1 of the activities covering that muscle group that is not used yet, add it to the list
3.   mark it as used
4. continue until all muscle groups are covered
5. append required stuff to our list of activities



LEGS(Name, Muscle Groups, 'Rep'x'Set'

Squats- Quads/Glutes- 6x4 *
Bulgarian Split Squats- Quads/Glutes- 8x3 *
Pause Squats- Quads/Glutes- 6x4
Hamstring Curls- Hamstrings- 16x2
Weighted Calf Raises- Calves- Failurex3
Lifted Heel Squats- Quads/Glutes- 15x3
Curtsy Squats- Quads/Calves- 10x2
Leg Extensions- Quads- 15x3
Goblet Squat- Quads/Glutes- 15x4
Hip Thrust- Glutes- 12x4
Romanian Deadlift- Hamstring/Glutes- 15x4











PUSH

Bench Press
Tricep Pushdowns
Push Ups
Overhead Shoulder Press
Arnold Press
Dumbbell Pull Over
Chest Fly
Dips
Skull Crushers
Tricep Kickbacks
Rows
Dumbell Rows
Lawnmowers
Lateral Raises
Front Raises
Bicep Curls
Hammer Curls
Pulldown

