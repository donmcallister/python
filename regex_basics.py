Basics¶
Let's see how this scheme works for the simplest case, in which the pattern is an exact substring.

pattern = 'fox'
pattern_matcher = re.compile (pattern)

input = 'The quick brown fox jumps over the lazy dog'
matches = pattern_matcher.search (input)



# you can also skip creating the pattern object and just call the module-level search function, re.search().

matches_2 = re.search ('jump', input)
print ("Found", matches_2.group (), "@", matches_2.span ())
Found jump @ (20, 24)


# Other Search Methods

# match() - Determine if the RE matches at the beginning of the string.
# search() - Scan through a string, looking for any location where this RE matches.
# findall() - Find all substrings where the RE matches, and returns them as a list.
# finditer() - Find all substrings where the RE matches, and returns them as an iterator.


# Creating pattern groups

# Make the above more readable with a re.VERBOSE pattern
re_names2 = re.compile ('''^              # Beginning of string
                           ([a-zA-Z]+)    # First name
                           \s             # At least one space
                           ([a-zA-Z]+\s)? # Optional middle name
                           ([a-zA-Z]+)    # Last name
                           $              # End of string
                        ''',
                        re.VERBOSE)
print (re_names2.match ('Rich Vuduc').groups ())
print (re_names2.match ('Rich S Vuduc').groups ())
print (re_names2.match ('Rich Salamander Vuduc').groups ())
('Rich', None, 'Vuduc')
('Rich', 'S ', 'Vuduc')
('Rich', 'Salamander ', 'Vuduc')

# Tagging pattern groups

# Named groups
re_names3 = re.compile ('''^
                           (?P<first>[a-zA-Z]+)
                           \s
                           (?P<middle>[a-zA-Z]+\s)?
                           \s*
                           (?P<last>[a-zA-Z]+)
                           $
                        ''',
                        re.VERBOSE)
print (re_names3.match ('Rich Vuduc').group ('first'))
print (re_names3.match ('Rich S Vuduc').group ('middle'))
print (re_names3.match ('Rich Salamander Vuduc').group ('last'))
# Rich
# S 
# Vuduc
