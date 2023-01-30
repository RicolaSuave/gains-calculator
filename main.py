import yaml
from pprint import pprint
from dataclasses import dataclass
from random import shuffle

with open("config.yaml", "r") as file:
    data = yaml.safe_load(file)


pprint(data)

# lets generate 1 day

# Algorithm for building schedule

current_workout = data["Workouts"][0]

muscle_groups = current_workout["Possible Muscle Groups"]

schedule = list()

for exercise in current_workout["List"]:
    if exercise.get("Important"):
        schedule.append((exercise["Name"], exercise["Sets"]))
        exercise["Used"] = True

# schedule = [ (exercise["Name"], exercise["Sets"])
#              for exercise in current_workout["List"] 
#              if exercise.get("Important") ]

# 1. For each uncovered muscle group,
for muscle_group in muscle_groups:
    filtered_exercises = list()
    for exercise in current_workout["List"]:
        if exercise.get("Important"): continue # skip if important

        if exercise.get("Used"): continue # skip if used

        if muscle_group in exercise["Muscle Groups"]:
            filtered_exercises.append((exercise["Name"], exercise["Sets"]))
            
    # filtered_exercises = [ (exercise["Name"], exercise["Sets"])
    #                        for exercise in current_workout["List"] 
    #                        if muscle_group in exercise["Muscle Groups"] ]


    shuffle(filtered_exercises)

    chosen_exercise = filtered_exercises[0]

    for exercise in current_workout["List"]:
        if exercise["Name"] == chosen_exercise[0]:
            exercise["Used"] = True
            break

    schedule.append(chosen_exercise)

remaining_exercises = [ (exercise["Name"], exercise["Sets"])
                        for exercise in current_workout["List"] 
                        if not exercise.get("Used") ]

shuffle(remaining_exercises)

if len(schedule) < data["Options"]["NumberOfWorkoutsPerDay"]:
    number_of_exercises_to_add = data["Options"]["NumberOfWorkoutsPerDay"] - len(schedule)
    schedule += remaining_exercises[ 0 : number_of_exercises_to_add ]

pprint(schedule)

    

# we want to generate 1 day for now

# data = preprocessInput(data)

# def preprocessInput(data: dict):
#     pass


# @dataclass
# class WorkoutItem:
#     Important: bool
#     MuscleGroups: list[str]
#     Name: str
#     Sets: str

# @dataclass
# class Workout:
#     Name: str
#     Items: list[WorkoutItem]