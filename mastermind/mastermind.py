import random as rd
import os

try_limit=12
colours=["r","g","b","y","p","w"] # red, green, blue, yellow, purple, white
length_of_combination=4
def combination_to_guess(length:int): #returns a string 
    l=[]
    for i in range(length):
        l.append(rd.choice(colours))
    return l

def reset_stats():
    os.system("attrib -h mastermind_score.txt")
    score=open("mastermind_score.txt","w")#resets the score file
    score.close()
    os.system("attrib +h mastermind_score.txt")

    os.system("attrib -h mastermind_game_number.txt")
    game_number=open("mastermind_game_number.txt","w")#resets the game_number file
    game_number.truncate()
    game_number.write("0")
    game_number.close()
    os.system("attrib +h mastermind_game_number.txt")

def comparison(guess:list,code:list):
    partial,correct=0,0
    c_buffer=c.copy()
    for i in range (len(guess)) :
        if guess[i] in c_buffer:
            partial+=1
            c_buffer.remove(guess[i])
    for i in range(length_of_combination):
        if guess[i]==code[i]:
            correct+=1
            partial-=1
    return correct,partial

ingame=False
partial=0
correct=0
choice=str(input("Type p to play, q to quit or r to reset your statistics "))
if choice not in ["p","q","r"]:
    replay=str(input("Pls type either p, q or r "))
if choice=="p":
    ingame=True
if choice =="q":
    print("see you")
if choice =="r": # choosing to reset the statistics do not entail palying a game, hence nothing happens once stats get reset
    reset_stats()



while ingame==True: #initial loop to begin to play a game of mastermind (find ONE code)
    c=combination_to_guess(length_of_combination)
    print(c)
    c_buffer=c.copy()
    tries=1
    while tries<=try_limit:
        g=str(input("Pls input a combination of r(red) g(green) b(blue) y(yellow) p(purple) w(white) , for instance rgrp ")) # People are asked to input
        #a string, that is converted into a list in order to be able to remove elements form it during the comparison with the secret code 
        g_to_list=[i for i in g]
        if len(g)!=4:
            g=str(input("Pls enter a four digit code "))
            g_to_list=[i for i in g]
        if g_to_list==c:
            print("you won in "+str(tries)+" tries")
            os.system("attrib -h mastermind_score.txt")
            score=open("mastermind_score.txt","a")
            score.write(str(try_limit-tries))# shows, appends the score (number of tries minus your number or tries to find the code), closes and hides
            score.write("\n")
            score.close()
            os.system("attrib +h mastermind_score.txt")
            break
        a=comparison(g_to_list,c)       
        print("correct: "+str(a[0])+"\n"+"partial: "+str(a[1]))
        partial,correct=0,0
        tries+=1
        c_buffer=c.copy()
    game_number=os.system("attrib -h mastermind_game_number.txt")# l52->l61 : opens, takes the values, closes, opens with write mode to clear the text
    game_number=open("mastermind_game_number.txt","r+")# then writes the value +1, then closes again and hides
    gn=game_number.read()
    gn=int(gn)
    game_number.close()
    gn+=1
    game_number=open("mastermind_game_number.txt","w")
    game_number.write(str(gn))
    game_number.close()
    game_number=os.system("attrib +h mastermind_game_number.txt")

    replay=str(input("type p to play again, q to quit or r to reset your statistics "))
    if replay not in ["p","q","r"]:
        replay=str(input("pls enter either p, q or r "))
    if replay=="q":
        ingame=False
    if replay=="r":
        reset_stats()
        play_after_resetting=str(input("Wanna play again? y for yes, n for no "))
        if play_after_resetting not in ["y","n"]:
            play_after_resetting=str(input("Pls type either y or n "))
        if play_after_resetting=="n":
            ingame=False
    

