#	Swiftnotes Export

##	Description
Quick and dirty Python application to export notes from the apparently unsupported or
feature-complete (depending on how you look at it) Android app [Swiftnotes] to separate text files
in a local directory.

##	Installation
Clone this repository:

```bash
git clone <URL> swiftnotes_export
cd swiftnotes_export
```

##	Usage
The project is a runnable Python module:

```bash
python -m swiftnotes_export
```

Arguments:
```
Quick and dirty utility to export notes from Swiftnotes to a path of files

Usage:
    swiftnotes_export [options]

Options:
    -i, --input-file=PATH      Path to the Swoftnotes export JSON [default: swiftnotes_backup.json]
    -o, --output-dir=PATH      Target directory where notes should be exported as files
                               [default: out]
    -e, --extension=EXTENSION  Extension of the output files. Assumes markdown [default: md]
    -h, --help                 Print this help text and exit
```

##	Contributing
Feel free to fork this project and suggest features or bug fixes.


##	Authors and acknowledgment
Readme based on <https://www.makeareadme.com/>

Acknowledgements to the original authors of [Swiftnotes], which has served me well for many years.


##	License
[LICENSE]


##	Project status
So simple that it probably doesn't need any more work.


[Swiftnotes]: https://github.com/adrianchifor/Swiftnotes

[LICENSE]: ./LICENSE

