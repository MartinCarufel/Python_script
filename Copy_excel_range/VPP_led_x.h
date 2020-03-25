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

#define SENSE_ENT_TRUNK_GLASS_OPEN_CAN          CAN1
#define SENSE_ENT_TRUNK_GLASS_OPEN_ID           0x001

#define SENSE_ENT_GAS_CAP_OPEN_CAN              CAN1
#define SENSE_ENT_GAS_CAP_OPEN_ID               0x001

#define SENSE_ENT_WINDOWS_FD_UP_CAN             CAN1
#define SENSE_ENT_WINDOWS_FD_UP_ID              0x001

#define SENSE_ENT_ROOFTOP_OPEN_CAN              CAN1
#define SENSE_ENT_ROOFTOP_OPEN_ID               0x001

#define SENSE_RKE_REMOTE_ID_CAN                 CAN1
#define SENSE_RKE_REMOTE_ID_ID                  0x001

#define SENSE_RKE_IDLE_CAN                      CAN1
#define SENSE_RKE_IDLE_ID                       0x001

#define SENSE_RKE_LOCK_CAN                      CAN1
#define SENSE_RKE_LOCK_ID                       0x001

#define SENSE_RKE_UNLOCK_CAN                    CAN1
#define SENSE_RKE_UNLOCK_ID                     0x001

#define SENSE_RKE_TRUNK_CAN                     CAN1
#define SENSE_RKE_TRUNK_ID                      0x001

#define SENSE_RKE_PANIC_CAN                     CAN1
#define SENSE_RKE_PANIC_ID                      0x001

#define SENSE_RKE_DRIVER_SLIDE_DOOR_CAN         CAN1
#define SENSE_RKE_DRIVER_SLIDE_DOOR_ID          0x001

#define SENSE_RKE_POP_GLASS_CAN                 CAN1
#define SENSE_RKE_POP_GLASS_ID                  0x001

#define SENSE_DL_HANDLE_FD_CAN                  CAN1
#define SENSE_DL_HANDLE_FD_ID                   0x001

#define SENSE_DL_HANDLE_FP_CAN                  CAN1
#define SENSE_DL_HANDLE_FP_ID                   0x001

#define SENSE_DL_HANDLE_TRUNK_CAN               CAN1
#define SENSE_DL_HANDLE_TRUNK_ID                0x001

#define SENSE_DL_GAS_CAP_LOCK_CAN               CAN1
#define SENSE_DL_GAS_CAP_LOCK_ID                0x001

#define SENSE_DL_KEYPAD_IDLE_CAN                CAN1
#define SENSE_DL_KEYPAD_IDLE_ID                 0x001

#define SENSE_DL_KEYPAD_LOCK_CAN                CAN1
#define SENSE_DL_KEYPAD_LOCK_ID                 0x001

#define SENSE_DL_KEYPAD_UNLOCK_CAN              CAN1
#define SENSE_DL_KEYPAD_UNLOCK_ID               0x001

#define SENSE_DL_KEYPAD_TRUNK_CAN               CAN1
#define SENSE_DL_KEYPAD_TRUNK_ID                0x001

#define SENSE_DL_BARREL_DRIVER_KEY_IN_CAN       CAN1
#define SENSE_DL_BARREL_DRIVER_KEY_IN_ID        0x001

#define SENSE_DL_FOLD_MIRROR_OPEN_CAN           CAN1
#define SENSE_DL_FOLD_MIRROR_OPEN_ID            0x001

#define SENSE_DL_GLOVE_COMP_LOCK_CAN            CAN1
#define SENSE_DL_GLOVE_COMP_LOCK_ID             0x001

#define SENSE_SEC_ALARM_DISARM_CAN              CAN1
#define SENSE_SEC_ALARM_DISARM_ID               0x001

#define SENSE_SEC_ALARM_ARMING_CAN              CAN1
#define SENSE_SEC_ALARM_ARMING_ID               0x001

#define SENSE_SEC_ALARM_ARMED_CAN               CAN1
#define SENSE_SEC_ALARM_ARMED_ID                0x001

#define SENSE_SEC_ALARM_TRIGGERED_CAN           CAN1
#define SENSE_SEC_ALARM_TRIGGERED_ID            0x001

#define SENSE_SEC_LIGHT_ON_CAN                  CAN1
#define SENSE_SEC_LIGHT_ON_ID                   0x001

#define SENSE_SAF_BRAKE_SWITCH_ON_CAN           CAN1
#define SENSE_SAF_BRAKE_SWITCH_ON_ID            0x001

#define SENSE_SAF_EMERGENCY_BRAKE_ON_CAN        CAN1
#define SENSE_SAF_EMERGENCY_BRAKE_ON_ID         0x001

#define SENSE_SEC_ALARM_LIGHT_ON_CAN            CAN1
#define SENSE_SEC_ALARM_LIGHT_ON_ID             0x001

#define SENSE_IGN_SW_KEY_IN_CAN                 CAN1
#define SENSE_IGN_SW_KEY_IN_ID                  0x001

#define SENSE_IGN_SW_IGN_CAN                    CAN1
#define SENSE_IGN_SW_IGN_ID                     0x001

#define SENSE_IGN_SW_START_CAN                  CAN1
#define SENSE_IGN_SW_START_ID                   0x001

#define SENSE_EXTERNAL_LIGHT_PARK_CAN           CAN1
#define SENSE_EXTERNAL_LIGHT_PARK_ID            0x001

#define SENSE_EXTERNAL_LIGHT_LOW_BEAM_CAN       CAN1
#define SENSE_EXTERNAL_LIGHT_LOW_BEAM_ID        0x001

#define SENSE_EXTERNAL_LIGHT_HIGH_BEAM_CAN      CAN1
#define SENSE_EXTERNAL_LIGHT_HIGH_BEAM_ID       0x001

#define SENSE_EXTERNAL_LIGHT_HAZARD_CAN         CAN1
#define SENSE_EXTERNAL_LIGHT_HAZARD_ID          0x001

#define SENSE_ENT_HOOD_OPEN                     0x4C63A615
#define SENSE_ENT_SLIDE_DOOR_RP_POSITION        0xBF9EE99D
#define SENSE_ENT_TRUNK_GLASS_OPEN              0x9FF0B873
#define SENSE_ENT_GAS_CAP_OPEN                  0x63BED4ED
#define SENSE_ENT_WINDOWS_FD_UP                 0x6872233F
#define SENSE_ENT_ROOFTOP_OPEN                  0xBEC3B324
#define SENSE_RKE_REMOTE_ID                     0x78EB6F1B
#define SENSE_RKE_IDLE                          0x1A0E4E29
#define SENSE_RKE_LOCK                          0x41A56032
#define SENSE_RKE_UNLOCK                        0x9D9220C4
#define SENSE_RKE_TRUNK                         0x6CA5FBF3
#define SENSE_RKE_PANIC                         0x8A60F726
#define SENSE_RKE_DRIVER_SLIDE_DOOR             0x013E257F
#define SENSE_RKE_POP_GLASS                     0xBD0CF77E
#define SENSE_DL_HANDLE_FD                      0x5DC620FF
#define SENSE_DL_HANDLE_FP                      0x471CF482
#define SENSE_DL_HANDLE_TRUNK                   0x2C8B74EC
#define SENSE_DL_GAS_CAP_LOCK                   0x1DEAF055
#define SENSE_DL_KEYPAD_IDLE                    0xE15853B4
#define SENSE_DL_KEYPAD_LOCK                    0xBAF37DAF
#define SENSE_DL_KEYPAD_UNLOCK                  0x3A7B431C
#define SENSE_DL_KEYPAD_TRUNK                   0xE2E04217
#define SENSE_DL_BARREL_DRIVER_KEY_IN           0x1D6794DC
#define SENSE_DL_FOLD_MIRROR_OPEN               0x21B13142
#define SENSE_DL_GLOVE_COMP_LOCK                0xD0330900
#define SENSE_SEC_ALARM_DISARM                  0x3313CEE2
#define SENSE_SEC_ALARM_ARMING                  0xCC993C95
#define SENSE_SEC_ALARM_ARMED                   0xD641D6C7
#define SENSE_SEC_ALARM_TRIGGERED               0xE235DD6A
#define SENSE_SEC_LIGHT_ON                      0x5F3CC94B
#define SENSE_SAF_BRAKE_SWITCH_ON               0x36DE2C1F
#define SENSE_SAF_EMERGENCY_BRAKE_ON            0xB5D45AA4
#define SENSE_SEC_ALARM_LIGHT_ON                0xCBB371E3
#define SENSE_IGN_SW_KEY_IN                     0xE8A1EE48
#define SENSE_IGN_SW_IGN                        0x100C163F
#define SENSE_IGN_SW_START                      0x6AF807CA
#define SENSE_EXTERNAL_LIGHT_PARK               0x094549B4
#define SENSE_EXTERNAL_LIGHT_LOW_BEAM           0x2008D046
#define SENSE_EXTERNAL_LIGHT_HIGH_BEAM          0x096544E9
#define SENSE_EXTERNAL_LIGHT_HAZARD             0x10EA1EA2

STATUS_DATA Status_Memory[] = {
  {SENS_RKE_DRIVER_SLIDE_DOOR           , 0},
  {SENS_EXTERNAL_LIGHT_PARK             , 0},
  {SENS_EXTERNAL_LIGHT_HIGH_BEAM        , 0},
  {SENS_IGN_SW_IGN                      , 0},
  {SENS_EXTERNAL_LIGHT_HAZARD           , 0},
  {SENS_RKE_IDLE                        , 0},
  {SENS_DL_BARREL_DRIVER_KEY_IN         , 0},
  {SENS_DL_GAS_CAP_LOCK                 , 0},
  {SENS_EXTERNAL_LIGHT_LOW_BEAM         , 0},
  {SENS_DL_FOLD_MIRROR_OPEN             , 0},
  {SENS_DL_HANDLE_TRUNK                 , 0},
  {SENS_SEC_ALARM_DISARM                , 0},
  {SENS_SAF_BRAKE_SWITCH_ON             , 0},
  {SENS_DL_KEYPAD_UNLOCK                , 0},
  {SENS_RKE_LOCK                        , 0},
  {SENS_DL_HANDLE_FP                    , 0},
  {SENS_ENT_HOOD_OPEN                   , 0},
  {SENS_DL_HANDLE_FD                    , 0},
  {SENS_SEC_LIGHT_ON                    , 0},
  {SENS_ENT_GAS_CAP_OPEN                , 0},
  {SENS_ENT_WINDOWS_FD_UP               , 0},
  {SENS_IGN_SW_START                    , 0},
  {SENS_RKE_TRUNK                       , 0},
  {SENS_RKE_REMOTE_ID                   , 0},
  {SENS_RKE_PANIC                       , 0},
  {SENS_RKE_UNLOCK                      , 0},
  {SENS_ENT_TRUNK_GLASS_OPEN            , 0},
  {SENS_SAF_EMERGENCY_BRAKE_ON          , 0},
  {SENS_DL_KEYPAD_LOCK                  , 0},
  {SENS_RKE_POP_GLASS                   , 0},
  {SENS_ENT_ROOFTOP_OPEN                , 0},
  {SENS_ENT_SLIDE_DOOR_RP_POSITION      , 0},
  {SENS_SEC_ALARM_LIGHT_ON              , 0},
  {SENS_SEC_ALARM_ARMING                , 0},
  {SENS_DL_GLOVE_COMP_LOCK              , 0},
  {SENS_SEC_ALARM_ARMED                 , 0},
  {SENS_DL_KEYPAD_IDLE                  , 0},
  {SENS_SEC_ALARM_TRIGGERED             , 0},
  {SENS_DL_KEYPAD_TRUNK                 , 0},
  {SENS_IGN_SW_KEY_IN                   , 0},
}; 

STATUS_DATA Status_Memory_WStr[] = {
  { 0x13e257f, 0, "RKE_DRIVER_SLIDE_DOOR           "},
  { 0x94549b4, 0, "EXTERNAL_LIGHT_PARK             "},
  { 0x96544e9, 0, "EXTERNAL_LIGHT_HIGH_BEAM        "},
  { 0x100c163f, 0, "IGN_SW_IGN                      "},
  { 0x10ea1ea2, 0, "EXTERNAL_LIGHT_HAZARD           "},
  { 0x1a0e4e29, 0, "RKE_IDLE                        "},
  { 0x1d6794dc, 0, "DL_BARREL_DRIVER_KEY_IN         "},
  { 0x1deaf055, 0, "DL_GAS_CAP_LOCK                 "},
  { 0x2008d046, 0, "EXTERNAL_LIGHT_LOW_BEAM         "},
  { 0x21b13142, 0, "DL_FOLD_MIRROR_OPEN             "},
  { 0x2c8b74ec, 0, "DL_HANDLE_TRUNK                 "},
  { 0x3313cee2, 0, "SEC_ALARM_DISARM                "},
  { 0x36de2c1f, 0, "SAF_BRAKE_SWITCH_ON             "},
  { 0x3a7b431c, 0, "DL_KEYPAD_UNLOCK                "},
  { 0x41a56032, 0, "RKE_LOCK                        "},
  { 0x471cf482, 0, "DL_HANDLE_FP                    "},
  { 0x4c63a615, 0, "ENT_HOOD_OPEN                   "},
  { 0x5dc620ff, 0, "DL_HANDLE_FD                    "},
  { 0x5f3cc94b, 0, "SEC_LIGHT_ON                    "},
  { 0x63bed4ed, 0, "ENT_GAS_CAP_OPEN                "},
  { 0x6872233f, 0, "ENT_WINDOWS_FD_UP               "},
  { 0x6af807ca, 0, "IGN_SW_START                    "},
  { 0x6ca5fbf3, 0, "RKE_TRUNK                       "},
  { 0x78eb6f1b, 0, "RKE_REMOTE_ID                   "},
  { 0x8a60f726, 0, "RKE_PANIC                       "},
  { 0x9d9220c4, 0, "RKE_UNLOCK                      "},
  { 0x9ff0b873, 0, "ENT_TRUNK_GLASS_OPEN            "},
  { 0xb5d45aa4, 0, "SAF_EMERGENCY_BRAKE_ON          "},
  { 0xbaf37daf, 0, "DL_KEYPAD_LOCK                  "},
  { 0xbd0cf77e, 0, "RKE_POP_GLASS                   "},
  { 0xbec3b324, 0, "ENT_ROOFTOP_OPEN                "},
  { 0xbf9ee99d, 0, "ENT_SLIDE_DOOR_RP_POSITION      "},
  { 0xcbb371e3, 0, "SEC_ALARM_LIGHT_ON              "},
  { 0xcc993c95, 0, "SEC_ALARM_ARMING                "},
  { 0xd0330900, 0, "DL_GLOVE_COMP_LOCK              "},
  { 0xd641d6c7, 0, "SEC_ALARM_ARMED                 "},
  { 0xe15853b4, 0, "DL_KEYPAD_IDLE                  "},
  { 0xe235dd6a, 0, "SEC_ALARM_TRIGGERED             "},
  { 0xe2e04217, 0, "DL_KEYPAD_TRUNK                 "},
  { 0xe8a1ee48, 0, "IGN_SW_KEY_IN                   "},
}; 

func_Hash_Name[] = {
  { 0xbb38b52e, 0, "LOW_PRIORITY0                   "},
  { 0xcc3f85b8, 0, "LOW_PRIORITY1                   "},
}; 

#endif
