# program testowany na symulatorze: https://gears.aposteriori.com.sg/
# w trybie Pybricks 
# na robocie: Single Sensor Line Follower
# import niezbędnych bibliotek 
from pybricks.parameters import *
from pybricks.hubs import *
from pybricks.ev3devices import *
from pybricks.tools import *
from pybricks.robotics import *

ev3 = EV3Brick() # przypisanie kostki 
left_motor = Motor(Port.A) # przypisanie silnika A 
right_motor = Motor(Port.B) # przypisanie silnika B
ultrasonic_sensor = UltrasonicSensor(Port.S2) # przypisanie sensora ultrasonicznego
robot = DriveBase(left_motor, right_motor, wheel_diameter=56, axle_track = 152) 
# DriveBase służy do obsługi 2 silników na raz
# axel track - rostaw osi
# wheel_diameter - średnica koła

# poniższa metoda sprawdza przy użyciu sensora ultrasonicznego odległość od przeszkody 
# oraz wykonuje ruch do przodu oraz skręt
# jako argumenty metody podajemy:
# total_distance - całkowita odległość do przejechania przez robota
# angle - kąt o jaki robot ma się obracać 
# total_turn - suma obrotów jakie robot ma wykonać 
def ultrasonic_function(total_distance, angle, total_turn):
    while True: 
        obstacle_distance = ultrasonic_sensor.distance() # sprawdzenie dystansu do przeszkody
        new_distance = total_distance - robot.distance() # obliczenie dystansu pozostałego do przejechania 
        if obstacle_distance > new_distance: # sprawdzenie czy odległość od przeszkody jest odpowiednia jeśli nie jest program wychodzi z pętli 
            robot.straight(total_distance/total_turn) # robot porusza się o podaną odległość podzieloną na liczbę obrotów
            robot.turn(angle) # robot wykonuje skręt o podaną liczbę stopnii 
            print(new_distance)
            if total_distance - robot.distance() <= 0: 
                # sprawdzenie czy pozostała jakaś odległość do przejechania 
                # jeśli została przejechana podana odległość następuje wyjście z pętli 
                break
        else:
            break
            
ultrasonic_function(1800, 90, 4) # wywołanie metody z wybranymi argumentami 


