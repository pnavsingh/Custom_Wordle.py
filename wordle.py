#inspired from wordle a 5 letter word game
#Works well with words that do not repeat letters, otherwise kinda buggy
import random
import colorama
from colorama import Fore, Back, Style
colorama.init()
print("The rules are very simple: You need to guess the five-letter hidden word in 6 tries. To get started, just type any word on the first line. If the letter is guessed correctly and is in the correct place, it will be marked in green, if the letter is in the word, but in the wrong place - in yellow, and if the letter is not in the word, it will remain white.")


words=['about', 'above', 'abuse', 'actor', 'acute', 'admit', 'adopt', 'adult', 'after', 'again', 'agent', 'agree', 'ahead', 'alarm', 'album', 'alert', 'alike', 'alive', 'allow', 'alone', 'along', 'alter', 'among', 'anger', 'angle', 'angry', 'apart', 'apple', 'apply', 'arena', 'argue', 'arise', 'array', 'aside', 'asset', 'audio', 'audit', 'avoid', 'award', 'aware', 'badly', 'baker', 'bases', 'basic', 'basis', 'beach', 'began', 'begin', 'begun', 'being', 'below', 'bench', 'billy', 'birth', 'black', 'blame', 'blind', 'block', 'blood', 'board', 'boost', 'booth', 'bound', 'brain', 'brand', 'bread', 'break', 'breed', 'brief', 'bring', 'broad', 'broke', 'brown', 'build', 'built', 'buyer', 'cable', 'calif', 'carry', 'catch', 'cause', 'chain', 'chair', 'chart', 'chase', 'cheap', 'check', 'chest', 'chief', 'child', 'china', 'chose', 'civil', 'claim', 'class', 'clean', 'clear', 'click', 'clock', 'close', 'coach', 'coast', 'could', 'count', 'court', 'cover', 'craft', 'crash', 'cream', 'crime', 'cross', 'crowd', 'crown', 'curve', 'cycle', 'daily', 'dance', 'dated', 'dealt', 'death', 'debut', 'delay', 'depth', 'doing', 'doubt', 'dozen', 'draft', 'drama', 'drawn', 'dream', 'dress', 'drill', 'drink', 'drive', 'drove', 'dying', 'eager', 'early', 'earth', 'eight', 'elite', 'empty', 'enemy', 'enjoy', 'enter', 'entry', 'equal', 'error', 'event', 'every', 'exact', 'exist', 'extra', 'faith', 'false', 'fault', 'fiber', 'field', 'fifth', 'fifty', 'fight', 'final', 'first', 'fixed', 'flash', 'fleet', 'floor', 'fluid', 'focus', 'force', 'forth', 'forty', 'forum', 'found', 'frame', 'frank', 'fraud', 'fresh', 'front', 'fruit', 'fully', 'funny', 'giant', 'given', 'glass', 'globe', 'going', 'grace', 'grade', 'grand', 'grant', 'grass', 'great', 'green', 'gross', 'group', 'grown', 'guard', 'guess', 'guest', 'guide', 'happy', 'harry', 'heart', 'heavy', 'hence', 'henry', 'horse', 'hotel', 'house', 'human', 'ideal', 'image', 'index', 'inner', 'input', 'issue', 'japan', 'jimmy', 'joint', 'jones', 'judge', 'known', 'label', 'large', 'laser', 'later', 'laugh', 'layer', 'learn', 'lease', 'least', 'leave', 'legal', 'level', 'lewis', 'light', 'limit', 'links', 'lives', 'local', 'logic', 'loose', 'lower', 'lucky', 'lunch', 'lying', 'magic', 'major', 'maker', 'march', 'maria', 'match', 'maybe', 'mayor', 'meant', 'media', 'metal', 'might', 'minor', 'minus', 'mixed', 'model', 'money', 'month', 'moral', 'motor', 'mount', 'mouse', 'mouth', 'movie', 'music', 'needs', 'never', 'newly', 'night', 'noise', 'north', 'noted', 'novel', 'nurse', 'occur', 'ocean', 'offer', 'often', 'order', 'other', 'ought', 'paint', 'panel', 'paper', 'party', 'peace', 'peter', 'phase', 'phone', 'photo', 'piece', 'pilot', 'pitch', 'place', 'plain', 'plane', 'plant', 'plate', 'point', 'pound', 'power', 'press', 'price', 'pride', 'prime', 'print', 'prior', 'prize', 'proof', 'proud', 'prove', 'queen', 'quick', 'quiet', 'quite', 'radio', 'raise', 'range', 'rapid', 'ratio', 'reach', 'ready', 'refer', 'right', 'rival', 'river', 'robin', 'roger', 'roman', 'rough', 'round', 'route', 'royal', 'rural', 'scale', 'scene', 'scope', 'score', 'sense', 'serve', 'seven', 'shall', 'shape', 'share', 'sharp', 'sheet', 'shelf', 'shell', 'shift', 'shirt', 'shock', 'shoot', 'short', 'shown', 'sight', 'since', 'sixth', 'sixty', 'sized', 'skill', 'sleep', 'slide', 'small', 'smart', 'smile', 'smith', 'smoke', 'solid', 'solve', 'sorry', 'sound', 'south', 'space', 'spare', 'speak', 'speed', 'spend', 'spent', 'split', 'spoke', 'sport', 'staff', 'stage', 'stake', 'stand', 'start', 'state', 'steam', 'steel', 'stick', 'still', 'stock', 'stone', 'stood', 'store', 'storm', 'story', 'strip', 'stuck', 'study', 'stuff', 'style', 'sugar', 'suite', 'super', 'sweet', 'table', 'taken', 'taste', 'taxes', 'teach', 'teeth', 'terry', 'texas', 'thank', 'theft', 'their', 'theme', 'there', 'these', 'thick', 'thing', 'think', 'third', 'those', 'three', 'threw', 'throw', 'tight', 'times', 'tired', 'title', 'today', 'topic', 'total', 'touch', 'tough', 'tower', 'track', 'trade', 'train', 'treat', 'trend', 'trial', 'tried', 'tries', 'truck', 'truly', 'trust', 'truth', 'twice', 'under', 'undue', 'union', 'unity', 'until', 'upper', 'upset', 'urban', 'usage', 'usual', 'valid', 'value', 'video', 'virus', 'visit', 'vital', 'voice', 'waste', 'watch', 'water', 'wheel', 'where', 'which', 'while', 'white', 'whole', 'whose', 'woman', 'women', 'world', 'worry', 'worse', 'worst', 'worth', 'would', 'wound', 'write', 'wrong', 'wrote', 'yield', 'young', 'youth']

guess = random.choice(words)#picks the word
gset = []

top=["q","w","e","r","t","y","u","i","o","p"]
mid=["a","s","d","f","g","h","j","k","l"] 
low=["z","x","c","v","b","n","m"]
top1=["q","w","e","r","t","y","u","i","o","p"]
mid1=["a","s","d","f","g","h","j","k","l"] 
low1=["z","x","c","v","b","n","m"]
count=0
num=0
ans=""
us0=""
us1=""
us2=""
us3=""
us4=""
for i in range(5):
    gset.append(guess[i])

def check(word,words):
    if word in words:
        return True
    else:
        return False


while(count<6):
        user=input(Fore.WHITE+"Go ahead and guess your 5 letter word!: ")
        user=user.lower()
        num=0
        prev=""
        if(check(user,words)):
            if(user==guess):
                print("You Got The Word!")
                count=7
            
            
            else:
                for i in range(5):
                    if(user[i] == guess[i]):
                        wrd = user[i]
                        #print(Fore.GREEN+user[i]+ " Is Green") #
                        if(check(wrd,top)):
                            for i in range(10):
                                if top[i] == wrd:
                                    top[i] = "1"

                        if(check(wrd,mid)):
                            for i in range(9):
                                if mid[i] == wrd:
                                    mid[i] = "1"

                        if(check(wrd,low)):
                            for i in range(7):
                                if low[i] == wrd:
                                    low[i] = "1"
                        prev+=Fore.GREEN+wrd
                        print(Fore.GREEN+wrd+ " ",end="")

                    elif (user[i] in gset):
                        #print(Fore.YELLOW+user[i]+ " Is Yellow") #*
                        wrd = user[i]
                        if(check(wrd,top)):
                            for i in range(10):
                                if top[i] == wrd:
                                    top[i] = "2"

                        if(check(wrd,mid)):
                            for i in range(9):
                                if mid[i] == wrd:
                                    mid[i] = "2"

                        if(check(wrd,low)):
                            for i in range(7):
                                if low[i] == wrd:
                                    low[i] = "2"
                        prev+=Fore.YELLOW+wrd
                        print(Fore.YELLOW+wrd+" ",end="")
                    
                    else:
                        #print(Fore.WHITE+user[i]+" Is White")#/
                        wrd=user[i]
                        if(check(wrd,top)):
                            for i in range(10):
                                if top[i] == wrd:
                                    top[i] = "3"

                        if(check(wrd,mid)):
                            for i in range(9):
                                if mid[i] == wrd:
                                    mid[i] = "3"

                        if(check(wrd,low)):
                            for i in range(7):
                                if low[i] == wrd:
                                    low[i] = "3"
                        prev+=Fore.WHITE+wrd           
                        print(Fore.WHITE+wrd+" ",end="")
            print("")
            print("")
            print(Fore.WHITE+"Your previous guesses")
            ans+=prev+" "
            print(ans)
            

            print(Fore.WHITE+"Keyboard")
            while(num==0):
                for i in range(10):
                    if(top[i]=='1'):
                        print(Fore.GREEN+top1[i],end=" ")
                    elif(top[i]=='2'):
                        print(Fore.YELLOW+top1[i],end=" ")
                    elif(top[i]=='3'):
                        print(Fore.BLACK+top1[i],end=" ")
                    else:
                        print(Fore.WHITE+top1[i],end=" ")
                num+=1
                print("")
            while(num==1):
                for i in range(9):
                    if(mid[i]=='1'):
                        print(Fore.GREEN+mid1[i],end=" ")
                    elif(mid[i]=='2'):
                        print(Fore.YELLOW+mid1[i],end=" ")
                    elif(mid[i]=='3'):
                        print(Fore.BLACK+mid1[i],end=" ")
                    else:
                        print(Fore.WHITE+mid1[i],end=" ")
                num+=1
                print("")
            while(num==2):
                for i in range(7):
                    if(low[i]=='1'):
                        print(Fore.GREEN+low1[i],end=" ")
                    elif(low[i]=='2'):
                        print(Fore.YELLOW+low1[i],end=" ")
                    elif(low[i]=='3'):
                        print(Fore.BLACK+low1[i],end=" ")
                    else:
                        print(Fore.WHITE+low1[i],end=" ")
                    num+=1
                print("")
                
                count=count+1
               # print(top)
               # print(mid)
               # print(low)
        else:
            print("Thus word is not in thou dictionary try again")


print(Fore.WHITE+guess+ " Is the Word")

