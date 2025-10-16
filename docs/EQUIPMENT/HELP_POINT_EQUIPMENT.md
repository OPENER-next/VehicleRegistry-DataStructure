# HelpPointEquipment

An equipment to model driver or staff communication facilities like stop request buttons or phones.

```xml
<HelpPointEquipment version="any" id="321">
  ...
</HelpPointEquipment>
```

**XSD:** [`xsd/netex_part_1/part1_ifopt/netex_ifopt_equipmentPassenger_version.xsd`](https://github.com/NeTEx-CEN/NeTEx/blob/next/xsd/netex_part_1/part1_ifopt/netex_ifopt_equipmentPassenger_version.xsd#L359)

## Location
```
PublicationDelivery/dataObjects/ResourceFrame/equipments
```

## Properties

### HeightFromGround

Height of the phone or stop request button from ground.

#### Example
```xml
<HeightFromGround>1.1</HeightFromGround>
```

### Phone

Whether help point is a phone.

#### Example
```xml
<Phone>true</Phone>
```

### InductionLoop

Whether the phone provides induction loops.

#### Example
```xml
<InductionLoop>true</InductionLoop>
```

### StopRequestButton

Whether there is a button to request a vehicle to stop.

#### Example
```xml
<StopRequestButton>false</StopRequestButton>
```
