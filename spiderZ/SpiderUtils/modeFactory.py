from SpiderUtils.enums import Language
from SpiderMode.chineseMode import ChineseMode
from SpiderMode.englishMode import EnglishMode
from SpiderMode.koreanMode import KoreanMode
from SpiderMode.regexMode import Regex,RegexMode

class ModeFactory:
    @staticmethod
    def get_mode(mode):
        if isinstance(mode, Language):
            return ModeFactory.get_language_mode(mode)
        elif isinstance(mode, Regex):
            return ModeFactory.get_regex_mode(mode)

    @staticmethod
    def get_language_mode(mode):
        mode_map = {Language.English: EnglishMode, Language.Chinese: ChineseMode, Language.Korean: KoreanMode}
        return mode_map.get(mode)()

    @staticmethod
    def get_regex_mode(mode):
        return RegexMode(mode)
