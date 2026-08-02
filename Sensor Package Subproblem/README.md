# Nuclear Transport Vehicle State Monitoring Challenge

**Welcome!**

Congratulations! You've been chosen to join an engineering team at Canadian Nuclear Labs (CNL).

Your mission is to create an innovative system for real-time monitoring of vehicle and container conditions during nuclear waste transport across Canada.
---

## Background

Nuclear transport trucks travel through remote, isolated locations, making transportation difficult due to unpredictable and harsh road conditions.

Limited service and connectivity can make live updates difficult and unreliable.

Your system should allow the driver to monitor the state of:

- The package
- The truck
- The surrounding environment

This data can help the transport truck make important decisions, protecting local communities and the environment during emergencies or unexpected road hazards.

Nuclear transport is a high-security and high-risk job. Transport trucks may experience:

- Vibrations from uneven roads
- Shifting weight distribution during loading
- Harsh weather conditions
- Potential shielding failures

Your solution will help protect public safety and environmental health by promptly identifying potential risks.

---

## Table of Contents

- [Challenge Overview](#challenge-overview)
- [Tools Provided](#tools-provided)
  - [Main Components](#main-components)
  - [Grove Sensor Kit](#grove-sensor-kit)
  - [Additional Sensors and Components](#additional-sensors-and-components)
- [Documentation and Reference Material](#documentation-and-reference-material)
- [Getting Started](#getting-started)
  - [Arduino and Grove Shield Setup](#arduino-and-grove-shield-setup)
  - [Sensor Connections](#sensor-connections)
    - [A Note on I2C](#a-note-on-i2c)
  - [Simulating Radiation](#simulating-radiation)
  - [Testing Stations and Demos](#testing-stations-and-demos)
 
---

## Challenge Overview

Design a comprehensive sensor package using:

- Arduino Uno R4 Minima
- Grove Sensor Kit
- Additional sensors

The system should monitor relevant metrics for transporting nuclear material.

Examples of relevant emergencies include:

- Crashes
- Storms
- Fires
- Radiation leaks

The system should alert drivers or authorities immediately if anomalies occur.

---

## Tools Provided

### Main Components

- Arduino Uno R4 Minima

### Grove Sensor Kit

- Touch Sensor
- Light Sensor
- Temperature Sensor
- Rotary Angle Sensor
- Sound Sensor
- Buzzer
- Button
- LED Socket
- LCD Screen
- Servo
- Relay

### Additional Sensors and Components

- AHT20 Temperature and Humidity Sensor
- BMX160 9-axis IMU
- Radiation Source
- IR Emitter (Blue)
- 3V Coin Battery
- LED (Green)
- Resistors
- IR Sensor
- Potentiometers
- Pushbuttons
- Cardboard Box
- Wires
- Breadboard

> **Note**
>
> Students are not required to use all (or any) of the provided tools to create their solution.

![Sample Solution](https://github.com/IdeasClinicUWaterloo/F25-NuclearIC/blob/main/Sensor%20Package%20Subproblem/sensor_pckg_main/SensorPackSolution.JPG?raw=true)

## Documentation and Reference Material

- **Microcontroller:** Arduino Uno R4 Minima
- **Grove Sensor Kit:** [Grove Sensor Setup](https://github.com/IdeasClinicUWaterloo/Technologies-Utilized-for-Idea-s-Clinic-Challenges/blob/main/Seed%20Grove%20Kit/GUIDE.md), [Grove Sensor Wiki](https://wiki.seeedstudio.com/Grove_Starter_Kit_v3/#grove---rotary-angle-sensor), [Grove Code Starter Kit](https://github.com/Seeed-Studio/Sketchbook_Starter_Kit_V2.0/blob/master/README.md)
- **Additional Sensors:**

    - [DFRobot BMX160 9-Axis IMU](https://wiki.dfrobot.com/BMX160_9-axis_Sensor_Module_SKU_SEN0373)
    - [Adafruit AHT20 Temperature and Humidity Sensor](https://learn.adafruit.com/adafruit-aht20)
    - [IR Emitter](https://www.vishay.com/docs/81006/tsal4400.pdf)(Included in Radiation Source)
    - [IR Sensor](https://www.vishay.com/docs/81509/bpv22nf.pdf)
- **Breadboard Basics** [https://www.build-electronic-circuits.com/breadboard/]

  Detailed setup and code instructions for these modules are included in the sections below.

---

## Getting Started

Follow these steps to set up your vehicle state monitoring solution:

### Arduino and Grove Shield Setup

1. Connect your Arduino Uno R4 Minima to your computer via USB.
2. Attach the Grove Shield to your Arduino for simplified sensor connections.
3. Ensure your Arduino IDE is installed: [Arduino IDE Download](https://www.arduino.cc/en/software).

### Sensor Connections

For Grove kit sensor connections - refer to the provided [guide](https://github.com/IdeasClinicUWaterloo/Technologies-Utilized-for-Idea-s-Clinic-Challenges/blob/main/Seed%20Grove%20Kit/GUIDE.md) and the instruction manual inside the kits.
Follow these specific instructions for each additional sensor:
The LCD Screen will require the library: `Grove-LCD RGB Backlight`

- **DFRobot BMX160 9-Axis IMU**
    -   *Connection: (IMU -> Arduino)*
    >VCC -> 5V
    >GND -> GND
    >SLA -> SLA
    >SDA -> SDA  
    -   *Library:* Install `DFRobot_BMX160` via the Arduino IDE Library Manager.
    -   *Setup Notes:* This sensor provides accelerometer, gyroscope, and magnetometer data. It communicates via I2C. Ensure no other I2C devices on the same port have address conflicts (though unlikely for these modules).
    -   *Reference:* See [DFRobot Guide](https://wiki.dfrobot.com/BMX160_9-axis_Sensor_Module_SKU_SEN0373) for basic usage examples.

- **Adafruit AHT20 Temperature and Humidity Sensor**
    -   *Connection: (AHT20 -> Arduino)*
    >VCC -> 5V
    >GND -> GND
    >SLA -> SLA
    >SDA -> SDA
    -   *Library:* Install `Adafruit_AHTx0` via the Arduino IDE Library Manager.
    -   *Setup Notes:* Provides accurate ambient temperature and humidity. Communicates via I2C.
    -   *Reference:* See [Adafruit AHT20 Guide](https://learn.adafruit.com/adafruit-aht20/arduino) for library usage and example code.

#### A Note on I2C
Several of the sensors provided, such as the LCD display, AHT20, and IMU, all use I2C communication.

When wiring I2C:

- Connect the SCL on the sensors to the SCL of the Arduino.
- Connect the SDA on the sensors to the SDA of the Arduino.

You can connect as many sensors as needed to use I2C as long as the addresses of each sensor are different.

This, however, should not be an issue as the libraries will use a different address for each sensor.

Using multiple of the same I2C sensors will be more complicated.

### Simulating Radiation
Radiation is simulated using infrared emitters and sensors. The emitter has already been created and is part of the radiation source package.

- **IR Sensor connections**
See [Datasheet](https://www.vishay.com/docs/81509/bpv22nf.pdf). With the spherical side facing towards you, the anode is the left leg and the cathode the right leg. Here is one configuration of the sensor using a pull-down resistor: Connect the Anode to the Arduino 5V. Connect the cathode to an analog pin and to a 100k resistor, connected to Ground.  ![Circuit Diagram](https://github.com/IdeasClinicUWaterloo/F25-NuclearIC/blob/main/Sensor%20Package%20Subproblem/sensor_pckg_main/nuclearSensorCirc.jpg?raw=true) Our sensors only have 2 pins; ignore the middle pin in the diagram. 

![Sensor Pins](https://github.com/IdeasClinicUWaterloo/F25-NuclearIC/blob/main/Sensor%20Package%20Subproblem/sensor_pckg_main/NucSensor.jpg?raw=true)

- **Notes**

Reading the sensor data is simple, using:

```cpp
analogRead(analogPin)
```

The sensor signal is strongest when positioned directly above the emitter. Keep this in mind during testing and building your solution.

The sensor will, in theory, output a range of 0-1023 depending on the strength of the signal; however, in practice, the range will likely be around 0 to 500.

In the above wiring configuration, higher values represent stronger radiation.

When building your solution, test the sensitivity of your sensor so you can decide the threshold for a radiation leak.

During demos, your radiation source should be placed inside the cardboard box with the IR emitter facing directly out of a small hole to represent a damaged container and a radiation leak.

However, feel free to test your solution outside the box.

---

### Testing Stations and Demos

The nuclear waste container with the radiation source inside, alongside the students' sensor package, will be placed onto the car trailer/baseplate.

Students should have access to the battery switch to demonstrate how turning the radiation source on/off affects their radiation detection.

The car can then be:

- Driven into a wall
- Driven over speed bumps
- Tipped over

to demonstrate the student's ability to detect:

- Crashes
- Tips
- Rough terrain
- Other relevant conditions

In case of emergencies, make sure to create physical alerts for the driver.

Students are free to devise their own tests to demonstrate their unique solutions.
