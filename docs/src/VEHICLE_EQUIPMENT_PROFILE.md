# VehicleEquipmentProfile

Each `VehicleModel` will get one `VehicleEquipmentProfile` profile which defines the equipments available on the vehicle including their respective count.

## Location

```
PublicationDelivery/dataObjects/ResourceFrame/vehicleEquipmentProfiles
```

## Properties

### vehicleEquipmentProfileMembers
Contains multiple `VehicleEquipmentProfileMember` which must reference an equipment and describe the amount available in the vehicle via `MinimumUnits`.

#### Example:

```xml
<vehicleEquipmentProfileMembers>
  <VehicleEquipmentProfileMember version="any" id="a">
    <SeatEquipmentRef ref="1"/>
    <MinimumUnits>30</MinimumUnits>
  </VehicleEquipmentProfileMember>
  <VehicleEquipmentProfileMember version="any" id="b">
    <AccessVehicleEquipmentRef ref="2"/>
    <MinimumUnits>2</MinimumUnits>
  </VehicleEquipmentProfileMember>
</vehicleEquipmentProfileMembers>
```
