class lib():

    def __init__(self,listOfBook):
        self.listOfBook=listOfBook

    def displayavailablebooks(self):

        print('List of Books :')
        for i in self.listOfBook:
            print(i)

    def LendABook(self, requestedBook):
        if requestedBook in self.listOfBook:
            print('You have borrowed the book:', requestedBook)
            self.listOfBook.remove(requestedBook)
            print('Remaining books are :')
            for i in self.listOfBook:
                print(i)
        else:
            print('Sorry {} is not available'.format(requestedBook))

    def returnABook(self, returnedBook):
        self.listOfBook.append(returnedBook)
        print('You have returned the book, Thank you !')
        print('Remaining books are :')
        for i in self.listOfBook:
            print(i)

    
class customer():
    def requestBook(self):
        print('Enter the name of the book you want to lend :')
        self.book = input()
        return self.book

    def returnBook(self):
        print('name of the you want to return')
        self.book= input()
        return self.book

LIB= lib(['A', 'B', 'C', 'D'])
cust = customer()
while True:
    print('Welcome to your Lib, please find the menu below')
    print('enter 1 to display available books')
    print('enter 2 to lend a book')
    print('enter 3 to return a book')
    print('enter 4 to exit')
    #LIB.displayavailablebooks()
    user_choice = int(input())
    if user_choice is 1:
        LIB.displayavailablebooks()
    elif user_choice is 2:
        requestedbook= cust.requestBook()
        LIB.LendABook(requestedbook)
    elif user_choice is 3:
        returnbook=cust.returnBook()
        LIB.returnABook(returnbook)
    elif user_choice is 4:
        print('Thank you for visiting ! Lib is closed ! Please provide your feedback Below')
        a=input()
        print('''Thanks for the feedback({}), We will serve you better'''.format(a))
        quit()
