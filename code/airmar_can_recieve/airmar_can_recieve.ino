// demo: CAN-BUS Shield, receive data with check mode
// send data coming to fast, such as less than 10ms, you can use this way
// loovee, 2014-6-13


#include <SPI.h>
#include "mcp_can.h"


unsigned char Flag_Recv = 0;
unsigned char len = 0;
unsigned char buf[8];
char str[20];


MCP_CAN CAN(10);                                            // Set CS to pin 10

void setup()
{
    Serial.begin(115200);

START_INIT:
//Airmar WX200 NMEA 2000 standard is assumed to work at 250kbps
    if(CAN_OK == CAN.begin(CAN_250KBPS))                   // init can bus : baudrate = 500k
    {
        Serial.println("CAN BUS Shield init ok!");
    }
    else
    {
        Serial.println("CAN BUS Shield init fail");
        Serial.println("Init CAN BUS Shield again");
        delay(100);
        goto START_INIT;
    }
}


void loop()
{
    if(CAN_MSGAVAIL == CAN.checkReceive())            // check if data coming
    {
        CAN.readMsgBuf(&len, buf);    // read data,  len: data length, buf: data buf

        int id = CAN.getCanId();
        int rawid = CAN.getRawCanId();
        Serial.print(rawid, HEX);
        Serial.print(": ");
        Serial.print(id, HEX);
        Serial.print(": ");
        
        for(int i = 0; i<len; i++)    // print the data
        {
            Serial.print(buf[i], HEX);Serial.print(" ");
        }
        Serial.println();
    }
}

/*********************************************************************************************************
  END FILE
*********************************************************************************************************/
