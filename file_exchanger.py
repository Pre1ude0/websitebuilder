import json
import os
class API:
    def __init__(self, dir_folder="test", enable_logs=True):
        self.dir_folder = dir_folder
        self.file_dir = f"{os.getcwd()}/users/{self.dir_folder}"
        self.enable_logs = enable_logs

    # READ DATA BLOCK

    # loads the LOCAL json file
    def read_json(self, file="test"):

        # checks if there's such a file

        if file+".json" in os.listdir(self.file_dir):
            with open(f"users/{self.dir_folder}/{file}.json", "r") as f:

                # loads the text inside the user json file into "returndata"
                # ts (this) is a safeproof for crashing because json module is stupid
                # , so it will crash if the json file is empty while reading

                try:
                    # tries loading the json file

                    returndata = json.load(f)

                except json.decoder.JSONDecodeError:

                    # makes the returndata None so that the user doesn't get anything in return
                    # instead of the program crashing

                    returndata = None

                    # heh... it feels good knowing I saved python city again...heh........
                if returndata is None:
                    # informs the user that the json file selected is empty

                    if self.enable_logs: print(f'WARNING: json file "{file}" has nothing inside')

                    returndata = None
        else:

            # Informs that there is no such file in the folder and sets the returndata to None

            if self.enable_logs: print(f'No such file "{file}"')
            returndata = None

        # returns whichever data got fetched (data or None if there's nothing inside the file)

        return returndata

    # reads the html LOCAL html file
    def read_html(self, file="test"):

        # checks if there's such a file

        if file+".html" in os.listdir(self.file_dir):
            with open(f"users/{self.dir_folder}/{file}.html", "r") as f:

                # writes the data inside the file

                returndata = f.read()
                if returndata == "":

                    # informs the user that the html file selected is empty

                    if self.enable_logs: print(f'WARNING: html file "{file}" has nothing inside')

                    # makes the returndata None so that the user doesn't get anything in return

                    returndata = None
        else:

            # Informs that there is no such file in the folder and sets the returndata to None

            if self.enable_logs: print(f'No such file "{file}" in the folder')
            returndata = None

        # returns whichever data got fetched (data or None if there's nothing inside the file)

        return returndata

    # WRITE DATA BLOCK

    # writes data over to the LOCAL json files
    def write_json(self, data=None, file="test"):
        with open(f"users/{self.dir_folder}/{file}.json", "w") as f:
            if data is None:
                f.write("")
            else:
                f.write(json.dumps(data))

    # writes the html file to the local files
    def write_html(self, data=None, file="test"):
        with open(f"users/{self.dir_folder}/{file}.html", "w") as f:
            if data is None:
                f.write("")
            else:
                f.write(data)


    def exec_func(self, command):
        command_list = ["rj", "rh", "wj", "wh"]
        if "command" not in locals():
            command = input(com for com in command_list)

        while command not in command_list:
            print("Not a valid func name")
            command = input(com for com in command_list)

        if command == "wj":
            self.write_json()
if __name__ == "__main__":
    cl = API()
    cl.exec_func()