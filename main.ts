let strip = neopixel.create(DigitalPin.P0, 4, NeoPixelMode.RGB)
let número = randint(1, 2)
let distancia = maqueen.Ultrasonic(PingUnit.Centimeters)
maqueen.motorRun(maqueen.Motors.All, maqueen.Dir.CW, 255)
if (distancia > 5) {
    maqueen.motorStop(maqueen.Motors.All)
    music.playMelody("C5 G C5 G C5 G C5 G ", 120)
    strip.showColor(neopixel.rgb(0, 165, 100))
}
maqueen.motorRun(maqueen.Motors.All, maqueen.Dir.CCW, 255)
basic.pause(1000)
maqueen.motorStop(maqueen.Motors.All)
if (número == 1) {
    maqueen.motorRun(maqueen.Motors.M1, maqueen.Dir.CW, 255)
    maqueen.motorRun(maqueen.Motors.M2, maqueen.Dir.CW, 255)
} else {
    maqueen.motorRun(maqueen.Motors.M2, maqueen.Dir.CW, 255)
    maqueen.motorRun(maqueen.Motors.M1, maqueen.Dir.CW, 255)
}
maqueen.motorRun(maqueen.Motors.All, maqueen.Dir.CW, 255)
