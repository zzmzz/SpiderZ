from enums import Language


class SpiderStrategy:
    url = ""
    depth = 1
    is_out = False
    pattern = None
    language = Language.All

    def __init__(self, url = "", depth=1, is_out=False, pattern=None, language=Language.All):
        self.url = url
        self.depth = depth
        self.is_out = is_out
        self.pattern = pattern
        self.language = language
