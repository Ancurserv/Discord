import datetime
import time
# Alarm Clock "Bot" Example - This is simply just a unit code test for an alarm clock functionality so all you need to do is setup a Discord Bot and implement this code within it but of course replace the input function with the discord.py function that would be use to extract a message you should also insert it within a while loop or else it will only extract 1 message and end. 

# The usage of the time and datetime module here will only work if you are running the bot from your device and not from a cloud server because by default the device is registered to your area timezone however for a cloud server you would need to manually set a specific time zone
x = input("Insert command: ")
y = x.split()
if y[0] == "!remind":
    while True:
        z = datetime.datetime.now()
        w = z.strftime("%I:%M%p")
        if w == y[-1]:
            output = ''.join(y[1:-1])
            print(output)
            time.sleep(60)   
        else:
            continue

