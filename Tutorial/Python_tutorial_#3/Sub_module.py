



def emailProcess(email):
    email_Username = email[0:email.index("@")]
    #print(f"User Name : {email_Username}")
    email_Domain = email[email.index("@") + 1:]
    #print(f"User Domain : {email_Domain}")
    return(email_Username, email_Domain)

def PrintMsg(email_Username, email_Domain):
    print(f"User Name: {email_Username} User Domain {email_Domain}") 

def main():
    email = input("Please enter your email adress :").strip()
    email_Username, email_Domain = emailProcess(email)
    PrintMsg(email_Username, email_Domain)

if __name__ == "__main__":
    main()
