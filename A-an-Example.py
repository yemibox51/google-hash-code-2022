<<<<<<< HEAD
<<<<<<< HEAD

from typing import OrderedDict


def return_objs(filename):
    with open (filename,"r") as f:
        people, proj = f.readline().split(" ")
        print(f"people: {people} proj: {proj}")
        contrib = {}
        proj_info = {}
        for i in range(int(people)):
            name, skills = f.readline().split(" ")
            contrib[name] = {}
            for i in range(int(skills)):
                skill, lvl = f.readline().split(" ")
                contrib[name][skill] = int(lvl)

        for i in range(int(proj)):
            proj_name, days, score, best_before, roles = f.readline().split(" ")
            proj_info[proj_name] = [int(days), int(score), int(best_before), int(roles), OrderedDict()]
            
            for role in range(int(roles)):
                skill, lvl = f.readline().split(" ")
                proj_info[proj_name][4][skill] = int(lvl)

        print(contrib) 
        print(proj_info)
        f.close()
        return [proj_info, contrib]


[projects, people] = return_objs("a_an_example.in.txt")
"""

DS info:
conrib = {}
people[name] = {skill : skill_lvl}
projects[name] = [days, score_awarded, best_before, {roles}]

roles is an ordered dict
roles[skill] = skill_lvl


output:
num_proj_completed: int
for proj in num of projs// output:
    name_of_projc_completed:
    name1 nam3
## things to note:
#   order matters when we created the project skills dict proj_info[4]
    """


=======
# Open file in read mode
# Going to change need to submit a text file of the data later 
a = open("a_an_example.in.txt", 'r')

# prints the entire file
print(a.read())
>>>>>>> parent of 4fb0ea9 (Merge branch 'main' of https://github.com/yemibox51/google-hash-code-2022)
=======
# Open file in read mode
# Going to change need to submit a text file of the data later 
a = open("a_an_example.in.txt", 'r')

# prints the entire file
print(a.read())
>>>>>>> parent of 4fb0ea9 (Merge branch 'main' of https://github.com/yemibox51/google-hash-code-2022)
