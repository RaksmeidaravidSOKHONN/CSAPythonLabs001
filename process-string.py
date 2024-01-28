# Application 1
# Given a string, you have to return a string in which each character (case-sensitive) is repeated once.

# Examples (Input -> Output):
# * "String"      -> "SSttrriinngg"
# * "Hello World" -> "HHeelllloo  WWoorrlldd"
# * "1234!_ "     -> "11223344!!__  "

#Code
user_input = input("Enter the words: ")
user_input1 = list(user_input)
user_input2 = list(user_input)

user_input1_2 = [None]*(len(user_input1)+len(user_input2))
user_input1_2[::2] = user_input1
user_input1_2[1::2] = user_input2

user_str = ''. join(user_input1_2)
print(user_str)

# Application 2
#  Given a string indicating a range of letters, return a string which includes all the letters in that range, including the last letter. Note that if the range is given in capital letters, return the string in capitals also!

# Examples
# "a-z" ➞ "abcdefghijklmnopqrstuvwxyz"
# "h-o" ➞ "hijklmno"
# "Q-Z" ➞ "QRSTUVWXYZ"
# "J-J" ➞ "J"
# Notes A hyphen will separate the two letters in the string.

#Code
alphabet = "abcdefghijklmnopqrstuvwxyz"
upper_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
Com_al_up = alphabet + upper_alphabet

user_input = input("Enter a range of letters (e.g. a-z): ")
user_split = user_input.split("-")
first_letter = user_split[0]
second_letter = user_split[1]

first_index = Com_al_up.index(first_letter)
second_index = Com_al_up.index(second_letter)
result = Com_al_up[first_index: second_index +1]
print(result)
