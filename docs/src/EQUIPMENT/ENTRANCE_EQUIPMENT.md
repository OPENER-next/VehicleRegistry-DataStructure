# EntranceEquipment

An equipment to describe an entrance like a door or barrier.

```xml
<EntranceEquipment version="any" id="321">
  ...
</EntranceEquipment>
```

The definition of the inside and outside of an entrance requires its orientation. For fixed object entrances this is done via the `DoorOrientation` property. However this only allows compass directions which do not apply to vehicles. Therefore this requires the `Orientation` property from the `DeckEntrance` this `EntranceEquipment` is assigned to.

 The `Orientation` of the `DeckEntrance` points towards the **outside**.

```
             ▲
             │      Outside
             │   ┌───────────┐
Orientation  │   │Door       │
             │   └───────────┘
             │      Inside
```

**XSD:** [`xsd/netex_part_1/part1_ifopt/netex_ifopt_equipmentAccess_version.xsd`](https://github.com/NeTEx-CEN/NeTEx/blob/next/xsd/netex_part_1/part1_ifopt/netex_ifopt_equipmentAccess_version.xsd#L1234)

## Location
```
PublicationDelivery/dataObjects/ResourceFrame/equipments
```

## Properties

### Width
Clearance width of the entrance.

#### Example

```xml
<Width>1.2</Width>
```

### Height
Clearance height of the entrance.

#### Example

```xml
<Height>2</Height>
```

### DirectionOfUse

Direction in which the entrance can be used. Default is `both`.

#### Values (`DirectionOfUseEnumeration`):
- up
- down
- both

#### Example

```xml
<DirectionOfUse>both</DirectionOfUse>
```

### Door
Whether there is a door in the entrance. If `false` it describe an opening in a wall.

#### Example

```xml
<Door>true</Door>
```

### DoorHandleOutside

The type of the outer door handle. This property can also be thought of as the handle against the door direction.

#### Values (`DoorHandleEnumeration`):
- none
- lever
- button
- knob
- crashBar
- doorHandle
- grabRail
- windowLever
- vertical
- other

#### Example

```xml
<DoorHandleOutside>doorHandle</DoorHandleOutside>
```

### DoorHandleInside

The type of the inner door handle. This property can also be thought of as the handle in door direction.

#### Values (`DoorHandleEnumeration`):
- none
- lever
- button
- knob
- crashBar
- doorHandle
- grabRail
- windowLever
- vertical
- other

#### Example

```xml
<DoorHandleInside>doorHandle</DoorHandleInside>
```

### KeptOpen
Whether the door is kept open.

#### Example

```xml
<KeptOpen>false</KeptOpen>
```

### DoorType

The type of door.

#### Values (`DoorTypeEnumeration`):
- hingedSingle
- hingedPair
- slidingSingle
- slidingPair
- foldingSingle
- foldingPair
- hingedRamp
- revolving
- other
- none
- unknown

#### Example

```xml
<DoorType>slidingSingle</DoorType>
```

### Barrier

Whether there is a physical barrier across the doorway.

#### Example

```xml
<Barrier>true</Barrier>
```

### Staffing

Whether the door is staffed.

#### Example

```xml
<Staffing>false</Staffing>
```

### AutomaticDoor

Whether doors open automatically.

For doors with a `DoorType` set to `revolving` this indicates that the door rotates on its own without manually pushing it. `AutomaticDoor` therefore supersedes the `RevolvingDoor` property.

#### Example

```xml
<AutomaticDoor>false</AutomaticDoor>
```

### DoorControlElementHeight

Indicates door control element height. This could be e.g. a door handle or a door button.

#### Example

```xml
<DoorControlElementHeight>1</DoorControlElementHeight>
```

### GlassDoor

Whether the door is made of glass. Useful in navigation to warn visually impaired people.

#### Example

```xml
<GlassDoor>false</GlassDoor>
```

### WheelchairPassable

Whether the entrance can be passed with a wheelchair.

#### Example

```xml
<WheelchairPassable>true</WheelchairPassable>
```

### WheelchairUnaided

Whether the entrance can be passed in a wheelchair without aid.

#### Example

```xml
<WheelchairUnaided>false</WheelchairUnaided>
```

### DoorstepMark

Whether there is a tactile doorstep mark.

#### Example

```xml
<DoorstepMark>false</DoorstepMark>
```

### NecessaryForceToOpen

The necessary force to open the door. While these are subjective values they might still be beneficial in regards to accessibility.

#### Values (`NecessaryForceEnumeration`):
- noForce
- lightForce
- mediumForce
- heavyForce
- unknown

#### Example

```xml
<NecessaryForceToOpen>heavyForce</NecessaryForceToOpen>
```

### SuitableForCycles

Whether the entrance can be passed with a bicycle.

#### Example

```xml
<SuitableForCycles>true</SuitableForCycles>
```

### RampDoorbell

When there is a removable ramp, whether the entrance has a dedicated doorbell to ask for the ramp.

#### Example

```xml
<RampDoorbell>false</RampDoorbell>
```

### TurningSpacePosition

Whether there is a turning space for wheelchair users. The manoeuvering space for wheelchairs is a space left in the immediate vicinity of the door to operate it correctly and is materialised by a rectangle located at the base of the door.

#### Values (`EntranceTurningSpacePositionEnumeration`):
- none
- outside
- inside
- insideAndOutside

#### Example

```xml
<TurningSpacePosition>insideAndOutside</TurningSpacePosition>
```

### WheelchairTurningCircle

The diameter of the turning circle within the turning space for a wheelchair.

#### Example

```xml
<WheelchairTurningCircle>1.2</WheelchairTurningCircle>
```