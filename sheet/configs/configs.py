from .. import configs

def allConfigs():
    module = __import__("sheet")
    module = getattr(module, "configs")

    ret = {}
    for character in configs.__all__:
        current = getattr(module, character)
        ret[character] = current

    return ret
        
