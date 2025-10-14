# WheelchairVehicleEquipment

This equipment is not used because all properties are already covered by other elements of the data structure.

## Property mapping

### HasWheelchairSpaces + NumberOfWheelchairAreas
- `VehicleType/capacities/PassengerCapacity/WheelchairPlaceCapacity`
- `DeckSpace/deckSpaceCapacities/DeckSpaceCapacity/LocatableSpotType=wheelchairSpace`
- `PassengerSpot/LocatableSpotType=wheelchairSpace`

### WidthOfAccessArea + LengthOfAccessArea + HeightOfAccessArea
`PassengerSpot`:

```xml
<PassengerSpot>
  <LocatableSpotType>wheelchairSpace</LocatableSpotType>
  <Width>2</Width>
  <Length>1.5</Length>
  <Height>2.3</Height>
</PassengerSpot>
```

### WheelchairTurningCircle
Not perfectly covered, but the turning circle may also be calculated by width and length.
- `EntranceEquipment/WheelchairTurningCircle`
- `SanitaryEquipment/WheelchairTurningCircle`

### CompanionSeat
`spotAffinities` From `PassengerSpace`:
```xml
<spotAffinities>
  <SpotAffinity>
    <SpotAffinityType>wheelchairCompanionSeat</SpotAffinityType>
    <members>
      <PassengerSpotRef ref="3C" />
      <PassengerSpotRef ref="3D" />
    </members>
  </SpotAffinity>
</spotAffinities>
```
