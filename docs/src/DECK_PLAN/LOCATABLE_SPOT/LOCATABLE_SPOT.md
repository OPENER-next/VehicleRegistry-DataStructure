# LocatableSpot

An identifiable individual area within a given [PassengerSpace](../DECK_spot/PASSENENGER_SPACE.md), which may potentially be allocated to a single passenger.

The properties below are general properties that any `LocatableSpot` provides.

**XSD:** [`xsd/netex_framework/netex_reusableComponents/netex_seatingPlan_version.xsd`](https://github.com/NeTEx-CEN/NeTEx/blob/next/xsd/netex_framework/netex_reusableComponents/netex_seatingPlan_version.xsd#L281)

## Properties

### Name

A name to identify the spot.

#### Example
```xml
<Name>
  <Text lang="en">Compartment 3</Text>
</Name>
```

### Description

A description providing additional information about the spot.

#### Example
```xml
<Description>
  <Text lang="en">Second class family compartment.</Text>
</Description>
```

### Centroid

The center position of the `LocatableSpot` in a 2D cartesian coordinate system. The parent [Deck](../DECK.md) element acts as the bounding box of the `LocatableSpot` and the unit is in meters.
This is only useful for generating a visual deck plan.

#### Example
```xml
<Centroid>
  <Location>
    <gml:pos>2 10</gml:pos>
  </Location>
</Centroid>
```

### Label

An attached or printed name of the spot like the seat number.

#### Example
```xml
<Label>
  <Text lang="en">C3</Text>
</Label>
```

### Orientation

Orientation of the spot relative to the vehicle front. Default is `forwards`.
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

The inner width of the spot in meters.
Width is measured perpendicular to the spot's forward orientation.

#### Example
```xml
<Width>3</Width>
```

### Length

The inner length of the spot in meters.
Length is measure parallel to the spot's forward orientation.

#### Example
```xml
<Length>2</Length>
```

### Height

The inner height of the spot in meters.

#### Example
```xml
<Height>2</Height>
```

### FacilitySetRef

Facilities available at this spot. This is a reference to a `ServiceFacilitySet` defined under:

```
PublicationDelivery/dataObjects/ResourceFrame/vehicleTypes/VehicleType/facilities
```

#### Example

```xml
<ServiceFacilitySetRef ref="sfs:01"/>
```

### actualVehicleEquipments

Equipment available at this spot. This contains references to [`Equipment`](../EQUIPMENT/EQUIPMENT.md) defined under:

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

### LocatableSpotType

The category of the spot.

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
<LocatableSpotType>seat</LocatableSpotType>
```

### SpotRowRef

Reference to the [`SpotRow`](../DECK.md#spotrows) this spot belongs to.

#### Example

```xml
<SpotRowRef ref="5"/>
```

### SpotColumnRef

Reference to the [`SpotColumn`](../DECK.md#spotcolumns) this spot belongs to.

#### Example

```xml
<SpotColumnRef ref="B"/>
```
