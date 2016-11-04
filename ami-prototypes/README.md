This project intends to offer different examples about how to interact with the PHAT API witch uses a JSON RPC protocol.
The aim is to show examples for several programming languages. For now, only python is available.

# JSON RPC Methods
**IMPORTANT:** All parameters for the methods have to be String type!
## Get information
### Help method
help [env|body|device|info]
#### Help env
```JSON
[
    {
        "cDebug":"true",
        "cUsage":"SetWallTransparency <level>",
        "cName":"SetWallTransparency",
        "cType":"env"
    },{
        "cDebug":"false",
        "cUsage":"UpdateDateTime [hourOfDay] [min] [sec] [dayOfMonth] [month] [year]",
        "cName":"UpdateDateTime",
        "cType":"env"
    },{
        "cDebug":"false",
        "cUsage":"CreateHouse <House3room2bath|Duplex|BrickHouse60m>",
        "cName":"CreateHouse",
        "cType":"env"
    },{
        "cDebug":"false",
        "cUsage":"SwitchLight <roomName> <true|false>",
        "cName":"SwitchLight",
        "cType":"env"
    },{
        "cDebug":"true","cUsage":"ShowNavMesh <true|false>",
        "cName":"ShowNavMesh",
        "cType":"env"
    },{
        "cDebug":"true",
        "cUsage":"showLabels <true|false> [scale] [elevation]",
        "cName":"showLabels",
        "cType":"env"
    }
]
```
#### Help body
**Usage methods list:**

```
AlignBodyWith <bodyId> <entityId>
AttachIcon <bodyId> <imagePath> <true|false>
BodyLabel <bodyId> <true|false>
CloseObject <bodyId> <bodyId> <objectId> [minDistance]
CreateBody <bodyId> <Elder|Young|ElderLP>
DebugSkeleton <bodyId> <true|false>
FallDown <bodyId>
GoCloseToBody <bodyId> <targetBodyId>
GoCloseToObject <bodyId> <bodyId> <targetObjectId> [minDistance]
GoIntoBed <bodyId> <bedId>
GoToSpace <bodyId> <spaceId>
LookAt <bodyId> <targetId>
OpenObject <bodyId> <bodyId> <objectId> [minDistance]
PickUp <bodyId> <bodyId> <entityId> <Left|Right>
RemoveBodyFromSpace <bodyId>
RotateToward <bodyId> <bodyId> <entityId> [true|false]
SayASentence <bodyId> <message> [volume]
SetBodyColor <bodyId> <r> <g> <b> <a>
SetBodyHeight <bodyId> <height>
SetBodyInHouseSpace <bodyId> <spaceId>
SetBodyXYZ <bodyId> <x> <y> <z>
SetCameraToBody <bodyId> <distance> <height>
SetDisplSpeed <bodyId> <speed>
SetPCListenerToBody <bodyId>
SetRigidArm <bodyId> <true|false> <true|false>
SetShortSteps <bodyId> <true|false>
SetStoopedBody <bodyId> <true|false>
ShowLabelsOfVisibleObjects <bodyId> <true|false>
SitDown <bodyId> <placeId>
StandUp <bodyId>
TremblingHand <bodyId> <true|false> <true|false>
TremblingHead <bodyId> <true|false>
WaitForBody <bodyId> <targetBodyId>
```

### agentInfo method
agentInfo <bodyId>

### bodyInfo method
bodyInfo [bodyId]

**Result example:**
```JSON
[
  {
    "date":"Thu Sep 29 14:03:15 CEST 2016",
    "posture":"Standing",
    "walking":false,
    "lastCommand":"GoToCommand(Human0 (8.766094 2.3841858E-7 1.7770876))",
    "id":"Human0",
    "maxSpeed":0.5,
    "anim":null,
    "room":"LivingRoom"
  }
  {
    "date":"Thu Sep 29 14:03:15 CEST 2016",
    "posture":"Sitting",
    "walking":false,
    "lastCommand":"GoToCommand(Human0 (8.766094 2.3841858E-7 1.7770876))",
    "id":"Human1",
    "maxSpeed":0.5,
    "anim":null,
    "room":"Kitchen"
  }
]
```
### envInfo method
envInfo [roomId]

envInfo without arguments show main information about the environment, for example:
```JSON
{
  "rooms":
  [
    "Kitchen",
    "BathRoom1",
    "BathRoom2",
    "BedRoom1",
    "Hall",
    "BedRoom2",
    "LivingRoom",
    "Outside",
    "Terrace",
    "SCorridor0"
  ],
  "name":"House1",
  "type":"House3room2bath"
}
```
if you want to get more info about a room, you have to pass as parameter the name of the room.
For example, the methods with Kitchen as parameter returns:

```JSON
{
  "name":"Kitchen",
  "objects":
  [
    {
      "role":"PlaceToSeat",
      "id":"Chair1"
    }
    {
      "role":"PlaceToSeat",
      "id":"Chair2"
    }
    {
      "role":"Bottle",
      "id":"Bottle1"
    }
    {
      "role":"Sink",
      "id":"Sink"
    }
    {
      "role":"Table",
      "id":"Table1"
    }
    {
      "role":"Extractor",
      "id":"Extractor1"
    }
  ]
}
```
