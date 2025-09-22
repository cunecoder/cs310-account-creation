# File: account_creation.py
# Author: David Marin
# Created: 9/21/2025
# Description: Python script that prompts the user for a full name and role.
#              The script then configures the user's account based on their
#              answers.
#
# IMPORTANT NOTE: This script should be run inside of a WSL terminal

import subprocess

def get_role():
    ''' Get user input for account role. '''

    role = input("\nPlease choose a role from the list... \n"
    "(U)   User\n" \
    "(AVT) AV Tech\n" \
    "(A)   Admin\n" \
    "Role: ")

    return role


def role_confirmation(role):
    ''' Confirm the user's linux role. '''
    
    choice = ''

    while choice.lower() != 'y':
        
        role = get_role()
        
        if role == 'U':
            choice = input(f'\nYour linux account is about to be created with no default groups (basic user).\n' +
                           'Please enter (Y) to confirm your choice or (N) to re-select a role: ')
        elif role == 'AVT':
            choice = input(f'\nYour linux account is about to be created with the video/audio groups (AV Tech).\n' +
                    'Please enter (Y) to confirm your choice or (N) to re-select a role: ')
        elif role == 'A':
            choice = input(f'\nYour linux account is about to be created with the admin group (Admin).\n' +
                    'Please enter (Y) to confirm your choice or (N) to re-select a role: ')

    return role

def create_acc(role, username):
    ''' Create a linux account with the user-chosen role. '''

    if role == 'U':
        subprocess.run(['sudo', 'useradd', '-m', username])
        subprocess.run(['sudo', 'passwd', username])
    elif role == 'AVT':
        subprocess.run(['sudo', 'useradd', '-m', '-G', 'audio,video', username])
        subprocess.run(['sudo', 'passwd', username])
    elif role == 'A':
        subprocess.run(['sudo', 'useradd', '-m', '-G', 'root', username])
        subprocess.run(['sudo', 'passwd', username])


def main():
    name = input("Please enter your full name: ")
    name = name.lower()
    name = name.split()
    username = str(name[0] + '-' + name[-1])

    role = ''
    role = role_confirmation(role)

    create_acc(role, username)

    print(f"\nAccount automation complete. Your account '{username}' is now created with the specified role! :-)")

if __name__ == "__main__":
    main()