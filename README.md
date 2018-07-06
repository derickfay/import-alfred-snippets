# import-alfred-snippets
Import snippets to Alfred 3 from a .csv file

The csv needs to be named snippets.csv and must contain exactly three fields: the snippet name, the abbreviation, and the snippet text itself.  For example:

```bash

"any","Pan","PropTypes.any"
"array","Parr","PropTypes.array"
"arrayOf","Paro","PropTypes.arrayOf()"
"bool","Pbo","PropTypes.bool"
"element","Pel","PropTypes.element"
"func","Pfn","PropTypes.func"
"instanceOf","Pio","PropTypes.instanceOf()"
"node","Pno","PropTypes.node"
"number","Pnu","PropTypes.number"
"object","Pobj","PropTypes.object"
"objectOf","Pobo","PropTypes.objectOf()"
"oneOf","Poo","PropTypes.oneOf([])"
"oneOfType","Pot","PropTypes.oneOfType"
"shape","Psh","PropTypes.shape({})"
"string","Pst","PropTypes.string"

```

## Usage

Save the file **importSnippets.py** to a location of your choice - this should probably be a temporary folder because 
when the script is run, it will generate a file for each snippet.

Save your snippets in a csv file called **snippets.csv** as descibed above, in the same directory where you put the script.

To run the script, open a Terminal window in the same directory where you put the script, then at the prompt, type:

**python ./importSnippets.py**

If all goes well, you should then have individual files in the same directory with names like *any [8760badff15c594b6308564f4460e7].json* , where the text in brackets is a random string generated as the uid (used by Alfred to track usage).

Move the newly generated files to .../Alfred.alfredpreferences/snippets/*groupname* where groupname is the group where you want the snippets.  Creating a new folder will create a new group in Alfred.  After a few seconds, the new snippets willl appear in Alfred's preferences.  (To view this folder in Finder, you'll need to find your Alfred.alfredpreferences file

You can then delete or replace **snippets.csv** and start again.

I have occasionally had errors where the csv library used by the script thinks there are line breaks midway through a field -- the easiest fix I've found is to open snippets.csv in Excel, then save it as csv.

**DISCLAIMERS**: This is largely untested, and doesn't escape any special characters at the moment.  As far as I can tell, it causes no problems for Alfred, but you use it at your own risk.

Released under MIT License
