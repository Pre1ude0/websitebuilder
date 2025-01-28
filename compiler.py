import json
class API:
    def __init__(self, username="test"):
        self.username = username
    def read_data(self, file="test"):
        with open(f"users/{self.username}/{file}.json", "r") as f:
            #loads the text inside the user json file into "userfile"
            try:
                userfile = json.load(f)
            except json.decoder.JSONDecodeError:
                userfile = None
        return userfile
    def write_data(self, file="hi", userfile="Corrupted/no data"):
        with open(f"users/{self.username}/{file}.json", "w") as f:
            f.write(json.dumps(userfile))

if __name__ == "__main__":
    cl = API()