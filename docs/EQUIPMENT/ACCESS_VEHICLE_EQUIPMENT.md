# AccessVehicleEquipment

An equipment to describe features related to vehicle access such as steps, entrance and more.

```xml
<AccessVehicleEquipment version="any" id="321">
  ...
</AccessVehicleEquipment>
```
**XSD:** [`xsd/netex_framework/netex_reusableComponents/netex_equipmentVehiclePassenger_version.xsd`](https://github.com/NeTEx-CEN/NeTEx/blob/next/xsd/netex_framework/netex_reusableComponents/netex_equipmentVehiclePassenger_version.xsd#L137)

## Location
```
PublicationDelivery/dataObjects/ResourceFrame/equipments
```

## Properties

### NumberOfSteps

The number of steps passengers have to take when boarding/alighting the vehicle.

#### DELFI

- 3110 ↦ `NumberOfSteps > 0`
- 3112 ↦ `NumberOfSteps`

#### Example

```xml
<NumberOfSteps>3</NumberOfSteps>
```

### StepHeight

The average step height passengers have to take when boarding/alighting the vehicle. (See [NeTEx Proposal](https://github.com/NeTEx-CEN/NeTEx/issues/900))
Only relevant if `NumberOfSteps` is greater than 0.

#### DELFI

- 3111 ↦ `StepHeight`

#### Example

```xml
<StepHeight>0.15</StepHeight>
```

### BoardingHeight

Height of the outer entry point (lowest step), measured from the ground of the road or top of the rail. Together with `FloorHeight` this describes the lowest and highest point of an entrance.

```
───────┬───┐ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ┬
       │   │                     │
       │   └───┐ ─ ─ ┬           │
 Floor │ Step  │     │           │
───────┴───────┤     │           │
               │     │           │ Floor
               │     │ Boarding  │ Height
               │     │ Height    │
               │     │           │
          ┌─┐  │     │           │
──────────│ │──┘     │           │
 Track    └─┘─ ─ ─ ─ ┴ ─ ─ ─ ─ ─ ┴
```

#### DELFI

- 3101 ↦ `BoardingHeight from AccessVehicleEquipment where Kneeling == true`

#### Example

```xml
<BoardingHeight>0.32</BoardingHeight>
```

### FloorHeight

Height of the inner entry point (floor next to the entrance), measured from the ground of the road or top of the rail. Together with `BoardingHeight` this describes the lowest and highest point of an entrance. (See [NeTEx Proposal](https://github.com/NeTEx-CEN/NeTEx/issues/900))

#### DELFI

- 3100 ↦ `FloorHeight from AccessVehicleEquipment where Kneeling == true`

#### Example

```xml
<FloorHeight>0.75</FloorHeight>
```

### Kneeling

Whether `BoardingHeight` and `FloorHeight` values reflect the height when kneeling is active/inactive. (See [NeTEx Proposal](https://github.com/NeTEx-CEN/NeTEx/issues/873))

#### Example

```xml
<Kneeling>true</Kneeling>
```

### EdgeToTrackCenterDistance

Distance from the outer entry point (including any fixed outer steps) to the vehicle center (center point between axles). Can be used to calculate the horizontal gap in conjunction with the `EdgeToTrackCenterDistance` from `Quay`. (See [NeTEx Proposal](https://github.com/NeTEx-CEN/NeTEx/issues/900))

```
                Platform
                Distance
            ├─────────────────┤

            |   Entrance      |
                Distance
            ├──────────────┤  |

            |              |  ┌──────────
┌───────────────────────┬──┐  │ Platform
│           |           ├──┘  │
│                       │     │
│  ┌─┐      |      ┌─┐  │     │
└──│ │─────────────│ │──┘     │
   └─┘    Track    └─┘        └──────────
```

#### DELFI

- 3080 ↦ `Quay.EdgeToTrackCenterDistance - (EdgeToTrackCenterDistance [+ RetractableStepVehicleEquipment/ExternalLength])`
- 3090 ↦ `(EdgeToTrackCenterDistance [+ RetractableStepVehicleEquipment/ExternalLength]) * 2`

#### Example

```xml
<EdgeToTrackCenterDistance>2.4</EdgeToTrackCenterDistance>
```

### WidthOfAccessArea

Clearance width of the vehicle's entrance.

#### DELFI

- 3041 ↦ `WidthOfAccessArea`

#### Example

```xml
<WidthOfAccessArea>1.3</WidthOfAccessArea>
```

### HeightOfAccessArea

Clearance height of the vehicle's entrance.

#### Example

```xml
<HeightOfAccessArea>2</HeightOfAccessArea>
```

### AutomaticDoors

Whether the doors open automatically (e.g. by pushing a button) or have to be opened manually.

#### DELFI

- 3040 ↦ `AutomaticDoors` (semi-automatic missing)

#### Example

```xml
<AutomaticDoors>true</AutomaticDoors>
```
