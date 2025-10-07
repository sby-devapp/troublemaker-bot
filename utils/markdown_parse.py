
def escape_markdown(text: str) -> str:
    import re
    return re.sub(r'([_*\[\]()~`>#+\-=|.!])', r'\\\1', text)