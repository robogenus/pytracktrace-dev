#!/usr/bin/python3

import subprocess
import sys
import time

dst = "google.com"     # 'dest' value either domain name or IP addr
maxHop = "20"            # 2 default for ttl hops
numTracks = 1
dstOptRq = "Use Default Destination? (def: google.com) y/n "
dstRq = "Enter a Domain Name or an IPv4 Address: "
maxHopOptRq = "Use Default TTL Hops? (Def. 20) y/n "
maxHopRq = "Enter a number for TTL Hops: "
numTrackRq = "Enter number of times to Track: "
exitRq = "\nExit TracerTrack? y/n: "
defRq = "Run Default? y/n: "
default = "y"
m_ExitID = 1
m_OptID = -1
m_DestID = 1


def getDest():
    ansDest = input(dstOptRq)
    destination = dst

    if ansDest == "y":
        return destination
    else:
        destination = input(dstRq)
        return destination

def getMaxHop():
    maxHopOpt = input(maxHopOptRq)
    ttl = maxHop
    if maxHopOpt == "y":
        return ttl
    else:
        ttl = input(maxHopRq)
        return ttl

def getNumTracks():
    numTracks = input(numTrackRq)
    return int(numTracks)

def getOptId():
    ansDef = input(defRq)

    if ansDef == "y":
        m_OptID = 1
    elif ansDef == "n":
        m_OptID = -1
    return m_OptID

def menuOpts():      # menu() get user input y or n
    ansExit = input(exitRq)
    m_ans = []
    m_OptID = 1    # to be later assigned to m_OptID at final use

    if ansExit == "y":
        m_ExitID = -1
        sys.exit(0)
    elif ansExit == "n":
        m_ExitID = 1
        m_OptID = getOptId()

    else:
        m_ExitID = -1
        print("Unkown Response! TracerTrack will exit now.")
        sys.exit(0)

    m_ans.append(m_ExitID)
    m_ans.append(m_OptID)
    return m_ans

def traceIt(bComm,tCnt):
    tc = str(tCnt)
    print("\n")
    start = "Start Time: %s" % time.ctime()
    print("Seq # " + tc + " :: " + start)
    output = subprocess.check_output(['bash','-c', bComm])
    print(output)
    print("End Time: %s" % time.ctime())

def runApp():

    dst = getDest()
    maxHop = getMaxHop()
    numTracks = getNumTracks()

    bashComm = "traceroute -m " + maxHop + " " + dst

    for i in range(numTracks):
        tc = i + 1
        traceIt(bashComm,tc)
        time.sleep(1)

while m_ExitID > -1:
    m_Ans = menuOpts()
    m_ExitID = m_Ans[0]
    m_OptID = m_Ans[1]
    print("\n")

    runApp()
