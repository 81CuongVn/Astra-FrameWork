'''
      __        ________  ___________  _______        __      
     /""\      /"       )("     _   ")/"      \      /""\     
    /    \    (:   \___/  )__/  \\__/|:        |    /    \    
   /' /\  \    \___  \       \\_ /   |_____/   )   /' /\  \   
  //  __'  \    __/  \\      |.  |    //      /   //  __'  \  
 /   /  \\  \  /" \   :)     \:  |   |:  __   \  /   /  \\  \ 
(___/    \___)(_______/       \__|   |__|  \___)(___/    \___)

Github  : https://github.com/NotReeceHarris/Astra-FrameWork

Dev     : https://github.com/NotReeceHarris
          https://github.com/NotDevenBriers

Sponsor : https://techonaut.tech/
'''



import base64
import random
import os
import sys
import time

# 3 globaly used variables

version = 'V1.0.0'
operating_system = 'win' if os.name == 'nt' else 'unix'
terminal_color = {'black': u'\033[30m','red': u'\u001b[31m','green': u'\033[32m','orange': u'\033[33m','blue': u'\033[34m','purple': u'\033[35m','cyan': u'\033[36m','lightgrey': u'\033[37m','darkgrey': u'\033[90m','lightred': u'\033[91m','lightgreen': u'\033[92m','yellow': u'\033[93m','lightblue': u'\033[94m','pink': u'\033[95m','lightcyan': u'\033[96m','end': u'\033[0m', 'purplebg': u'\033[45m', 'bold':u'\033[1m'}

# Credits as there are multiple tools
# and scripts within this frame-work,
# All developers should support other 
# developers.

# The code in this frame-work is % 70 
# other developers code, This is a frame-work
# theres no point re-coding a pre-coded
# tool.

Credits = f'''
              ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
              ┃   {terminal_color["purple"]}Sponsor{terminal_color["end"]}           : techonaut.tech        ┃
              ┃                                             ┃
              ┃   {terminal_color["purple"]}Astra{terminal_color["end"]}             : NotReeceHarris        ┃
              ┃                       NotDevenBriers        ┃
              ┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
              ┃                                             ┃
              ┃   {terminal_color["purple"]}SqlMap{terminal_color["end"]}            : sqlmap.org            ┃
              ┃                                             ┃
              ┃   {terminal_color["purple"]}Metasploit{terminal_color["end"]}        : rapid7.com            ┃
              ┃                                             ┃
              ┃   {terminal_color["purple"]}Sherlock{terminal_color["end"]}          : Siddharth Dushantha   ┃
              ┃                       Yahya SayadArbabi     ┃
              ┃                                             ┃
              ┃   {terminal_color["purple"]}Scapy{terminal_color["end"]}             : secdev.org            ┃
              ┃                                             ┃
              ┃   {terminal_color["purple"]}Setoolkit{terminal_color["end"]}         : TrustedSec            ┃  
              ┃                       David Kennedy         ┃
              ┃                                             ┃                            
              ┃   {terminal_color["purple"]}Zphisher{terminal_color["end"]}          : htr-tech              ┃
              ┃                       Aditya Shakya         ┃
              ┃                       TheLinuxChoice        ┃
              ┃                       DarksecDevelopers     ┃
              ┃                       Moises Tapia          ┃
              ┃                                             ┃
              ┃   {terminal_color["purple"]}RED_HAWK{terminal_color["end"]}          : r3dhax0r              ┃  
              ┃                       Crowfunder            ┃
              ┃                       Romain Biard          ┃
              ┃                                             ┃
              ┃   {terminal_color["purple"]}RpiHunter{terminal_color["end"]}         : BusesCanFly           ┃  
              ┃                                             ┃
              ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
'''

# Clears the terminal to clear clutter
# and un-needed print nicer looking.

def clear_terminal(): 
    os.system('cls' if os.name == 'nt' else 'clear')
    return ''

# Clears the terminal and says bye
# its nice to be polite be like astra

def exit_astra():
    print(f'{clear_terminal()}{terminal_color["bold"]}Bye {terminal_color["end"]}{terminal_color["purple"]};){terminal_color["end"]}')
    exit()






def Recon():
    cur = '?'
    while True:
        print(f'''{clear_terminal()}    
              ┏━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┓                        
              ┃    sherlock ━ {terminal_color["purple"]}0{terminal_color["end"]} ┃ {terminal_color["purple"]}1{terminal_color["end"]} ━ simplyemail ┃
              ┣━━━━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━━━┫
              ┃        Back ━ {terminal_color["purple"]}?{terminal_color["end"]} ┃ {terminal_color["purple"]}!{terminal_color["end"]} ━ Exit        ┃
              ┗━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━┛
            ''')

        i = input(f'''
    ┃{terminal_color["purple"]} Recon {terminal_color["end"]}┃ {cur} {terminal_color["end"]}┃ $ ''')
        cur = '?'
        if i not in ['0','1','2','3','4','5','6','7','8','9','?','!']:
            cur = f'{terminal_color["red"]} X {terminal_color["end"]}'
        elif i == '0': # Sherlock
            while True:
                clear_terminal()
                print('''
        usage: >>> [-q, !] [-h] [--version] [--verbose] [--folderoutput FOLDEROUTPUT]
            [--output OUTPUT] [--tor] [--unique-tor] [--csv]
            [--site SITE_NAME] [--proxy PROXY_URL] [--json JSON_FILE]
            [--timeout TIMEOUT] [--print-all] [--print-found]
            [--no-color] [--browse] [--local]
            USERNAMES [USERNAMES ...]
                ''')
                i = input(f'{terminal_color["purple"]}>>>{terminal_color["end"]} ')
                if i == '-q' or i == '!':
                    break
                elif i == '':
                    pass
                clear_terminal()
                os.system(f'sudo "{os.path.dirname(sys.executable)}/python3" {os.path.abspath(os.path.dirname(sys.argv[0]))}/Source/sherlock/sherlock.py --folderoutput {os.path.abspath(os.path.dirname(sys.argv[0]))}/Loot/sherlock {i}')
                input('\nPress enter to continue...')
                
        elif i == '1': # 
            while True:
                clear_terminal()
                print('''
        usage: >>> [-q, !] [-all] [-e company.com] [-l] [-t html / flickr / google]
                      [-s] [-n] [-verify] [-v] [--json json-emails.txt]

                Email enumeration is a important phase of so many operation that a pen-tester
                or Red Teamer goes through. There are tons of applications that do this but I
                wanted a simple yet effective way to get what Recon-Ng gets and theHarvester
                gets. (You may want to run -h)

                optional arguments:
                -all                  Use all non API methods to obtain Emails
                -e company.com        Set required email addr user, ex ale@email.com
                -l                    List the current Modules Loaded
                -t html / flickr / google
                                        Test individual module (For Linting)
                -s                    Set this to enable 'No-Scope' of the email parsing
                -n                    Set this to enable Name Generation
                -verify               Set this to enable SMTP server email verify
                -v                    Set this switch for verbose output of modules
                --json json-emails.txt
                                        Set this switch for json output to specfic file
                ''')
                i = input(f'{terminal_color["purple"]}>>>{terminal_color["end"]} ')
                if i == '-q' or i == '!':
                    break
                elif i == '':
                    pass
                clear_terminal()
                os.system(f'"{os.path.dirname(sys.executable)}/python2" {os.path.abspath(os.path.dirname(sys.argv[0]))}/Source/simplyemail/SimplyEmail.py {i}')
                input('\nPress enter to continue...')
        elif i == '2': # 
            while True:
                clear_terminal()
                print('''
        usage: >>> [-q, !] [-all] [-e company.com] [-l] [-t html / flickr / google]
                      [-s] [-n] [-verify] [-v] [--json json-emails.txt]

                Email enumeration is a important phase of so many operation that a pen-tester
                or Red Teamer goes through. There are tons of applications that do this but I
                wanted a simple yet effective way to get what Recon-Ng gets and theHarvester
                gets. (You may want to run -h)

                optional arguments:
                -all                  Use all non API methods to obtain Emails
                -e company.com        Set required email addr user, ex ale@email.com
                -l                    List the current Modules Loaded
                -t html / flickr / google
                                        Test individual module (For Linting)
                -s                    Set this to enable 'No-Scope' of the email parsing
                -n                    Set this to enable Name Generation
                -verify               Set this to enable SMTP server email verify
                -v                    Set this switch for verbose output of modules
                --json json-emails.txt
                                        Set this switch for json output to specfic file
                ''')
                i = input(f'{terminal_color["purple"]}>>>{terminal_color["end"]} ')
                if i == '-q' or i == '!':
                    break
                elif i == '':
                    pass
                clear_terminal()
                os.system(f'"{os.path.dirname(sys.executable)}/python2" {os.path.abspath(os.path.dirname(sys.argv[0]))}/Source/simplyemail/SimplyEmail.py {i}')
                input('\nPress enter to continue...')
        elif i == '3': # 
            pass
        elif i == '4': # 
            pass
        elif i == '5': # 
            pass
        elif i == '6': # 
            pass
        elif i == '7': # 
            pass
        elif i == '8': # 
            pass
        elif i == '9': # 
            pass
        elif i == '!':
            exit_astra()
        elif i == '?':
            return f'{terminal_color["green"]} X {terminal_color["end"]}'

def Analysis():
    cur = '?'
    while True:
        print(f'''{clear_terminal()}    
              ┏━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┓               
              ┃     redhawk ━ {terminal_color["purple"]}0{terminal_color["end"]} ┃ {terminal_color["purple"]}1{terminal_color["end"]} ━ Rpi-Hunter  ┃
              ┣━━━━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━━━┫
              ┃        Back ━ {terminal_color["purple"]}?{terminal_color["end"]} ┃ {terminal_color["purple"]}!{terminal_color["end"]} ━ Exit        ┃
              ┗━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━┛
            ''')

        i = input(f'''
    ┃{terminal_color["purple"]} Analysis {terminal_color["end"]}┃ {cur} {terminal_color["end"]}┃ $ ''')
        cur = '?'
        if i not in ['0','1','2','3','4','5','6','7','8','9','?','!']:
            cur = f'{terminal_color["red"]} X {terminal_color["end"]}'
        elif i == '0': # 
            clear_terminal()
            os.system(f'php {os.path.abspath(os.path.dirname(sys.argv[0]))}/Source/redhawk/rhawk.php')
            input(f'\n{terminal_color["end"]}Press enter to continue...')
        elif i == '1': # 
            while True:
                clear_terminal()
                print('''
        usage: >>> [-q,!] [-h] [--list] [--no-scan] [-r IP_RANGE] [-f IP_LIST]
                     [-u UNAME] [-c CREDS] [--payload PAYLOAD] [-H HOST]
                     [-P PORT] [--safe] [-q]

                optional arguments:
                -q, !              Exit Rpi-Hunter
                -h, --help         show this help message and exit
                --list             list available payloads
                --no-scan          disable arp scanning
                -r IP_RANGE        ip range to scan
                -f IP_LIST         ip list to use (default ./Loot/rpihunter/rpi_list)
                -u UNAME           username to use when ssh'ing
                -c CREDS           password to use when ssh'ing
                --payload PAYLOAD  (name of, or raw) payload [ex. reverse_shell or 'whoami']
                -H HOST            (if using reverse_shell payload) host for reverse shell
                -P PORT            (if using reverse_shell payload) port for reverse shell
                --safe             print sshpass command, but don't execute it
                -dp                don't print banner or arp scan output
                ''')
                i = input(f'{terminal_color["purple"]}>>>{terminal_color["end"]} ')
                if i == '-q' or i == '!':
                    break
                elif i == '':
                    pass
                clear_terminal()
                os.system(f'sudo "{os.path.dirname(sys.executable)}/python2" {os.path.abspath(os.path.dirname(sys.argv[0]))}/Source/rpihunter/rpi-hunter.py {i}')
                input('\nPress enter to continue...')
        elif i == '2': # 
            pass
        elif i == '3': # 
            pass
        elif i == '4': # 
            pass
        elif i == '5': # 
            pass
        elif i == '6': # 
            pass
        elif i == '7': # 
            pass
        elif i == '8': # 
            pass
        elif i == '9': # 
            pass
        elif i == '!':
            exit_astra()
        elif i == '?':
            return f'{terminal_color["green"]} X {terminal_color["end"]}'

def WebApps():
    cur = '?'
    while True:
        print(f'''{clear_terminal()}    
              ┏━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┓                        
              ┃      sqlmap ━ {terminal_color["purple"]}0{terminal_color["end"]} ┃ {terminal_color["purple"]}1{terminal_color["end"]} ━ redhawk     ┃
              ┣━━━━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━━━┫
              ┃        Back ━ {terminal_color["purple"]}?{terminal_color["end"]} ┃ {terminal_color["purple"]}!{terminal_color["end"]} ━ Exit        ┃
              ┗━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━┛
            ''')

        i = input(f'''
    ┃{terminal_color["purple"]} Web Apps {terminal_color["end"]}┃ {cur} {terminal_color["end"]}┃ $ ''')
        cur = '?'
        if i not in ['0','1','2','3','4','5','6','7','8','9','?','!']:
            cur = f'{terminal_color["red"]} X {terminal_color["end"]}'
        elif i == '0': # 
            while True:
                clear_terminal()

                # Encoded in base64 to reduce
                # line clutter and space clutter

                print(base64.b64decode('ICAgICAgICBVc2FnZTogPj4+IFtvcHRpb25zXQoKICAgICAgICAgICAgT3B0aW9uczoKICAgICAgICAgICAgLXEsICEgICAgICAgICAgICAgICAgIEV4aXQgc2NyaXB0CiAgICAgICAgICAgIC1oLCAtLWhlbHAgICAgICAgICAgICBTaG93IGJhc2ljIGhlbHAgbWVzc2FnZSBhbmQgZXhpdAogICAgICAgICAgICAtaGggICAgICAgICAgICAgICAgICAgU2hvdyBhZHZhbmNlZCBoZWxwIG1lc3NhZ2UgYW5kIGV4aXQKICAgICAgICAgICAgLS12ZXJzaW9uICAgICAgICAgICAgIFNob3cgcHJvZ3JhbSdzIHZlcnNpb24gbnVtYmVyIGFuZCBleGl0CiAgICAgICAgICAgIC12IFZFUkJPU0UgICAgICAgICAgICBWZXJib3NpdHkgbGV2ZWw6IDAtNiAoZGVmYXVsdCAxKQoKICAgICAgICAgICAgVGFyZ2V0OgogICAgICAgICAgICAgICAgQXQgbGVhc3Qgb25lIG9mIHRoZXNlIG9wdGlvbnMgaGFzIHRvIGJlIHByb3ZpZGVkIHRvIGRlZmluZSB0aGUKICAgICAgICAgICAgICAgIHRhcmdldChzKQoKICAgICAgICAgICAgICAgIC11IFVSTCwgLS11cmw9VVJMICAgVGFyZ2V0IFVSTCAoZS5nLiAiaHR0cDovL3d3dy5zaXRlLmNvbS92dWxuLnBocD9pZD0xIikKICAgICAgICAgICAgICAgIC1nIEdPT0dMRURPUksgICAgICAgUHJvY2VzcyBHb29nbGUgZG9yayByZXN1bHRzIGFzIHRhcmdldCBVUkxzCgogICAgICAgICAgICBSZXF1ZXN0OgogICAgICAgICAgICAgICAgVGhlc2Ugb3B0aW9ucyBjYW4gYmUgdXNlZCB0byBzcGVjaWZ5IGhvdyB0byBjb25uZWN0IHRvIHRoZSB0YXJnZXQgVVJMCgogICAgICAgICAgICAgICAgLS1kYXRhPURBVEEgICAgICAgICBEYXRhIHN0cmluZyB0byBiZSBzZW50IHRocm91Z2ggUE9TVCAoZS5nLiAiaWQ9MSIpCiAgICAgICAgICAgICAgICAtLWNvb2tpZT1DT09LSUUgICAgIEhUVFAgQ29va2llIGhlYWRlciB2YWx1ZSAoZS5nLiAiUEhQU0VTU0lEPWE4ZDEyN2UuLiIpCiAgICAgICAgICAgICAgICAtLXJhbmRvbS1hZ2VudCAgICAgIFVzZSByYW5kb21seSBzZWxlY3RlZCBIVFRQIFVzZXItQWdlbnQgaGVhZGVyIHZhbHVlCiAgICAgICAgICAgICAgICAtLXByb3h5PVBST1hZICAgICAgIFVzZSBhIHByb3h5IHRvIGNvbm5lY3QgdG8gdGhlIHRhcmdldCBVUkwKICAgICAgICAgICAgICAgIC0tdG9yICAgICAgICAgICAgICAgVXNlIFRvciBhbm9ueW1pdHkgbmV0d29yawogICAgICAgICAgICAgICAgLS1jaGVjay10b3IgICAgICAgICBDaGVjayB0byBzZWUgaWYgVG9yIGlzIHVzZWQgcHJvcGVybHkKCiAgICAgICAgICAgIEluamVjdGlvbjoKICAgICAgICAgICAgICAgIFRoZXNlIG9wdGlvbnMgY2FuIGJlIHVzZWQgdG8gc3BlY2lmeSB3aGljaCBwYXJhbWV0ZXJzIHRvIHRlc3QgZm9yLAogICAgICAgICAgICAgICAgcHJvdmlkZSBjdXN0b20gaW5qZWN0aW9uIHBheWxvYWRzIGFuZCBvcHRpb25hbCB0YW1wZXJpbmcgc2NyaXB0cwoKICAgICAgICAgICAgICAgIC1wIFRFU1RQQVJBTUVURVIgICAgVGVzdGFibGUgcGFyYW1ldGVyKHMpCiAgICAgICAgICAgICAgICAtLWRibXM9REJNUyAgICAgICAgIEZvcmNlIGJhY2stZW5kIERCTVMgdG8gcHJvdmlkZWQgdmFsdWUKCiAgICAgICAgICAgIERldGVjdGlvbjoKICAgICAgICAgICAgICAgIFRoZXNlIG9wdGlvbnMgY2FuIGJlIHVzZWQgdG8gY3VzdG9taXplIHRoZSBkZXRlY3Rpb24gcGhhc2UKCiAgICAgICAgICAgICAgICAtLWxldmVsPUxFVkVMICAgICAgIExldmVsIG9mIHRlc3RzIHRvIHBlcmZvcm0gKDEtNSwgZGVmYXVsdCAxKQogICAgICAgICAgICAgICAgLS1yaXNrPVJJU0sgICAgICAgICBSaXNrIG9mIHRlc3RzIHRvIHBlcmZvcm0gKDEtMywgZGVmYXVsdCAxKQoKICAgICAgICAgICAgVGVjaG5pcXVlczoKICAgICAgICAgICAgICAgIFRoZXNlIG9wdGlvbnMgY2FuIGJlIHVzZWQgdG8gdHdlYWsgdGVzdGluZyBvZiBzcGVjaWZpYyBTUUwgaW5qZWN0aW9uCiAgICAgICAgICAgICAgICB0ZWNobmlxdWVzCgogICAgICAgICAgICAgICAgLS10ZWNobmlxdWU9VEVDSC4uICBTUUwgaW5qZWN0aW9uIHRlY2huaXF1ZXMgdG8gdXNlIChkZWZhdWx0ICJCRVVTVFEiKQoKICAgICAgICAgICAgRW51bWVyYXRpb246CiAgICAgICAgICAgICAgICBUaGVzZSBvcHRpb25zIGNhbiBiZSB1c2VkIHRvIGVudW1lcmF0ZSB0aGUgYmFjay1lbmQgZGF0YWJhc2UKICAgICAgICAgICAgICAgIG1hbmFnZW1lbnQgc3lzdGVtIGluZm9ybWF0aW9uLCBzdHJ1Y3R1cmUgYW5kIGRhdGEgY29udGFpbmVkIGluIHRoZQogICAgICAgICAgICAgICAgdGFibGVzCgogICAgICAgICAgICAgICAgLWEsIC0tYWxsICAgICAgICAgICBSZXRyaWV2ZSBldmVyeXRoaW5nCiAgICAgICAgICAgICAgICAtYiwgLS1iYW5uZXIgICAgICAgIFJldHJpZXZlIERCTVMgYmFubmVyCiAgICAgICAgICAgICAgICAtLWN1cnJlbnQtdXNlciAgICAgIFJldHJpZXZlIERCTVMgY3VycmVudCB1c2VyCiAgICAgICAgICAgICAgICAtLWN1cnJlbnQtZGIgICAgICAgIFJldHJpZXZlIERCTVMgY3VycmVudCBkYXRhYmFzZQogICAgICAgICAgICAgICAgLS1wYXNzd29yZHMgICAgICAgICBFbnVtZXJhdGUgREJNUyB1c2VycyBwYXNzd29yZCBoYXNoZXMKICAgICAgICAgICAgICAgIC0tdGFibGVzICAgICAgICAgICAgRW51bWVyYXRlIERCTVMgZGF0YWJhc2UgdGFibGVzCiAgICAgICAgICAgICAgICAtLWNvbHVtbnMgICAgICAgICAgIEVudW1lcmF0ZSBEQk1TIGRhdGFiYXNlIHRhYmxlIGNvbHVtbnMKICAgICAgICAgICAgICAgIC0tc2NoZW1hICAgICAgICAgICAgRW51bWVyYXRlIERCTVMgc2NoZW1hCiAgICAgICAgICAgICAgICAtLWR1bXAgICAgICAgICAgICAgIER1bXAgREJNUyBkYXRhYmFzZSB0YWJsZSBlbnRyaWVzCiAgICAgICAgICAgICAgICAtLWR1bXAtYWxsICAgICAgICAgIER1bXAgYWxsIERCTVMgZGF0YWJhc2VzIHRhYmxlcyBlbnRyaWVzCiAgICAgICAgICAgICAgICAtRCBEQiAgICAgICAgICAgICAgIERCTVMgZGF0YWJhc2UgdG8gZW51bWVyYXRlCiAgICAgICAgICAgICAgICAtVCBUQkwgICAgICAgICAgICAgIERCTVMgZGF0YWJhc2UgdGFibGUocykgdG8gZW51bWVyYXRlCiAgICAgICAgICAgICAgICAtQyBDT0wgICAgICAgICAgICAgIERCTVMgZGF0YWJhc2UgdGFibGUgY29sdW1uKHMpIHRvIGVudW1lcmF0ZQoKICAgICAgICAgICAgT3BlcmF0aW5nIHN5c3RlbSBhY2Nlc3M6CiAgICAgICAgICAgICAgICBUaGVzZSBvcHRpb25zIGNhbiBiZSB1c2VkIHRvIGFjY2VzcyB0aGUgYmFjay1lbmQgZGF0YWJhc2UgbWFuYWdlbWVudAogICAgICAgICAgICAgICAgc3lzdGVtIHVuZGVybHlpbmcgb3BlcmF0aW5nIHN5c3RlbQoKICAgICAgICAgICAgICAgIC0tb3Mtc2hlbGwgICAgICAgICAgUHJvbXB0IGZvciBhbiBpbnRlcmFjdGl2ZSBvcGVyYXRpbmcgc3lzdGVtIHNoZWxsCiAgICAgICAgICAgICAgICAtLW9zLXB3biAgICAgICAgICAgIFByb21wdCBmb3IgYW4gT09CIHNoZWxsLCBNZXRlcnByZXRlciBvciBWTkMKCiAgICAgICAgICAgIEdlbmVyYWw6CiAgICAgICAgICAgICAgICBUaGVzZSBvcHRpb25zIGNhbiBiZSB1c2VkIHRvIHNldCBzb21lIGdlbmVyYWwgd29ya2luZyBwYXJhbWV0ZXJzCgogICAgICAgICAgICAgICAgLS1iYXRjaCAgICAgICAgICAgICBOZXZlciBhc2sgZm9yIHVzZXIgaW5wdXQsIHVzZSB0aGUgZGVmYXVsdCBiZWhhdmlvcgogICAgICAgICAgICAgICAgLS1mbHVzaC1zZXNzaW9uICAgICBGbHVzaCBzZXNzaW9uIGZpbGVzIGZvciBjdXJyZW50IHRhcmdldAoKICAgICAgICAgICAgTWlzY2VsbGFuZW91czoKICAgICAgICAgICAgICAgIFRoZXNlIG9wdGlvbnMgZG8gbm90IGZpdCBpbnRvIGFueSBvdGhlciBjYXRlZ29yeQoKICAgICAgICAgICAgICAgIC0td2l6YXJkICAgICAgICAgICAgU2ltcGxlIHdpemFyZCBpbnRlcmZhY2UgZm9yIGJlZ2lubmVyIHVzZXJzCgogICAgICAgICAgICBbIV0gdG8gc2VlIGZ1bGwgbGlzdCBvZiBvcHRpb25zIHJ1biB3aXRoICctaGgn'.encode('ascii')).decode('ascii'))
                i = input(f'{terminal_color["purple"]}>>>{terminal_color["end"]} ')
                if i == '-q' or i == '!':
                    break
                elif i == '':
                    pass
                os.system(f'sudo "{os.path.dirname(sys.executable)}/python3" {os.path.abspath(os.path.dirname(sys.argv[0]))}/Source/sqlmap/sqlmap.py --dump-all {os.path.abspath(os.path.dirname(sys.argv[0]))}/Loot/sqlmap {i}')
                input('\nPress enter to continue...')
        elif i == '1': # 
            clear_terminal()
            os.system(f'php {os.path.abspath(os.path.dirname(sys.argv[0]))}/Source/redhawk/rhawk.php')
            {terminal_color["end"]}
            input('\nPress enter to continue...')
        elif i == '2': # 
            pass
        elif i == '3': # 
            pass
        elif i == '4': # 
            pass
        elif i == '5': # 
            pass
        elif i == '6': # 
            pass
        elif i == '7': # 
            pass
        elif i == '8': # 
            pass
        elif i == '9': # 
            pass
        elif i == '!':
            exit_astra()
        elif i == '?':
            return f'{terminal_color["green"]} X {terminal_color["end"]}'

def Cracking():
    cur = '?'
    while True:
        print(f'''{clear_terminal()}    
              ┏━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┓                        
              ┃                                   ┃
              ┣━━━━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━━━┫
              ┃        Back ━ {terminal_color["purple"]}?{terminal_color["end"]} ┃ {terminal_color["purple"]}!{terminal_color["end"]} ━ Exit        ┃
              ┗━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━┛
            ''')

        i = input(f'''
    ┃{terminal_color["purple"]} Cracking {terminal_color["end"]}┃ {cur} {terminal_color["end"]}┃ $ ''')
        cur = '?'
        if i not in ['0','1','2','3','4','5','6','7','8','9','?','!']:
            cur = f'{terminal_color["red"]} X {terminal_color["end"]}'
        elif i == '0': # 
            pass
        elif i == '1': # 
            pass
        elif i == '2': # 
            pass
        elif i == '3': # 
            pass
        elif i == '4': # 
            pass
        elif i == '5': # 
            pass
        elif i == '6': # 
            pass
        elif i == '7': # 
            pass
        elif i == '8': # 
            pass
        elif i == '9': # 
            pass
        elif i == '!':
            exit_astra()
        elif i == '?':
            return f'{terminal_color["green"]} X {terminal_color["end"]}'

def Wireless():
    cur = '?'
    while True:
        print(f'''{clear_terminal()}    
              ┏━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┓                        
              ┃                                   ┃
              ┣━━━━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━━━┫
              ┃        Back ━ {terminal_color["purple"]}?{terminal_color["end"]} ┃ {terminal_color["purple"]}!{terminal_color["end"]} ━ Exit        ┃
              ┗━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━┛
            ''')

        i = input(f'''
    ┃{terminal_color["purple"]} Wireless {terminal_color["end"]}┃ {cur} {terminal_color["end"]}┃ $ ''')
        cur = '?'
        if i not in ['0','1','2','3','4','5','6','7','8','9','?','!']:
            cur = f'{terminal_color["red"]} X {terminal_color["end"]}'
        elif i == '0': # 
            pass
        elif i == '1': # 
            pass
        elif i == '2': # 
            pass
        elif i == '3': # 
            pass
        elif i == '4': # 
            pass
        elif i == '5': # 
            pass
        elif i == '6': # 
            pass
        elif i == '7': # 
            pass
        elif i == '8': # 
            pass
        elif i == '9': # 
            pass
        elif i == '!':
            exit_astra()
        elif i == '?':
            return f'{terminal_color["green"]} X {terminal_color["end"]}'

def Exploitation():
    cur = '?'
    while True:
        print(f'''{clear_terminal()}    
              ┏━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┓                        
              ┣━━━━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━━━┫
              ┃        Back ━ {terminal_color["purple"]}?{terminal_color["end"]} ┃ {terminal_color["purple"]}!{terminal_color["end"]} ━ Exit        ┃
              ┗━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━┛
            ''')

        i = input(f'''
    ┃{terminal_color["purple"]} Exploitation {terminal_color["end"]}┃ {cur} {terminal_color["end"]}┃ $ ''')
        cur = '?'
        if i not in ['0','1','2','3','4','5','6','7','8','9','?','!']:
            cur = f'{terminal_color["red"]} X {terminal_color["end"]}'
        elif i == '0': # 
            pass
        elif i == '1': # 
            pass
        elif i == '2': # 
            pass
        elif i == '3': # 
            pass
        elif i == '4': # 
            pass
        elif i == '5': # 
            pass
        elif i == '6': # 
            pass
        elif i == '7': # 
            pass
        elif i == '8': # 
            pass
        elif i == '9': # 
            pass
        elif i == '!':
            exit_astra()
        elif i == '?':
            return f'{terminal_color["green"]} X {terminal_color["end"]}'

def Sniffing():
    cur = '?'
    while True:
        print(f'''{clear_terminal()}    
              ┏━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┓                        
              ┃       scapy ━ {terminal_color["purple"]}0{terminal_color["end"]} ┃                 ┃
              ┣━━━━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━━━┫
              ┃        Back ━ {terminal_color["purple"]}?{terminal_color["end"]} ┃ {terminal_color["purple"]}!{terminal_color["end"]} ━ Exit        ┃
              ┗━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━┛
            ''')

        i = input(f'''
    ┃{terminal_color["purple"]} Sniffing {terminal_color["end"]}┃ {cur} {terminal_color["end"]}┃ $ ''')
        cur = '?'
        if i not in ['0','1','2','3','4','5','6','7','8','9','?','!']:
            cur = f'{terminal_color["red"]} X {terminal_color["end"]}'
        elif i == '0': # 
            clear_terminal()
            os.system(f'sudo "{os.path.dirname(sys.executable)}/python3" {os.path.abspath(os.path.dirname(sys.argv[0]))}/Source/scapy/main.py')
            input('\nPress enter to continue...')
        elif i == '1': # 
            pass
        elif i == '2': # 
            pass
        elif i == '3': # 
            pass
        elif i == '4': # 
            pass
        elif i == '5': # 
            pass
        elif i == '6': # 
            pass
        elif i == '7': # 
            pass
        elif i == '8': # 
            pass
        elif i == '9': # 
            pass
        elif i == '!':
            exit_astra()
        elif i == '?':
            return f'{terminal_color["green"]} X {terminal_color["end"]}'

def Spoofing():
    cur = '?'
    while True:
        print(f'''{clear_terminal()}    
              ┏━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┓                        
              ┃                                   ┃
              ┣━━━━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━━━┫
              ┃        Back ━ {terminal_color["purple"]}?{terminal_color["end"]} ┃ {terminal_color["purple"]}!{terminal_color["end"]} ━ Exit        ┃
              ┗━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━┛
            ''')

        i = input(f'''
    ┃{terminal_color["purple"]} Spoofing {terminal_color["end"]}┃ {cur} {terminal_color["end"]}┃ $ ''')
        cur = '?'
        if i not in ['0','1','2','3','4','5','6','7','8','9','?','!']:
            cur = f'{terminal_color["red"]} X {terminal_color["end"]}'
        elif i == '0': # 
            pass
        elif i == '1': # 
            pass
        elif i == '2': # 
            pass
        elif i == '3': # 
            pass
        elif i == '4': # 
            pass
        elif i == '5': # 
            pass
        elif i == '6': # 
            pass
        elif i == '7': # 
            pass
        elif i == '8': # 
            pass
        elif i == '9': # 
            pass
        elif i == '!':
            exit_astra()
        elif i == '?':
            return f'{terminal_color["green"]} X {terminal_color["end"]}'

def Forensics():
    cur = '?'
    while True:
        print(f'''{clear_terminal()}    
              ┏━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┓                        
              ┃                                   ┃
              ┣━━━━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━━━┫
              ┃        Back ━ {terminal_color["purple"]}?{terminal_color["end"]} ┃ {terminal_color["purple"]}!{terminal_color["end"]} ━ Exit        ┃
              ┗━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━┛
            ''')

        i = input(f'''
    ┃{terminal_color["purple"]} Forensics {terminal_color["end"]}┃ {cur} {terminal_color["end"]}┃ $ ''')
        cur = '?'
        if i not in ['0','1','2','3','4','5','6','7','8','9','?','!']:
            cur = f'{terminal_color["red"]} X {terminal_color["end"]}'
        elif i == '0': # 
            pass
        elif i == '1': # 
            pass
        elif i == '2': # 
            pass
        elif i == '3': # 
            pass
        elif i == '4': # 
            pass
        elif i == '5': # 
            pass
        elif i == '6': # 
            pass
        elif i == '7': # 
            pass
        elif i == '8': # 
            pass
        elif i == '9': # 
            pass
        elif i == '!':
            exit_astra()
        elif i == '?':
            return f'{terminal_color["green"]} X {terminal_color["end"]}'

def Phishing():
    cur = '?'
    while True:
        print(f'''{clear_terminal()}    
              ┏━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┓                        
              ┃    zphisher - {terminal_color["purple"]}0{terminal_color["end"]} ┃ {terminal_color["purple"]}1{terminal_color["end"]} - setoolkit   ┃
              ┣━━━━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━━━┫
              ┃        Back ━ {terminal_color["purple"]}?{terminal_color["end"]} ┃ {terminal_color["purple"]}!{terminal_color["end"]} ━ Exit        ┃
              ┗━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━┛
            ''')

        i = input(f'''
    ┃{terminal_color["purple"]} Phishing {terminal_color["end"]}┃ {cur} {terminal_color["end"]}┃ $ ''')
        cur = '?'
        if i not in ['0','1','2','3','4','5','6','7','8','9','?','!']:
            cur = f'{terminal_color["red"]} X {terminal_color["end"]}'
        elif i == '0': # 
            os.system(f'sudo bash {os.path.abspath(os.path.dirname(sys.argv[0]))}/Source/zphisher/zphisher.sh')
            input('...')
        elif i == '1': # 
            if not os.path.isdir('/usr/share/setoolkit/'):
                os.system(f'sudo "{os.path.dirname(sys.executable)}/python3" {os.path.abspath(os.path.dirname(sys.argv[0]))}/Source/setoolkit/setup.py')
            os.system(f'sudo setoolkit')
            input('...')
        elif i == '2': # 
            pass
        elif i == '3': # 
            pass
        elif i == '4': # 
            pass
        elif i == '5': # 
            pass
        elif i == '6': # 
            pass
        elif i == '7': # 
            pass
        elif i == '8': # 
            pass
        elif i == '9': # 
            pass
        elif i == '!':
            exit_astra()
        elif i == '?':
            return f'{terminal_color["green"]} X {terminal_color["end"]}'






if __name__ == '__main__':
    
    # This test for both operating system
    # support and also root check
    
    if os.geteuid() != 0 and operating_system != 'win':
        print(f'Please run {terminal_color["red"]}root{terminal_color["end"]}')
        exit()
    elif operating_system == 'win':
        print(f'{terminal_color["purple"]}Astra{terminal_color["end"]} doesnt support your operating system')
        exit()

    # visual propaganda variables
    # used to make astra look pretty ;)

    decoded_propaganda = base64.b64decode('DQogICAgICBfXyAgICAgICAgX19fX19fX18gIF9fX19fX19fX19fICBfX19fX19fICAgICAgICBfXyAgICAgIA0KICAgICAvIiJcICAgICAgLyIgICAgICAgKSgiICAgICBfICAgIikvIiAgICAgIFwgICAgICAvIiJcICAgICANCiAgICAvICAgIFwgICAgKDogICBcX19fLyAgKV9fLyAgXFxfXy98OiAgICAgICAgfCAgICAvICAgIFwgICAgDQogICAvJyAvXCAgXCAgICBcX19fICBcICAgICAgIFxcXyAvICAgfF9fX19fLyAgICkgICAvJyAvXCAgXCAgIA0KICAvLyAgX18nICBcICAgIF9fLyAgXFwgICAgICB8LiAgfCAgICAvLyAgICAgIC8gICAvLyAgX18nICBcICANCiAvICAgLyAgXFwgIFwgIC8iIFwgICA6KSAgICAgXDogIHwgICB8OiAgX18gICBcICAvICAgLyAgXFwgIFwgDQooX19fLyAgICBcX19fKShfX19fX19fLyAgICAgICBcX198ICAgfF9ffCAgXF9fXykoX19fLyAgICBcX19fKQ=='.encode('ascii')).decode('ascii')
    text_propaganda = ['                  A framework out of this world','                   Script kiddies wet dream','            Ment for ethical pen-testing, Don\'t lie!','	            Kali Linux in one script', '              Toolbox used by aliens to find humans','           41 73 74 72 61 20 66 72 61 6d 65 57 6f 72 6b','           You need the right toolbox for pen-testing']

    # Looks for the '--setup' as an argument
    # if so the setup scripts will run

    if '--setup' in sys.argv or '--setup-exit' in sys.argv:
        print(f'{clear_terminal()}{terminal_color["purple"]}{decoded_propaganda}{terminal_color["end"]} {terminal_color["purplebg"]}{terminal_color["bold"]}{version}{terminal_color["end"]} {terminal_color["purplebg"]}{terminal_color["bold"]}Setup{terminal_color["end"]}\n      We are setting up all the needed packages, be patient!\n')

        # Using 'sys.stdout' we can update the
        # terminal without clearing the terminal.

        sys.stdout.write(f'               ┣{terminal_color["purple"]}                              {terminal_color["end"]}┃ MetaSploit\r')
        os.system(f'sudo bash {os.path.abspath(os.path.dirname(sys.argv[0]))}/Source/setoolkit/msfinstall > /dev/null 2>&1')
        sys.stdout.flush()

        sys.stdout.write(f'               ┣{terminal_color["purple"]}━━━━━━━━━━━                   {terminal_color["end"]}┃ SimplyEmail\r')
        os.system(f'sudo bash {os.path.abspath(os.path.dirname(sys.argv[0]))}/Source/simplyemail/setup/setup.sh > /dev/null 2>&1')
        os.system(f'sudo pip install -r {os.path.abspath(os.path.dirname(sys.argv[0]))}/Source/simplyemail/setup/requirments.txt > /dev/null 2>&1')
        sys.stdout.flush()

        sys.stdout.write(f'               ┣{terminal_color["purple"]}━━━━━━━━━━━━━━━━━━━━━━━       {terminal_color["end"]}┫ Pip packages\r')
        os.system(f'sudo pip3 install -r requirements.txt > /dev/null 2>&1')
        os.system('sudo pip2 install -U argparse termcolor > /dev/null 2>&1')
        sys.stdout.flush()

        sys.stdout.write(f'               ┣{terminal_color["purple"]}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{terminal_color["end"]}┫ Sudo packages\r')
        os.system(f'sudo apt install arp-scan tshark sshpass -y')
        sys.stdout.flush()

        if '--setup-exit' in sys.argv:
            exit_astra()


    # cur means cursor the little 
    # symbol showing exit code (?, X[red], X[green])

    cur = '?'

    while True:  
        try:         

            # print the menu and also the propaganda, 
            # liability and random shit. 

            print(f'{clear_terminal()}{terminal_color["purple"]}{decoded_propaganda}{terminal_color["end"]} {terminal_color["purplebg"]}{terminal_color["bold"]}{version}{terminal_color["end"]} {terminal_color["purplebg"]}{terminal_color["bold"]}Frame-Work{terminal_color["end"]}\n      We take no liability for use of this tool, be ethical!\n{terminal_color["purple"]}{random.choice(text_propaganda)}{terminal_color["end"]}')
            print(f'''    
              ┏━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┓                        
              ┃       Recon ━ {terminal_color["purple"]}0{terminal_color["end"]} ┃ {terminal_color["purple"]}1{terminal_color["end"]} ━ Analysis    ┃
              ┃    Web Apps ━ {terminal_color["purple"]}2{terminal_color["end"]} ┃ {terminal_color["purple"]}3{terminal_color["end"]} ━ Cracking    ┃
              ┃    Wireless ━ {terminal_color["purple"]}4{terminal_color["end"]} ┃ {terminal_color["purple"]}5{terminal_color["end"]} ━ Exploitation┃
              ┃    Sniffing ━ {terminal_color["purple"]}6{terminal_color["end"]} ┃ {terminal_color["purple"]}7{terminal_color["end"]} ━ Spoofing    ┃
              ┃   Forensics ━ {terminal_color["purple"]}8{terminal_color["end"]} ┃ {terminal_color["purple"]}9{terminal_color["end"]} ━ Phishing    ┃
              ┣━━━━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━━━┫
              ┃     Credits ━ {terminal_color["purple"]}?{terminal_color["end"]} ┃ {terminal_color["purple"]}!{terminal_color["end"]} ━ Exit        ┃
              ┃       Setup ━ {terminal_color["purple"]}={terminal_color["end"]} ┃ {terminal_color["purple"]}@{terminal_color["end"]} ━ Update      ┃
              ┗━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━┛
            ''')

            # User input var with the identity
            # cursor (subtle user error visualiser)

            i = str(input(f'''
    ┃{terminal_color["purple"]} {cur} {terminal_color["end"]}┃ $ '''))

            # This allows functions to execute faster
            # without having 9 elif statments

            options = {'0': Recon,'1': Analysis,'2': WebApps,'3': Cracking,'4': Wireless,'5': Exploitation,'6': Sniffing,'7': Spoofing,'8': Forensics,'9': Phishing}
            
            # Parses user input. Instead of print 
            # "ERROR INVALID INPUT" we just alter 
            # the cursor, run the correlating function

            cur = '?'
            if i not in ['0','1','2','3','4','5','6','7','8','9','?','!','@','=']:
                cur = f'{terminal_color["red"]} X {terminal_color["end"]}'
            elif i == '!':
                exit_astra()
            elif i == '?':
                input(f'''{clear_terminal()}{Credits}''')
                cur = f'{terminal_color["green"]} X {terminal_color["end"]}'
            elif i == '=':
                os.system(f'sudo "{os.path.dirname(sys.executable)}/python3" {os.path.abspath(os.path.dirname(sys.argv[0]))}/astra.py --setup-exit')
            elif i == '@':
                os.system(f'git pull > /dev/null 2>&1')
                exit_astra()
            else:
                cur = options[i]()
            
        # Test for just keyboard errors (CTRL + C)
        # this doesnt allow you to exit the script
        # with ctrl c. don't worry your not stuck
        # in the script all you need to type is '!'

        except KeyboardInterrupt:
            pass