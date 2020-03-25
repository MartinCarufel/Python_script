#ifndef __VPP_H__
#define __VPP_H__

#define VPP_YEAR                              2019
#define VPP_MAKE                              "HONDA PUSH2START GAZ"
#define VPP_MODEL                             "ACCORD 4DOOR SEDAN  "

#define VPP_VPP_VERSION                       1.001

#define SENSE_CAN_COUNT                         2
#define SENSE_CAN1_SPEED                        500000
#define SENSE_CAN2_SPEED                        250000

#define SENSE_ENT_HOOD_OPEN_CAN                 CAN1
#define SENSE_ENT_HOOD_OPEN_ID                  0x001

#define SENSE_ENT_SLIDE_DOOR_RP_POSITION_CAN    CAN1
#define SENSE_ENT_SLIDE_DOOR_RP_POSITION_ID     0x001

#define SENSE_ENT_HOOD_OPEN                     0x4C63A615
#define SENSE_ENT_SLIDE_DOOR_RP_POSITION        0xBF9EE99D

STATUS_DATA Status_Memory[] = {
  {SENS_ENT_HOOD_OPEN                   , 0},
  {SENS_ENT_SLIDE_DOOR_RP_POSITION      , 0},
}; 

STATUS_DATA Status_Memory_WStr[] = {
  { 0x4c63a615, 0, "ENT_HOOD_OPEN                   "},
  { 0xbf9ee99d, 0, "ENT_SLIDE_DOOR_RP_POSITION      "},
}; 

func_Hash_Name[] = {
  { 0xbb38b52e, 0, "LOW_PRIORITY0                   "},
  { 0xcc3f85b8, 0, "LOW_PRIORITY1                   "},
}; 

#endif
