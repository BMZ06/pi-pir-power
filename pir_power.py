import RPi.GPIO as GPIO
import time

# Set up GPIO
GPIO.setmode(GPIO.BCM)

# GPIO pin for PIR sensor
pir_pin = 4

# GPIO pin for LED
led_pin = 18  # Example: using GPIO pin 18 for LED

# Set up PIR sensor
GPIO.setup(pir_pin, GPIO.IN)

# Set up LED
GPIO.setup(led_pin, GPIO.OUT)
GPIO.output(led_pin, GPIO.LOW)  # Initially turn off LED

try:
    print("PIR Module Test (CTRL+C to exit)")
    time.sleep(2)  # Allow sensor to settle
    print("Ready")

    while True:
        if GPIO.input(pir_pin):  # Check if motion is detected
            print("Motion detected!")
            GPIO.output(led_pin, GPIO.HIGH)  # Turn on LED
            time.sleep(1)  # Keep LED on for 1 second
            GPIO.output(led_pin, GPIO.LOW)  # Turn off LED
        time.sleep(0.1)  # Small delay to reduce CPU usage

except KeyboardInterrupt:
    print("Exiting...")
    GPIO.cleanup()
