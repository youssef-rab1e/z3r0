# z3r0 Lexer
from enum import Enum
from dataclasses import dataclass

#Token Types
class TokenType(Enum):
    NUMBER = "NUMBER"
    IDENTIFIER = "IDENTIFIER"
    STRING = "STRING"    
    EQUALS = "EQUALS" #
    COMA = "COMA" #
    OPERATOR = "OPERATOR" #
    KEYWORD = "KEYWORD"
    BOOLEAN = "BOOLEAN" #
    OPENPARENTHESIS = "OPENPARENTHESIS" #
    CLOSEPARENTHESIS = "CLOSEPARENTHESIS" #
    OPENBRACKET = "OPENBRACKET" #
    CLOSEBRACKET = "CLOSEBRACKET" #
    OPENCURLY = "OPENCURLY"    #
    CLOSECURLY = "CLOSECURLY"    #


@dataclass
class Token:
    value: str
    type: TokenType


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
          # Here We Will Handle MultiChar tokens

          pass
    return tokens