import os
import json


def setup(folder_name: str, subFolder_name: str, file_name: str, data_to_save, json_info_name: str):
    # This will do all actions needed for a proper setup
    try:
        if create_files(folder_name, subFolder_name, file_name):
            print("\n\nSuccessfully created files\n\n")
        if save_files(folder_name, subFolder_name, file_name, data_to_save, json_info_name, True):
            print("\n\nSuccessfully saved files\n\n")
        if load_files(folder_name, subFolder_name, file_name, data_to_save, False):
            print("\n\nSuccessfully loaded files\n\n")

        print("\n\nSetup finished, everything is working as intended\n\n")
    except:
        print("\n\nSetup failed to work... Try creating files via function\n\n")


def create_files(folder_name: str, subFolder_name: str, file_name: str):
    cur = os.getcwd()
    try:
        os.mkdir(f"{cur}\\{folder_name}")
        print(f"\n{folder_name} file created\n")
    except (FileNotFoundError, FileExistsError):
        cur = os.getcwd()

    try:
        os.mkdir(f"{cur}\\{folder_name}\\{subFolder_name}")
        print(f"\n{subFolder_name} file created\n")
    except (FileNotFoundError, FileExistsError):
        cur = os.getcwd()

    cur = os.getcwd()
    # os.chdir(f"{cur}\\{name}\\userData")
    create_files_save(cur, folder_name, subFolder_name, file_name)
    # Add code here for creating individual files
    # Eg: Tutorial.txt
    try:
        os.mkdir(f"{cur}\\{folder_name}\\{subFolder_name}")
        print(f"\n{folder_name} folder file created\n")
    except (FileNotFoundError, FileExistsError):
        cur = os.getcwd()

    try:
        os.mkdir(f"{cur}\\{folder_name}\\{subFolder_name}")
        print(f"\n{subFolder_name} folder file created\n")
    except (FileNotFoundError, FileExistsError):
        cur = os.getcwd()


def create_files_save(cur, folder_name, subF_name, file_name):
    file = f"{cur}\\{folder_name}\\{subF_name}\\{file_name}.json"
    isreal = os.path.isfile(file)

    if isreal is False:
        try:
            with open(file, "w") as f:
                f.write("")
            print(f"\n{file_name}.json file created\n")
        except:
            cur = os.getcwd()


def save_files(folder_name: str, subF_name: str, file_name: str, data, data_save_name: str, txt_output: True):
    save_dic = {}
    cur = os.getcwd()
    file = f"{cur}\\{folder_name}\\{subF_name}\\{file_name}.json"
    # Saves data via dictionary - {'Game_Info': game_info}
    save_dic[data_save_name] = data
    # try:
    with open(file, 'w') as f:
        f.write(json.dumps(save_dic))

# Keep loading system in main py file
def load_files(folder_name, sub_folder, file_name, data_var, list_value):
    cur = os.getcwd()
    file = f"{cur}\\{folder_name}\\{sub_folder}\\{file_name}.json"
    database_list = []
    database_lName = []

    try:
        with open(file, "r") as g:
            data = json.load(g)
            for e_name in data:
                sub_name = data[e_name]
                for sub_info in sub_name:
                    value = sub_name[sub_info]
                    if list_value is True:
                        for platform, password in value:
                            data_var[sub_info] = (platform, password)
                            database_list.append((sub_info, platform, password))
                        database_lName.append(sub_info)
                    elif list_value is False:
                        data_var[sub_info] = (sub_info, value)
                        database_list.append((sub_info, "", value))
                        database_lName.append(sub_info)

                    elif sub_info in data_var:
                        data_var[sub_info] = value

            # print("\n\nData Loaded\n")
            return data_var, database_list, database_lName
    except:
        print(f"\n{'-'*50}\n")
