"""
This is a program that converts strings to morse code and vice versa
"""



SPACE = ' '
EOL = '#'
EMPTYSTRING = ''

def ReportError(s):
  print('{0:<5}'.format('*'),s,'{0:>5}'.format('*')) 


def SendSignals(MorseCodeString):
  return_string = ""
  for i in str(MorseCodeString):
        if i == ".":
            return_string= return_string +  "= "
        elif i == "-":
            return_string= return_string + "=== "
        elif i == " ":
            return_string= return_string + " "
  return return_string




def StripLeadingSpaces(Transmission): 
  TransmissionLength = len(Transmission)
  if TransmissionLength > 0:
    FirstSignal = Transmission[0]
    while FirstSignal == SPACE and TransmissionLength > 0:
      TransmissionLength -= 1
      Transmission = Transmission[1:]
      if TransmissionLength > 0:
        FirstSignal = Transmission[0]
  if TransmissionLength == 0:
    ReportError("No signal received")
  return Transmission

def StripTrailingSpaces(Transmission): 
  LastChar = len(Transmission) - 1
  while Transmission[LastChar] == SPACE:
    LastChar -= 1
    Transmission = Transmission[:-1]
  return Transmission  

def GetTransmission():
  FileName = input("Enter file name: ")
  try:
    FileHandle = open(FileName, 'r')
    Transmission = FileHandle.readline()
    FileHandle.close()
    Transmission = StripLeadingSpaces(Transmission)
    if len(Transmission) > 0:
      Transmission = StripTrailingSpaces(Transmission)
      Transmission = Transmission + EOL
  except:
    ReportError("No transmission found")
    Transmission = EMPTYSTRING
  return Transmission

def GetNextSymbol(i, Transmission):
  if Transmission[i] == EOL:
    print()
    print("End of transmission")
    Symbol = EMPTYSTRING
  else:
    SymbolLength = 0
    Signal = Transmission[i]
    while Signal != SPACE and Signal != EOL:
      i += 1
      Signal = Transmission[i]
      SymbolLength += 1
    if SymbolLength == 1:
      Symbol = '.'
    elif SymbolLength == 3:
      Symbol = '-'
    elif SymbolLength == 0: 
      Symbol = SPACE
    else:
      ReportError("Non-standard symbol received") 
      Symbol = EMPTYSTRING
  return i, Symbol 

def GetNextLetter(i, Transmission):
  SymbolString = EMPTYSTRING
  LetterEnd = False
  while not LetterEnd:
    i, Symbol = GetNextSymbol(i, Transmission)
    if Symbol == SPACE:
      LetterEnd = True
      i += 4
    elif Transmission[i] == EOL:
      LetterEnd = True
    elif Transmission[i + 1] == SPACE and Transmission[i + 2] == SPACE:
      LetterEnd = True
      i += 3
    else:
      i += 1
    SymbolString = SymbolString + Symbol
  return i, SymbolString

def Decode(CodedLetter, Dash, Letter, Dot):
  CodedLetterLength = len(CodedLetter)
  Pointer = 0
  for i in range(CodedLetterLength):
    Symbol = CodedLetter[i]
    if Symbol == SPACE:
      return SPACE
    elif Symbol == '-':
      Pointer = Dash[Pointer]
    else:
      Pointer = Dot[Pointer]
  return Letter[Pointer]

def ReceiveMorseCode(Dash, Letter, Dot): 
  PlainText = EMPTYSTRING
  MorseCodeString = EMPTYSTRING
  Transmission = GetTransmission() 
  LastChar = len(Transmission) - 1
  i = 0
  while i < LastChar:
    i, CodedLetter = GetNextLetter(i, Transmission)
    MorseCodeString = MorseCodeString + SPACE + CodedLetter
    PlainTextLetter = Decode(CodedLetter, Dash, Letter, Dot)
    PlainText = PlainText + PlainTextLetter
  print(MorseCodeString)
  print(PlainText)

def SendMorseCode(Letter,MorseCode, first_key, second_key, third_key ):
    MorseCodeString = EMPTYSTRING
    PlainText = input("Enter your message (uppercase letters and spaces only): ")
    for i,PlainTextLetter in enumerate(PlainText):
        if PlainTextLetter != " " and  PlainTextLetter.isupper()==False:
            ReportError("Non-standard symbol received")
            break  # Break out of the loop
        else:
            if i%3 == 1:
              PlainTextLetter = Letter[((Letter.index(PlainTextLetter)+second_key)%len(Letter))]
            
            elif i%3 ==2:
              PlainTextLetter = Letter[((Letter.index(PlainTextLetter)+third_key)%len(Letter))]
            elif i%3 ==0:
              PlainTextLetter = Letter[((Letter.index(PlainTextLetter)+first_key)%len(Letter))]
              


            if PlainTextLetter == " ":
              Index = 0
            else:
                Index = ord(PlainTextLetter) - ord('A') + 1
            CodedLetter = MorseCode[Index]
            MorseCodeString = MorseCodeString + CodedLetter + SPACE

            print(PlainTextLetter)

    
    


    print(MorseCodeString)
    print(SendSignals(MorseCodeString))


def OutputAlphabetWithCode(Letter,MorseCode):
  
    print(f"""
            {Letter[1]} {MorseCode[1]}     {Letter[2]} {MorseCode[2]}    {Letter[3]} {MorseCode[3]}     {Letter[4]} {MorseCode[4]}
            {Letter[5]} {MorseCode[5]}      {Letter[6]} {MorseCode[6]}    {Letter[7]} {MorseCode[7]}      {Letter[8]} {MorseCode[8]}
            {Letter[9]} {MorseCode[9]}     {Letter[10]} {MorseCode[10]}    {Letter[11]} {MorseCode[11]}      {Letter[12]} {MorseCode[12]}
            {Letter[13]} {MorseCode[13]}     {Letter[14]} {MorseCode[14]}      {Letter[15]} {MorseCode[15]}      {Letter[16]} {MorseCode[16]}
            {Letter[17]} {MorseCode[17]}   {Letter[18]} {MorseCode[18]}     {Letter[19]} {MorseCode[19]}      {Letter[20]} {MorseCode[20]}
            {Letter[21]} {MorseCode[21]}    {Letter[22]} {MorseCode[22]}    {Letter[23]} {MorseCode[23]}      {Letter[24]} {MorseCode[24]}
            {Letter[25]} {MorseCode[25]}   {Letter[26]} {MorseCode[26]}"""
            )
          
  



def DisplayMenu():
  print()
  print("Main Menu")
  print("=========")
  print("A - Display Morse code")
  print("R - Receive Morse code")
  print("S - Send Morse code")
  print("X - Exit program")
  print()

def GetMenuOption():
  MenuOption = EMPTYSTRING
  while len(MenuOption) != 1:
    MenuOption = input("Enter your choice: ")
  return MenuOption



def SendReceiveMessages():
  Dash = [20,23,0,0,24,1,0,17,0,21,0,25,0,15,11,0,0,0,0,22,13,0,0,10,0,0,0]
  Dot = [5,18,0,0,2,9,0,26,0,19,0,3,0,7,4,0,0,0,12,8,14,6,0,16,0,0,0]
  Letter = [' ','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

  MorseCode = [' ','.-','-...','-.-.','-..','.','..-.','--.','....','..','.---','-.-','.-..','--','-.','---','.--.','--.-','.-.','...','-','..-','...-','.--','-..-','-.--','--..']

  ProgramEnd = False
  while not ProgramEnd:



    DisplayMenu() 
    MenuOption = GetMenuOption()
    if MenuOption == "A":
      OutputAlphabetWithCode(Letter,MorseCode)
    if MenuOption == 'R':
      ReceiveMorseCode(Dash, Letter, Dot)
    elif MenuOption == 'S':
      first_key = int(input("Input first key:") )
      second_key = int(input("Input second key:") )
      third_key = int(input("Input third key:"))
      SendMorseCode(Letter,MorseCode, first_key, second_key, third_key ) 
    elif MenuOption == 'X':
      ProgramEnd = True


if __name__ == "__main__":
   SendReceiveMessages()
