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

    # Flag to track LED state
    led_state = GPIO.LOW

    # Timer variables
    motion_detected_time = 0
    timeout_duration = 30  # Timeout duration in seconds

    while True:
        if GPIO.input(pir_pin):  # Check if motion is detected
            if led_state == GPIO.LOW:  # If LED is off, turn it on
                print("Motion detected!")
                GPIO.output(led_pin, GPIO.HIGH)
                led_state = GPIO.HIGH
                motion_detected_time = time.time()  # Record time of motion detection
        else:  # No motion detected
            if led_state == GPIO.HIGH:  # If LED is on, turn it off
                print("No motion detected")
                if time.time() - motion_detected_time >= timeout_duration:
                    GPIO.output(led_pin, GPIO.LOW)
                    led_state = GPIO.LOW
        time.sleep(0.1)  # Small delay to reduce CPU usage

except KeyboardInterrupt:
    print("Exiting...")
    GPIO.cleanup()
