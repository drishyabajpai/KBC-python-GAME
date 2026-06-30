'''  Start Program
      │
      ▼
Load Questions
      │
      ▼
Shuffle Questions
      │
      ▼
Show Welcome
      │
      ▼
Ask Question
      │
      ▼
User Gives Answer
      │
      ▼
Is Correct?
   │          │
 Yes         No
 │            │
Prize      Show Correct Answer
 │            │
Next Q    Game Over
 │
After All Questions
 │
Final Prize
 │
Play Again?
 │
Yes → Restart
No  → Exit        '''

import random

questions = [
("What is the capital of India?",["Delhi","Mumbai","Kolkata","Chennai"],0,"Delhi is the capital of India."),
("Which language is used for AI the most?",["Python","HTML","CSS","XML"],0,"Python has the largest AI ecosystem."),
("2 + 2 = ?",["3","4","5","6"],1,"2+2=4."),
("Largest planet?",["Earth","Mars","Jupiter","Venus"],2,"Jupiter is the largest planet."),
("Who developed Python?",["Guido van Rossum","Elon Musk","Bill Gates","Dennis Ritchie"],0,"Guido created Python."),
("Which is a mammal?",["Shark","Whale","Octopus","Fish"],1,"Whales are mammals."),
("Which is the fastest land animal?",["Tiger","Cheetah","Lion","Horse"],1,"Cheetah."),
("Which keyword creates a function?",["func","define","def","function"],2,"Python uses def."),
("Which symbol starts a comment?",["//","#","/*","--"],1,"# starts comments."),
("Sun is a?",["Planet","Star","Galaxy","Moon"],1,"The Sun is a star."),
("5*6=?",["11","30","25","35"],1,"5x6=30."),
("Which data type stores True/False?",["int","bool","float","str"],1,"bool."),
("Which loop repeats while condition is true?",["for","repeat","while","loop"],2,"while loop."),
("RGB stands for?",["Red Green Blue","Right Green Black","Red Gold Blue","None"],0,"RGB."),
("HTML is used for?",["AI","Web pages","Database","OS"],1,"HTML builds webpages."),
("CPU means?",["Central Processing Unit","Computer Power Unit","Central Print Unit","None"],0,"CPU."),
("Earth has how many moons?",["1","2","3","4"],0,"One natural moon."),
("Water formula?",["CO2","H2O","O2","NaCl"],1,"H2O."),
("India's national animal?",["Lion","Tiger","Elephant","Leopard"],1,"Royal Bengal Tiger."),
("Python file extension?",[".java",".py",".cpp",".html"],1,"Python uses .py.")
]
'''┌────────────────────────────┐
Question
Options
Correct Answer
Explanation
└────────────────────────────┘ '''
#Why list inside tuple?
'''(
Question,

[Options],

Answer,

Explanation
)

Question never changes.

Explanation never changes.

Only options are stored as a list.
'''


prizes=[1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,640000,1250000,2500000,5000000,10000000,20000000,30000000,50000000,70000000,100000000]

letters=["A","B","C","D"]

def beep(correct=True):
    try:
        if __import__("platform").system()=="Windows":
            import winsound
            winsound.Beep(1000 if correct else 400,250)
            winsound.Beep(1400 if correct else 300,250)
        else:
            print("\a")
    except:
        print("\a")


    ''' Function

def beep(correct=True):

Function means

A reusable block of code.

Instead of writing beep code again and again

We write once

Call many times.

Inside

try:

means

Try this.

If something fails

Don't crash.

except:

means

If error happens

Do this instead.

Why winsound?

Windows has

winsound

Example

winsound.Beep(1000,250)

1000

↓

Frequency

250

↓

Milliseconds

Higher frequency

↓

Sharper sound  '''

def play():
    score=0
    qs=questions[:]
    random.shuffle(qs)
    print("="*45)
    print("        WELCOME TO PYTHON KBC")
    print("="*45)

    for i,(q,opts,ans,exp) in enumerate(qs):
        print(f"\nQuestion {i+1}  Prize: ₹{prizes[i]:,}")
        print(q)
        for j,opt in enumerate(opts):
            print(f"{letters[j]}. {opt}")
        choice=input("Enter A/B/C/D: ").strip().upper()
        while choice not in letters:
            choice=input("Enter valid option: ").strip().upper()
        if letters.index(choice)==ans:
            beep(True)
            score=prizes[i]
            print("✅ Correct!")
            print("Explanation:",exp)
            print(f"Current Prize: ₹{score:,}")
        else:
            beep(False)
            print("❌ Wrong!")
            print("Correct Answer:",letters[ans],"-",opts[ans])
            print("Explanation:",exp)
            break

    print("\n"+"="*45)
    print(f"Game Over! You won ₹{score:,}")
    print("="*45)

while True:
    play()
    again=input("\nPlay Again? (Y/N): ").strip().upper()
    if again!="Y":
        print("Thanks for playing KBC!")
        break
