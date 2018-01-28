#author:    Isaac Morales
#File Name: Brandon_morales_lab24.py
#purpose:   practicing with files
#date:      November 12, 2015

#section1
f=open('lab24.txt','r')
f.close()
#i-nothing happened
#ii- we just opened the file, didn't do anything to it.
#iii-my python file and my txt file
f=open('lab24.txt','w')
print(f)
f.close()
#i-a message describing the file was printed
#ii-no
#iii- i am supposing that printing the file just prints its description
#iv-same as before.

#section2
f=open('lab24.txt','w')
f.write('Using files is fun!')
f.close()

#i-the text in my file was overwritten with 'using file is fun!'
#ii-i expected it to be added to the end of the file.
#iii- its meant to over write what text is in the file.
#iv-the over written text file.

#section3
with open('lab24.txt','r') as f:
    data = f.read(5)
    print(data)
f.close()

#i-it gave me an unexpected EOF while parsing error
#ii-no
#iii-it did not work.

#i-it printed the content of the txt file.
#ii-i am just surprised that something worked
#iii-'using files is fun!'

#i-it only read the first 5 characters of the file.
#ii-sure why not
#iii-using

#section4
def readMyFile(x):
    with open(x,'r') as f:
        for i in f :
            print(i)

#section5
def main():
    response=''
    while response!='Done':
        file=input('please enter a file name:')
        readMyFile(file)
        response=input('are you done?(Done to exit, anything else to continue)')
        
main()
