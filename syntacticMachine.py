import lexicMachine
from lexicMachine import LexicMachineClass
#----------------------------------------------------------------------------
# variables globales
#----------------------------------------------------------------------------
EOF=0                   #solo es 0==FALSE cuando encuentra el EOF
reading_token=0         #fichero_tokens.txt
                        #va a almacenar el número de tokens que va encontrando
char_counter=0          #cuando termino de leer el codigo.txt y llamo a stop(), reinicio char_counter
tokens=0                #numero de tokens no tratados por el analizador sintáctico en fichero_tokens.txt

#----------------------------------------------------------------------------
# métodos
#----------------------------------------------------------------------------
def init():
    global EOF, reading_token
    print("##SYNTACTIC MACHINE")
# Solo se termina el análisis sintáctico si ya no quedan caracteres en fichero_codigo.txt
    while EOF==0:
    #----------------------------------------------------------------------------
    # 2) Si el analizador sintáctico no tiene tokens nuevos para leer,
    #    entonces pide al analizador léxico que se los proporcione y este lee el fichero entero
    #----------------------------------------------------------------------------
        if tokens > 0:
            print("## tokens_left: %d" %(tokens))
            tratar_token()
        else:
            reading_token=1
            while reading_token==1:     #la condición de parada es generar_token
                                        #Es decir, va a leer el fichero completo
                    print("## char_counter: {}" .format(char_counter))
                    i = LexicMachineClass() #instancia de la clase
                    i.init()


#----------------------------------------------------------------------------
def compruebaToken():
    print("## compruebaToken()")
def tratar_token():
    global tokens
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
    tokens-=1
def next():
    global char_counter
    char_counter+=1
def addToken():
    global tokens
    tokens+=1
def stop_reading_token():
    global reading_token
    reading_token=0
def stop_reading_file():
    global EOF, reading_token
    reading_token=0
    EOF = 1
