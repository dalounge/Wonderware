import os, re
import it_info # Contains all the WW data we are looking for

'''
Check List
This is all assuming that WW prints everything in order:
    - Need to do key checking on if it doesn't  
    - .lower() string check

Scripts:
    - Do I need to separate each script into its own function or as a whole is good enough?
'''


window = {}
base_path = r'c:\Wapsie'
links_details = 'LinksAndDetails'
qf_funcs = []

# Look into scoping
# Has an S in the header.  Otherwise we got to elminate the colon for line check
def ActiveScript(row):
    for scripts in it_info.it_scripts:
        if re.search(scripts.lower(), row.lower()):
            return scripts
    return None

for folders, subfolders, filenames in os.walk(os.path.join(base_path, links_details)):
    for filename in filenames:
        join_path = os.path.join(folders, filename)



with open(join_path, 'r') as data:
    for row in data:
        if re.search('Window Report'.lower(), row.lower()):
            active_phase = row.split("\"")[1]
            window[active_phase] = {}
        
        script = ActiveScript(row)

        if script != None:
            active_phase = script
            window[active_phase] = {}

        if active_phase == 'QuickFunctions':
            if 'QuickFunction:' in row:
                qf_funcs.append(row.split(':')[1].split('(')[0] + '(')

# Function this
        for func in it_info.all_funcs:
            if f'{func}(' in row:
                if func not in window[active_phase]:
                    window[active_phase][func] = 1
                    
                elif func in window[active_phase]:
                    window[active_phase][func] += 1

## Don't need to re-read this file, start the memory version back at 0
with open(join_path, 'r') as data:
    for row in data:

        if re.search('Window Report'.lower(), row.lower()):
            active_phase = row.split("\"")[1]

        for qf in qf_funcs:
            if qf in row: 
                if qf not in window[active_phase]:
                    window[active_phase]['QF-' + qf[:-1]] = 1

                elif qf in window[active_phase]:
                    window[active_phase]['QF-' + qf[:-1]] += 1

print(window)
