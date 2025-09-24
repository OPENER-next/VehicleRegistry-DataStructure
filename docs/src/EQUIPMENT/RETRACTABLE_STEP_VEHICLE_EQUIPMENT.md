# RetractableStepVehicleEquipment

A special vehicle equipment for sliding and folding steps which reduce the horizontal and partially vertical gap between vehicle and platform. (See [NeTEx Proposal](https://github.com/NeTEx-CEN/NeTEx/issues/873))

## DELFI

- 3113 ↦ Existence of `RetractableStepVehicleEquipment`

```xml
<RetractableStepVehicleEquipment version="any" id="321">
  ...
</RetractableStepVehicleEquipment>
```

## Location
```
PublicationDelivery/dataObjects/ResourceFrame/equipments
```

## Properties

### BoardingHeight

The height from ground to the lowest retractable step. For a sliding step also know as gap filler which are used to bridge the horizontal gap, this is almost identical to the vehicle boarding height.

#### Example

```xml
<BoardingHeight>0.3</BoardingHeight>
```

### ExternalLength

Length of the retractable step when fully extended and only the part outside the VEHICLE.

#### Example

```xml
<ExternalLength>0.2</ExternalLength>
```

### IsAdjustableLength

Whether the retractable step (e.g. a sliding step) can be adjusted to be used at shorter lengths. Useful if there is not enough space to deploy the sliding step at its full length.

#### Example

```xml
<IsAdjustableLength>true</IsAdjustableLength>
```

### ExternalWidth

Width of the retractable step when fully extended and only the part outside the VEHICLE.

#### Example

```xml
<ExternalWidth>0.2</ExternalWidth>
```

### BearingCapacity

Maximum weight that the retractable step can bear.

#### Example

```xml
<BearingCapacity>350</BearingCapacity>
```

### NumberOfTreads

Number of retractable steps.

#### Example

```xml
<NumberOfTreads>1</NumberOfTreads>
```

### NumberOfSteps

Total number of steps, starting from the lowest step and also including any fixed steps, to access the vehicle. "Steps" is to be understood as rises wherefore it can be 0 for a single sliding step which does not introduce any meaningful vertical height difference as it just bridges the horizontal gap.

#### Example

```xml
<NumberOfSteps>0</NumberOfSteps>
```
