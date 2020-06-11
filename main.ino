// INIT PINS
// digital
const int strip_out = 13;
const int strip_in = 12;
// analog
const int tilt = A0;
const int ambient = A1;
const int temp = A2;
const int motion = A3;



// awake
void setup()
{
    // digital pins
    pinMode(strip_out, OUTPUT);
    pinMode(strip_in, INPUT);
    // analog pins
    pinMode(tilt, INPUT);
    pinMode(ambient, INPUT);
    pinMode(temp, INPUT);
    pinMode(motion, INPUT);

    Serial.begin(9600);
}

// infinite loop
void loop()
{
    // write led strip
    digitalWrite(strip_out, HIGH);

    // read led strip
    Serial.println(digitalRead(strip_in));
}
