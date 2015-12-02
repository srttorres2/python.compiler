import lexicMachine
from lexicMachine import LexicMachineClass
#--------------------------------------
# variables globales
#--------------------------------------
unprocessed_tokens=1    #son los tokens del fichero codigo.txt
                        #solo es 0==FALSE cuando encuentra el EOF
tokens_left=0           #son los tokens procesados que se encuentran en tokens.txt
                        #va a almacenar el número de tokens que va encontrando
char_counter=0          #cuando termino de leer el codigo.txt y llamo a stop(), reinicio char_counter
zona_declarativa=0

#--------------------------------------
# métodos
#--------------------------------------
def init():
    global tokens_left, unprocessed_tokens
    print("##SYNTACTIC MACHINE")
    #--------------------------------------
    # 2) Si el analizador sintáctico no tiene tokens nuevos para leer,
    #    entonces pide al analizador léxico que se los proporcione y este lee el fichero entero
    #--------------------------------------

    while unprocessed_tokens==1:    #la condición de parada es un token EOF
                                    #Es decir, va a leer el fichero completo
        print("## char_counter: {}" .format(char_counter))
        i = LexicMachineClass() #instancia de la clase
        i.init()

    if tokens_left > 0:
    #--------------------------------------
    # 2.1) los tokens recogidos tiene que cumplir unas normas
        # tal vez un while tokens_left > 0:
        print("## tokens_left es %s" %(tokens_left))
        readToken()
        compruebaToken
    else:
        print("## tokens_left es 0")
#--------------------------------------
def compruebaToken():
    print("## compruebaToken()")
def readToken():
    global tokens_left
    print("## readToken()")
#    tokensfilename = "fichero_tokens.txt"
#    inputfile = open(tokensfilename, 'r')
    # inputfile.seek(char_counter)    #si, char_counter viene reiniciado
    # c = inputfile.read(1)
    # token_abierto=0
    # while c is not '<':
    #     token_abierto=0
    #     next()
    #     c=inputfile.read(1)
    #     if c=='<':
    #         token_abierto=1

    #aquí va el token, (su abreviatura)
    # while c is not '>':
    #     token_abierto=0
    #     next()
    #     c=inputfile.read(1)
    #     if c=='>':
    #         token_abierto=1

    tokens_left-=1
def next():
    global char_counter,tokens_left
    char_counter+=1
def addToken():
    global tokens_left
    tokens_left+=1
def stop(): # método de parada del init, se activa con fin de fichero, no hay más que analizar
    global unprocessed_tokens
    print("##stopping syntactic ")
    unprocessed_tokens=0
    char_counter=0
