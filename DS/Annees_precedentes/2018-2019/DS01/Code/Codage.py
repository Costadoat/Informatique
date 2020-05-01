# -*- coding: utf-8 -*-
"""
Created on Tue Oct 06 23:52:57 2015

@author: Renaud
"""

def codage(mot):
    motcode=""
    li = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '&']
    for i in range(0,len(mot)):
        if mot[i] == ' ':       
            newlettre = mot[i]
        else: 
            p=li.index(mot[i])
            newlettre =  li[p+1]
        motcode = motcode[:i] + newlettre
    return motcode

def decodage(mot):
    motdecode=""
    li = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '&']
    for i in range(0,len(mot)):
        if mot[i] == ' ':       
            newlettre = mot[i]
        else: 
            p=li.index(mot[i])
            newlettre =  li[p-1]
        motdecode = motdecode[:i] + newlettre
    return motdecode

message="bonjour les ptsi de dorian"
message="venez tous a dorian"
print "MESSAGE ORIGINAL: %s" % message
messagecode=codage(message)
print "MESSAGE CODE: %s" % messagecode
messagedecode=decodage(messagecode)
print "MESSAGE DECODE: %s" % messagedecode