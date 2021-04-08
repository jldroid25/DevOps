# Example file for retrieving data from the internet 
# run file with python3 filename

# helps make http request for python3
import urllib.request 

def main():
    # 1- Let's open the url & Print its status http code
    webUrl = urllib.request.urlopen("http://www.cashdatastack.com")
    print("CashDataStack.com HTTP result code is : " + str(webUrl.getcode()))

    # 2 now lets get read/print& print some data from the site url
    data = webUrl.read()
    print(data)



if __name__ == "__main__":
    main()