#include <Wire.h>
#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x3f, 20, 4);

byte sx[][9] = {
{ B00010,
  B00111,
  B01001,
  B01111,
  B10111,
  B11111,
  B11111,
  B11011},//0

{ B10010,
  B11111,
  B11001,
  B11111,
  B10101,
  B11101,
  B01111,
  B11011},//1

{ B00000,
  B10000,
  B11000,
  B11110,
  B10101,
  B11101,
  B01111,
  B11011//2
},

{ B00000,
  B00000,
  B00001,
  B01111,
  B10101,
  B11101,
  B01111,
  B11011//3
},
{ B00001,
  B00010,
  B10101,
  B11111,
  B10101,
  B11101,
  B01111,
  B11011},//4
  {
  B11101,
  B11010,
  B10101,
  B11111,
  B10101,
  B11101,
  B01111,
  B11011//5
},
{
  B11101,
  B11010,
  B10101,
  B11111,
  B10110,
  B11101,
  B01000,
  B11000//6
},
{
  B11101,
  B11010,
  B10101,
  B11100,
  B10100,
  B00000,
  B00000,
  B00000//7
},
{
  B10011,
  B10100,
  B01010,
  B10000,
  B00000,
  B00000,
  B00000,
  B00000//8
  }
};

void setup() {
  pinMode(2,INPUT_PULLUP);
  lcd.begin();
  int i;
  for(i=0; i<8; i++){
    lcd.createChar(i, sx[i]);
  }
  lcd.setBacklight(1);

}

void write_smoke(int st)
{
  int ch_num =0;
  int j;
  int k=5;
  for(j=st;j<8+st; j++){
    lcd.setCursor(j+5,0); //x,y
    lcd.write(ch_num);
    lcd.setCursor(j,1);
    lcd.write(ch_num);
    lcd.setCursor(j+5,2); //x,y
    lcd.write(ch_num);
    lcd.setCursor(j,3);
    lcd.write(ch_num);
    ch_num++;
  }
}

void printTxt()
{
  lcd.setCursor(0,0);
  lcd.printstr("141  4min||148  7min");
  lcd.setCursor(0,1);
  lcd.printstr("145 13min||");
  lcd.setCursor(0,2);
  lcd.printstr("====================");
  lcd.setCursor(0,3);
  lcd.printstr("soon : 463");
}
void loop(){
  lcd.clear();
  printTxt();
  for(int i = 0;i<7;i++){
    lcd.clear();
    printTxt();
    write_smoke(i);
    delay(500);
  }
  for(int i = 7;i>=1;i--){
    lcd.clear();
    printTxt();
    write_smoke(i);
    delay(500);
  }
}