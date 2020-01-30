print('\n#############################   regexs  ########################################\n')


import re



txt = '''Matches the empty strinring, but only at the start or end of a word.
        \B       Matches the empty string, but not at the start or end of a 
        strinring'''


print(re.findall(r'\S+(?:rin){2}\S+',txt))
#['strinring,', 'strinring']



var2 = """
Welcome 44 72
Welcome 22 72"""
search = re.search(r'Welcome (\d+) (\d+)',var2)
print(search.groups())
# ('44', '72')
print(search.groups(0))
# ('44', '72')
print(search.groups(1))
# ('44', '72')
print(search.group(0))
# 'Welcome 44 72'
print(search.group(1))
# '44'
print(search.group(2))
# '72'
print(re.findall(r'Welcome (\d+) (\d+)',var2))
# [('44', '72'), ('22', '72')]



print('\n#############################   regexs True example  ########################################\n')

f = open('Training/ShowInterface')
read = f.read()
f.close()


pattern = """(.+) is .+, line protocol is (\S+)"""



print('\n###########      Find the first match   ########### ')
find = re.search(pattern, read)

print('##  find.group()  ########### ',end=' ')
print(find.group())
print('##  find.groups() ########### ',end=' ')
print(find.groups())


print('\nFind all that match ')

findall = re.findall(pattern,read)

#print(findall)








#print(help(re))
'''
    The special characters are:
        "."      Matches any character except a newline.
        "^"      Matches the start of the string.
        "$"      Matches the end of the string or just before the newline at
                 the end of the string.
        "*"      Matches 0 or more (greedy) repetitions of the preceding RE.
                 Greedy means that it will match as many repetitions as possible.
        "+"      Matches 1 or more (greedy) repetitions of the preceding RE.
        "?"      Matches 0 or 1 (greedy) of the preceding RE.
        {m,n}    Matches from m to n repetitions of the preceding RE.
        {m,n}?   Causes the resulting RE to match from m to n repetitions of the preceding RE, attempting to match as few repetitions as possible. This is the non-greedy version of the previous qualifier. For example, on the 6-character string 'aaaaaa', a{3,5} will match 5 'a' characters, while a{3,5}? will only match 3 characters.
        "\\"     Either escapes special characters or signals a special sequence.
        []       Indicates a set of characters.
                 A "^" as the first character indicates a complementing set.
        "|"      A|B, creates an RE that will match either A or B.
        (...)    Matches the RE inside the parentheses.
                 The contents can be retrieved or matched later in the string.
        (?iLmsux) Set the I, L, M, S, U, or X flag for the RE (see below).
        (?:...)  Non-grouping version of regular parentheses.
        (?P<name>...) The substring matched by the group is accessible by name.
        (?P=name)     Matches the text matched earlier by the group named name.
        (?#...)  A comment; ignored.
        (?=...)  Matches if ... matches next, but doesn't consume the string.
        (?!...)  Matches if ... doesn't match next.
        (?<=...) Matches if preceded by ... (must be fixed length).
        (?<!...) Matches if not preceded by ... (must be fixed length).
        (?(id/name)yes|no) Matches yes pattern if the group with id/name matched,
                           the (optional) no pattern otherwise.
    
    The special sequences consist of "\\" and a character from the list
    below.  If the ordinary character is not on the list, then the
    resulting RE will match the second character.
        \number  Matches the contents of the group of the same number.
        \A       Matches only at the start of the string.
        \Z       Matches only at the end of the string.
        \b       Matches the empty string, but only at the start or end of a word.
        \B       Matches the empty string, but not at the start or end of a word.
        \d       Matches any decimal digit; equivalent to the set [0-9].
        \D       Matches any non-digit character; equivalent to the set [^0-9].
        \s       Matches any whitespace character; equivalent to [ \t\n\r\f\v].
        \S       Matches any non-whitespace character; equiv. to [^ \t\n\r\f\v].
        \w       Matches any alphanumeric character; equivalent to [a-zA-Z0-9_].
                 With LOCALE, it will match the set [0-9_] plus characters defined
                 as letters for the current locale.
        \W       Matches the complement of \w.
        \\       Matches a literal backslash.
    
    This module exports the following functions:
        match    Match a regular expression pattern to the beginning of a string.
        search   Search a string for the presence of a pattern.
        sub      Substitute occurrences of a pattern found in a string.
        subn     Same as sub, but also return the number of substitutions made.
        split    Split a string by the occurrences of a pattern.
        findall  Find all occurrences of a pattern in a string.
        finditer Return an iterator yielding a match object for each match.
        compile  Compile a pattern into a RegexObject.
        purge    Clear the regular expression cache.
        escape   Backslash all non-alphanumerics in a string.
    
    Some of the functions in this module takes flags as optional parameters:
        I  IGNORECASE  Perform case-insensitive matching.
        L  LOCALE      Make \w, \W, \b, \B, dependent on the current locale.
        M  MULTILINE   "^" matches the beginning of lines (after a newline)
                       as well as the string.
                       "$" matches the end of lines (before a newline) as well
                       as the end of the string.
        S  DOTALL      "." matches any character at all, including the newline.
        X  VERBOSE     Ignore whitespace and comments for nicer looking RE's.
        U  UNICODE     Make \w, \W, \b, \B, dependent on the Unicode locale.
'''


print('########################   fun fun fun ###################')

s = '''
1.0.0.0/30 is subnetted, 4 subnets
 C    1.1.1.0 is directly connected, FastEthernet0/1
 O    1.1.1.4 [110/2] via 1.1.1.2, 00:10:04, FastEthernet0/1
 O    1.1.1.8 [110/2] via 1.1.1.13, 00:10:04, FastEthernet0/0
 C    1.1.1.12 is directly connected, FastEthernet0/0
172.16.0.0/24 is subnetted, 4 subnets
 C    172.16.0.0 is directly connected, Ethernet0/0/0
 O    172.16.1.0 [110/11] via 1.1.1.2, 00:10:04, FastEthernet0/1
 O    172.16.2.0 [110/12] via 1.1.1.13, 00:09:24, FastEthernet0/0
                 [110/12] via 1.1.1.2, 00:09:24, FastEthernet0/1
 O    172.16.3.0 [110/11] via 1.1.1.13, 00:10:04, FastEthernet0/0
 '''

p = r'\d\S+.+(?:\n [COI ].+){1,100}'
test = re.findall(p,s)
#print(test)

for i in test:
    print([i])


print('\n\n\n##########################')
p = r'^\s*(\d\S+).+(?=\n [COI]    (\S+) .+){1,10}'

test = re.findall(p,s)
print(test)

for i in test:
    print('-----------------------------------------------------------')
    print(i)
    print(re.findall(r'(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}).+\b(\S*Ethernet.+)',i))

