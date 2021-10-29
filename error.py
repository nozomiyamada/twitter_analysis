CORRECT_DICT = {
    'ราษฏร':'ราษฎร',
    'ม๊อบ':'ม็อบ'
}

def correct(text):
    for k,v in CORRECT_DICT.items():
        text = text.replace(k, v)
        
    return text