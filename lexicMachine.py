
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
RC_counter = 0 # contador de líneas para situar el error()
#----------------------------------------------------------------------------
# métodos
#----------------------------------------------------------------------------
def error(machine,linea,mensaje):
    print("# ERROR (%s, linea: %d, Token %s mal construido)" %(machine,linea,mensaje))
    errors_filename = "fichero_errores.txt"
    file_descriptor = open(errors_filename, 'a')

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
        self.inputfile.seek(syntacticMachine.char_counter)
        c = self.inputfile.read(1)              #un solo carácter

        if c is '':
            self.genToken("EOF","")
            syntacticMachine.stop_reading_file()#esto solo es para fin de fichero

        elif c is '\n':
            self.genToken("RC","")              #DELIMITADOR
            syntacticMachine.next()
            RC_counter +=0.5

        elif c is '{':
            self.genToken("LLA","")              #LLAVE APERTURA
            syntacticMachine.next()

        elif c is '}':
            self.genToken("LLC","")              #LLAVE CIERRE
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
                error("LEXIC",RC_counter,"predecremento")
        elif c is '"':                          #STRING (O CADENA)
            pal = ''
            while True:
                pal = pal + c
                c = self.inputfile.read(1)
                syntacticMachine.next()
                if c is '\n':
                    error("LEXIC",RC_counter,"cadena de String no cerrado con comillas,")
                if c is '"':
                    break
            pal = pal + c
            self.genToken("STR", pal)
            syntacticMachine.next()
        elif c is '/':                      #COMENTARIO
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
                error("LEXIC",RC_counter,"Comentario")
        elif c.isdigit():                   #ENTERO
            d = 0
            while c.isdigit():
                d  = d*10 + int(c)
                c = self.inputfile.read(1)
                syntacticMachine.next()
                if c=="." or c==",":
                    error("LEXIC",RC_counter,"Entero")
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
