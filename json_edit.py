import json

def fetch(filename):
    rfile = open(filename, "r")
    text = json.load(rfile)
    rfile.close()
    return text

def edit(text_dict, filename):
    wfile = open(filename, "w")
    json.dump(text_dict, wfile, indent=4, sort_keys=True)
    wfile.close()
    return True