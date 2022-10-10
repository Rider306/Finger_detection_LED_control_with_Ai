#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pyfirmata
import time

comport = "COM4"

board = pyfirmata.Arduino(comport) #I am using pyfirmata with the controller Arduino which is connected to my comport

time.sleep(1)

#for LEDs
led1 = board.get_pin(" d:13:o ") 
led2 = board.get_pin(" d:12:o ")
led3 = board.get_pin(" d:8:o ")
led4 = board.get_pin(" d:7:o ")
led5 = board.get_pin(" d:4:o ")

#Leds will glow according to number or fingers you show on screen. Limit is 5
def led(total):
    if total == 0:
        led1.write(0)
        led2.write(0)
        led3.write(0)
        led4.write(0)
        led5.write(0)
        
    elif total == 1:
        led1.write(1)
        led2.write(0)
        led3.write(0)
        led4.write(0)
        led5.write(0)
        
    elif total == 2:
        led1.write(1)
        led2.write(1)
        led3.write(0)
        led4.write(0)
        led5.write(0)
        
    elif total == 3:
        led1.write(1)
        led2.write(1)
        led3.write(1)
        led4.write(0)
        led5.write(0)
        
    elif total == 4:
        led1.write(1)
        led2.write(1)
        led3.write(1)
        led4.write(1)
        led5.write(0)
        
    elif total == 5:
        led1.write(1)
        led2.write(1)
        led3.write(1)
        led4.write(1)
        led5.write(1)


# In[3]:


#ek hi cell me kam karna he .py file banane k lie


# In[ ]:




