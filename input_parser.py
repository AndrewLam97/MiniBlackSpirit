#Parses message.content
import boss_timer
import sanitizer

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
        return "Couldn't find boss, check spelling"
    if not result:
        return "No spawns left for today"
    else:
        return result


# def parse_enhancement_sim(inputstr):
#     sanitizedstr = sanitizer.sanitize(double)
#     check_for_validity_and_convert_to_double(sanitizedstr)

#     enhancer_module.enhancement_sim_function(doubleprobability) returns a success/failstring

#     return above string