# swh

## Description

A lamp controlled over WiFi by a cube. The cube has a colour sensor on its bottom. The sensor measures the colour of the surface the cube is sitting on. Thus the cube can control the colour of the lamp remotely. Furthermore, the cube has an acceleration sensor which senses if the cube is rotated clock or anti-clockwise to dim the light intensity of the lamp accordingly. A button allows saving a colour as default, cube gives haptic feedback after the saving process was successful . The lamp has RGB light outputs as well as speakers and motors. The motors control panels which control how much light is emitted by the lamp.

## Features

A lamp controlled over WiFi by a cube. The cube has a colour sensor on its bottom. The sensor measures the colour of the surface the cube is sitting on. Thus the cube can control the colour of the lamp remotely. Furthermore, the cube has an acceleration sensor which senses if the cube is rotated clock or anti-clockwise to dim the light intensity of the lamp accordingly. A button allows saving a colour as default, cube gives haptic feedback after the saving process was successful . The lamp has RGB light outputs as well as speakers and motors. The motors control panels which control how much light is emitted by the lamp.

- cube: compact, physical controller as input
  - minimal, compact cube which houses multiple sensors
  - colour sensor on the bottom which changes the colour of the lamp to the colour of the surface the cube is sitting on
  - acceleration sensor to dim the light intensity if the cube is rotated
  - button to save colour
  - haptic feedback (vibration motor) after saving colour
- lamp: light installation, an assembly of multiple light sources
  - has multi-colour light sources (RGB leds)
  - option to emit sound (speaker)
  - control light intensity with motors which move panels (motors)
  - objects are asymmetric, cube controller and lamp are connected via WiFi
  - “invented” sensor: DIY colour sensor

## Commands

Install pipenv:

```bash=
pip install --upgrade pipenv
```

Install dependencies:

```bash=
pipenv install
```

## Contributors

- Andreas Ellwanger
- Andreas Griesbeck
- Aline Neumann
- Maximilian Rauh

### Individual contributions

Due to the small group size of 4 it is impossible for us to properly distinguish what of our project has been done by whom. We all worked on all parts of our application, especially since we mostly did “pair-programming” (with two or often all four of us working together). So all of us were equally involved in all parts of our application.
We would be happy to answer questions about our development process, as well as our individual/collective contributions at the examination.
