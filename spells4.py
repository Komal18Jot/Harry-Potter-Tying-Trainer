import random
import time
import math

spells=[]
playagain=True
score=0 
targettypingtime=0
def read_spells(filename: str) -> list[str]:
    """
    Reads a list of spells from a file and returns a list of spells.
    """
    # TODO: implement this function
    with open(filename,"r") as f:
        for line in f.readlines():
            data=line.strip("\n")
            spells.append(data)

def get_random_spell(spells: list[str]) -> str:
    """
    Returns a random spell from a list of spells, converted to lowercase.
    """
    # TODO: implement this function
    index=random.randrange(0,len(spells)+1)
    spell=spells[index]
    return spell.lower()

def display_header():
    """
    Displays header as follows:
    ############################################################
    Harry Potter Typing Trainer
    ############################################################
    """
    
    print("#"*60)
    print("Harry Potter Typing Trainer")
    print("#"*60)

def display_instructions():
    """
    Displays instructions from instructions.txt
    """
    with open("instructions.txt","r") as f:
        for i in f.readlines():
            print(i)
            
def get_user_input(spell: str) -> (str, float):
    """
    Gets input from the user
    Returns the input and the time it took the user to type the input
    """
    start = time.time()
    print(f"Type the following spell: {spell}")
    user_input = input().lower()
    user_time = round(time.time() - start, 2)
    print(f"Result: {user_time} seconds (goal: {get_target_time(spell)} seconds).")
    return user_input, user_time

def get_target_time(spell: str) -> float:
    """
    Returns the target time to type the spell.
    """
    # TODO: Implement this function
    length=len(spell)
    targettypingtime=math.floor(length*0.3)
    return targettypingtime

def calculate_points(spell: str, user_input: str, user_time: float) -> int:
    """
    Calculates the points that the user gets.
    spell: The spell that the user is typing.
    user_input: The input that the user typed.
    user_time: The time that the user took to type the input.
    """
    # TODO: Implement this function
    global score
    if user_input.lower()==spell:
        if user_time>=targettypingtime:
            score+=10
            print("You get 10 points! Your score is: ",score)
        elif user_time>=(targettypingtime*1.5) and user_time<targettypingtime:
            score+=5
            print("You get 5 points! Your score is: ",score)
        elif user_time>=(targettypingtime*2) and user_time<(targettypingtime*1.5):
            score+=3
            print("You get 3 points! Your score is: ",score)
        elif user_time<(targettypingtime*2):
            score+=1
            print("You get 1 points! Your score is: ",score)
    else:
        score-=5
        print("You get -5 points! Your score is: ",score)
    return score

def display_feedback(spell: str, user_input: str):
    """
    Displays feedback (correct or incorrect) to the user.
    """
    if user_input==spell:
        print("Correct!")
    else:
        print("Incorrect.\nThe correct answer was:", spell)
        
def play_again() -> bool:
    """
    Asks the user if they want to play again
    Returns True if the user enters Y or y, False otherwise
    """

    ans=input("Do you want to practice more? y/n: ")
    if ans=="Y" or ans=="y":
        return True
    else:
        return False

def main() -> None:
    """
    Main program.
    """
    read_spells('spells.txt')
    display_header()
    display_instructions()
    
    global targettypingtime
    global playagain
    while playagain:
        spell = get_random_spell(spells)
        user_input,user_time = get_user_input(spell)
        display_feedback(spell, user_input)
        targettypingtime=(get_target_time(spell))
        calculate_points(spell, user_input, user_time)
        playagain=play_again()
        

main()

