//  Write some awesome Swift code, or import libraries like "Foundation",
//  "Dispatch", or "Glibc"
class Node {
	var value: Int
	var next: Node?
	init (value: Int){
		self.value = value
	}

}
class linkedList{
	var head:Node?
	var tail:Node?

	func append(value:Int){
		let newNode = Node(value:value)
		if let tailNode = tail{
			tailNode.next = tail
		}

		else{
			head = newNode
		}
		tail = newNode

	}
		
}

let newList = linkedList()
newList.append(value:1)
newList.append(value:5)
newList.append(value:6)
newList.append(value:2)

print(newList)