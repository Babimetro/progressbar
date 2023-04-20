
#A progress bar for bacckend developers and geeky guys
import sys
import time

def progressBar(count,total,suffix=''):
    barlenght=60 #or up to 100
    filledlenght=int(round(barlenght*count/float(total)))
    percent=round(100.0*count/float(total),1)
    bar='#'*filledlenght+'-'*(barlenght-filledlenght)
    sys.stdout.write('[%s] %s%s...%s\r' %(bar,percent,'%',suffix))
    sys.stdout.flush()
    
number=525 # or any other number this is your maximum value of range considering we start from zero

for value in range(0,number+1):
    progressBar(round((value*100/number),1),100)
    time.sleep(0.1)
  