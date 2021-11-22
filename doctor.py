"""
Program: doctor.py
Author: Peter Rand 11/3/2021
Conducts an interactive session of nondirective psychotherapy.
"""

import random

# Global variables (data pool)
hedges = ("Please tell me more.", "Many of my patients tell me the same thing.", "Please continue.", "Go on, go on...", "You don't say...")

qualifiers = ("Why do you say that ", "You seem to think that ", "Can you explain why ")

replacements = {"I":"you", "me":"you", "my":"your", "we":"you", "us":"you", "mine":"yours"}

# definition of the reply() function
def reply(sentence):
	"""Builds and returns a reply to user input sentence."""
	probability = random.randint(1, 4)
	if probability == 1:
		return random.choice(hedges)
	else:
		return random.choice(qualifiers) + changePerson(sentence)

# definition of the changePerson() function
def changePerson(sentence):
	"""Replaces first-person pronouns with second-person pronouns."""
	# take the user input sentence data and split it into an array.
	words = sentence.split()
	# empty array to hold onto the modified words.
	replyWords = []
	# loop through the words array and decide if the word the loop is examining needs to be replaced.
	for word in words:
		replyWords.append(replacements.get(word, word))
	# now that replyWords array is complete, let's turn it back into a string so it can be returned
	return " ".join(replyWords)

# definition of the main() function for the program entry
def main():
	"""Handles the interaction between patient and doctor."""
	print("Good morning, I hope that you're well today.")
	print("What can I do for you?")
	# keep this ap running untill the user enters QUIT
	while True:
		sentence = input("Type a response or QUIT to exit >>")
		# check if the user typed QUIT, if so we exit the program.
		if sentence.upper() == "QUIT":
			print("Have a nice day!")
			break;
		# if we are here, the user must NOT have typed QUIT
		print(reply(sentence))	

# call to the main function for program execution
if __name__ == "__main__":
	main()