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
    def findById(self, objId):
        ans = None
        try:
            if self.props['id'] == objId:
                return self
        except:
            pass
        for x in self.children:
            if type(x) == XMLElement:
                ans = x.findById(objId)
        return ans

class Form(XMLElement):
    """Pythonic representation of a Form."""
    def __init__(self, UI: XMLElement, serverside, r):
        """Creates a form from a frontend and code that is to be run with the answers"""
        super().__init__('form', props={
            'action': r,
            'method': 'post'
        })
        @route(r)
        def UIInterface():
            return UI.repr
        @post(r)
        def ServersideInterface():
            args = request.forms
            return serverside(args)

class ObjStyle:
    def __init__(self, attributes, tag, idName=None, className=None):
        self.tag = tag
        self.attributes = attributes
        self.id = idName
        selectorString = f"{tag}{'.' + className if className else ''}{'#' + idName if idName else ''}"
        adjustedatts = ""
        for x in attributes:
            adjustedatts += f"{x}: {attributes[x]};\n"
        self.repr = f"{selectorString} {self.attributes}"

class Style(XMLElement):
    def __init__(self, objstyles: list):
        super().__init__('style', "\n".join(objstyles))

class Scripts:
    def __init__(self):
        self.history = []
    def runHTML(self, element: XMLElement, r: str):
        self.history.append({'name': 'runHTML', 'function': self.runHTML})
        @route(r)
        def bottleWrapper():
            return element.repr
        run()

def main():
    client = Scripts()
    e = XMLElement
    h = e('html')
    body = e('body')
    body += e('h1', 'let\'s see if this works')
    div = e('div')
    '''
    div += Form(
        e(
            'input', 
            props={
                'name': 'WhoIAm',
                'type': 'text'
            },
            onetag=True
        ) + e(
            'input',
            props={
                'value': 'Let\'s see',
                'type': 'submit'
            }
        ),
        (lambda args:
            e('p', 'You are me!') if args.get('name') == "ME!" else e('p', 'YOU ARE NOT ME!!!')
        ),
        '/'
    )'''
    body += div
    h += body
    client.runHTML(h, '/')

if __name__ == "__main__":
    main()