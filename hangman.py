import string
from words import choose_word
from images import IMAGES
def ifvailid(user_input):
  if len(user_input)!=1:
    return False
  if not user_input.isalpha():
    return False
  return False

def is_word_gussed(secreat_word,letters_gussed):
  if secreat_word==get_gussed_word(secreat_word,letters_gussed):
    return True
  return  False

def get_gussed_word(secreat_word,letters_gussed):
  index=0
  guessed_word=" "
  while (index<len(secreat_word)):
    if secreat_word[index] in letters_gussed:
      guessed_word+=secreat_word[index]
    else:
      guessed_word+=" "
      index+=1
    return guessed_word

def get_avilable_letters(letter_guessed):
  import string
  letters_left=string.ascii_lowercase
  for i in letter_guessed:
    letter_left=letters_left.replace(i," ")
  return letters_left

def get_hint(secreat_word,letters_guessed):
  import random
  letters_not_guessed=[]
  for i in secreat_word:
    if i not in letters_guessed:
      if i not in letters_not_guessed:

        letters_not_guessed.append(i)

  return random.choice(letters_not_guessed)

remaining_lives=8
stotallives=remaining_lives=8
def hangman (secraet_word):
  print("welcome to the game,hangman!")
  print(secraet_word,'secreat_wordsecreat_word')
  print("I am thinking of a word that is "+str(len(secraet_word))+"letters long.")
  print(" ")
  letters_guessed=[]
  level=input("enter the level in which u want to play:\n(a for  easy\n""(b) for medium\n""(c)for  hard level:")
  total_lives=remaining_lives=8
  images_selection_last_indices=[0,1,2,3,4,5,6,7]

  if level=="b":
    total_lives=remaining_lives=6
    image_selection=[0,2,3,5,6,7]
  elif level=="c":
    total_lives=remaining_lives=4
    image_selection=[1,3,5,7]
  elif level=="a":
    total_lives=remaining_lives=8
    image_selection=[0,1,2,3,4,5,6,7]
  else:
    if level!="a":
      print("your choice is invailid")

  while remaining_lives>0:
    available_letters=get_avilable_letters(letters_guessed)
    print("available letters:",available_letters)
    guess=input("please guess a letter: ")
    letter=guess.lower()
    if letter=="hint":
      print("your hint for the secreat word is ",get_hint(secreat_word,letters_guessed))
    elif (not ifvailid(letter)):

      print("invailid")
    if letter in secreat_word:
      letters_guessed.append(letter)
      print("Good guess: "+ get_gussed_word(secreat_word,letters_guessed))
      print(" ")
      if is_word_gussed(secraet_word,letters_guessed)==True:
        print("* * congratulation,you won! * *")
      print(" ")
    else:
      print("Oops! That letter is not in my word :"+ get_gussed_word(secreat_word,letter))
      letters_guessed.append(letter)
      print(IMAGES[image_selection[total_lives-remaining_lives]])
      remaining_lives-=1
      print("remaining_lives: "+str(remaining_lives))
      print(" ")
  else:
    print("sorry,you run out of guess,the word was"+str(secreat_word)+".")
secreat_word=choose_word()
hangman(secreat_word)








