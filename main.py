import yaml
from pprint import pprint
from dataclasses import dataclass
from random import shuffle

with open("config.yaml", "r") as file:
    data = yaml.safe_load(file)

# Algorithm for building schedule
# 0. Start schedule with required exercises
# 1. While we do not cover all muscle groups,
# 2.   get a list of unused exercises
# 3.   shuffle it
# 4.   get first item and add to schedule
# 5.   add onto muscle groups that we have covered, all of the muscle groups for that item
# 6. make sure to cover the minimum number of wkouts/day

current_workout = data["Workouts"][0]

# set is a list with unique items
muscle_groups = set(current_workout["Possible Muscle Groups"])

schedule = list()

# 0. Start schedule with required exercises
used_muscle_groups = set()
for exercise in current_workout["List"]:
    if exercise.get("Important"):
        schedule.append( (exercise["Name"], exercise["Sets"]) )
        exercise["Used"] = True
        used_muscle_groups = used_muscle_groups.union(exercise["Muscle Groups"])

# 1. While we do not cover all muscle groups
while muscle_groups != used_muscle_groups:
    # 2.   get a list of unused "remaining" exercises
    remaining_exercises = list()
    for exercise in current_workout["List"]:
        if exercise.get("Used"):
            continue
        # skip if we have used *all* of the muscle groups of this exercise before
        # >>> bigger = set( [1,2,3] ) 
        # >>> subset = set( [1,2] )
        # >>> bigger.intersection(subset)
        # {1, 2}
        # >>> bigger.intersection(subset) == subset
        # True # all the items in subset are also in bigger, we can skip these
        if used_muscle_groups.intersection(exercise["Muscle Groups"]) == set(exercise["Muscle Groups"]):
            continue
        remaining_exercises.append( (exercise["Name"], exercise["Sets"]) ) # "tuple" of 2 items: (__str__, str)
    
    # 3.   shuffle it
    shuffle(remaining_exercises)

    # 4.   get first item and add to schedule
    schedule.append(remaining_exercises[0])

    # 5.  add onto muscle groups that we have covered, all of the muscle groups for that item
    # 5a. search all exercises for this item name
    for exercise in current_workout["List"]:
        # remaining_exercises: list[(STR,str)]
        # remaining_exercises[0]: (STR,str)
        # remaining_exercises[0][0]: STR
        name = remaining_exercises[0][0]
        if exercise["Name"] == name:
            # 5b. concatenate (add sets together) all muscle groups for that item into used_muscle_groups
            used_muscle_groups = used_muscle_groups.union(exercise["Muscle Groups"])
            exercise["Used"] = True


# dict[key] throws an error if key does not exist
# dict.get(key) does not even if the key does not exist 

# 6. make sure to cover the minimum number of wkouts/day
remaining_exercises = [ (exercise["Name"], exercise["Sets"])
                        for exercise in current_workout["List"] 
                        if not exercise.get("Used") ]

shuffle(remaining_exercises)

if len(schedule) < data["Options"]["NumberOfWorkoutsPerDay"]:
    number_of_exercises_to_add = data["Options"]["NumberOfWorkoutsPerDay"] - len(schedule)
    schedule += remaining_exercises[ 0 : number_of_exercises_to_add ]

# Done

pprint(schedule)
