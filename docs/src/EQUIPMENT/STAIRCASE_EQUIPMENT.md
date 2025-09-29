# StaircaseEquipment

An equipment to describe properties of a stair case. A staircase can contain multiple flights.

```xml
<StaircaseEquipment version="any" id="321">
  ...
</StaircaseEquipment>
```

**XSD:** [`xsd/netex_part_1/part1_ifopt/netex_ifopt_equipmentAccess_version.xsd`](https://github.com/NeTEx-CEN/NeTEx/blob/next/xsd/netex_part_1/part1_ifopt/netex_ifopt_equipmentAccess_version.xsd#L520)

## Location
```
PublicationDelivery/dataObjects/ResourceFrame/equipments
```

## Properties

### DirectionOfUse

Direction in which the stairs can be used. Default is `both`.

#### Values (`DirectionOfUseEnumeration`):
- up
- down
- both

#### Example
```xml
<DirectionOfUse>both</DirectionOfUse>
```

### NumberOfSteps

The total number of steps.

#### Example
```xml
<NumberOfSteps>0.45</NumberOfSteps>
```

### StepHeight

Height of an individual step in meters.

#### Example
```xml
<StepHeight>0.2</StepHeight>
```

### StepLength

The depth of an individual step in metres.

#### Example
```xml
<StepLength>0.35</StepLength>
```

### StepColourContrast

Whether there is a colour contrast on the step nosings.

#### Example
```xml
<StepColourContrast>0.45</StepColourContrast>
```

### HandrailType

Whether handrails are available.

#### Values (`HandrailEnumeration`):
- none
- oneSide
- bothSides

#### Example
```xml
<HandrailType>oneSide</HandrailType>
```

### HandrailHeight

Height of the (upper) handrail measured from the steps.

#### Example
```xml
<HandrailHeight>0.6</HandrailHeight>
```
### LowerHandrailHeight

Height of any additional lower handrail measured from steps.

#### Example
```xml
<LowerHandrailHeight>0.45</LowerHandrailHeight>
```

### TactileWriting

Whether signage that can be read tactilely (e.g. in Braille) is available on the handrail.

#### Example
```xml
<TactileWriting>0.45</TactileWriting>
```

### StairRamp

Indicates the presence and type of a ramp included within the staircase.

#### Values (`StairRampEnumeration`):
- none
- bicycle
- luggage
- stroller
- other
- unknown

#### Example
```xml
<StairRamp>luggage</StairRamp>
```

### TopEnd

Details about the top of the stairs.

#### Properties

##### ContinuingHandrail
Whether there is a handrail that continues from previous section.

##### TexturedSurface
Whether there is a textured ground surface. Useful for blind or visually impaired people to safely detect the stairs.

##### VisualContrast
Whether there is a colour contrast. Useful for visually impaired people to safely detect the stairs.

#### Example
```xml
<TopEnd>
  <ContinuingHandrail>false</ContinuingHandrail>
  <TexturedSurface>true</TexturedSurface>
  <VisualContrast>false</VisualContrast>
</TopEnd>
```

### BottomEnd

Details about the bottom of the stairs.

#### Properties
##### ContinuingHandrail
Whether there is a handrail that continues from previous section.

##### TexturedSurface
Whether there is a textured ground surface. Useful for blind or visually impaired people to safely detect the stairs.

##### VisualContrast
Whether there is a colour contrast. Useful for visually impaired people to safely detect the stairs.

#### Example
```xml
<BottomEnd>
  <ContinuingHandrail>false</ContinuingHandrail>
  <TexturedSurface>true</TexturedSurface>
  <VisualContrast>false</VisualContrast>
</BottomEnd>
```

### ContinuousHandrail

Whether the handrail is continuous across the staircase.

#### Example
```xml
<ContinuousHandrail>false</ContinuousHandrail>
```

### WithoutRiser

Whether it is an openwork staircase (no riser).

#### Example
```xml
<WithoutRiser>false</WithoutRiser>
```

### SpiralStair

Whether it is a spiral staircase.

#### Example
```xml
<SpiralStair>true</SpiralStair>
```

### NumberOfFlights

Number of flights of stairs.

#### Example
```xml
<NumberOfFlights>2</NumberOfFlights>
```





