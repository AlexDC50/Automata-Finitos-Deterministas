class MooreAutomata:
    def __init__(self):
      
        self.state = "START"

    def transition(self, bit):
        
        if self.state == "START":
            if bit == "1":
                self.state = "FIRST_1"
            else:
                self.state = "START"
        
        elif self.state == "FIRST_1":
            if bit == "1":
                self.state = "REPLACE_0"
            else:
                self.state = "START"
        
        elif self.state == "REPLACE_0":
            if bit == "1":
                self.state = "REPLACE_0" 
            else:
                self.state = "START"

        outputs = {
            "START": "0", 
            "FIRST_1": "0",   
            "REPLACE_0": "0"  
        }
        
        return outputs[self.state]

def procesar_cadena(cadena):
    automata = MooreAutomata()
    salida = ""
    for bit in cadena:
        salida += automata.transition(bit)
    return salida

if __name__ == "__main__":
    entrada = input("Ingrese flujo de bits (0 y 1): ")
    resultado = procesar_cadena(entrada)
    print(f"Entrada: {entrada}")
    print(f"Salida:  {resultado}")