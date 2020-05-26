from bottle import *

class XMLElement:
    """Python code which represents an XML Element"""
    def __init__(self, tag: str, value = '', props={}, master = None, onetag=False):
        """Creates a representation with a tag, value, and properties"""
        self.tag = tag
        self.props = props
        self.onetag = onetag
        self.master = master
        self.children = [value] if type(value) != list else value
        adjustedprops = ""
        if props:
            for x in props:
                adjustedprops += x + '=' + props[x] + ' '
        if onetag:
            self.repr = f"<{tag} {adjustedprops}/>\n"
        else:
            self.repr = f"<{tag} {adjustedprops}>\n"
            for x in self.children:
                self.repr += f"\t{x}\n"
            self.repr += f"</{tag}>"
    def __repr__(self):
        return self.repr
    def __str__(self):
        return self.repr
    def __add__(self, obj):
        return XMLElement(self.tag, self.children + [obj], props = self.props, onetag=self.onetag)

def runHTML(element: XMLElement, r):
    assert(element.tag == 'html')
    @route(r)
    def bottleWrapper():
        return element.repr
    run()

def main():
    e = XMLElement
    h = e('html')
    body = e('body')
    body += e('h1', 'let\'s see if this works')
    div1 = e('div')
    div1 += e('h2', 'Vunderbar!!!')
    div1 += e('p', 'Viola!')
    body += div1
    h += body
    runHTML(h, '/')

if __name__ == "__main__":
    main()