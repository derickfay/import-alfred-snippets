# import-alfred-snippets
Import snippets to Alfred 3 from a .csv file

The csv needs to be named snippets.csv and must contain exactly three fields: the snippet name, the abbreviation, and the snippet text itself.

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

when the script is run, it will generate individual files with names like *any [8760badff15c594b6308564f4460e7].json* , where the text in brackets is a random string generated as the uid (used by Alfred to track usage)

Quit Alfred 3, move the newly generated files to .../Alfred.alfredpreferences/snippets/*groupname* where groupname is the group where you want the snippets.  Creating a new folder will create a new group in Alfred.

**DISCLAIMERS**: This is largely untested, and doesn't escape any special characters at the moment.  As far as I can tell, it causes no problems for Alfred, but you use it at your own risk.
