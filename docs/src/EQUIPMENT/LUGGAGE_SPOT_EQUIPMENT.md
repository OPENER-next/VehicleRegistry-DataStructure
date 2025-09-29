# LuggageSpotEquipment

An equipment to describe a luggage storage like a locker, rack or bay.

```xml
<LuggageSpotEquipment version="any" id="321">
  ...
</LuggageSpotEquipment>
```

**XSD:** [`xsd/netex_framework/netex_reusableComponents/netex_spotEquipment_version.xsd`](https://github.com/NeTEx-CEN/NeTEx/blob/next/xsd/netex_framework/netex_reusableComponents/netex_spotEquipment_version.xsd#L327)

## Location
```
PublicationDelivery/dataObjects/ResourceFrame/equipments
```

## Properties

### HeightFromFloor

Height of the luggage storage above floor.

#### Example
```xml
<HeightFromFloor>0.45</HeightFromFloor>
```

### HasPowerSupply

Whether the luggage storage has a power supply socket.

#### Example
```xml
<HasPowerSupply>true</HasPowerSupply>
```

### HasUsbPowerSocket

Whether the luggage storage has an USB power supply socket.

#### Example
```xml
<HasUsbPowerSocket>true</HasUsbPowerSocket>
```

### LuggageSpotType

The specific type of luggage storage.

#### Values (`LuggageSpotTypeEnumeration`)
- rackAboveSeats
- spaceUnderSeat
- luggageBay
- luggageCompartment
- luggageVan
- cycleRack
- other

#### Example
```xml
<LuggageSpotType>luggageCompartment</LuggageSpotType>
```

### HeadroomForLuggage

The height available for the luggage.

#### Example
```xml
<HeadroomForLuggage>0.35</HeadroomForLuggage>
```

### IsLockable

Whether the luggage storage can be locked.

#### Example
```xml
<IsLockable>true</IsLockable>
```

### HasDoor

Whether the luggage storage has a door.

#### Example
```xml
<HasDoor>true</HasDoor>
```
