# BedEquipment

An equipment to describe a bed. This is mostly relevant for night trains with sleeping cars.

```xml
<BedEquipment version="any" id="321">
  ...
</BedEquipment>
```

## Location
```
PublicationDelivery/dataObjects/ResourceFrame/equipments
```

## Properties

### HeightFromFloor

Height of the bed above floor.

#### Example
```xml
<HeightFromFloor>0.45</HeightFromFloor>
```

### HasPowerSupply

Whether the bed has a power supply socket.

#### Example
```xml
<HasPowerSupply>true</HasPowerSupply>
```

### HasUsbPowerSocket

Whether the bed has an USB power supply socket.

#### Example
```xml
<HasUsbPowerSocket>true</HasUsbPowerSocket>
```
### BedType

The specific type of bed.

#### Values (`BedTypeEnumeration`)
- singleBed
- doubleBed
- bedForChild
- cot
- bottomBunk
- middleBunk
- topBunk
- hammock
- other

#### Example
```xml
<BedType>singleBed</BedType>
```

### IsStowable

Whether the bed can be stowed away when not in use.

#### Example
```xml
<IsStowable>true</IsStowable>
```

### Headroom

The height available above the bed.

#### Example
```xml
<Headroom>0.8</Headroom>
```

### BedLength

The length of the bed.

#### Example
```xml
<BedLength>1.8</BedLength>
```
