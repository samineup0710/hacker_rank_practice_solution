""" Consider the following:

A string, s, of length n  where .
An integer, k, where k is a factor of n.
We can split s into n/k subsegments where each subsegment,ti , consists of a contiguous block of  k characters s . Then, use each ti to create string ui such that:

The characters in ui  are a subsequence of the characters in ti .
Any repeat occurrence of a character is removed from the string such that each character in ui  occurs exactly once. In other words, if the character at some index  j in  ti occurs at a previous index  in  ui, then do not include the character in string .
Given  s and k, print  lines where each line i denotes string ui.

Input Format:
        The first line contains a single string denoting s.
        The second line contains an integer,k , denoting the length of each subsegment.
Output Format:

            Print  (n/k) lines where each line i contains string ui .

"""
def merge(string, k):
    for i in range(0,len(string), k):
        #slicingabba string upto k characters.
        line = string[i:i+k]
        sub_str_list = []
        for i in line:
            #only print if we haven't already seen these characters.
            if i not in sub_str_list:
                sub_str_list.append(i)
        print("".join(sub_str_list))

if __name__ == '__main__':
    string, k  = input(), int(input())
    merge(string, k)