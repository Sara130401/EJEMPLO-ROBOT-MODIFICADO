# Definimos la clase base 'Robot'
class Robot:
    """
    Clase que representa un robot genérico.
    Tiene un nombre y un nivel de batería.
    """

    def __init__(self, nombre, bateria=100, posicion = 0 ):
        # Guardamos el nombre del robot en un atributo
        self.nombre = nombre
        # Guardamos la batería inicial (por defecto 100)
        self.bateria = bateria
        # Estado inicial: apagado
        self.encendido = False
        self.posicion = 0
        
        

    def encender(self):
        # Solo puede encenderse si hay batería
        if self.bateria > 0:
            self.encendido = True
            print(f"{self.nombre} está encendido.")
        else:
            print(f"{self.nombre} no puede encenderse: batería agotada.")

    def apagar(self):
        # Cambiamos el estado a apagado
        self.encendido = False
        print(f"{self.nombre} se apagó.")

    def describir(self):
        # Devuelve un texto con la información del robot
        estado = "encendido" if self.encendido else "apagado"
        return f"Robot {self.nombre} | Batería: {self.bateria}% | Estado: {estado}"
    
    def bajar(self):
        if self.posicion == 0:
            self.bajar = True
            print(f"{self.nombre} esta bajando")
        else:
            print(f"{self.nombre} esta subiendo")
    def giro(self):
        if self.giro == 0:
            self.giro = False
            print(f"{self.nombre} no esta girando")
        if self.giro == 1 :
                self.giro = True
                print("f{self.nombre} esta girando a la izquierda")
        if self.giro == 2:
                self.giro = True
                print(f"{self.nombre} gira a la derecha")
                
            
# %%
    
# Creamos un objeto (instancia) de la clase Robot
robot1 = Robot("R2D2", bateria=80)

# Usamos sus métodos
print(robot1.describir())   # Muestra la información inicial
robot1.encender()           # Cambia el estado a encendido
print(robot1.describir())   # Ahora debe mostrar "encendido"
robot1.apagar()             # Cambia el estado a apagado
# %%


# Definimos una subclase que hereda de Robot
class RobotMovil(Robot):
    """
    Robot que puede moverse en un plano 2D.
    Hereda de Robot y añade atributos x, y.
    """

    def __init__(self, nombre, bateria=100, x=0, y=0):
        # Llamamos al constructor de la clase base
        super().__init__(nombre, bateria)
        # Añadimos atributos propios
        self.x = x
        self.y = y

    def mover(self, dx, dy):
        # Solo se mueve si está encendido
        if self.encendido and self.bateria > 0:
            self.x += dx
            self.y += dy
            # Cada movimiento consume 10% de batería
            self.bateria = max(0, self.bateria - 10)
            print(f"{self.nombre} se movió a ({self.x}, {self.y}).")
        else:
            print(f"{self.nombre} no puede moverse (apagado o sin batería).")

    # Sobrescribimos el método describir
    def describir(self):
        estado = "encendido" if self.encendido else "apagado"
        return (f"RobotMovil {self.nombre} | Posición: ({self.x}, {self.y}) | "
                f"Batería: {self.bateria}% | Estado: {estado}")
# %%
    
class Robotgirador(Robot):
    """Robot que puede girar en su propio eje."""

    def __init__(self, nombre, bateria=100, nada=0, izquierda=1, derecha=2):
        super().__init__(nombre, bateria)
        self.nada = nada
        self.izquierda = izquierda
        self.derecha = derecha

    def giro(self, direccion):
        if self.encendido and self.bateria > 0:
            self.bateria = max(0, self.bateria - 5)
            print(f"{self.nombre} giró hacia {direccion}")
        else:
            print(f"{self.nombre} no puede girar (apagado o sin batería).")

    def describir(self):
        estado = "Encendido" if self.encendido else "Apagado"
        return (f"Robotgirador {self.nombre} | "
                f"Opciones de giro: nada={self.nada}, izquierda={self.izquierda}, derecha={self.derecha} | "
                f"Batería: {self.bateria}% | Estado: {estado}")

                    
# %%
    

# Creamos un objeto de tipo RobotMovil
robot2 = RobotMovil("Wall-E", bateria=50)

print(robot2.describir())  # Muestra la información inicial
robot2.encender()          # Encendemos el robot
robot2.mover(2, 3)         # Lo movemos en el plano
print(robot2.describir())  # Ahora debe mostrar la nueva posición y batería
# %%
robot3 = Robotgirador("Bender", bateria=80, nada=0)

print(robot3.describir())
robot3.encender()
robot3.giro(1)   # izquierda
robot3.giro(2)   # derecha
robot3.giro(0)   # nada
print(robot3.describir())


# %%

robot4 = RobotMovil("Marvin", bateria=70)

print(robot4.describir())   # Estado inicial
robot4.encender()           # Encendemos
robot4.mover(5, 7)          # Lo movemos
# Aquí no hay bajar(), así que podemos hacerlo manual con y -= 1:
robot4.y -= 1
print(f"{robot4.nombre} bajó en Y a la posición {robot4.y}")
print(robot4.describir())   # Estado final

# Mensaje "está triste"
print(f"{robot4.nombre} está triste")

# %%


# Creamos una lista con robots de distintos tipos
robots = [robot1, robot2, robot3, robot4]

# Recorremos la lista y llamamos al mismo método 'describir'
for r in robots:
    print(r.describir())  # Cada objeto responde según su clase
# %%
