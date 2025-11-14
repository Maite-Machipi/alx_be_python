#mad_libs_story.py
#A fun Mad libs story generator with conditional twists

#Prompt the user for words
noun = input("Enter a noun: ")
verb = input("Enter a verb: ")
adjective = input("Enter an adjective: ")
place = input("Enter a place: ")
animal = input("Enter your favourite animal: ")

#Build the basic stpry template
story = f"\nOnce upon a time, in {place}, there was a very {adjective} {animal}."
story += f"It loved to {verb} all day long, especially near the {noun}."

#Add a conditional twist
if adjective.lower() in ["brave","strong", "fearless"]:
        story += f" Everyone admired the {animal} for its courage and determination."
elif adjective.lower() in ["lazy", "sleepy", "tired"]:
        story += f" Most days, the {animal} preferred to nap instead of doing anything exciting."
else:
        story += f" The {animal} was known for its unique personality, no one quite like it in {place}!"

#Display the final story
print("\n Your Mad Libs Story")
print(story)
