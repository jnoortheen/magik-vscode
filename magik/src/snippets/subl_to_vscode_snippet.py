"""This module will help to covert smallworld auto-completion file to VS Code snippet interactively"""
import json
import os
from vs_code_snip_modal import VSCodeSnip

# "define_exemplar": "_pragma(classify_level=${1:basic}, topic={${2:basic}}, usage={${3:basic}})\ndef_slotted_exemplar(:${4:class_name},\n\t##\n\t## $5\n\t##\n\t{\n\t\t$6\n\t}${7:,\n\t{${8:parent_classes}}}\n)\n\\$\n",
def main():
    # get the target snippet file name
    fname = raw_input("Enter a name for the target snippet file[magik]: ") or "magik"
    if not fname.endswith(".json"):
        fname += ".json"

    # get the source file name
    srcName = raw_input("Enter the path to the sublime formatted text file[completions.json]: ", ) or "completions.json"
    if not os.path.exists(srcName) or not os.path.isfile(srcName):
        raise Exception("Check source file path")

    with open(fname, "w") as f, open(srcName) as srcFile:
        fdict = json.loads(srcFile.read())
        rsltDict = dict()
        for snip in fdict:
            vs_snip = VSCodeSnip(snip, fdict[snip])
            rsltDict[vs_snip.name] = vs_snip.to_dict()

        f.write(json.dumps(rsltDict, indent=2))

if __name__ == '__main__':
    main()
