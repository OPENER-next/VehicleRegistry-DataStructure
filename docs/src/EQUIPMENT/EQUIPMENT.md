# Equipment

An equipment allows adding additional details by assigning it to a `VehicleModel` or a `DeckPlan` element such as a `PassengerSpot` or `PassengerEntrance`. All equipments are defined in a single place and must be referenced via their specific `EquipmentRef` element.

The properties below are general properties that any equipment provides.

**XSD:** [`xsd/netex_framework/netex_reusableComponents/netex_equipment_version.xsd`](https://github.com/NeTEx-CEN/NeTEx/blob/next/xsd/netex_framework/netex_reusableComponents/netex_equipment_version.xsd#L103)

## Location
```
PublicationDelivery/dataObjects/ResourceFrame/equipments
```

## Properties

### Name

A name to identify the equipment.

#### Example

```xml
<Name>Lift - PALFINGER CL300</Name>
```

### Description

Description or other comment targeted at the passenger.

#### Example

```xml
<Description>The lift is operated by the driver. Notify the driver by pushing the green button.</Description>
```

### Note

Description or other comment targeted at internal people like the operator of the equipment.

#### Example

```xml
<Note>The lift must be unlocked via the special toolkit, ...</Note>
```

### Image

URI pointing to an image of the equipment.

#### Example

```xml
<Image>URI</Image>
```
