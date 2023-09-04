def indent(s: str, width: int) -> str:
    return''* (max(0, width - len(s))) + s
print(indent('123', 123))



def functionn(s: str = '') -> int:
    return len(s)

def functionnn(a:list, b:list) -> int:
        return (max(len(a), len(b))
                
