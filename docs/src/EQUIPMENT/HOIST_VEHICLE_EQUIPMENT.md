# Equipment

## Location

```
PublicationDelivery/dataObjects/ResourceFrame/equipments
```

## HoistVehicleEquipment

A special equipment to model hoists and lifts used to bridge the vertical and partially horizontal gap between vehicle and platform. (See [NeTEx Proposal](https://github.com/NeTEx-CEN/NeTEx/issues/873))

#### DELFI

- 3130 ↦ Existence of `HoistVehicleEquipment`

```xml
<HoistVehicleEquipment version="any" id="321">
  ...
</HoistVehicleEquipment>
```

### IsAutomatic

Whether the lift operates automatically, meaning the entire operation from start to finish requires no manual handling (except of pressing e.g. a button).

#### Example

```xml
<IsAutomatic>true</IsAutomatic>
```

### AssistanceRequired

Whether the usage or operation of the lift requires assistance, meaning the passenger either physically or legally cannot board/alight independently.

#### Example

```xml
<AssistanceRequired>false</AssistanceRequired>
```

### InOperationDuration

The time it takes to retract the lift. For none automatic equipment an estimated or average usage time can be provided.

#### Example

```xml
<InOperationDuration>PT8S</InOperationDuration>
```

### OutOperationDuration

The time it takes to deploy the lift. For none automatic equipment an estimated or average usage time can be provided.

#### Example

```xml
<OutOperationDuration>PT8S</OutOperationDuration>
```

### ExternalLength

Length of the lift when fully extended and only the part outside the vehicle. Length is measured perpendicular to the vehicle's forward orientation.

#### DELFI

- 3131 ↦ `ExternalLength - Quay.Width`

#### Example

```xml
<ExternalLength>0.6</ExternalLength>
```

### ExternalWidth

Width of the lift when fully extended and only the part outside the vehicle. Width is measured parallel to the vehicle's forward orientation.

#### DELFI

- 3132 ↦ `ExternalWidth - Quay.Length`

#### Example

```xml
<ExternalWidth>1</ExternalWidth>
```

### BearingCapacity

Maximum weight that the lift can bear.

#### DELFI

- 3133 ↦ `BearingCapacity`

#### Example

```xml
<BearingCapacity>350</BearingCapacity>
```

### InnerLength

The usable length of the lifting platform. Can be used to determine if a wheelchair fits on the lift.

#### Example

```xml
<InnerLength>1.3</InnerLength>
```

### InnerWidth

The usable width of the lifting platform. Can be used to determine if a wheelchair fits on the lift.

#### Example

```xml
<InnerWidth>1</InnerWidth>
```

### LiftingHeight

The maximum height difference the lift can overcome. In other words the distance between the vehicle floor height and the lowest point the lift can reach.

#### Example

```xml
<LiftingHeight>1.2</LiftingHeight>
```
