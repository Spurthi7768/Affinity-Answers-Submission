# Task-1
Programming Skils

## Question
BestDelivery Courier Company has an issue. Many parcels they get to deliver have the wrong PIN code and that leads to packages going to the wrong location and then someone figuring out manually that the PIN code is wrong from the other parts of the address. You are the programmer who has to fix this issue by writing a program that takes as input a free flowing address and checking if the PIN code indeed corresponds to the address mentioned. Use this free API http://www.postalpincode.in/Api-Details for the purpose of PIN code identification.
e.g. of correct addresses: "2nd Phase, 374/B, 80 Feet Rd, Mysore Bank Colony, Banashankari 3rd Stage, Srinivasa Nagar, Bengaluru, Karnataka 560050”, "2nd Phase, 374/B, 80 Feet Rd, Bank Colony, Banashankari 3rd Stage, Srinivasa Nagar, Bengaluru, Karnataka 560050”, "374/B, 80 Feet Rd, State Bank Colony, Banashankari 3rd Stage, Srinivasa Nagar, Bangalore. 560050”, 
e.g. of an incorrect addresses: "2nd Phase, 374/B, 80 Feet Rd, Mysore Bank Colony, Banashankari 3rd Stage, Srinivasa Nagar, Bengaluru, Karnataka 560095”, “Colony, Bengaluru, Karnataka 560050”

## Instructions to use
* Create a virtual environment in python
* Activate the virtual environment
* Install the packages from requirements.txt file
* Run the command : `python pincode_validation.py`

## Flow of the Program

Accept the Input of Address ------> Split the Address -----> Extract the PIN code -----> Pass the PIN Code as a input to the API Call -----> Extract the locations from the JSON output -----> Check if any of these locations are present in the input address -----> Output


## Output 

This output is for the test cases mentioned in the question
