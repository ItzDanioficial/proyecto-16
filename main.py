strip = neopixel.create(DigitalPin.P0, 4, NeoPixelMode.RGB)
número = randint(1, 2)
distancia = maqueen.ultrasonic(PingUnit.CENTIMETERS)
maqueen.motor_run(maqueen.Motors.ALL, maqueen.Dir.CW, 255)
if distancia > 5:
    maqueen.motor_stop(maqueen.Motors.ALL)
    music.play_melody("C5 G C5 G C5 G C5 G ", 120)
    strip.show_color(neopixel.rgb(0, 165, 100))
maqueen.motor_run(maqueen.Motors.ALL, maqueen.Dir.CCW, 255)
basic.pause(1000)
maqueen.motor_stop(maqueen.Motors.ALL)
if número == 1:
    maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 255)
    maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, 255)
else:
    maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, 255)
    maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 255)
maqueen.motor_run(maqueen.Motors.ALL, maqueen.Dir.CW, 255)