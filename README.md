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
0. Start schedule with required exercises
1. While we do not cover all muscle groups,
2.   get a list of unused exercises
3.   shuffle it
4.   get first item and add to schedule
5.   add onto muscle groups that we have covered, all of the muscle groups for that item
6. make sure to cover the minimum number of wkouts/day



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

A simple to use random workout generator. Input your desired push-pull-leg split and the program will generate a 
