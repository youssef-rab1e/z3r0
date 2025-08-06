# z3r0 Lexer
from enum import Enum
from dataclasses import dataclass

#Token Types
class TokenType(Enum):
    NUMBER = "NUMBER" 
    IDENTIFIER = "IDENTIFIER"  
    EQUALS = "EQUALS" 
    COMA = "COMA" 
    OPERATOR = "OPERATOR" 
    BOOLEAN = "BOOLEAN" 
    OPENPARENTHESIS = "OPENPARENTHESIS" 
    CLOSEPARENTHESIS = "CLOSEPARENTHESIS" 
    OPENBRACKET = "OPENBRACKET" 
    CLOSEBRACKET = "CLOSEBRACKET" 
    OPENCURLY = "OPENCURLY"    
    CLOSECURLY = "CLOSECURLY" 
    LETTOKEN = "LETTOKEN" 
   

KEYWORDS: dict[str, TokenType] = {
    "let": TokenType.LETTOKEN,
    "true": TokenType.BOOLEAN,
    "false": TokenType.BOOLEAN,
}

@dataclass
class Token:
    value: str
    type: TokenType

def isskipper(src: str):
    return src == " " or src == "\n" or src == "\t"

def crt_token(value: str, type: TokenType):
    return Token(value, type)

def isalpha(src: str):
    return src.upper() != src.lower()

def isnum(src: str) -> bool:
    return src.isdigit()

def tokenize(SourceCode: str):
    """Takes Src and Outputs a list Tokens"""
    tokens = []
    src = list(SourceCode)
    
    while len(src) > 0:
        # Skip whitespace
        if isskipper(src[0]):
            src.pop(0)
            continue
            
        # Handle single character tokens
        if src[0] == "(":
            tokens.append(crt_token(src.pop(0), TokenType.OPENPARENTHESIS))
        elif src[0] == ")":
            tokens.append(crt_token(src.pop(0), TokenType.CLOSEPARENTHESIS))
        elif src[0] == "[":
            tokens.append(crt_token(src.pop(0), TokenType.OPENBRACKET))
        elif src[0] == "]":
            tokens.append(crt_token(src.pop(0), TokenType.CLOSEBRACKET))
        elif src[0] == "{":
            tokens.append(crt_token(src.pop(0), TokenType.OPENCURLY))
        elif src[0] == "}":
            tokens.append(crt_token(src.pop(0), TokenType.CLOSECURLY))
        elif src[0] in "+-*/":
            tokens.append(crt_token(src.pop(0), TokenType.OPERATOR))
        elif src[0] == "=":
            tokens.append(crt_token(src.pop(0), TokenType.EQUALS))
        elif src[0] == ",":
            tokens.append(crt_token(src.pop(0), TokenType.COMA))
        # Handle multi-character tokens
        elif isnum(src[0]):
            num = ""
            while len(src) > 0 and isnum(src[0]):
                num += src.pop(0)
            tokens.append(crt_token(num, TokenType.NUMBER))
        elif isalpha(src[0]):
            identifier = ""
            while len(src) > 0 and isalpha(src[0]):
                identifier += src.pop(0)
            # Check for reserved keywords
            reserved = KEYWORDS.get(identifier)
            if reserved is None:
                tokens.append(crt_token(identifier, TokenType.IDENTIFIER))
            else:
                tokens.append(crt_token(identifier, reserved))
        else:
            print(f"Unrecognized Character Found in Source: {src[0]}")
            exit(1)
    return tokens

# Test the lexer
if __name__ == "__main__":
    test_input = "let x = 564"
    print(f"Input: {test_input}")
    tokens = tokenize(test_input)
    print(f"Number of tokens: {len(tokens)}")
    print(tokens)