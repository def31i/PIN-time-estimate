import time 
import random


Focuskey_list = []
Focuskey_track = []
Focuskey_digits = [0,1,2,3,4,5,6,7,8,9]

#Time tracking block
Attempt_count = 0
Attempt_time = 0
Entry_time = None

#timing your entry
#also included error handling incase anything apart from a float is entered
while True:
    try:
        start_time = time.time()
        Delay = float(input("Enter your desired delay between attempts (in seconds)")) 
        Focuskey = input("Enter your password:")
        end_time = time.time()
        Entry_time = end_time - start_time
        break
    except ValueError:
        print("Only floats are supported please enter a float")

print("your entry time was", Entry_time, "seconds")
#Adds password into a list (as strings)
for item in Focuskey:
    Focuskey_list.append(item)

#Converting strings to ints using list comprehension
Focuskey_list = [int(i) for i in Focuskey_list]
  
#Checks password against random generations
while (Focuskey_list != Focuskey_track):
    Focuskey_track = random.sample(Focuskey_digits, len(Focuskey_list))
    time.sleep(Delay)  #You can adjust speed depending on your CPU power  
    Attempt_count +=1
    print(Focuskey_track)
    #Time_taken = Delay - Entry_time

    if Focuskey_track == Focuskey_list:
        print("Password found, it is:", Focuskey_track)
        break

Attempt_time = Attempt_count * Delay  #Total time taken for each attempt eg 24 attempts would be 24 * time delay in seconds 2 for eg = 24*2 = 48 seconds
print("Time it took to find:",Attempt_time, "seconds")    #entry time is not included in the time taken for attempts I keep them seperate
print("Attempt count:", Attempt_count)
input() #keeps command prompt open
