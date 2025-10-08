# DeckSpace

A `DeckSpace` is an area within a vehicle delimiting a particular use such as a seating compartment, WC, on-board restaurant or gangway. A `DeckSpace` may contain other spaces (see [`ParentDeckSpaceRef`](#parentdeckspaceref)) and different types of `DeckSpace`s may overlap.

The properties below are general properties that any `DeckSpace` provides.

**XSD:** [`xsd/netex_framework/netex_reusableComponents/netex_deckPlan_version.xsd`](https://github.com/NeTEx-CEN/NeTEx/blob/next/xsd/netex_framework/netex_reusableComponents/netex_deckPlan_version.xsd#L322)

## Properties

### Label

An attached or printed name of the space like the name found on a room sign.

#### Example
```xml
<Label>
  <Text lang="en">C3</Text>
</Label>
```

### Name

A name to identify the space.

#### Example
```xml
<Name>
  <Text lang="en">Compartment 3</Text>
</Name>
```

### Description

A description providing additional information about the space.

#### Example
```xml
<Description>
  <Text lang="en">Second class family compartment.</Text>
</Description>
```

### Orientation

Orientation of the space relative to the vehicle front. Default is `forwards`.
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
<Orientation>backwards</Orientation>
```

### Width

The inner width of the space in meters.
Width is measured perpendicular to the space's forward orientation.

#### Example
```xml
<Width>3</Width>
```

### Length

The inner length of the space in meters.
Length is measure parallel to the space's forward orientation.

#### Example
```xml
<Length>2</Length>
```

### Height

The inner height of the space in meters.

#### Example
```xml
<Height>2</Height>
```

### FacilitySetRef

Facilities available at this space. This is a reference to a `ServiceFacilitySet` defined under:

```
PublicationDelivery/dataObjects/ResourceFrame/vehicleTypes/VehicleType/facilities
```

#### Example

```xml
<ServiceFacilitySetRef ref="sfs:01"/>
```

### actualVehicleEquipments

Equipment available at this space. This contains references to [`Equipment`](../EQUIPMENT/EQUIPMENT.md) defined under:

```
PublicationDelivery/dataObjects/ResourceFrame/equipments
```

#### Example

```xml
<actualVehicleEquipments>
  <ActualVehicleEquipment version="any" id="1">
    <Units>1</Units>
    <SanitaryEquipmentRef version="any" ref="1"/>
  </ActualVehicleEquipment>
</actualVehicleEquipments>
```

### PublicUse

Whether the space is open to the public. Default is `true`.

#### Example
```xml
<PublicUse>false</PublicUse>
```

### DeckLevelRef

Reference to the [`DeckLevel`](../DECK_LEVEL.md) this space belongs to. If omitted this shall be inherited from the [Deck](../DECK.md) in which the `DeckSpace` is defined.

#### Example
```xml
<DeckLevelRef ref="level:2"/>
```

### FareClass

The fare class of this space. Defaults to `any`.

#### Values (`FareClassEnumeration`):
- unknown
- firstClass
- secondClass
- thirdClass
- preferente
- premiumClass
- businessClass
- standardClass
- turista
- economyClass
- any

#### Example
```xml
<FareClass>firstClass</FareClass>
```

### Covered

Whether the space is covered. Default is `true`.

#### Example
```xml
<Covered>false</Covered>
```

### AirConditioned

Whether the space has air conditioning.

#### Example
```xml
<AirConditioned>true</AirConditioned>
```

### SmokingAllowed

Whether smoking is allowed in this space. Defaults to `false`.

#### Example
```xml
<SmokingAllowed>true</SmokingAllowed>
```

### ParentDeckSpaceRef

Reference to another `DeckSpace` of which this space is a part of.

#### Example
```xml
<ParentDeckSpaceRef ref="passenger-space:43"/>
```

### deckEntrances

Entrances connected to this space. This contains a list of [`DeckEntrance`](../DECK_ENTRANCE/DECK_ENTRANCE.md) definitions or references.

#### Example

```xml
<deckEntrances>
  <PassengerEntrance version="any" id="2">
    ...
  </PassengerEntrance>

  <PassengerEntranceRef ref="1">
</deckEntrances>
```

### deckWindows

Windows adjoining this space. This contains a list of [`DeckWindow`](../DECK_WINDOW.md) definitions or references.

#### Example
```xml
<deckWindows>
  <DeckWindow version="any" id="2">
    ...
  </DeckWindow>

  <DeckWindowRef ref="1">
</deckWindows>
```

### TotalCapacity

The total capacity of people for the space.

#### Example
```xml
<TotalCapacity>10</TotalCapacity>
```

### deckSpaceCapacities

Individual capacities by category such as bed, standing, seat etc.

#### Values (`TypeOfLocatableSpotEnumeration`):
- seat
- bed
- standingSpace
- wheelchairSpace
- pushchairSpace
- luggageSpace
- bicycleSpace
- vehicleSpace
- specialSpace
- other

#### Example
```xml
<deckSpaceCapacities>
  <DeckSpaceCapacity version="any" id="1">
    <LocatableSpotType>seating</LocatableSpotType>
    <Capacity>20</Capacity>
  </DeckSpaceCapacity>
  <DeckSpaceCapacity version="any" id="2">
    <LocatableSpotType>standingSpace</LocatableSpotType>
    <Capacity>20</Capacity>
  </DeckSpaceCapacity>
</deckSpaceCapacities>
```
