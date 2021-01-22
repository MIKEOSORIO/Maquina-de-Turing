N = 1000  # longitud de la cinta, inicializar a un valor grande


class TuringMachine:
    '''
    inicializar la máquina de Turing, lee el programa y la entrada
    '''

    def __init__(self, program, input, state=0):  #datos requeridos program(almacena reglas de la suma) | input(almacenara los datos a sumar)
                                                  #estado en el que se encuentra el cabezal = 0 ya que no contiene acciones )
        self.trf = {} #Se empieza a realizar la conversion de los numeros
        self.state = str (state) #crear objeto state
        self.tape = ''.join (['_'] * N)
        self.head = N // 2  # el cabezal lo situamos en el centro
        self.tape = self.tape[:self.head] + input + self.tape[self.head:] #instanciamos el objeto tape en la maquina de turing
        for line in program.splitlines ():
            s, a, r, d, s1 = line.split (' ')
            # s = dato leido | a = posicion del apuntador en la cinta | r = reglas | d=direccion | Estado = s1
            self.trf[s, a] = (r, d, s1)

    '''
    paso a paso que llevara el programa
    '''

    def step(self):
        if self.state != 'H': # si el estado es diferente de H
            a = self.tape[self.head]
            action = self.trf.get ((self.state, a))
            if action:
                r, d, s1 = action #estado es igual a la action
                self.tape = self.tape[:self.head] + r + self.tape[self.head + 1:]
                if d != '*':
                    self.head = self.head + (1 if d == 'r' else -1)
                self.state = s1
                print (self.tape.replace ('_', ''), self.state)

    '''
    run a program
    '''
#--------------------------------------------------------------------- Previene bucle infinito

    def run(self, max_iter=9999):
        iter = 0
        while self.state != 'H' and iter < max_iter:
            self.step ()
            iter += 1
        print (self.tape.replace ('_', ''), self.state)

#----------------------------------------------------------------------

input = input("Ingresa los numeros binarios a sumar separados por un '_'" + "\t") #ingreso de numeros binarios a sumar
program = open('program.txt').read() #lectura las reglas almacenadas en el archivo .txt
tm = TuringMachine(program, input) #analiza/valida las reglas con los datos de entrada
tm.run()   # corre el programa
# 10010 H

