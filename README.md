# Bottle-Wrapper
This module creates a pythonic wrapper for Bottle

# Motivation
Bottle was and is my favorite web framework. But I had, since the beginning, had observed something which I didn't like: Bottle's reliance on HTML. This made bottle very bad for shell scripting and such things. Thus, I created a module which allowes XML (and by extension, HTML) documents to be easily created and run on a server. 

# Items
> Note that every single function that I have written will not raise an error. If there is a possiblity of an error happening and it happens, my functions will return a boolean with states if it succeeded or failed.

## Objects
### XMLElement
This module contains one main object: an XMLElement. By notating this with a shorthand, writing html code will be made much easier. An example will illustrate this:

```python
e = XMLElement
master = e('html')
body = e('body')
body += e('h1', 'An Example')
body += e('p', value='This is how you give objects values!')
div = e('div')
div += e('p', value='To give values to divs and other containers, you need to add other elements to it.')
body += div
master += body
runHTML(master)
```

This results in the following:
<div style="border-width: 1ex; padding: 1ex">
    <h1>An Example</h1>
    <p>This is how you give objects values!</p>
    <div>
        <p>To give values to divs and other containers, you need to add other elements to it</p>
    </div>
</div>

#### Inputs
```python
XMLElement(tag: str, value = '', props={}, onetag = False)
```

* tag: the tag's equivalent value in HTML
* value: what goes inside of the tags (if there are two tags)
* props: a dictionary of the properties the tag should have (e.g. `<div id='foo'></div>` gets turned into `e('div', props={'id': 'foo'}`))
* onetag: whether the tag should be closed in one tag or not (`<OneTag/>` compared to `<TwoTags></TwoTags>`)

#### Attributes
* `e.tag`: the element's tag
* `e.props`: a dictionary of the element's properties
* `e.onetag`: whether the tag is one tag or two
* `e.children`: the element's children; in other words, what is inside of an element
* `e.repr`: the element's HTML representation

#### Methods
* `e.findById(objId)`: finds the element with the id property set to `objId`

### Form
> Please note that this feature doesn't work yet. 

The `Form` object represents a form. It takes a frontend, with a submit button, and code to be run with the backend. 

#### Inputs
```python
Form(UI: XMLElement, serverside: function, r: str)
```

* XMLElement: the UI for the form
* serverside: a function which takes a request object and does stuff

## Style
### ObjStyle
This class contains functions for a single object. For example:
```css
div.content {
    border: 0.5ex;
    background-color: lightblue;
}
```
would be written as:
```python
ObjStyle(
    tag = 'div',
    attributes = {
        'border': '0.5ex',
        'background-color': 'lightblue'
    },
    className = 'content'
)
```

## Functions
### Running the code
As you can see in the example above, the last line is what runs the code. runHTML takes an XMLElement and runs it as HTML. 
> This module runs code by transforming it into HTML. You can access this transformation by calling `e.repr` on an XMLElement e. In fact, every element has a repr attribute