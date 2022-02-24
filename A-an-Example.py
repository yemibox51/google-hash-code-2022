with open ("a_an_example.in.txt","r") as f:
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
        proj_info[proj_name] = [int(days), int(score), int(best_before), int(roles), {}]
        
        for role in range(int(roles)):
            skill, lvl = f.readline().split(" ")
            proj_info[proj_name][4][skill] = int(lvl)

    print(contrib) 
    print(proj_info)
    f.close()        