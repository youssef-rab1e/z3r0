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
}

@dataclass
class Token:
    value: str
    type: TokenType

def isskipper(src: str):
    return src == " " | src == "\n" | src == "\t"

def crt_token(value: str, type: TokenType):
    return {value , type}

def isalpha(src: str):
    return src.upper() != src.lower()

def isnum(src: str) -> bool:
    return src[:1].isdigit()

def tokenize(SourceCode: str):
    """Takes Src and Outputs a list Tokens"""
    tokens = []
    src = SourceCode.split("")
    # Handle Single Char Tokens
    while src.__len__ > 0:
        if src[0] == "(":
          token = crt_token(src.pop(0) , TokenType.OPENPARENTHESIS)
          tokens.append(token)
        elif src[0] == ")":
          token = crt_token(src.pop(0), TokenType.CLOSEPARENTHESIS)
          tokens.append(token)
        elif src[0] == "[":
          token = crt_token(src.pop(0), TokenType.OPENBRACKET)
          tokens.append(token)
        elif src[0] == "]":
          token = crt_token(src.pop(0), TokenType.CLOSEBRACKET)
          tokens.append(token)
        elif src[0] == "{":
          token = crt_token(src.pop(0), TokenType.OPENCURLY)
          tokens.append(token)
        elif src[0] == "}":
          token = crt_token(src.pop(0), TokenType.CLOSECURLY)
          tokens.append(token)
        elif src[0] == "+" | src[0] == "-" | src[0] == "*" | src[0] == "/":
          token = crt_token(src.pop(0), TokenType.OPERATOR)
          tokens.append(token)
        elif src[0] == "=":
          token = crt_token(src.pop(0), TokenType.EQUALS)
          tokens.append(token)
        elif src[0] == "true" | src[0] == "false":
          token = crt_token(src.pop(0), TokenType.BOOLEAN)
          tokens.append(token)
        elif src[0] == ",":
          token = crt_token(src.pop(0), TokenType.COMA)
          tokens.append(token)
        elif src[0] in [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 0]:
          token = crt_token(src.pop(0), TokenType.NUMBER)
          tokens.append(token)
        else :
          # Here We Will Handle MultiChar tokens Or Unkown Ones
          if isnum(src[0]):
            num = ""
            while src.__len__ > 0 and isnum(src[0]):
              num += src.pop(0)
            tokens.append(crt_token(num, TokenType.NUMBER))
          elif isalpha(src[0]):
            identifier = ""
            while src.__len__ > 0 and isalpha(src[0]):
              identifier += src.pop(0)
            # Check for reserved keywords
            reserved = KEYWORDS.get(identifier)
            if reserved ==  None:
              tokens.append(crt_token(identifier, TokenType.IDENTIFIER))
            else:
              tokens.append(crt_token(identifier, reserved))
          elif isskipper(src[0]):
            src.pop(0)
          else:
            print(f"Unrecognized Character Found in Source: {src[0]}")
            exit(1)
    return tokens

