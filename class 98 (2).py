introString="my name is willy,i am 14 years old" 
words=introString.split(',')
print(words)

def greet(name):
    print("hello " + name + ". how are you?" )

def countWordsFromFile():
    fileName=input("enter the file name: ")
    file=open(fileName,'r')
    for line in file:
        words=line.split()
        numberOfWords = numberOfWords + len(words)
        print("numberOfWords")
        
