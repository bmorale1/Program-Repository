//: # Midterm Playground Spring 2017


var studentName = "Isaac Morales"

/*:
 ## Author Class
 (10 pts.)
 > Create a class named Author. It should have first name and last name as well as date of birth.
 */

class Author {
	var firstName: String 
	var lastName: String 
	var DOB: String 
	convenience init(){
		self.init(newFirstN: "no", newLastN: " name", newDOB: " void")
	}
	init(newFirstN: String, newLastN: String, newDOB: String){
		firstName = newFirstN
		lastName = newLastN
		DOB = newDOB
	}
    
}

/*:
 ## Book Class
 (30 pts.)
 > Create a class named Book. It should have instance variables for Title, Author, Publisher and number of pages. It shoud have a description method that returns a string containing the title, author, publisher and number of pages. Think of the appropriate data types for each variable.
 */

class Book {
    var title:String 
	var author:String
	var publisher:String 
	var pages:Int 
	convenience init(){
		self.init(newTitle: "none", newAuthor: "no name", newPublisher: "none", newPages: 0)
	}
	init(newTitle: String, newAuthor: String, newPublisher: String, newPages: Int){
		title = newTitle
		author = newAuthor
		publisher = newPublisher
		pages = newPages
	}
	func description() -> (String, String, String, String){
		return (title,  author , publisher , pages as! String)
	}
}

/*:
 ## Shelf Class
 (45 pts.)
 > Create a class named Shelf. It should hold a series of objects of type Book. It should be able to hold a name for the shelf. The class should implement the following methods:
 
 > `init()` // convenience initializer that sets the name to "No Name"
 > `init(name: String)` // designated initializer
 > `func shelve(book: Book)` //put a book in the shelf
 > `func numberOfBooks() -> Int` //returns the number of books in the shelf
 > `func titles() -> [String]` //returns the titles of the books in the shelf
 > `func authors() -> [String]` //returns the authors' names of all the books in the shelf
 > `func totalPages() -> Int` // returns with the sum of all the pages in the books in the shelf
 > `func description() -> String` //returns a String with the name of the shelf and the titles of the books in the shelf separated by carriage returns (\n)
 */

class Shelf {
	var shelfName: String
	var books = [Book]()    
	 convenience init(){
		self.init(name:"no name")
	}
	init(name:String){
		shelfName = name
	}
	func shelve(book: Book){
		books.append(book)
	}
	func numberOfBooks() -> Int{
		return books.count
	}
	func titles() -> [String]{
		var i: Int = 0
		var bookTitles = [String]()
		for i in books {
			bookTitles.append(books[i].title)
		}
		return bookTitles
	}
	func authors() -> [String]{
		var i: Int = 0
		var bookAuthors = [String]()
		for i in books{
			bookAuthors.append(books[i].author)
		}
		return bookAuthors
	}
	func totalPages() -> Int{
		var total: Int = 0
		var i: Int = 0
		for i in books{
			print("adding books page numbers")
			total += books[i].pages
		}
		return total
	}
	func description() -> String{
		return shelfName , titles() 
	}
}

/*:
 ## Create a function to create a filled shelf as follows:
 (15 pts.)
 > `defaultFilledShelf() -> Shelf` // returns a shelf with some books in it
 
 */

func defaultFilledShelf() -> Shelf {
    return Shelf()
}

/*:
 ## Bonus
 (5 pts.)
 > Draw the UML Class Diagram for the system on a piece of paper. Put your name on it.
 
 (15 pts.)
 > Create the following method in the Shelf class
 
 > `func remove(title: String) -> Book` // removes a book from the shelf given the title of the book
 */

