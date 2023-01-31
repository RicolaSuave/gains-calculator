### Pull Day Generator (Chest, Triceps, Shoulders)

import yaml
from pprint import pprint
from dataclasses import dataclass
from random import shuffle

with open("config(push).yaml", "r") as file:
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

#set is a list with unique items
muscle_groups = set(current_workout["Possible Muscle Groups"])

schedule = list()
#We are skipping required exercises, check to see if there are any remaining workouts that have muscle groups that are unused. Add them to a remaining list


used_muscle_groups = set()
while muscle_groups != used_muscle_groups:
    remaining_exercises =list()
    for exercise in current_workout["List"]:
        if muscle_groups == used_muscle_groups:
            continue
        remaining_exercises.append( (exercise ["Name"], exercise["Sets"]))

    shuffle(remaining_exercises)

    schedule.append(remaining_exercises[0])
    
    for exercise in current_workout["List"]:
        name = remaining_exercises[0][0]
        if exercise["Name"] == name:
            used_muscle_groups = used_muscle_groups.union(exercise["Muscle Groups"])
            exercise["Used"] = True

remaining_exercises = [ (exercise["Name"], exercise["Sets"])
                       for exercise in current_workout["List"]
                       if not exercise.get("Used") ]

shuffle(remaining_exercises)

if len(schedule) < data["Options"]["NumberOfWorkoutsPerDay"]:
    number_of_exercises_to_add = data["Options"]["NumberOfWorkoutsPerDay"] - len(schedule)
    schedule += remaining_exercises[0 : number_of_exercises_to_add ]

pprint(schedule)