#Parses message.content
import boss_timer
import sanitizer
import enhancer

#Handles $test and $next
def parse(inputstr):
    if inputstr == '$next':
        return boss_timer.till_next_boss()
    if inputstr == '$test':
        return "Test Successful"

#Handles $showme
def parse_showme(inputstr):
    sanitizedstr = sanitizer.sanitize(inputstr)

    result = boss_timer.showme(sanitizedstr)

    if not boss_timer.valid_boss(sanitizedstr):
        return "Couldn't find boss, check spelling."
    if not result:
        return "No spawns in the next 24 hours."
    else:
        return result

def parse_enhancement_sim(inputstr):
    sanitizedstr = sanitizer.sanitize(inputstr)
    try:
        sanitizedfloat = float(sanitizedstr)
    except:
        print("Error during string to float conversion")
        return "Please enter a valid number."

    return enhancer.enhancement_sim(sanitizedfloat)