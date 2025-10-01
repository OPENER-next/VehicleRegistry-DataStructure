# PassengerSpace

A [`DeckSpace`](DECK_SPACE.md) defining an area within a vehicle for use by passengers.

```xml
<PassengerSpace version="any" id="321">
  ...
</PassengerSpace>
```

**XSD:** [`xsd/netex_framework/netex_reusableComponents/netex_deckPlan_version.xsd`](https://github.com/NeTEx-CEN/NeTEx/blob/next/xsd/netex_framework/netex_reusableComponents/netex_deckPlan_version.xsd#L458)

## Location

```
PublicationDelivery/dataObjects/ResourceFrame/deckPlans/DeckPlan/decks/Deck/deckSpaces
```

## Properties

### PassengerSpaceType

The category of this passenger space.

#### Values (`PassengerSpaceTypeEnumeration`):
- seatingArea
- passengerCabin
- vehicleArea
- luggageStore
- corridor
- restaurant
- toilet
- bathroom
- other

#### Example
```xml
<PassengerSpaceType>passengerCabin</PassengerSpaceType>
```

### StandingAllowed

Whether standing is allowed in this passenger space.

#### Example

```xml
<StandingAllowed>false</StandingAllowed>
```

### passengerSpots

Individual passenger spots (usually seats) contained in this passenger space. This contains a list of [`PassengerSpot`](../PASSENGER_SPOT.md) definitions or references.

#### Example

```xml
<passengerSpots>
  <PassengerSpot version="any" id="2">
    ...
  </PassengerSpot>

  <PassengerSpotRef ref="1">
</passengerSpots>
```

### luggageSpots

Individual luggage spots contained in this passenger space. This contains a list of [`LuggageSpot`](../LUGGAGE_SPOT.md) definitions or references.

#### Example

```xml
<luggageSpots>
  <LuggageSpot version="any" id="2">
    ...
  </LuggageSpot>

  <LuggageSpotRef ref="1">
</luggageSpots>
```

### passengerVehicleSpots

Individual passenger vehicle spots like bicycle stands on a train or parking spots on a ferry contained in this passenger space. This contains a list of [`PassengerVehicleSpot`](../PASSENGER_VEHICLE_SPOT.md) definitions or references.

#### Example

```xml
<passengerVehicleSpots>
  <PassengerVehicleSpot version="any" id="2">
    ...
  </PassengerVehicleSpot>

  <PassengerVehicleSpotRef ref="1">
</passengerVehicleSpots>
```

### spotAffinities

A grouping of related passenger spots. This contains a list of `SpotAffinity` definitions which in turn describe the type (`SpotAffinityType`) and members (`members`) of the relation.

This is mainly relevant when booking tickets as a group, but some people may also prefer booking a seat not part of a seat block.

#### Values (`SpotAffinityTypeEnumeration`):
- faceToFace
- sideBySide
- contiguousRow
- sharedTable
- seatBlock
- lowerBerths
- sharedCompartment
- wheelchairCompanionSeat
- other

#### Example

```xml
<spotAffinities>
  <SpotAffinity>
    <SpotAffinityType>sharedTable</SpotAffinityType>
    <members>
      <PassengerSpotRef ref="3C" />
      <PassengerSpotRef ref="3D" />
      <PassengerSpotRef ref="4C" />
      <PassengerSpotRef ref="4D" />
    </members>
  </SpotAffinity>
</spotAffinities>
```
