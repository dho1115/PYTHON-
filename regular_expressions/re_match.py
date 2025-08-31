import re;

string = "The date this was created was 8-30-2025.";
string2 = "blah blah blah *"

match1 = re.match("...", string); # matches the first 3 characters. Returns 'The'
group_match1 = match1.group(0);
print(dict(group_match1=group_match1));

match2 = re.match(".*", string); # * is a wildcard. .* returns the entire string.
group_match2 = match2.group(0);
print(dict(group_match2=group_match2));

match3 = re.match(".*?\d\d", string); # returns all the strings up to 30. ? means, do not be greedy.
group_match3 = match3.group(0);
print(dict(group_match3=group_match3));

match4 = re.match(".*\*", string2) # returns up to *. Notice, the escape character.
group_match4 = match4.group(0);
print(dict(group_match4=group_match4));