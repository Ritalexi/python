#!/usr/bin/python3
def multiple_returns(sentence):
    if(not sentence):
        return 0, "None"
    for i in range(len(sentence)):
        return len(sentence), sentence[i]
