class Conference{
   
	var venue: String = "Cunningham center"
    
	var date: String  = "march 17, 2017"
    
	var presenters: Int = 42

	func announce() {
        
	if presenters<=0{
            
		print("The conference has now closed, thank you for attending!")
        
	}
	else{
            
		print("Thank you for coming to " + venue + "the date is: " + date + " we have: " + presenters + "remaining thank you for attending")
        
	}
	 presenters-=1
  	}
   

}
class Presentation{
    
	var presenter: String = "martha" 
    
	var timeAllowed: Int = 5
    
	var topic: String = "ecology"

	func introduce(){
        
		print( "please welcome " + presenter + " who will be speaking on: " + topic + "the presentation will last " + timeAllowed + " minutes")
	 }
    
	func callTime(){
        
		timeAllowed -= 1
        
		if timeAllowed <= 0 {
           
			print( "time is up!" )
        
	}
		else {
          
			print( presenter + " you have: " + timeAllowed + " minutes left.")
        
		}
	 }
        

}
