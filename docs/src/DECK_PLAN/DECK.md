# Deck

NeTEx loosely defines a `Deck` as an area within a vehicle made up of one or more [DeckSpaces](DECK_SPACE/DECK_SPACE.md). In this data structure a `Deck` is defined as an area grouping all [DeckSpaces](DECK_SPACE/DECK_SPACE.md) located on the same [DeckLevel](DECK_LEVEL.md). [DeckSpaces](DECK_SPACE/DECK_SPACE.md) spanning multiple decks (e.g. a staircase) must be recreated per `Deck` (see [rational](../rationales/DECK_SPACES_ACROSS_LEVELS.md)). Therefore a one to one mapping from `Deck` to [DeckLevel](DECK_LEVEL.md) should exist.

```xml
<Deck version="any" id="321">
  ...
</Deck>
```

**XSD:** [`xsd/netex_framework/netex_reusableComponents/netex_deckPlan_version.xsd`](https://github.com/NeTEx-CEN/NeTEx/blob/next/xsd/netex_framework/netex_reusableComponents/netex_deckPlan_version.xsd#L190)

## Location

```
PublicationDelivery/dataObjects/ResourceFrame/deckPlans/DeckPlan/decks
```

## Properties

### Name

A name to identify the deck.

#### Example
```xml
<Name>
  <Text lang="en">1. Deck</Text>
</Name>
```

### DeckLevelRef

### deckSpaces

Any [DeckSpaces](DECK_SPACE/DECK_SPACE.md) that are part of this deck.

#### Example
```xml
<deckSpaces>
  <DeckSpace version="any" id="2">
    ...
  </DeckSpace>
  <DeckSpaceRef ref="1">
  ...
</deckSpaces>
```

### spotRows

Rows on a deck which can later be referenced by [LocatableSpots](LOCATABLE_SPOT/LOCATABLE_SPOT.md) (usually seats).

#### Properties

##### Label
The name of the row as found in the vehicle.
##### NumberingFromFront
Whether the numbering of the rows starts at the front of the vehicle. Default is `true`.

#### Example
```xml
<spotRows>
  <SpotRow version="any" id="1">
    <Label>
      <Text lang="en">Row 1</Text>
    </Label>
    <NumberingFromFront>false</NumberingFromFront>
  </SpotRow>
  <SpotRow version="any" id="2">
    <Label>
      <Text lang="en">Row 2</Text>
    </Label>
    <NumberingFromFront>false</NumberingFromFront>
  </SpotRow>
  ...
</spotRows>
```

### spotColumns

Columns on a deck which can later be referenced by [LocatableSpots](LOCATABLE_SPOT/LOCATABLE_SPOT.md) (usually seats).

#### Properties

##### Label
The name of the column as found in the vehicle.
##### NumberingFromLeft
Whether the numbering of the columns starts from the left or right side of the vehicle when facing forward. Default is `true`.

#### Example
```xml
<spotColumns>
  <SpotColumn version="any" id="1">
    <Label>
      <Text lang="en">Column A</Text>
    </Label>
    <NumberingFromLeft>false</NumberingFromFront>
  </SpotRow>
  <SpotColumn version="any" id="2">
    <Label>
      <Text lang="en">Column B</Text>
    </Label>
    <NumberingFromLeft>false</NumberingFromFront>
  </SpotRow>
  ...
</spotColumns>
```
