def addParagraphTags(string):
    if "\n" in string:
        strings = string.replace("  ", "").split("\n")
        del strings[0:1]
        del strings[-1]

        stringPieces = []

        for current in strings:
            current = "<p>" + current + "</p>"
            stringPieces.append(current)

        return "".join(stringPieces)
    return "<p>" + string + "</p>"
