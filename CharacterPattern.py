class CharacterPattern():

    omitted_chars = []
    allowed_chars = []

    def __init__(self):
        pass

    def append_omitted_char(self, ch):
        self.omitted_chars.append(ch)
    
    def remove_omitted_char(self, ch):
        self.omitted_chars.remove(ch)

    def append_allowed_char(self, ch):
        self.allowed_chars.append(ch)
    
    def remove_allowed_chat(self, ch):
        self.allowed_chars.remove(ch)
    
    def getPattern(self) -> str:
        omitted_char_pattern = '[^{}]'.format(''.join(self.omitted_chars))
        allowed_chars_pattern = '[{}]'.format(''.join(self.allowed_chars))

        return '({}|{})'.format(omitted_char_pattern, allowed_chars_pattern)


