#Get user input and normalize case
Hard_Skill = input("Enter Hard_Skills: ").strip().title()
Soft_Skill = input("Enter Soft_Skills: ").strip().title()

#define valid skills 
Hard_Skill_Lists = ["Programming" or "Maintenance" or \
                  "Automotive" or "Graphics"\
                  or "Intelligent System"]
Soft_Skill_Lists = ["Positive Attitude" or \
                      "Problem Solving"  or\
                      "Creative Thiking" or\
                      "Time Management"]

#Validate input
if Hard_Skill in Hard_Skill_Lists:
    if Soft_Skill in Soft_Skill_Lists:
        print("You have both soft and hard skills")
    else:
        print("You have to improve your soft skills")
else:
    print("You have to improve your hard skills")
