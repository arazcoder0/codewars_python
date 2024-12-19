def hello(name = ''):
    if name:
        first_letter = name[0].upper()
        other_letters = name[slice(1, len(name))].lower()
        return "Hello, " + first_letter + other_letters + "!"
    else:
        return "Hello, World!"
    pass