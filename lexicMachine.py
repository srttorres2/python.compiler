import fileinput        # para usar input() en readder
import syntacticMachine # para cambiar el estado de tokens_left y char_counter mediante stop() y next()
#--------------------------------------
# variables globales
#--------------------------------------
unprocessed_tokens = 0  #esta variable tiene que ser estática de alguna forma, tendrán que acceder
                        # el lexic, el syntactic y el (creo) que el main
palabras_reservadas = {"True":0,
                    "False":1,
                    "if":2,
                    "else":3,
                    "bool":4,
                    "char":5,
                    "int":6,
                    "function":7,
                    "promt":8,
                    "write":9,
                    "var":10}
RC_counter = 1 # contador de líneas para situar el error()
#----------------------------------------------------------------------------
# Métodos
#----------------------------------------------------------------------------
def error(machine,linea,mensaje):
    print("# ERROR (%s, linea: %d, token %s)" %(machine,linea,mensaje))
    errors_filename = "fichero_errores.txt"
    file_descriptor = open(errors_filename, 'a')
    file_descriptor.write("# ERROR (%s, linea: %d, token %s)\n" %(machine,linea,mensaje))
    file_descriptor.close()

class LexicMachineClass:
    def init(self):
        print("##LEXIC MACHINE")

        #otra manera es averiguar el tamaño del fichero
        codefilename = "codigo_1.txt"
        self.inputfile = open(codefilename, 'r')
        tokensfilename = "fichero_tokens.txt"
        self.outputfile = open(tokensfilename, 'a') #append
        self.readCharByChar()
        self.inputfile.close()

    def readCharByChar(self):
        global RC_counter
        fail_digit = False
        self.inputfile.seek(syntacticMachine.char_counter)
        c = self.inputfile.read(1)              #un solo carácter

        if c is '':
            self.genToken("EOF","")
            syntacticMachine.stop_reading_file()#esto solo es para EOF

        elif c is '\n':
            self.genToken("RC","")              #DELIMITADOR
            syntacticMachine.next()
            RC_counter +=0.5

        elif c is '{':
            self.genToken("LLA","")             #LLAVE APERTURA
            syntacticMachine.next()

        elif c is '}':
            self.genToken("LLC","")             #LLAVE CIERRE
            syntacticMachine.next()

        elif c is '!':
            self.genToken("NEG","")             #OPERADOR NEGACIÓN
            syntacticMachine.next()

        elif c is '+':                          #OPERADOR SUMA
            self.genToken("SUMA","")
            syntacticMachine.next()

        elif c is '=':
            syntacticMachine.next()
            c = self.inputfile.read(1)
            if c is '=':
                self.genToken("COMP", "")       #COMPARACION
                syntacticMachine.next()
            else:
                self.genToken("ASIG", "")       #ASIGNACION

        elif c is '-':
            syntacticMachine.next()
            c = self.inputfile.read(1)
            if c is '-':
                self.genToken("PRE", "")        #PREDECREMENTO
                syntacticMachine.next()
            else:
                error("LEXIC",RC_counter,"PRE: Expected '-'")

        elif c is '"':                          #STRING (O CADENA)
            pal = ''
            fin = False
            while True:
                pal = pal + c
                c = self.inputfile.read(1)
                syntacticMachine.next()
                if c is '\n':
                    error("LEXIC",RC_counter,"STR: Expected closing '\"'")
                    fin = True
                    break
                if c is '"':
                    break
            if not fin:
                pal = pal + c
                self.genToken("STR", pal)
                syntacticMachine.next()

        elif c is '/':                          #COMENTARIO
            syntacticMachine.next()
            c = self.inputfile.read(1)
            if c is '/':
                pal = '/'
                while c is not '\n':
                    pal = pal + c
                    c = self.inputfile.read(1)
                    syntacticMachine.next()
                self.genToken("COM", pal)
            else:
                error("LEXIC",RC_counter,"COM: Expected '//'")

        elif c.isdigit():                       #ENTERO
            d = 0            
            while c.isdigit() or c is ',' or c is '.':
                if c is '.' or c is ',':
                    d = d*10 + 0
                    fail_digit = True
                else:
                    d = d*10 + int(c)
                c = self.inputfile.read(1)
                syntacticMachine.next()                                    
            if fail_digit:
                error("LEXIC",RC_counter,"INT: Expected Integer")
                syntacticMachine.stop_reading_token()
            else:
                self.genToken("INT", d)

        elif c.isalpha():
            pal = ''
            while c.isalnum() or c is '_':
                pal = pal + c
                c = self.inputfile.read(1)
                syntacticMachine.next()
            if pal in palabras_reservadas:
                self.genToken("PR", pal)
            else:
                self.genToken("ID", pal)

        else:
            #Aqui vienen los espacios en blanco de momento
            syntacticMachine.next()

    def genToken(self,code,value):
        print("#####escribe el token <%s, %s>" %(code,value))
        self.outputfile.write("<%s, %s>\n" %(code,value))
        self.outputfile.close()
        syntacticMachine.addToken()
        syntacticMachine.stop_reading_token()