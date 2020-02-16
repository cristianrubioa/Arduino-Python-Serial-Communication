int data; //Declara la variable data de tipo entero
int led = 13;

void setup() {

 Serial.begin(9600); //Inicia la comunicación serial a 9600 baudios
 pinMode(led, OUTPUT); //Pone como salida el Led incorporado
 digitalWrite(led, LOW); //Comienza en off
 Serial.println("Estableciendo Comunicacion... "); //Envia mensaje a Python

}

void loop() {

  while(Serial.available()){ //Obtiene los datos(bytes) y los almacena
    data = Serial.read(); //Lee los datos Serie entrantes y se asigna el valor a la variable data
  }

  if (data == '1') //Si data es 1
  digitalWrite(led, HIGH); //Pone en ON (Alto)

  else if(data == '0') //Si data es 0
  digitalWrite(led, LOW); //Pone en OFF (Bajo)
}
