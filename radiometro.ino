float temp=0;
float power=0;
int tempInt=0;
int powerInt=0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {  
  
  tempInt = analogRead(A0);
  powerInt = analogRead(A2);
  for (int i = 1; i <= 9; i++) {
    tempInt = 0.5*(tempInt+analogRead(A0));
    powerInt = 0.5*(powerInt+analogRead(A2));
    delay(10);
  }
    
  temp = tempInt*5.0/1024.0;
  power = powerInt*5.0/1024.0;

  // print out the value you read:
  Serial.print(temp);Serial.print(",");Serial.println(power);
  delay(10);  // delay in between reads for stability

}
