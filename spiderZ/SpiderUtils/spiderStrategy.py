from enums import Language


class SpiderStrategy:
    url = ""
    depth = 1
    is_out = False
    pattern = None
    mode = Language.Chinese

    # url: website url
    # depth: depth of the crawl
    # is_out: whether the crawl go outside the domain
    def __init__(self, url = "", depth=1, is_out=False, pattern=None, mode=Language.Chinese):
        self.url = url
        self.depth = depth
        self.is_out = is_out
        self.pattern = pattern
        self.mode = mode
