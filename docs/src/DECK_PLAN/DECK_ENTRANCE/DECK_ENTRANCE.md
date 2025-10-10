# DeckEntrance

A `DeckEntrance` is an entrance to or within a [`Deck`](../DECK.md).

In the current NeTEx `DeckPlan` examples `DeckEntrance` connections are modelled via special `DeckEntranceCouple` elements. However this method is very verbose and leads to data duplications, see:
- [https://public.3.basecamp.com/p/HfgDsdYNKac6zjw3J1Y3K5SY](https://public.3.basecamp.com/p/HfgDsdYNKac6zjw3J1Y3K5SY)
- [https://github.com/NeTEx-CEN/NeTEx/pull/952](https://github.com/NeTEx-CEN/NeTEx/pull/952)

Therefore in this data structure a `DeckEntrance` is simply modeled in one of the rooms it belongs to and referenced from the other room.

Simple example pseudo code:
```
<DeckSpace id="A">
  <deckEntrances>
    <DeckEntrance id="1">
<DeckSpace id="B">
  <deckEntrances>
    <DeckEntranceRef ref="2">
```

The properties below are general properties that any `DeckEntrance` provides.

**XSD:** [`xsd/netex_framework/netex_reusableComponents/netex_deckPlan_version.xsd`](https://github.com/NeTEx-CEN/NeTEx/blob/next/xsd/netex_framework/netex_reusableComponents/netex_deckPlan_version.xsd#L652)

## Properties

The properties `HeightFromGround`, `IsAutomatic` and `HasDoor` are omitted in favor of equivalent properties from `AccessVehicleEquipment` and `EntranceEquipment`.

### Name

A name to identify the entrance.

#### Example
```xml
<Name>
  <Text lang="en">Compartment 3</Text>
</Name>
```

### Description

A description providing additional information about the entrance.

#### Example
```xml
<Description>
  <Text lang="en">Front entrance to carriage W02.</Text>
</Description>
```

### Centroid

The center position of the `DeckEntrance` in a 2D cartesian coordinate. The parent [Deck](../DECK.md) element acts as the bounding box of the `DeckEntrance` and the unit is in meters.
This is only useful for generating a visual deck plan.

#### Example
```xml
<Centroid>
  <Location>
    <gml:pos>2 10</gml:pos>
  </Location>
</Centroid>
```

### Orientation

Orientation of the entrance relative to the vehicle front. Default is `forwards`.
**Note:** The orientation is **not** linked to the driving direction, instead vehicles even carriages have a front and back which defines their directionality.

#### Values (`ComponentOrientationEnumeration`):
- forwards
- backwards
- unknown
- leftwards
- rightwards
- angledLeft
- angledRight
- angledBackLeft
- angledBackRight

#### Example
```xml
<Orientation>rightwards</Orientation>
```

### Width

The inner width of the entrance in meters.

#### Example
```xml
<Width>3</Width>
```

### Height

The inner height of the entrance in meters.

#### Example
```xml
<Height>2</Height>
```

### FacilitySetRef

Facilities available at this entrance. This is a reference to a `ServiceFacilitySet` defined under:

```
PublicationDelivery/dataObjects/ResourceFrame/vehicleTypes/VehicleType/facilities
```

#### Example

```xml
<ServiceFacilitySetRef ref="sfs:01"/>
```

### actualVehicleEquipments

Equipment available at this entrance. This contains references to [`Equipment`](../EQUIPMENT/EQUIPMENT.md) defined under:

```
PublicationDelivery/dataObjects/ResourceFrame/equipments
```

#### Example

```xml
<actualVehicleEquipments>
  <ActualVehicleEquipment version="any" id="1">
    <Units>1</Units>
    <EntranceEquipmentRef version="any" ref="1"/>
  </ActualVehicleEquipment>
</actualVehicleEquipments>
```

### PublicUse

Whether the entrance is open to the public. Default is `true`.

#### Example
```xml
<PublicUse>false</PublicUse>
```

### DeckLevelRef

Reference to the [`DeckLevel`](../DECK_LEVEL.md) this entrance belongs to. If omitted this shall be inherited from the [Deck](../DECK.md) in which the `DeckEntrance` is defined.

#### Example
```xml
<DeckLevelRef ref="level:2"/>
```

### AccessibilityAssessment

Specific [AccessibilityAssessment](../ACCESSIBILITY_ASSESSMENT.md) of this `DeckEntrance`.

#### Example
```xml
<AccessibilityAssessment version="any" id="1">
  <MobilityImpairedAccess>partial</MobilityImpairedAccess>
  <suitabilities>
    <Suitability>
      <MedicalNeed>heartCondition</MedicalNeed>
      <Suitable>notSuitable</Suitable>
    </Suitability>
  </suitabilities>
  <Comment>Unsuitable for people with a heart pacemaker.</Comment>
</AccessibilityAssessment>
```

### VehicleSide

The location of the entrance relative to forward orientation of the vehicle (see [Orientation](#orientation)).

#### Values (`VehicleSideEnumeration`):
- leftSide
- rightSide
- frontEnd
- backEnd
- internal
- above
- below

#### Example
```xml
<VehicleSide>rightSide<VehicleSide/>
```

### DistanceFromFront

The distance of the door's forward edge from the front of the vehicle in meters.

#### Example
```xml
<DistanceFromFront>20.3</DistanceFromFront>
```

### DeckEntranceType

The category this deck entrance belongs to.

#### Values (`DeckEntranceTypeEnumeration`):
- external (entrance for boarding/alighting the vehicle)
- communicating (entrance for connecting carriages)
- internal (entrance inside a vehicle)

#### Example
```xml
<DeckEntranceType>external</DeckEntranceType>
```

### IsEmergencyExit

Whether the door is an emergency exit.

#### Example
```xml
<IsEmergencyExit>true</IsEmergencyExit>
```
