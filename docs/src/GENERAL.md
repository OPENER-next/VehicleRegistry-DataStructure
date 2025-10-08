# General

## Properties

### validityConditions

Every element described in this data structure can be assigned zero or multiple `ValidityCondition`s via the `validityConditions` property.

The `validityConditions` shall contain references to `ValidityCondition` elements defined in the [`DeckPlan/configurationConditions`](../DECK_PLAN/DECK_PLAN.md#configurationconditions).
If a `ValidityConditionRef` is provided then the equipment is only active if one of the referenced configurations is active.

#### Example

The example shows an excerpt of a sleeper configuration. Depending on the active configuration either seats or beds are available.

```xml
<PassengerSpace version="any" id="1">
  <deckSpaceCapacities>
    <DeckSpaceCapacity version="any" id="1">
      <validityConditions>
        <ValidityConditionRef ref="day_time_configuration"/>
      </validityConditions>
      <LocatableSpotType>seat</LocatableSpotType>
      <Capacity>8</Capacity>
    </DeckSpaceCapacity>
    <DeckSpaceCapacity version="any" id="2">
      <validityConditions>
        <ValidityConditionRef ref="night_time_configuration"/>
      </validityConditions>
      <LocatableSpotType>bed</LocatableSpotType>
      <Capacity>4</Capacity>
    </DeckSpaceCapacity>
  </deckSpaceCapacities>

  <actualVehicleEquipments>
    <ActualVehicleEquipment version="any" id="1">
      <validityConditions>
        <ValidityConditionRef ref="day_time_configuration"/>
      </validityConditions>
      <Units>8</Units>
      <SeatEquipmentRef version="any" ref="1"/>
    </ActualVehicleEquipment>
    <ActualVehicleEquipment version="any" id="2">
      <validityConditions>
        <ValidityConditionRef ref="night_time_configuration"/>
      </validityConditions>
      <Units>4</Units>
      <BedEquipmentRef version="any" ref="1"/>
    </ActualVehicleEquipment>
  </actualVehicleEquipments>
</PassengerSpace>
```
