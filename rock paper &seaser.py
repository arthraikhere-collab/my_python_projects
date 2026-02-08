#making game rpck paper seaser by using random in vilt dfunction
import random 
emojis={'r': '🪨','p':'📃','s':'✂️'}
choise=('r','p','s')

user_choice=input("inter your choice b/w (r/p/s): ")
if user_choice not in choise:
    print('invalid choise ')
computer_choise=random.choice(choise)    
print(f'you chose{emojis[user_choice]}')
print(f'computer chose{emojis[computer_choise]}')


if user_choice==computer_choise:
    print("tie?????")
elif():
  (user_choice =='r'and computer_choise =='s') or\
  (user_choice =='s'and computer_choise =='p') or\
  (user_choice =='p' and computer_choise =='r') 
  print ('you win congo 😍  😍  😍 ')
else:
   print("you lose sad 🥲  🥲  🥲  🥲")  

should_continue= input('continue ? (y/n): ')
if should_continue =='n':
   exit() 