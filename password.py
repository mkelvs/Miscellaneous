#! python3
import random, sys, pyperclip
#  Create a password manager application that uses only one Master password that will unlock the password manager

def randomPassword(characters):
    password = []
    list_alpha = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    list_numeric = list("1234567890")
    passchars = list_alpha + list_numeric
    for i in range(characters):
        random_pass = random.choice(passchars)
        password.append(random_pass)
    new_password = "".join(password)
    return new_password

PASSWORDS = {'facebook': 'VbCpEYuI9fXd16xfeqo5x4pzres4g7',
             'email': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
             'phone': '1234'}

if len(sys.argv) < 2:
    print('Usage: python password.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]      # first command line arg is the account name

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account named ' + account)

