# RampVehicleEquipment

A special equipment to model ramps used to bridge the horizontal and vertical gap between vehicle and platform. (See [NeTEx Proposal](https://github.com/NeTEx-CEN/NeTEx/issues/873))

```xml
<RampVehicleEquipment version="any" id="321">
  ...
</RampVehicleEquipment>
```

## Location
```
PublicationDelivery/dataObjects/ResourceFrame/equipments
```

## DELFI

- 3120 ↦ Existence of `RampVehicleEquipment`

## Properties

### Fixed

Whether the ramp is integrated into the vehicle or portable.

#### Example

```xml
<Fixed>true</Fixed>
```

### IsAutomatic

Whether the ramp operates automatically, meaning the entire operation from start to finish requires no manual handling (except of pressing e.g. a button).

#### Example

```xml
<IsAutomatic>true</IsAutomatic>
```

### AssistanceRequired

Whether the usage or operation of the ramp requires assistance, meaning the passenger either physically or legally cannot board/alight independently.

#### Example

```xml
<AssistanceRequired>false</AssistanceRequired>
```

### InOperationDuration

The time it takes to retract the ramp. For none automatic equipment an estimated or average usage time can be provided.

#### Example

```xml
<InOperationDuration>PT8S</InOperationDuration>
```

### OutOperationDuration

The time it takes to deploy the ramp. For none automatic equipment an estimated or average usage time can be provided.

#### Example

```xml
<OutOperationDuration>PT8S</OutOperationDuration>
```

### ExternalLength

Length of the ramp when fully extended and only the part outside the vehicle. Length is measured perpendicular to the vehicle's forward orientation. This is undefined if the ramp is portable.

#### DELFI

- 3125 ↦ `ExternalLength - Quay.Width`

#### Example

```xml
<ExternalLength>0.6</ExternalLength>
```

### ExternalWidth

Width of the ramp when fully extended and only the part outside the vehicle. Width is measured parallel to the vehicle's forward orientation.

#### DELFI

- 3122 ↦ `ExternalWidth`
- 3126 ↦ `ExternalWidth - Quay.Length`

#### Example

```xml
<ExternalWidth>1</ExternalWidth>
```

### BearingCapacity

Maximum weight that the ramp can bear.

#### DELFI

- 3123 ↦ `BearingCapacity`

#### Example

```xml
<BearingCapacity>350</BearingCapacity>
```

### Length

Length of the ramp when fully extended. Length is measured perpendicular to the vehicle's forward orientation.

#### DELFI

- 3121 ↦ `Length`
- 3127 ↦ `100 / (Length / (FloorHeight - (Quay.PlatformHeight))`

#### Example

```xml
<Length>350</Length>
```
