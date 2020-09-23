""" Kevin and Stuart want to play the 'The Minion Game'.

Game Rules

Both players are given the same string, .
Both players have to make substrings using the letters of the string .
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings.

Scoring
A player gets +1 point for each occurrence of the substring in the string .

Input Format

A single line of input containing the string .
Note: The string  will contain only uppercase letters: .

Constraints



Output Format

Print one line: the name of the winner and their score separated by a space.

If the game is a draw, print Draw.
"""

def minion(string):
    stu = 0
    kev =0
    vowels = ['A', 'E', 'I', 'O', 'U']
    for i in range(len(string)):
        if string[i] in vowels:
            kev += len(string) - i
        else:
            stu += len(string) - i
    if kev>stu:
        print("Kevin"+" "+  str(kev))
    elif stu>kev:
        print("stuart"+" "+ str(stu))
    else: 
        print("Draw")
if __name__ == '__main__':
    s = input()
    minion(s)