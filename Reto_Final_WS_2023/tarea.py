class Tareas:
    def __init__( self, ev3, MD, MI, MG, SD, SI , SC, wait,   Stop, sonidos, Colores, DriveBase, time):
        self.sound= sonidos
        self.ev3 = ev3
        self.MD = MD
        self.MI = MI
        self.MG = MG
        self.SD = SD
        self.SI = SI
        self.SC = SC
        self.delay = wait
        self.Stop = Stop
        self.Color= Colores
        self.time = time
        self.robot = DriveBase(MI, MD, wheel_diameter= 62.4, axle_track= 154)
        self.robot.settings(straight_speed = 200, straight_acceleration = 100, turn_rate = 100)

    def mover_por_distancia(self, distancia, direccion):
        if direccion == "adelante":
            self.robot.straight(distancia*10)
            self.robot.stop()
        elif direccion== "atras":
            self.robot.straight(distancia(-10))
            self.robot.stop()
        else:
            self.robot.straight(distancia*0)
            self.robot.stop()
    
    def girar_n_grados(self, n, direccion = None):
        if direccion == "izquierda":
            self.robot.turn(-n)
            self.robot.stop()
        elif direccion == "derecha":
            self.robot.turn(n)
            self.robot.stop()
        else:
            self.robot.turn(-n)
            self.robot.stop()




