//: # MineSweeper - Text based game


var studentname = "Isaac Morales"

class Cell {
    var nBombs = 0 // number of bombs in the cells around this cell
    var open = false // true indicates that the content of the cell is visible
    var bomb = false // true indicates that the cell has a bomb
    var neighbors = [Cell]() // we are not using this yet
    
    init() {
        
    }
    
    func getnBombs() -> Int {
        nBombs = 0
        for neighbor in neighbors {
            if neighbor.bomb {
                nBombs += 1
            }
        }
        return nBombs
    }
    
    // Assignment 3 - see at the bottom
    func description() -> String {
		if open == true{
			return "[_]"
		}
		else{
       	 return bomb ? "[X]" : (nBombs == 0 ? "[ ]" : "[" + nBombs.description + "]")
		}
    }
}

//: ## Main declarations

class Board {
    var width = 5
    var height = 7
    var board = [[Cell]]()
    
    init(newWidth: Int, newHeight: Int) {
        width = newWidth
        height = newHeight
        for row in 0..<width {
            let r = [Cell]()
            board.append(r)
            for column in 0..<height {
                let c = Cell()
                board[row].append(c)
            }
        }
        var bombsLeft = width * height/10
        while bombsLeft > 0 {
            let rPoint = Int(arc4random_uniform(UInt32(height)))
            let cPoint = Int(arc4random_uniform(UInt32(width)))
            if board[cPoint][rPoint].bomb == false {
                board[cPoint][rPoint].bomb = true
                bombsLeft -= 1
            }
        }
        setBombNum()
        
    }
    
    // Assignment 3 - see at the bottom
    func openCell(row: Int, col: Int) -> Bool{
        return board[col][row].open = true
    }
    
    func withinBounds(cRow: Int, cCol: Int) -> Bool {
        if cRow >= 0 && cRow < height && cCol >= 0 && cCol < width {
            return true
        } else {
            return false
        }
    }
    
    func printBoard() {
        for row in 0..<height {
            for column in 0..<width {
                print(board[column][row].description(), terminator:" ")
            }
            print("")
        }
        
    }
    
    func setBombNum() {
        //var bombCount = 0
        for row in 0..<height {
            for column in 0..<width {
                if board[column][row].bomb == false {
                    for rd in -1...1 {
                        for cd in -1...1 {
                            let cRow = row + rd
                            let cColumn = column + cd
                            if withinBounds(cRow: cRow, cCol: cColumn) {
                                if board[cColumn][cRow].bomb {
                                    board[column][row].nBombs += 1
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}

let ms = Board(newWidth: 5, newHeight: 7)
ms.printBoard()
print("-----")

let bms = Board(newWidth: 15, newHeight: 20)
bms.printBoard()




//: ## Assignment 3
//: Implement and change the following methods.
//: Modify the description method in Cell to use the information of the open variable. If the value is true then it should show what it does now. If the value is false, it should show "[_]".
//: implement the openCell method in Board class so that it opens the cell indicated by the column and row; it should return whether the cell has a bomb or not.
