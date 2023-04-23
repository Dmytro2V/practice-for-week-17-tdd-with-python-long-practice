def parse(s):
    # if value == 'I': return 1
    # elif value == 'II': return 2
    # elif value == 'III': return 3
    # elif value == 'IV': return 4
    # elif value == 'V': return 5
    # elif value == 'VI': return 6
    # elif value == 'VII': return 7
    # elif value == 'VIII': return 8    
    special = {'IV': 4,}
    usual = {'I': 1, 'V': 5}
    res = 0
    i = 0
        
    while i < len(s):
        print(i)
        if s[i:i+2] in special:
            print ('---sp')
            res += special[s[i:i+2]]
            i += 2
        elif s[i] in usual:
            res += usual[s[i]]
            i += 1
        else:
            raise Exception('Symbol {s[i]} at {i} position is not Roman')
    return res



print(parse('IV'))

