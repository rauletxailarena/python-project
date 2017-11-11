substitutions = {
"witness": "dude I know",
"witnesses": "theese dudes I know",
"new study": "tumbler post",
"rebuild": "avenge",
"space": "spaaaace",
"google glass": "Virtual Boy",
"smartphone": "Pokédex",
"electric": "atomic",
"car": "cat",
"cars": "cats",
"election": "eating contest",
"congressional leaders": "river spirits",
"homeland security": "homestar runner",
"could not be reached for comment": "is guilty and everyone knows it"
}

def substitute_word(word):
    return substitutions[word]


def contains_keyword(phrase):
    phrase = phrase.split()
    for word in phrase:
        if (word in substitutions):
            return True
    else:
        return False


def is_keyword(word):
    if (word in substitutions):
        return True
    else:
        return False

def substitute_keywords(phrase):
    if contains_keyword(phrase):
        new_phrase = ""
        phrase = phrase.split()
        for word in phrase:
            if is_keyword(word):
                new_phrase += " "
                new_phrase += substitutions[word]
            else:
                new_phrase += " "
                new_phrase += word
        return new_phrase
