# Bottle-Wrapper
This module creates a pythonic wrapper for Bottle

# Motivation
Bottle was and is my favorite web framework. But I had, since the beginning, had observed something which I didn't like: Bottle's reliance on HTML. This made bottle very bad for shell scripting and such things. Thus, I created a module which allowes XML (and by extension, HTML) documents to be easily created and run on a server. 

# Items
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

#### Inputs
```python
XMLElement(tag: str, value = '', props={}, master = None, onetag=False)
```

* tag: the tag's equivalent value in HTML
* value: what goes inside of the tags (if there are two tags)
* props: a dictionary of the properties the tag should have (e.g. `<div id='foo'></div>` gets turned into `e('div', props={'id': 'foo'}`))
* master: DON'T USE
* onetag: whether the tag should be closed in one tag or not (<OneTag/> compared to <TwoTags></TwoTags>)

## Functions
### Running the code
As you can see in the example above, the last line is what runs the code. runHTML takes an XMLElement and runs it as HTML. 