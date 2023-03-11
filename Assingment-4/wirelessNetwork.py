class WirelessNetwork():
    #defining the static variables
    ADHOC_Mode= "ON"
    BRAND_NAME="Cisco"
    
    def __init__(self):
        self._sensorId=""
        self._oxygenLevel= 0
        self._temperature = 0.0

    @staticmethod
    def greetMessage():
        print("****************************************************************************************************************************")
        print("Welcome to company's Iot-Based Health System")
        print("These are sensors of {0} brand, and their Ad Hoc Mode is {1}".format(WirelessNetwork.BRAND_NAME,WirelessNetwork.ADHOC_Mode))
        print("****************************************************************************************************************************")        

