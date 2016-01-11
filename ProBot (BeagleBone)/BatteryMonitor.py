#!/usr/bin/python

# Python Standard Library Imports
import Adafruit_BBIO.ADC as ADC
import Adafruit_BBIO.GPIO as GPIO
import ProBotConstants

Pconst = ProBotConstants.Constants()

# Start the ADC
ADC.setup()

# Definition of the GPIO's
GPIO.setup(Pconst.GreenBatteryBeagle, GPIO.OUT)
GPIO.setup(Pconst.RedBatteryBeagle, GPIO.OUT)
GPIO.setup(Pconst.GreenBatteryMotors, GPIO.OUT)
GPIO.setup(Pconst.RedBatteryMotors, GPIO.OUT)


# Battery measurement
class BatteryVoltage():
        def VoltageValue(self, type):
            options = {'BeagleBone': [Pconst.AnalogPinBeagle, Pconst.mBeagle, Pconst.bBeagle, Pconst.MinRedBeagle, Pconst.GreenBatteryBeagle, Pconst.RedBatteryBeagle], 'Motors': [Pconst.AnalogPinMotors, Pconst.mMotors, Pconst.bMotors, Pconst.MinRedMotors, Pconst.GreenBatteryMotors, Pconst.RedBatteryMotors]}

            voltageVar = options[type]		

            BatteryVoltageVal = ADC.read(voltageVar[0])
            BatteryRealValue = float((voltageVar[1]*BatteryVoltageVal)+voltageVar[2])   # Real voltage from the BeagleBone battery

            if BatteryRealValue < voltageVar[3]:					    # Define Red region, under 10,5V
                GPIO.output(voltageVar[4], GPIO.LOW)
                GPIO.output(voltageVar[5], GPIO.HIGH)
            else:
                GPIO.output(voltageVar[4], GPIO.HIGH)
                GPIO.output(voltageVar[5], GPIO.LOW)

            return BatteryRealValue