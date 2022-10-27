import re

def extract(data):
    #RegEx
    url = re.compile("(https?://[^\s]+)",re.UNICODE) #Search for http or https
    mail = re.compile("[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+",re.UNICODE) #Any charracter follow by @
    phone = re.compile("([+?84|0]+[3|5|7|8|9]\d{8})",re.UNICODE) #Following the format (+)84/0 + mobilenetwork(3,5,7,8,9) + 8digits
    
    list = []
    
    for match in re.finditer(url,data):
        tuple =([match.start(),match.end()-match.start()+1,match.group()])
        list.append(tuple)
        
    for match in re.finditer(mail,data):
        tuple =([match.start(),match.end()-match.start()+1,match.group()])
        list.append(tuple)
        
    for match in re.finditer(phone,data):
        tuple =([match.start(),match.end()-match.start()+1,match.group()])
        list.append(tuple)
          
    for i in range(len(list)):
        print(list[i])   
    
def main():
    filename = input("Input filename: ")
    data = ""

    #read
    with open(filename,encoding='utf8') as file:
        for line in file:
            if not line.isspace():
                data+=line
                
    extract(data)
    
if __name__=="__main__":
    main()