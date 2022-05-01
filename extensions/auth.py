import json
import sys

sys.path.append("..")


import json_edit
import args



logged_in = False

def login(argv):
    json_dict = json_edit.fetch(".auth")
    json_dict["logged_in"] = True
    _ = json_edit.edit(json_dict, ".auth")

def logout(argv):
    json_dict = json_edit.fetch(".auth")
    json_dict["logged_in"] = False
    _ = json_edit.edit(json_dict, ".auth")

logout("")