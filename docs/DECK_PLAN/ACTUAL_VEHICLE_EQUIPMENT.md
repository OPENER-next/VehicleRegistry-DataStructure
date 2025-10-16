# ActualVehicleEquipment

The instantiation of an [equipment definition](../EQUIPMENT/EQUIPMENT.md) available at a specific place (usually in a [DeckPlan](DECK_PLAN.md)).

```xml
<ActualVehicleEquipment>
  ...
</ActualVehicleEquipment>
```

**XSD:** [`xsd/netex_framework/netex_reusableComponents/netex_equipmentVehiclePassenger_version.xsd`](https://github.com/NeTEx-CEN/NeTEx/blob/next/xsd/netex_framework/netex_reusableComponents/netex_equipmentVehiclePassenger_version.xsd#L103)

## Properties

### Fixed

Whether the referenced equipment is fixed inside the vehicle.

#### Example
```xml
<Fixed>True</Fixed>
```

### Units

The number of available units of the referenced equipment.

#### Example
```xml
<Units>4</Units>
```

### EquipmentRef

Reference to the equipment that is available.

#### Example
```xml
<EquipmentRef ref="SeatEquipment:87"/>
```

### AccessibilityAssessment

Specific [AccessibilityAssessment](ACCESSIBILITY_ASSESSMENT.md) of the referenced equipment.

#### Example
```xml
<AccessibilityAssessment version="any" id="1">
  <suitabilities>
    <Suitability>
      <MobilityNeed>assistedWheelchair</MobilityNeed>
      <Suitable>suitable</Suitable>
    </Suitability>
  </suitabilities>
</AccessibilityAssessment>
```
