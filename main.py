import re as regex
import WebCrawly

def main():
  # Calling the result of WebCrawly.py 
  WebCrawly.web_crawly()
  u=input("Please Enter Your Username> ")
  p=input("Please Enter Your Password> ")
  ip = input("Please Enter Your IP Address> ")


  pattern = regex.search("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", ip)
  if pattern == None:
    print("invalid IP address")
    return

  ip = pattern.group(0)
  
  # Prevent continous looping when fields ar emtpy
  
  while(True):
    if u == "" and p == "" and ip == "":
      print("Please Enter Your Credentials \n")
      break

    if u != "" and p != "" and ip != "":
      question = input("Do you want to enter your credentials again? (yes|no) ").lower()

      
      # Using __main__ call the prompts again requesting for use imput.
      if question == "yes":
        main()
      else:
        break
    
# Call the functions again after the inital display of results.
    sammy_creds = creds(u, p)
    asset = asset_ip(ip)
    # Print the result of inputs to the screen
    print(sammy_creds)
    print(asset)
    # Ask the user if they want to run the program again
    u=input("Please Enter Your Username> ")
    p=input("Please Enter Your Password> ")
    ip=input("Please Enter Your IP Address> ")
    
  
  print("Exiting the application")


def creds(username: str, password: str) -> str:
  # Gretting user credentials
  print("="*80 + "\nViolation of this credential will be percecuted to full extent of the law\n" + "="*80)
  new_username = username.capitalize()
  new_password = password.upper()

  # Prints credentials to the screen.
  credentials = f"Username: {new_username}\nPassword: {new_password}"
  # print(f"Username: {new_username}\nPassword: {new_password}")

  return credentials
  
def asset_ip(net_ip: str):
  new_print = net_ip.capitalize()

  return new_print
  

  
if __name__ == "__main__":
  main()
