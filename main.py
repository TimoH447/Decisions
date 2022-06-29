#This program is supposed to predict the next key you press
#
#
from pathlib import Path
import json
import keyboard

def evaluation(exp_key, key_press, score):
    if exp_key == key_press:
        score[0] += 1
        score[1] +=1
        print('Correct Guess')
    else:
        score[1]+=1
        print('Wrong Guess')
    


def guess(last_keys, pat_dict):
    x = 'a'
    a = last_keys[1:]+'a'
    f = last_keys[1:]+'f'
    a1 =  a in pat_dict
    f1 =  f in pat_dict
    if a1 and f1:
        if pat_dict[a] > pat_dict[f]:
            x='a'
        elif pat_dict[f] > pat_dict[a]:
            x='f'
        else: 
            x='a'
    elif a1:
        x='a'
    elif f1:
        x='f'
    else:
        x= 'a'
    return x

def main():
    pattern = []
    if Path('pat_dict.json').exists():
        with open('pat_dict.json','r') as f:
            pat_dict=json.load(f)
    else:
        print('hi')
        pat_dict = {}
    pattern_length = 5

    score = [0,0]
    last_keys = ''
    exp_key = 'a'
    run = True
    while run:
        event = keyboard.read_event()
        #Beginning, append keypresses until enough
        if len(last_keys)>=pattern_length:
            #pattern.append(last_keys)
            if last_keys in pat_dict:
                pat_dict[last_keys] +=1
            else: 
                pat_dict[last_keys] = 1
            last_keys = last_keys[1:]
        

        # 2 Keys to decide between
        #if keyboard.read_key() == 'a':
        if event.event_type == keyboard.KEY_DOWN and event.name == 'a':
            print('a')
            evaluation(exp_key, 'a', score)
            last_keys = last_keys + 'a'
            exp_key = guess(last_keys,pat_dict)
        #if keyboard.read_key()== 'f':
        if event.event_type == keyboard.KEY_DOWN and event.name == 'f':
            evaluation(exp_key, 'f', score)
            last_keys = last_keys +'f'
            exp_key = guess(last_keys,pat_dict)
        
        #Exit the programm
        if keyboard.read_key()=='q':
            run = False


    print('\n Percentage of correct guesses: ', score[0], ' ', score[1], ' ',score[0]/score[1])
    with open('pat_dict.json','w') as f:
        json.dump(pat_dict, f)

if __name__ == '__main__':
    main()    
