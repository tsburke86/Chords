# Chord generator
'''
        Adding a new chord
    1.) make a list of the intervals in the
        qualities used to generate chords section
    2.) make a letter map if need be
    3.) make a list for the user input to be compared to
        a.) make indecies 0 and 1 be the quality and the
            lettermap respectively
    4.) add the list from step 3 to qList
'''
def main():

    # Check pitches2 to make sure user input is valid
    pitches2 = ["C","C#","DB","D","D#","EB","E","FB","E#","F",
               'F#',"GB","G","G#","AB","A","A#","BB","B","B#","CB"]


    # These tuples represent the actual tones with enharmonic names.
    pitches = [("B#","C","DBB"),("B##","C#","DB"),("C##","D","EBB"),
               ("D#","EB","FBB"),("D##","E","FB",),("E#","F","GBB"),
               ("E##",'F#',"GB"),("G","F##","ABB"),("G#","AB"),
               ("G##","A","BBB"),("A#","BB","CBB"),("A##","B","CB")]

    # Quality maps used to generate a chord, the numbers are half steps
    # from the root.  This will generate the picthes but not the letters
    major = [0,4,7,11]
    minor = [0,3,7,10]
    dom = [0,4,7,10]
    dim = [0,3,6,10]
    sus = [0,5,7,0]

    # Modes interval maps
    ionian = [0,2,4,5,7,9,11]
    dorian = [0,2,3,5,7,9,10]
    phrygian = [0,1,3,5,7,8,10]
    lydian = [0,2,4,6,7,9,11]
    mixolydian = [0,2,4,5,7,9,10]
    aeolean = [0,2,3,5,7,8,10]
    locrian = [0,1,3,5,6,8,10]

    # Letter maps used to tell the computer which letters to use.
    # reLetter is just 1,3,5,7.  susLetter is 1,4,5,1.  The numbers
    # in the list refer to indices of the notes list below
    susLetter = [0,3,4,0]
    regLetter = [0,2,4,6]
    modLetter = [0,1,2,3,4,5,6,7]
    
    # notes list is used to generate the letter names with the letter map.
    #         0   1   2   3   4   5   6
    notes = ["C","D","E","F","G","A","B"]


    # Lists for chord qualities, includes quality list, and letter map as 0,1
    # Enter all strings as CAPS so the computer can search them
    majList = [major,regLetter,'MAJ', 'MAJOR', 'MAJ7', 'MAJOR7']
    minList = [minor,regLetter,'MIN', 'MINOR','MIN7','MINOR7']
    domList = [dom,regLetter,'DOM','7']
    dimList = [dim,regLetter,'DIM','DIMINISHED','DIM7']
    susList = [sus,susLetter, 'SUS','SUS4']

    # Modes
    ionList = [ionian, modLetter, 'IONIAN', 'ION']
    dorList = [dorian, modLetter, "DORIAN", "DOR"]
    phrList = [phrygian, modLetter, 'PHRYGIAN', 'PHR']
    lydList = [lydian, modLetter, 'LYDIAN', 'LYD']
    mixList = [mixolydian, modLetter, 'MIXOLYDIAN', 'MIX']
    aeoList = [aeolean, modLetter, 'AEOLEAN', 'AEO']
    locList = [locrian, modLetter, 'LOCRIAN', 'LOC']
    
    # qList is used to querey the quality lists for possible matches
    # as well as assign qualities and letter maps
    qList = [majList, minList, domList, dimList, susList, ionList,
             dorList, phrList, lydList, mixList, aeoList, locList]

    # Generate chord from pitches with quality
    # tonic is the index of the pitches list, quality is a list
    def generateChord(tonic, quality, chordNumbers):
        for i in range(0, len(quality)):
            if tonic + quality[i] > 11:
                chordNumbers.append(tonic + quality[i] - 12)
            else:
                chordNumbers.append(tonic + quality[i])
                

    # Convert chord nubmers to letters with accidentals
    def convertChord(chordNumbers, chordLetters, pitches, chord):
        for i in range(0, len(chordNumbers)):
            v = accidental(chordLetters[i],pitches[chordNumbers[i]])
            chord.append(v)

    # Get base note index out of the pitches list via note name ("C").
    # Use this to calculate other notes of the chord.
    def findNote(note):
        for i in range(0,len(pitches)):
            if note in pitches[i]:
                return i

    # Take in a note as a letter and generate the chord letters
    # append to chordLetters list. Also takes in the userinput quality
    # and chooses the correct lettermap to use
    def getChordLetters(letterNote, chordLetters, quality):
        note = notes.index(letterNote[0])
        for i in range(0,len(qList)):
            if quality in qList[i]:
                letterMap = qList[i][1]
        for i in letterMap:
            if note+i > 6:
                chordLetters.append(notes[note+i-7])
            else:
                chordLetters.append(notes[note+i])
            
    # Takes in a note that may have an accidental and checks the
    # corresponding tuple if it should be # or b
    def accidental(note, tpl):
        if note in tpl:
            return note
        elif note+"B" in tpl:
            return note+"b"
        elif note+"BB" in tpl:
            return note+"bb"
        elif note+"#" in tpl:
            return note+"#"
        elif note+"##" in tpl:
            return note+"##"
        else:
            return "opps"
        
    # Print the chord
    def printChord(chord):
        for i in chord:
            print(i, end=' ')
        print()
        
    # Set quality variable to the actual list of intervals needed
    # takes in approved user input and selects the quality map
    def setQualityMap(entry):
        for i in range(0,len(qList)):
            if entry[1] in qList[i]:
                return qList[i][0]
            
    # User Entry functions

    # Verify the chord before generating it
    def checkChord(entry):
        lst = entry.split()
        if len(lst) != 2:
            return "Invalid input, needs root and quailty separated by a space"
        note = lst[0].upper()
        if note not in pitches2:
            return "Invalid root"  
        quality = lst[1].upper()
        for i in qList:
            if quality in i:
                return [note,quality]
        return "Invalid chord quality or mode"

    # Accept user input and verify it
    def enterChord():
        chord = str()
        while type(chord) == str:
            userInput = input("\nEnter the chord or q to quit: ")
            if userInput == 'q':
                return userInput
            chord = checkChord(userInput)
            if type(chord) == str:
                print(chord)
        return chord

    # Header and usage
    def intro():
        print(" ############################")
        print(" # Chord And Mode Generator #")
        print(" ############################")      
        print()
        print("Enter the chord/scale with the ROOT and QUALITY/MODE\nseparated by a space: c maj7")
        print("Recognizes major, minor, dom, sus, (half) dim 7th chords and all modes")
        print("Examples: C min7 | f# dom | bb dim7 | E 7 | g sus ||  c dorian | b mix")
        print()
    # Run the program                 
    def run():
        intro()
        while True:
            chordLetters = []
            chordNumbers = []
            chordPrint = []
            chord = enterChord()
            if chord == 'q':
                print("Quitting")
                break
            note = chord[0]
            quality = chord[1]
            qualityMap = setQualityMap(chord)
            getChordLetters(note, chordLetters, quality)
            tonic = findNote(note)
            generateChord(tonic, qualityMap, chordNumbers)
            convertChord(chordNumbers, chordLetters, pitches, chordPrint)
            print()
            printChord(chordPrint)
            print()
    run()
main()
