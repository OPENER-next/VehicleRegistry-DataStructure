
# DeckVehicleEntrance

A [`DeckEntrance`](DECK_ENTRANCE.md) defining an entrance to or within a [`Deck`](../DECK.md) for vehicles.

```xml
<DeckVehicleEntrance version="any" id="321">
  ...
</DeckVehicleEntrance>
```

**XSD:** [`xsd/netex_framework/netex_reusableComponents/netex_deckPlan_version.xsd`](https://github.com/NeTEx-CEN/NeTEx/blob/next/xsd/netex_framework/netex_reusableComponents/netex_deckPlan_version.xsd#L848)

## Location

```
PublicationDelivery/dataObjects/ResourceFrame/deckPlans/DeckPlan/decks/Deck/deckSpaces/DeckSpace/deckEntrances
```

## Properties

### VehicleCategories

Vehicle categories that may use this entrance.

#### Values (`AllRoadVehicleCategoriesListOfEnumerations`):
- scooter
- eScooter
- cycle
- pedalCycle
- eCycle
- cargoCycle
- tricycle
- tandem
- moped
- motorcycle
- quadbike
- car
- microCar
- miniCar
- smallCar
- mediumCar
- largeCar
- minivan
- transporter
- van
- snowmobile
- moped
- motorcycle
- motorcycleWithSidecar
- motorScooter
- twoWheeledVehicle
- threeWheeledVehicle
- car
- microCar
- miniCar
- smallCar
- mediumCar
- passengerCar
- largeCar
- fourWheelDrive
- taxi
- camperCar
- caravan
- carWithTrailer
- carWithCaravan
- minibus
- minivan
- snowmobile
- undefined
- other
- allPassengerVehicles
- all
- bus
- van
- transporter
- largeVan
- highSidedVehicle
- lightGoodsVehicle
- heavyGoodsVehicle
- agriculturalVehicle
- tanker
- truck
- articulatedVehicle
- largeTrailer
- vehicleWithTrailer
- lightGoodsVehicleWithTrailer
- heavyGoodsVehicleWithTrailer

#### Example

```xml
<VehicleCategories>car van</VehicleCategories>
```
