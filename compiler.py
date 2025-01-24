import json
class API:
    def __init__(self, username="test"):
        #opens the set user file for "username" being the user token
        #for test the token is "test", file is the json opened
        with open(f"users/{username}/{username}.json", "r") as f:
            #loads the text inside the user json file into "userfile"
            userfile = json.load(f)
        #print(userfile)

class data_compiler:
    #cl_object is an object of the API class which is gonna be compiled into plain html file text
    def __init(self, cl_object):
        pass

if __name__ == "__main__":
    API()