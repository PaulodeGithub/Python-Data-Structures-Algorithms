def group_anagrams(strings):
    # create an empty hash table
    anagram_groups = {}
 
    # iterate through each string in the array
    for string in strings:
        # sort each string to get its canonical form
        # sorted('eat') returns ['a', 'e', 't']
        # ''.join(['a', 'e', 't']) coverts the array of chars to 'aet' string
        canonical = ''.join(sorted(string))
 
        # check to see if the canonical form of the string exists in the hash table
        if canonical in anagram_groups:
            # if it does then add the string there
            anagram_groups[canonical].append(string)
        else:
            # otherwise create new canonical form and add the string there
            anagram_groups[canonical] = [string]
 
    # convert the hash table to a list of lists
    return list(anagram_groups.values())