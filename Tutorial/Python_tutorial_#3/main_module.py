from bang import emailProcess, PrintMsg

emails = ['hoangdaibang0804@gmail.com', 'bang95pro@gmail.com', '16t1031004@gmail.com']

def main():
    for email in emails : 
        email_Username, email_Domain = emailProcess(email)
        PrintMsg(email_Username, email_Domain)



if __name__ == "__main__" :
    main()