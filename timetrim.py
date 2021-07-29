import os
import csv

print('make sure that both the audio file and csv file (the one with the timestamps have the same name')
filename = input('Enter Audio file name without extensions: ')
# if (not filename.endswith(".mp3")): #or .avi, .mpeg, whatever.


names_list = []
try:
    with open(f'{filename}.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter='-')
        line_count = 0
        for row in csv_reader:
            timestamp = row[0].split(sep=':')
            timestamp.append('_'.join(row[1].strip().split(' ')))
            
            names_list.append(timestamp)
            
            
            print(f'\t timestamp: {row[0]} \tname:{row[1].lstrip().rstrip()}')
            line_count += 1


        print(f'Processed {line_count} lines.')

except FileNotFoundError as e:
    print(f'File not found error: {e}')

newpath = f'./{filename}' 
if not os.path.exists(newpath):
    os.makedirs(newpath)

i = 0
minDiff = 0
secDiff = 0
while i < len(names_list):
    if i + 1 >= len(names_list):
        os.system(f'ffmpeg -ss {names_list[i][0]}:{names_list[i][1]} -i {filename}.mp3 ./{filename}/{names_list[i][2]}.mp3 &> /dev/null')
        break

    curr = names_list[i]
    nxt = names_list[i+1]
    
    durationSec = (int(nxt[0]) * 60 + int(nxt[1])) - (int(curr[0]) * 60 + int(curr[1]))


    os.system(f'ffmpeg -ss {curr[0]}:{curr[1]} -i {filename}.mp3 -t {durationSec} ./{filename}/{curr[2]}.mp3 &> /dev/null')

    print(f'{i}th created with time duration: {durationSec}\n\n')
    i += 1
    
print('Finished Triming Audio File')