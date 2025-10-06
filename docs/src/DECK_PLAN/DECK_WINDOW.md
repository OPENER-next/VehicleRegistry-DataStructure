# DeckWindow

A window adjoining a [DeckSpace](DECK_SPACE/DECK_SPACE.md).

```xml
<DeckWindow version="any" id="321">
  ...
</DeckWindow>
```

**XSD:** [`xsd/netex_framework/netex_reusableComponents/netex_deckPlan_version.xsd`](https://github.com/NeTEx-CEN/NeTEx/blob/next/xsd/netex_framework/netex_reusableComponents/netex_deckPlan_version.xsd#L1157)

## Location

```
PublicationDelivery/dataObjects/ResourceFrame/deckPlans/DeckPlan/decks/Deck/deckSpaces/DeckSpace/deckWindows
```

## Properties

### Name

A name to identify the window.

#### Example
```xml
<Name>Window Row 3-4</Name>
```

### Description

A description providing additional information about the window.

#### Example
```xml
<Description>Interior window to compartment 4.</Description>
```

### Orientation

Orientation of the window relative to the vehicle front. Default is `forwards`.
**Note:** The orientation is **not** linked to the driving direction, instead vehicles and even carriages have a front and back which defines their directionality.

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

The inner width of the window in meters.

#### Example
```xml
<Width>3</Width>
```

### Height

The inner height of the window in meters.

#### Example
```xml
<Height>2</Height>
```

### DeckLevelRef

Reference to the [`DeckLevel`](DECK_LEVEL.md) this window belongs to.

#### Example
```xml
<DeckLevelRef ref="level:2"/>
```

### DistanceFromFront

The distance of the windows's forward edge from the front of the vehicle in meters.

#### Example
```xml
<DistanceFromFront>15.3</DistanceFromFront>
```

### HeightFromFloor

The height of the window from the floor in meters.

#### Example
```xml
<HeightFromFloor>0.45</HeightFromFloor>
```

### VehicleSide

The location of the window relative to forward orientation of the vehicle (see [Orientation](#orientation)).

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

### DeckWindowType

The classification of the window.

#### Values (`DeckWindowTypeEnumeration`):
- interspaced
- continuous
- panorama
- porthole
- other

#### Example
```xml
<DeckWindowType>interspaced<DeckWindowType/>
```

### HasBlind

Whether the window has a blind.

#### Example
```xml
<HasBlind>True<HasBlind/>
```

### CanBeOpened

Whether the window can be opened.

#### Example
```xml
<CanBeOpened>False<CanBeOpened/>
```