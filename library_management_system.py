#Encapsulation is the process of hidng the details from the user.
#It is done to achieve abstraction.
"""
example: abstraction and encapsulation.
Problem: implement a lib management system which will handle the following task:
1.customer should be able to display all the books in the lib.
2.handle the process when a customer requests to borrow a book.
3.update the lib collection whne the customer returns a book.
"""

class Library:
    def __init__(self,listOfBooks):     #initializing the list of books as defined in the library object 
        self.availableBooks = listOfBooks
    
    def displayAvailableBooks(self):
        print('List of Available books:')
        for book in self.availableBooks:    #step1: print the list of books available using a for loop.
            print(book)

    def lendAbook(self, requestedBook):
        if requestedBook in self.availableBooks:
            print('You can borrow the book!')
            self.availableBooks.remove(requestedBook) #step3: if the book is borrowed by the customer, then that book is removed from the list of availableBooks 
        else:
            print('Sorry, the book is not available!')
    def addAbook(self, returnedBook):
        self.availableBooks.append(returnedBook)
        print('You have now returned the book. Thank You!') #step5: when the book has been returned it will be added to the list of availableBooks using the append() function
        

class Customer:
    def requestAbook(self):
        print('Enter the name of the book you want to borrow:')
        self.book = input()     #step2: this will take the 'book' from the displayAvailableBooks method of Library class
        return self.book

    def returnAbook(self):
        print('Enter the name of the book to be returned:')
        self.book = input()
        return self.book        #step4: this will ask the customer for the book he/she wants to return.


library = Library (['The Deliverance of The Evil', 'People and Places', 'Fastest Cars'])
customer = Customer()
while True:     #this menu has to be active until user presses the 4th key, hence an unlimited while loop, until quit() is called.
    #menu creation 
    print('1: Display Available Books')
    print('2: Borrow A Book')
    print('3: Return a Book')
    print('4: Exit')
    userChoice = int(input())
    if userChoice == 1:
       library.displayAvailableBooks()  #call the displayAvailableBooks method using the 'library' object
    elif userChoice == 2:
        requestedBook = customer.requestAbook() #create requestedBook and assign to requestAbook method to perform that function
        library.lendAbook(requestedBook)    #remove the book from requestedBook by calling it
    elif userChoice == 3:
        returnedBook = customer.returnAbook #create a returnedBook variable and assign it to the returnAbook  method
        library.addAbook(returnedBook) #add the book to the list by append() and calling the addAbook of library object
    elif userChoice == 4:
        quit()
                                          

                                
