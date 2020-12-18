# Chord generator quiz
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

    # Letter maps used to tell the computer which letters to use.
    # reLetter is just 1,3,5,7.  susLetter is 1,4,5,1.  The numbers
    # in the list refer to indices of the notes list below
    susLetter = [0,3,4,0]
    regLetter = [0,2,4,6]

    # notes list is used to generate the letter names with the letter map.
    #         0   1   2   3   4   5   6
    notes = ["C","D","E","F","G","A","B"]


    # Lists for chord qualities, includes quality list, and letter map as 0,1
    # Enter all strings as CAPS so the computer can search them
    majList = [major,regLetter,'MAJ', 'MAJOR', 'MAJ7', 'MAJOR7']
    minList = [minor,regLetter,'MIN', 'MINOR','MIN7','MINOR7']
    domList = [dom,regLetter,'DOM','7',"DOM7"]
    dimList = [dim,regLetter,'DIM','DIMINISHED',"DIM7"]
    susList = [sus,susLetter, 'SUS','SUS4']

    # qList is used to querey the quality lists for possible matches
    # as well as assign qualities and letter maps
    qList = [majList, minList, domList, dimList, susList]

    # qualityList has a list of recognizable quality names to generate
    # chords for a quiz
    qualityList = ['maj7','min7','dom7','dim7','sus']
    majMinDom = ['maj7','min7','7']
    # create quizList
    def generateQuiz(notes, qualities):
        from random import shuffle
        quizList = []
        for i in notes:
            for j in qualities:
                quizList.append(i+' '+j)
        shuffle(quizList)
        return quizList
                
    # Generate chord from pitches with quality
    # tonic is the index of the pitches list, quality is a list
    def generateChord(tonic, qualityMap, chordNumbers):
        for i in range(0, len(qualityMap)):
            if tonic + qualityMap[i] > 11:
                chordNumbers.append(tonic + qualityMap[i] - 12)
            else:
                chordNumbers.append(tonic + qualityMap[i])
                

    # Convert chord nubmers to letters with accidentals
    def convertChord(chordNumbers, chordLetters, pitches, chord):
        for i in range(0, len(chordNumbers)):
            v = accidental(chordLetters[i],pitches[chordNumbers[i]])
            chord.append(v)
        return chord

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
    # corresponding tuple for the accidental on that letter
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
    #def printChordName(chord):
        


        
    # Set quality variable to the actual list of intervals needed
    # takes in approved user input as list and selects the quality map
    def setQualityMap(entry):
        for i in range(0,len(qList)):
            if entry in qList[i]:
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
        return "Invalid chord quality"

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

    #       Quiz Stats


    # Quiz header
    def quizHeader(quizList, chord, quality):
        print("\t###################")
        print("Chord:", chord[0], quality, end='\t')
        print("Remaining Chords:",len(quizList))
        
        
        
        

    # Header and usage
    def intro():
        print(" ########################")
        print(" # Chord Tone Generator #")
        print(" ########################")      
        print()
        print("Enter the chord with the ROOT and QUALITY separated by a space: c maj7")
        print("Recognizes major, minor, dom, (half) dim 7th chords")
        print("Examples: C min7 | f# dom | BB dim7 | e 7")
        print()
    # Quiz Header
    def quizIntro():
        print(" ########################")
        print(" #  Chord Tone Trainer  #")
        print(" ########################")      
        print()

    # Quiz selector
    def quizSelector():
        answer = ''
        quizList = ''
        while True:
            print("1.) All notes: major")
            print("2.) All notes:  minor")
            print("3.) All notes: 7")
            print("4.) All notes: half dim")
            print("5.) All notes : sus")
            print("6.) Natural notes: maj, min, 7, half dim")
            print("7.) The Buck Nasty")
            print()
            while quizList == '':
                if answer == '':
                    answer = input("Select the quiz by the number: ")
                if answer == '1':
                    quizList = generateQuiz(pitches2, ['maj'])
                elif answer == '2':
                    quizList = generateQuiz(pitches2, ['min'])
                elif answer == '3':
                    quizList = generateQuiz(pitches2, ['7'])
                elif answer == '4':
                    quizList = generateQuiz(pitches2, ['dim'])
                elif answer == '5':
                    quizList = generateQuiz(pitches2, ['sus'])
                elif answer == '6':
                    quizList = generateQuiz(notes, ['maj','min','dim','7'])
                elif answer == '7':
                    quizList = generateQuiz(pitches2, qualityList)
                else:
                    answer = input("\nInvalid selection, enter the number: ")
                    continue
            print("\nBeginning Quiz...\n")
            return quizList
        
    # Run the program                 
    def run():
        quizIntro()
        exit = False
        while True:
            quizList = quizSelector() 
            while True:
                chordLetters = []
                chordNumbers = []
                chordPrint = []
                if len(quizList) == 0:
                    break
                chord = quizList.pop()
                chord = chord.split()
                note = chord[0]
                quality = chord[1].upper()
                qualityMap = setQualityMap(quality)
                getChordLetters(note, chordLetters, quality)
                tonic = findNote(note)
                generateChord(tonic, qualityMap, chordNumbers)
                chord = convertChord(chordNumbers, chordLetters, pitches, chordPrint)
                print()
                print("Press enter to reveal or type anything to quit")
                quizHeader(quizList, chord, quality.capitalize())
                quitting = input()
                printChord(chordPrint)
                input()
                if quitting != '':
                    break
            if exit == True:
                break
            else:
                print("Done with quiz")
                answer = input("Go again? y/n: ")
                if answer != 'y' and answer != '':
                    break
        print("Quitting")
                    
    run()
main()

