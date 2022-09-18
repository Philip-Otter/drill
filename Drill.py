############################
########### Drill ##########
## Created by Philip Otter #
####Created August 2022 ####
############################

import subprocess

select="JustNamesnsLayer2.txt"  # Put your desired file path in this line!
print("\n\n")

origFile=open(select, 'r')

for line in origFile:
    prefix = "Name:	"
    newLine=line.removeprefix(prefix).strip()

    dig = subprocess.run(["nslookup", "-type=any", "-query=AXFR", newLine, "ns.inlanefreight.htb"])

    dig

    
origFile.close()
print("\n\n")