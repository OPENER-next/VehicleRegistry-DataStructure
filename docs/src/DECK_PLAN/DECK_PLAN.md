# DeckPlan

The main element for modeling deck plans. This contains seat maps, paths and points of interest.
A `DeckPlan` is composed of multiple `Deck` elements that contain the actual elements.

```xml
<DeckPlan version="any" id="321">
  ...
</DeckPlan>
```

**XSD:** [`xsd/netex_framework/netex_reusableComponents/netex_deckPlan_version.xsd`](https://github.com/NeTEx-CEN/NeTEx/blob/next/xsd/netex_framework/netex_reusableComponents/netex_deckPlan_version.xsd#L101)

## Location
```
PublicationDelivery/dataObjects/ResourceFrame/deckPlans
```

## Properties

### configurationConditions

Conditions used to group different deck plan elements to a single configuration which can be used to activate/deactivate these elements. Useful if a vehicle has different configurations like a carriage that can be configured as a sleeping car.

This technically allows multiple different `Condition` elements allowing for complex condition matching with timing, comparison operators and more. However for this data structure we only use the `ValidityCondition` which is only the definition of a possible configuration, without saying anything about when this configuration applies (the vehicle registry has no knowledge about this).

#### Properties
- `Name` - A name to identify the validity condition.
- `Description` - Description or other comment describing further details about the configuration.

#### Example
```xml
<configurationConditions>
  <ValidityCondition version="any" id="1">
    <Name>Sleeper configuration</Name>
    <Description>Changes seats to beds.</Description>
  </ValidityCondition>
  <ValidityCondition version="any" id="2">
    ...
  </ValidityCondition>
  ...
</configurationConditions>
```

### deckLevels

The [DeckLevels](DECK_LEVEL.md) of this deck plan.

#### Example
```xml
<deckLevels>
  <DeckLevel>
    ...
  </DeckLevel>
  ...
</deckLevels>
```

### decks

The [Decks](DECK.md) contained in this deck plan.

#### Example
```xml
<decks>
  <Deck>
    ...
  </Deck>
  ...
</decks>
```
