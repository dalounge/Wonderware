import csv
import os
import sys


def readLinks(base_path):
    window = []
    link_file = ''

    for filenames in os.walk(os.path.join(base_path)):
        for filename in filenames[2]:
            if '.txt'.lower() in os.path.splitext(filename)[1].lower():
                link_file = filename
                break

    with open(os.path.join(base_path, link_file), 'r') as f:
        for row in f:
            clean = row.strip()

            if len(clean) > 0:
                window.append(clean)

    return window

def aggregateSearch(window, search_str):
    current_key = ''
    contain = {}
    script = [
        'Application Script:',
        'Key Script:',
        'Condition Script:',
        'Data Change Script:',
        'QuickFunction:'
    ]

    for row in window:
        for s in script:
            if s in row:
                current_key = row
                contain[row] = []

        if 'Window Report' in row:
            contain[row] = []
            current_key = row

        if search_str.lower() in row.lower():
            contain[current_key].append(row)

    return contain

def writeResults(contain, search_str, base_path):
    with open(os.path.join(base_path, 'results.csv'), 'w', newline='') as f:
        c = csv.writer(f)
        c.writerow([f'Search Results: {search_str}'])
        for k in contain.keys():
            if len(contain[k]) > 0:
                c.writerow('')
                c.writerow([k])
            for v in contain[k]:
                c.writerow([v])

def main():
    
    base_path = os.path.dirname(sys.argv[0])

    print('This utility searches this directory for the first .txt file which should be')
    print('your links and details.  Print from InTouch Links and Details/Window Scripts/All Scripts')
    print('currently works for WW IT 2017 U3 SP1')
    print('')
    print('Search for tag:')
    
    search_str = input()
    
    window = readLinks(base_path)
    contain = aggregateSearch(window, search_str)
    writeResults(contain, search_str, base_path)

    os.startfile(os.path.join(base_path, 'results.csv'), 'open')

if __name__ == '__main__':
    main()
