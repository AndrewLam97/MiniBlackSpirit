import random

#Returns Success of Random Roll as a String
def enhancement_sim(inputnum):
    random.seed()
    roll_num = random.random()*100
    if roll_num <= inputnum:
        return "{:.2f} was rolled. Enchantment Success!".format(roll_num)
    else:
        return "{:.2f} was rolled. Enchantment Failed. Better luck next time.".format(roll_num)

