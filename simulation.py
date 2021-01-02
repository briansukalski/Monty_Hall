import random

num_trials = 0

switch_win_count = 0
stay_win_count = 0

#Function to generate doors
def gen_doors():
    doors = ["goat", "goat", "goat"]
    car_index = random.randint(0, 2)
    doors[car_index] = "car"
    return doors

#Host knows the door example
while num_trials < 100000:
    trial_doors = gen_doors()
    contestant_choice = trial_doors.pop(random.randint(0, 2))
    trial_doors.remove("goat")
    switch_choice = trial_doors[0]
    if contestant_choice == "car":
        stay_win_count += 1
    elif switch_choice == "car":
        switch_win_count += 1
    num_trials += 1

print("If the host shows you a goat: /n")
print("Probability of winning if you stay with your door:")
print(stay_win_count / num_trials)
print("/n")
print("Probability of winning if you switch doors:")
print(switch_win_count / num_trials)


num_trials = 0
switch_win_count = 0
stay_win_count = 0
#Contestant luckily gets to end
while num_trials < 100000:
    trial_doors = gen_doors()
    contestant_choice = trial_doors.pop(random.randint(0, 2))
    removed_door = trial_doors.pop(0)
    if removed_door == "goat":
        switch_choice = trial_doors[0]
        if contestant_choice == "car":
            stay_win_count += 1
        elif switch_choice == "car":
            switch_win_count += 1
        num_trials += 1


print("If you successfully reveal a goat door: /n")
print("Probability of winning if you stay with your door:")
print(stay_win_count / num_trials)
print("/n")
print("Probability of winning if you switch doors:")
print(switch_win_count / num_trials)