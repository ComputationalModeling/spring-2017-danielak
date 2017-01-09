import nltk
import re # regular expressions for pattern matching
from nltk.corpus import webtext

# Load and inspect the first few elements of data
# You can view the movie script text at https://gist.github.com/briandk/61d60180accecff51807ffddf0c5f18e
pirates_of_the_caribbean = webtext.raw('pirates.txt').splitlines()
pirates_of_the_caribbean[:20]

# ## Does Pirates of the Caribbean: Dead Man's Chest pass the Bechdel Test?
# 
# ### Criteria
# 
# 1. Is there a scene with at least two women in it?
# 2. Are those women talking to each other?
# 3. Are they talking about something *other than* a man?
# 
# ## What's the distribution of speaking lines by gender

# Visualize this regular expression at https://www.debuggex.com/r/Gpqh5VW146QH4acn
dialogue_pattern = r"(?P<character_name>[A-Z,\s]+):\s*(?P<what_they_say>.*?$)"

dialogue_lines = [
    script_line
        for script_line 
        in pirates_of_the_caribbean
        if re.match(dialogue_pattern, script_line)
]

unique_characters = set([
        re.match(dialogue_pattern, line).groupdict()['character_name']
            for line
            in dialogue_lines
    ]
)

def create_dialogue_element(line_from_script, pattern):
    element = re.match(pattern, line_from_script).groupdict()
    return element

dialogue_elements = [
    create_dialogue_element(script_line, dialogue_pattern)
        for script_line
        in dialogue_lines
]


    