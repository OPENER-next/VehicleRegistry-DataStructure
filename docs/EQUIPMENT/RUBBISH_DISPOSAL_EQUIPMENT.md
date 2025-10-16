# RubbishDisposalEquipment

An equipment to describe any form of rubbish disposal like wastebins.

```xml
<RubbishDisposalEquipment version="any" id="321">
  ...
</RubbishDisposalEquipment>
```

**XSD:** [`xsd/netex_part_1/part1_ifopt/netex_ifopt_equipmentPassenger_version.xsd`](https://github.com/NeTEx-CEN/NeTEx/blob/next/xsd/netex_part_1/part1_ifopt/netex_ifopt_equipmentPassenger_version.xsd#L517)

## Location
```
PublicationDelivery/dataObjects/ResourceFrame/equipments
```

## Properties

### SharpsDisposal

Whether there is a dedicated disposal for sharps and syringes. Sharps are classified as biohazardous waste and therefore require special disposal.

#### Example
```xml
<SharpsDisposal>false</SharpsDisposal>
```

### Recycling

Whether there is separation for recycling.

#### Example
```xml
<Recycling>false</Recycling>
```
