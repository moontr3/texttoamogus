# texttoamogus
This small Python library is used for enlarging any text by converting it into amogus text characters.<br><br>
<i>Inspired by [l62.ng](https://l62.ng)</i><br>
<i>This tool is also available in [my Discord bot](https://moontr3.github.io/dabot/)</i>

### How does it work?
Basically, it converts text into a binary string, where 0 and 1 are representing different amogus text characters, and while decodind this text, converting these characters back to zeroes and ones, and then back to text.

## How to use
* <b>Step 1: </b>Download the `texttoamogus.py` file<br>
* <b>Step 2: </b>Place this file in the folder with your project<br>
* <b>Step 3: </b>Import this library in your code: 
```py
import texttoamogus
```

## Reference

### <i>function</i> `amoguser(text, encoding='utf-8')`
This function is used to convert text into amogus text characters.<br>
`unamoguser()` function should be used to convert amogused text back to normal.

| Argument | Description |
|-----|-----|
| text: <i>any</i> | Text that should be converted into amogus characters<br><i>(note that text will be converted to string in any case)</i> |
| encoding: <i>str</i> | Encoding that should be used for converting the text to binary |


### <i>function</i> `unamoguser(text, encoding='utf-8', raise_on_incorrect_text=False)`
This function is used to convert amogus text characters into text.<br>
`amoguser()` function should be used to get amogused text for this function.

| Argument | Description |
|-----|-----|
| text: <i>any</i> | Amogused text that should be converted into normal text<br><i>(note that text will be converted to string in any case)</i> |
| encoding: <i>str</i> | Encoding that should be used for converting the binary to text<br><i>(it is heavily recommended to use the same encoding as you used in amoguser() function)</i> |
| raise_on_incorrect_text: <i>bool</i> | Used for raising an exception if program detects any symbols other than amogus text characters in the text<br><i>Set to False to automatically remove unnecessary characters</i> |
