from bottle import run, route, post

class Style:
    """Python code used to create valid CSS documents."""
    def __init__(self, styles: list):
        """Creates a CSS document from a list of ObjStyles"""
        stylerepr = [x.repr for x in styles]
        self.styles = styles
        self.repr = "\n\n".join(stylerepr)
    def save(self, filename: str) -> bool:
        """Saves the CSS to a file."""
        try:
            with open(filename, 'w') as f:
                f.write(self.repr)
            return True
        except:
            return False
    def __add__(self, other):
        return Style(self.styles + other)

class ObjStyle:
    """Python code which represents CSS code which describes one particular object."""
    def __init__(self, tag: str, attributes: dict, idName = None, className = None):
        """Creates valid CSS code from the tag, attributes, and optionally, the id and classname."""
        self.tag = tag
        self.attributes = attributes
        self.id = idName
        selectorString = f"{tag}{'.' + className if className else ''}{'#' + idName if idName else ''}"
        adjustedatts = ""
        for x in attributes:
            adjustedatts += f"\t{x}: {attributes[x]};\n"
        self.repr = f"{selectorString} {{\n{adjustedatts}}}"
    def __add__(self, other) -> Style:
        return Style([self, other])

class XMLElement:
    """Python code which represents an XML Element"""
    def __init__(self, tag: str, value = '', props={}, onetag = False):
        """Creates a representation with a tag, value, and properties"""
        self.tag = tag
        self.props = props
        self.onetag = onetag
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
    def load(self, stylings: Style) -> None:
        self += XMLElement('style', stylings.repr)
    def save(self, filename: str) -> bool:
        try:
            with open(filename, 'w') as f:
                f.write(self.repr)
            return True
        except:
            return False
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

# class Form(XMLElement):
#     """Pythonic representation of a Form."""
#     def __init__(self, UI: XMLElement, serverside, r):
#         """Creates a form from a frontend and code that is to be run with the answers"""
#         super().__init__('form', props={
#             'action': r,
#             'method': 'post'
#         })
#         @route(r)
#         def UIInterface():
#             return UI.repr
#         @post(r)
#         def ServersideInterface():
#             args = request.forms
#             return serverside(args)

class Scripts:
    def __init__(self):
        self.history = []
    def runHTML(self, element: XMLElement, r: str):
        self.history.append({'name': 'runHTML', 'function': self.runHTML})
        @route(r)
        def bottleWrapper():
            return element.repr
        run()

def _main():
    p1 = ObjStyle('p', {
        'border': '1ex',
        'border-color': 'light-red'
    }, idName='paragraph1')
    p2 = ObjStyle('p', {
        'border': '2ex',
        'border-color': 'light-red'
    }, idName = 'paragraph2')
    print((p1 + p2).repr)

if __name__ == "__main__":
    _main()