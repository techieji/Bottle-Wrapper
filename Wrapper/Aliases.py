from Core import XMLElement

class HTML(XMLElement):
    def __init__(self, value = '', props = {}):
        super().__init__('html', value, props)

class head(XMLElement):
    def __init__(self, value = '', props = {}):
        super().__init__('head', value, props)

class body(XMLElement):
    def __init__(self, value = '', props = {}):
        super().__init__('body', value, props)

class div(XMLElement):
    def __init__(self, value = '', props = {}):
        super().__init__('div', value, props)

class header(XMLElement):
    def __init__(self, degree: int, value = '', props = {}):
        super().__init__(f'h{degree}', value, props)

class p(XMLElement):
    def __init__(self, degree: int, value = '', props = {}):
        super().__init__('p', value, props)