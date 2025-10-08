# DeckLevel

An identified level (1, 2 , 3, etc.) within the [DeckPlan](DECK_PLAN.md) of a vehicle (boat, train, airplane, etc.).

```xml
<DeckLevel version="any" id="321">
  ...
</DeckLevel>
```

**XSD:** [`xsd/netex_framework/netex_reusableComponents/netex_deckPlan_version.xsd`](https://github.com/NeTEx-CEN/NeTEx/blob/next/xsd/netex_framework/netex_reusableComponents/netex_deckPlan_version.xsd#L1268)

## Location

```
PublicationDelivery/dataObjects/ResourceFrame/deckPlans/DeckPlan/deckLevels
```

## Properties

### Label

The name of the level as found in the vehicle, e.g. GF (ground floor) or B1 (first basement level).

#### Example
```xml
<Label>
  <Text lang="en">GF</Text>
</Label>
```

### Name

A name to identify the level, e.g. 0, 1, 2, 3, etc.

#### Example
```xml
<Name>
  <Text lang="en">0</Text>
</Name>
```

### Description

A description providing additional information about the level.

#### Example
```xml
<Description>
  <Text lang="en">Parking deck level.</Text>
</Description>
```

### PublicUse

Whether the deck level can be used by public. Useful to denote an entire level as inaccessible to the public.

#### Example
```xml
<PublicUse>True</PublicUse>
```
