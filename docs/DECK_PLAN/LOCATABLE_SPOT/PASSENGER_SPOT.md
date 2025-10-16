# PassengerSpot

A [LocatableSpot](LOCATABLE_SPOT.md) defining a designated seat or other space for a passenger within a given [PassengerSpace](../DECK_SPACE/PASSENGER_SPACE.md).

```xml
<PassengerSpot version="any" id="321">
  ...
</PassengerSpot>
```

**XSD:** [`xsd/netex_framework/netex_reusableComponents/netex_seatingPlan_version.xsd`](https://github.com/NeTEx-CEN/NeTEx/blob/next/xsd/netex_framework/netex_reusableComponents/netex_seatingPlan_version.xsd#L366)

## Location

```
PublicationDelivery/dataObjects/ResourceFrame/deckPlans/DeckPlan/decks/Deck/deckSpaces/PassengerSpace/passengerSpots
```

## Properties

### TableType

Whether the passenger spot offers the usage of a table and what kind of table.

#### Values (`TableTypeEnumeration`):
- none
- fixedFlat
- foldDownFlat
- seatBackFolding
- armRestFolding
- seatClipon
- other
- unknown

#### Example

```xml
<TableType>fixedFlat</TableType>
```

### HasArmrest

Whether the passenger spot has an armrest.

#### Example

```xml
<HasArmrest>True</HasArmrest>
```

### LegSpace

The available leg space for the passenger spot in meters.

#### Example

```xml
<Legspace>0.4</Legspace>
```

### HasPower

Whether passenger spot offers the usage a power socket.

#### Example

```xml
<HasPower>False</HasPower>
```

### IsByWindow

Whether the passenger spot is next to a window. Useful for seat reservation preferences.

#### Example

```xml
<IsByWindow>True</IsByWindow>
```

### IsByAisle

Whether the passenger spot is next to an aisle. Useful for seat reservation preferences.

#### Example

```xml
<IsByAisle>False</IsByAisle>
```

### IsBetweenSeats

Whether the passenger spot is between two seats, i.e. not next to an aisle or a window with seats on either side. Useful for seat reservation preferences.

#### Example

```xml
<IsBetweenSeats>True</IsBetweenSeats>
```

### IsInFrontRow

Whether the passenger spot is in the front row. Useful for seat reservation preferences.

#### Example

```xml
<IsInFrontRow>False</IsInFrontRow>
```

### IsInEndRow

Whether the passenger spot is in the end row, next to a wall. Useful for seat reservation preferences.

#### Example

```xml
<IsInEndRow>True</IsInEndRow>
```

### IsFacingWindow

Whether the passenger spot is facing a window. Useful for seat reservation preferences.

#### Example

```xml
<IsFacingWindow>True</IsFacingWindow>
```

### IsFacingAisle

Whether the passenger spot is facing a window. Useful for seat reservation preferences.

#### Example

```xml
<IsFacingAisle>True</IsFacingAisle>
```

### PriorityUse

Whether some passengers are privileged to use this `PassengerSpot`. (See [NeTEx Proposal](https://github.com/NeTEx-CEN/NeTEx/issues/898))

### Values (`PriorityUseEnumeration`):
- none
- personWithReducedMobility (priority seat as defined in EN 16585-2:2022)
- senior
- disabled
- injured
- pregnantWoman
- infantCarryingPerson
- child
- woman
- guideDog
- wheelchairUser (wheelchair space as defined in EN 16585-2:2022)
- walkingChair
- pram
- bicycle

### Example
```xml
<PriorityUse>senior disabled injured pregnantWoman infantCarryingPerson</PriorityUse>
```
