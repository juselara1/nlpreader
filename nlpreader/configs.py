import nltk, json, os
from os.path import expanduser

def make_defaults():
    bindings = {
            "l": "nw",
            "h": "pw",
            "j": "wpm-",
            "k": "wpm+",
            "r": "rst",
            "p": "pause",
            "q": "quit"
            }

    colors = {
            "color1": "white",
            "color2": "red",
            "color3": "cyan",
            "tags": {
                "VB": "green",
                "VBD": "green",
                "VBG": "green",
                "VBN": "green",
                "VBP": "green",
                "VBZ": "green",
                "NN": "red",
                "NNS": "red",
                "NNP": "red",
                "NNPS": "red"
                }
            }

    defaults = {
            "spacing": 20,
            "wpm": 256,
            "mode": "clear"
            }

    home = expanduser("~")
    with open(f"{home}/.config/nlpreader/bindings.json", "w") as f:
        json.dump(bindings, f)
    
    with open(f"{home}/.config/nlpreader/colors.json", "w") as f:
        json.dump(colors, f)
    
    with open(f"{home}/.config/nlpreader/defaults.json", "w") as f:
        json.dump(defaults, f)

    nltk.download('averaged_perceptron_tagger')
