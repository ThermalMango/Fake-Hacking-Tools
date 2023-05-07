from saveData import setup, load_files, save_files
import os
import random as r
from time import sleep as s
from colorama import init
from termcolor import colored

init()

version = "v0.0.201"

save_locations = [("save_data", "password_cracker", "passwords", "Passwords"),
                  ("save_data", "password_cracker", "emails", "Emails")]


class FakeHackingTools:
    def __init__(self):
        # Vars
        ## Booter vars
        self.host = ""
        self.attacks = 250

        ## Password Cracker vars
        self.database = []
        self.passwords = []
        try:
            self.load_passwords()
        except FileNotFoundError:
            print("\nError loading passwords...\npasswords.txt not found\n")
        self.social_medias = ["Youtube", "Twitter", "Instagram", "Facebook", "Snapchat"]
        self.cracking_methods = ["in archives", "in hacking forms", "in data breaches", "by taking a wild guess",
                                 "by brute force"]
        self.d_name = ""

        self.username = ""
        self.password = {}
        self.email = {}
        self.email_at = ["gmail", "outlook", "yahoo", "email"]
        self.email_dot = [".com", ".ca", ".org", ".net", ".io"]
        self.user_ip = {}
        self.user_location = {}

        if not os.path.exists("save_data\password_cracker"):
            setup("save_data", "password_cracker", "database", self.password, "Passwords")

        self.load_data()
        self.main_menu()

    # def remove_dupes(self, x: list):
    #     new_data = []
    #     for num in range(len(x)):
    #         new_data.append(list(dict.fromkeys(self.database[num])))
    #     return new_data

    def load_data(self):
        try:
            self.password, self.d_name = load_files(save_locations[0][0], save_locations[0][1], save_locations[0][2], self.password, True)[0], \
                                         load_files(save_locations[0][0], save_locations[0][1], save_locations[0][2], self.password, True)[2]
            self.database.append(load_files(save_locations[0][0], save_locations[0][1],save_locations[0][2], self.password, True)[1])

            self.email = load_files(save_locations[1][0], save_locations[1][1], save_locations[1][2], self.email, False)[0]
            self.database.append(load_files(save_locations[1][0], save_locations[1][1], save_locations[1][2], self.email, False)[1])
        except TypeError:
            return

    def main_menu(self):
        while True:
            print(colored(f"\n\nFake Hacking Tools {version}\n'Quit [q]' - Quits the program\n'Booter [b]' - "
                          "Opens the Booter menu\n'Password Cracker [pc]' - Opens password cracker menu'\n", "white"))
            option = input("").lower()
            if option == "quit" or option == "q":
                quit()
            elif option == "booter" or option == "b":
                self.fake_booter_menu()
            elif option == "password cracker" or option == "pc":
                self.fake_PSWC_menu()

    def saveData(self, info, data, text):
        # Main folder  Sub folder  File name  Data  Data var name
        save_files(info[0], info[1], info[2], data, info[3], text)

    def get_database(self):
        print(colored("\n=========================\nDatabase\n=========================", "red"))
        for name in self.d_name:
            print(colored(f"{name}:", "yellow"))
            for num in range(len(self.database)):
                data = self.database[num]
                # print(f"{data}\n\n{data[0]}\n\n{data[0][0]}\n\n{data[0][1]}")
                if not data[0][1] == "":
                    for name, platform, value in self.database[num]:
                        print(colored(f"{platform}: {value}", "white"))
                elif data[0][1] == "":
                    print(colored(f"Email: {data[0][2]}", "white"))

            print("\n")
        input("Press enter to continue...")
    # Ip generator

    def ip_generator(self, amount):
        ip_list = []
        for x in range(amount):
            ip_list.append(f"{r.randint(1, 255)}.{r.randint(0, 255)}.{r.randint(0, 255)}.{r.randint(0, 255)}")
        return ip_list
    # Fake Password Cracker

    def load_passwords(self):
        with open('passwords.txt', 'r') as f:
            _passwords = f.readlines()
            for password in _passwords:
                c_pw = password.split('\n')
                self.passwords.append(c_pw[0])

    def fake_PSWC_menu(self):
        while True:
            print(colored(f"\nPassword Cracker\n'Back [b]' - Bring you back to the main menu\n'Username [un]' - "
                          f"{self.username}\n'Start [s]' - Start cracking username\n'Database [d]' - Opens the database",
                          "white"))
            option = input("").lower()
            if option == "back" or option == "b":
                return
            elif option == "username" or option == "un":
                self.username = self.get_username()
            elif option == "start" or option == "s":
                if not self.username == "":
                    self.fake_PSWC()
                else:
                    print("\nAdd a username to start cracking\n")
            elif option == "database" or option == "d":
                self.get_database()

    def get_username(self):
        return input(f"\n\nEnter username ({self.username}): ")

    def social_media_check(self):
        confirmed = []
        for social in self.social_medias:
            s(1.5)
            percent = r.randint(1, 4)
            if percent < 4 > 1:
                print(f'{colored("Found", "yellow")} {colored(self.username, "white")} {colored("on", "yellow")} '
                      f'{colored(social, "white")}')
                confirmed.append(social)

            elif percent == 4:
                print(f'{colored(self.username, "white")} {colored("not found on", "yellow")} '
                      f'{colored(social, "white")}')
        print("\n")
        return confirmed

    def get_passwords(self, platforms):
        self.password[self.username] = {}
        for platform in platforms:
            while True:
                for method in self.cracking_methods:
                    if method == self.cracking_methods[4]:
                        print(
                            f"{colored('Obtaining password for', 'yellow')} {colored(f'''{self.username}''', 'white')} "
                            f"{colored('on', 'yellow')} {colored(platform, 'white')} {colored(f'{method}...', 'yellow')}")
                        s(2)
                        pword = r.choice(self.passwords)
                        print(f"\n{colored('Obtained password:', 'yellow')} {colored(f'''{pword}''', 'white')} "
                              f"{colored('for', 'yellow')} {colored(f'''{self.username}'s {platform}''', 'white')} {colored(method, 'yellow')}\n")
                        self.password[self.username] = {platform, pword}
                        break
                    else:
                        print(f"{colored('Searching for', 'yellow')} {colored(f'''{self.username}'s''', 'white')} "
                              f"{colored('password for', 'yellow')} {colored(f'{platform}', 'white')} {colored(f'{method}...', 'yellow')}")
                        chance = r.randint(1, 3)
                        s(2)
                        if chance == 1:
                            pword = r.choice(self.passwords)
                            print(f"\n{colored('Obtained password:', 'yellow')} {colored(f'''{pword}''', 'white')} "
                                  f"{colored('for', 'yellow')} {colored(f'''{self.username}'s {platform}''', 'white')} {colored(method, 'yellow')}\n")
                            self.password[self.username] = {platform, pword}
                            s(1.5)
                            break
                        elif chance > 1:
                            print(f"{colored('Failed to find', 'yellow')} {colored(f'''{self.username}'s''', 'white')} "
                                  f"{colored('password for', 'yellow')} {colored(platform, 'white')} {colored(f'{method}', 'yellow')}")
                            s(1.2)
                break

    def get_email_simple(self):
        self.email[self.username] = ""
        if " " in self.username:
            new_username = self.username.replace(" ", "_")
        else:
            new_username = self.username
        user_email = f"{new_username}{r.randint(0, 9999)}@{r.choice(self.email_at)}{r.choice(self.email_dot)}"
        self.email[self.username] = user_email
        print(f"\n\n{colored('Searching', 'yellow')} {colored(f'''{self.username}'s''', 'white')} {colored('socials for email...', 'yellow')}")
        s(3)
        print(f"\n{colored('Obtained email:', 'yellow')} {colored(user_email, 'white')} {colored('for account', 'yellow')} {colored(self.username, 'white')}")
        s(2)
        return

    # get_email_adv - Planned

    def fake_PSWC(self):
        print(f"\n{colored('Searching for', 'yellow')} {colored(self.username, 'white')} "
              f"{colored('on social medias...', 'yellow')}")

        s(3)
        socials = self.social_media_check()
        if not socials:
            print(f'{colored("No social media found for", "yellow")} {colored(self.username, "white")}')
            return
        s(1)
        self.get_passwords(socials)
        self.get_email_simple()
        self.saveData(save_locations[0], self.password, False)
        self.saveData(save_locations[1], self.email, False)
        # save_files(save_locations[0][0], save_locations[0][1], save_locations[0][2], [(self.password, save_locations[0][3]), (self.email, save_locations[1][3])], [''])
        # print(self.password)

    # Fake Booter
    def fake_booter_menu(self):
        while True:
            print(colored(f"\nIP/Website Booter\n'Back [b]' - Brings you back to the main menu\n'Host [h]' - "
                          f"{self.host}\n'Attacks [a]' - {self.attacks}\n'Start [s]' - Start the attacks\n", "white"))
            option = input("").lower()
            if option == "back" or option == "b":
                return
            elif option == "host" or option == "h":
                self.host = self.get_host()
            elif option == "attacks" or option == "a":
                attacks = self.get_attacks()
                if not int(attacks.isnumeric()):
                    self.attacks = 250
            elif option == "start" or option == "s":
                if not self.host == "":
                    self.fake_booter()
                else:
                    print("\nAdd a host to start attacking\n")

    def get_attacks(self):
        return input(f"\n\nEnter the number of attacks ({self.attacks}): ")

    def get_host(self):
        return input(f"\n\nEnter host ({self.host}): ")

    def fake_booter(self):
        for attack in range(int(self.attacks)):
            ip = self.ip_generator(1)
            print(f"{colored('Used', 'yellow')} {colored(ip[0], 'white')} {colored('to DDoS', 'yellow')} "
                  f"{colored(self.host, 'white')}")
            s(0.025)
        print("\nAttacks completed!\n")


if __name__ == "__main__":
    app = FakeHackingTools()
    app.main_menu()
