# LuggageSpot

A [LocatableSpot](LOCATABLE_SPOT.md) defining a specified space to stow a passenger's luggage onboard like a luggage rack or luggage bay.

```xml
<LuggageSpot version="any" id="321">
  ...
</LuggageSpot>
```

**XSD:** [`xsd/netex_framework/netex_reusableComponents/netex_seatingPlan_version.xsd`](https://github.com/NeTEx-CEN/NeTEx/blob/next/xsd/netex_framework/netex_reusableComponents/netex_seatingPlan_version.xsd#L585)

## Location

```
PublicationDelivery/dataObjects/ResourceFrame/deckPlans/DeckPlan/decks/Deck/deckSpaces/PassengerSpace/luggageSpots
```

## Properties

`HeightFromFloor` is superseded by the equivalent property from the [LuggageSpotEquipment](../../EQUIPMENT/LUGGAGE_SPOT_EQUIPMENT.md#heightfromfloor).

### IsAccessibleOnVoyage

Whether the luggage spot can be accessed during the journey. Default is `true`.

An Example could be the luggage compartment of a coach which is below the passenger seats wherefore it can only be accessed from the outside.

#### Example
```xml
<IsAccessibleOnVoyage>False</IsAccessibleOnVoyage>
```
