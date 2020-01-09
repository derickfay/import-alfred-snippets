# import-alfred-snippets
Import snippets to Alfred 3 from a .csv file or .vim file

The csv needs to be named snippets.csv and must contain exactly three fields: the snippet name, the abbreviation, and the snippet text itself.  For example:

## Usage

Can be used to turn a tab-separated csv file into a alfredsnippets file.
For example a file `your.csv`:

```bash
any	Pan	PropTypes.any
array	Parr	PropTypes.array
arrayOf	Paro	PropTypes.arrayOf()
bool	Pbo	PropTypes.bool
element	Pel	PropTypes.element
func	Pfn	PropTypes.func
instanceOf	Pio	PropTypes.instanceOf()
node	Pno	PropTypes.node
number	Pnu	PropTypes.number
object	Pobj	PropTypes.object
objectOf	Pobo	PropTypes.objectOf()
oneOf	Poo	PropTypes.oneOf([])
oneOfType	Pot	PropTypes.oneOfType
shape	Psh	PropTypes.shape({})
string	Pst	PropTypes.string
```

Can be turned into an alfredsnippets file like this:

```bash
> ./importSnippets.py your.csv Snippets # generates Snippets.alfredsnippets
```

However it can also be used to generate an alfredsnippets file from a vim file containing declarations with digraphs.
For example a file `digraphs.vim`:

```vim
""" basic arrows
digraph -> 8594 " right arrow
digraph -< 8592 " left arrow
digraph -- 8596 " leftright

digraph /> 8603 " right neg arrow
digraph /< 8602 " left neg arrow
digraph // 8622 " leftright neg arrow

digraph => 8658 " right double arrow
digraph =< 8656 " left double arrow
digraph == 8660 " leftright double arrow

digraph F> 8655 " right double neg arrow
digraph F< 8653 " left double neg arrow
digraph FF 8654 " leftright double neg arrow
```

Can be turned into alfredsnippets like this:

```bash
> ./fromDigraphToCsv digraphs.vim Snippets # generates Snippets.alfredsnippets
```

The alfredsnippets can then be imported into Alfred 3.

**DISCLAIMERS**: This is largely untested, and doesn't escape any special characters at the moment.  As far as I can tell, it causes no problems for Alfred, but you use it at your own risk.

Released under MIT License
