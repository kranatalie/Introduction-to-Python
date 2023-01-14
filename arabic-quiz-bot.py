# Greeting and start
print ("⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐")
print ()
print ("Hello and Marḥaba! Welcome to this short Arabic test. We want to check your knowledge about verbs!")
print ()
print ("⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐")
print ()
your_name = input ("First of all, please tell us: What's your name? ")
your_age = input ("How old are you? ")
print ("Great, nice to meet you, " + your_name + "! Now let's begin!")
success_message = ("That's correct!")

# Question 1
print ()
count = 0
answer_1 = input ("First question: What does كَبُرَ mean? ")
if answer_1 == "grow" or answer_1 == "to grow":
    count += 1
    print (success_message)
    
else:
    print ("Sorry, '" + answer_1 + "' is wrong. The correct answer is 'to grow'.")

# Question 2
print ()
answer_2 = input ("Second question: What does سَمِعَ mean? ")
if answer_2 == "hear" or answer_2 == "to hear" or answer_2 == "to listen" or answer_2 == "listen":
     count += 1
     print (success_message)
   
else:
    print ("Sorry, '" + answer_2 + "' is wrong. The correct answer is 'to hear' or 'to listen'.")

#Question 3
print ()
answer_3 = input ("Third question: What does ضَعُفَ mean? ")
if answer_3 == "weaken" or answer_3 == "to weaken" or answer_3 == "to become weak" or answer_3 == "become weak":
    count += 1
    print (success_message)
    
else:
    print ("Sorry, '" + answer_3 + "' is wrong. The correct answer is 'to weaken' or 'to become weak'")

# Question 4
print ()
answer_4 = input ("Fourth question: What does شَهِدَ mean? ")
if answer_4 == "testify" or answer_4 == "to testify" or answer_4 == "witness" or answer_4 == "to witness" or answer_4 == "see" or answer_4 == "to see":
    count += 1
    print (success_message)
    
else:
    print ("Sorry, '" + answer_4 + "' is wrong. The correct answer is 'to see', 'to witness' or 'to testify'.")

# Question 5
print ()
answer_5 = input ("Fifth question: What does ذَهَبَ mean? ")
if answer_5 == "to go" or answer_5 == "go" or answer_5 == "to walk" or answer_5 == "walk":
    count += 1
    print (success_message)
    
else:
    print ("Sorry, '" + answer_5 + "' is wrong. The correct answer is 'to go' or 'to walk'.")

# Counting the correct answers
print ()
print ("You have " + str(count) + " correct answer(s).")

# Goodbye and result
print ()
print ("Your answers were " + "1. " + answer_1 + ", 2. " + answer_2 + ", 3. " + answer_3 + ", 4. " + answer_4 + ", 5. " + answer_5 + ".")
if count > 3 and count != 5:
    print ("Good job!")
elif count < 3:
    print ("Don't give up. Keep learning and try again!")
elif count == 5:
    print ("Perfect! You did a great job! Well done.")
