import requests
import re


# Function for splitting the address

def split_address(address):
    '''

    Function for spliting the address with comma and space as delimiter
    
    
    '''
    parts = address.split(', ')  

   
    return parts


#Function for extracting the pincode from the address

def find_postal_code(address_parts):
    '''
    Function which takes input as split address and returns  extracted pin code 
    
    '''
    postal_code_pattern = r'\b\d{6}\b' # Regex for the pin code (for 6 digits)

    postal_code=None

    # Loop through the split address and find whether the pin code matches the regex pattern

    if re.match(postal_code_pattern, address_parts[-1][-6:]):

        postal_code = address_parts[-1][-6:] # the address will always contain the pincode at the last

    else:
        print("No PIN Code")
        exit()

    return postal_code


# Function for making PIN API call 

def make_api_request(postal_code):

    '''
    Function which takes input as pin code for the API Call and returns JSON output
    
    '''
    try:
        PINCODE=postal_code

        url=f"https://api.postalpincode.in/pincode/{PINCODE}" # PIN Code API

        response = requests.get(url)

        # Check for successful response (status code 200)
        if response.status_code == 200:            
            return response.json()  # Return JSON data
        

        else:
            response.raise_for_status()  # Raise an exception for non-200 status codes

    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)
        return None  # Return None to indicate an error
    

# Function for extracting the places under the pincode mentioned in the given address

def pincode_place_mapping(result):
    '''
    Function takes the input of the JSON output from the API Call and returns a list of locations
    
    '''
    answer=[]

    for item in result:

        for place in item["PostOffice"]:

            if(place["Name"].__contains__("(")):  # Some output contains locations in brackets e.g. Dasarahalli(Srinagar)

                text_r = re.findall(r'\(.+?\)|".+?"|\w+', place["Name"]) #Extract locations within brackets

                for bracket_string in text_r: 

                    district=place["District"]

                    # Some places have district within brackets e.g. Ashoknagar (Bangalore)
                    # In such cases districts are not added to the final list
                    
                    if(bracket_string==f"({district})" or bracket_string==f"({district})"): 
                        pass

                    else:
                        bracket_string=bracket_string.replace("(","").replace(")","")  # Extract the place from the brackets  

                        answer.append(bracket_string) #Add the place to the final list
            
            else:        
                answer.append(place["Name"].rstrip().lstrip()) #Remove any starting or trailing white spaces
    return answer



# Function for checking the 

def check_validity(full_address,valid_list):

    '''
    Function which takes input of the address and the list of places under the pincode of the address
    and returns True/False if the address and location under the pincode of the address match
    
    '''
    for place in valid_list:
        if(re.search(place,full_address)): # Check whether the place under the Pincode and the address match
            return True
    return False



if __name__=='__main__':


    # Accept the input from the user

    full_address = str(input("Enter the address: "))

    #Split the address into a list

    address_parts = split_address(full_address)

    #Extract the pincode from the address list

    postal_code=find_postal_code(address_parts)

    # Make API Call to get the locations from the extracted pin code

    result = make_api_request(postal_code)

    # If the JSON output is obtained from the API 

    if result is not None:        

        # Process the API response data

        for item in result:

            if item["Status"]=="Success":

                # Format the JSON output into a list of locations

                valid_list=pincode_place_mapping(result)               

                #Check if the locations match with the input address

                output=check_validity(full_address,valid_list)

                if(output==True):
                    print("Address and PIN Code MATCH")
                else:
                    print("Address and PIN Code DO NOT MATCH")
        
            else:  #If the Pin Code is not correct
                print("Invalid Pin Code")
       
    else:
        print("API request failed.") # If the API Call failed






