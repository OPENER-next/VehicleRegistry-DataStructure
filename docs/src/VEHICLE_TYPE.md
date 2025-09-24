# VehicleType

NeTEx separates train engines and carriages from other public transport vehicle types. They are modelled via specific `TractiveElementType` and `TrailingElementType` under a different location:

```
PublicationDelivery/dataObjects/ResourceFrame/trainElementTypes/TractiveElementType|TrailingElementType
```

However this distinction is not used in the registry data structure. Instead everything is based on `VehicleType` and further detailed via `TransportMode`. Carriages can be detected by checking the `SelfPropelled` property.

A `VehicleType` builds the foundation of a `VehicleModel`. It contains
relevant properties like the capacity, dimensions, propulsion and the reference to a `DeckPlan`.

## Location
```
PublicationDelivery/dataObjects/ResourceFrame/vehicleTypes
```

## Properties

### EuroClass
Euro emission standard classification (e.g., Euro 6).

#### Example:
```xml
<EuroClass>B</EuroClass>
```

### SelfPropelled
Indicates whether the vehicle has independent propulsion capability.

#### Example:
```xml
<SelfPropelled>true</SelfPropelled>
```

### PropulsionType
Propulsion technology(s) used by the vehicle. Multiple values must be separated by spaces.

#### Values (`PropulsionTypeEnumeration`):
- combustion
- electric
- electricAssist
- hybrid
- human
- other

#### Example:
```xml
<PropulsionType>hybrid</PropulsionType>
```

### FuelType
Energy source(s) used by the vehicle. Multiple values must be separated by spaces.

#### Values (`FuelTypeEnumeration`):
- battery
- biodiesel
- diesel
- dieselBatteryHybrid
- electricContact
- electricity
- ethanol
- hydrogen
- liquidGas
- tpg
- methane
- naturalGas
- petrol
- petrolBatteryHybrid
- petrolLeaded
- petrolUnleaded
- none
- other

#### Example:
```xml
<FuelType>diesel battery</FuelType>
```

### MaximumRange
Maximum operational range in meters on full energy source.
System for units can be specified on frame. Default is metres as defined [here](http://www.ordnancesurvey.co.uk/xml/resource/units.xml).

#### Example:
```xml
<MaximumRange>240</MaximumRange>
```

### MaximumVelocity
Maximum design speed in m/s.
System for units can be specified on frame. Default is metres per second as defined [here](http://www.ordnancesurvey.co.uk/xml/resource/units.xml).

#### Example:
```xml
<MaximumVelocity>100</MaximumVelocity>
```

### TransportMode
Primary transport mode category according to NeTEx classification.

#### Values (`AllModesEnumeration`):
- all
- anyMode
- unknown
- air
- bus
- trolleyBus
- tram
- coach
- rail
- intercityRail
- urbanRail
- metro
- water
- ferry
- cableway
- funicular
- lift
- snowAndIce
- taxi
- selfDrive
- foot
- bicycle
- motorcycle
- scooter
- car
- shuttle

#### Example:
```xml
<TransportMode>bus</TransportMode>
```

### DeckPlanRef

A reference to the DeckPlan of this vehicle depicting the entrances, areas, seats and more.

#### DELFI

- 3010 ↦ Can be generated from the `DeckPlan` if detailed enough.

#### Example:
```xml
<DeckPlanRef ref="id"/>
```

### capacities
Container for passenger/vehicle capacity specifications.

- `PassengerVehicleCapacity`: Capacity for transporting other vehicles.
  - `VehicleCategory`
  - `VehicleCapacity`
- `PassengerCapacity`: Passenger capacity by fare class.
  - `TotalCapacity`: The maximum capacity the vehicle is allowed to carry. This is **not** necessarily equal to the sum of all sub capacities.
  - `SeatingCapacity`
  - `StandingCapacity`
  - `PrioritySeatingCapacity`: See [NeTEx Proposal](https://github.com/NeTEx-CEN/NeTEx/issues/898)
  - `WheelchairPlaceCapacity`
  - `PramPlaceCapacity`
  - `BicycleRackCapacity`: While it is technically possible to depict the bicycle capacity via `PassengerVehicleCapacity`, it should be done here, regardless of whether the space is a rack or not.

#### DELFI

- 3050 ↦ `PrioritySeatingCapacity > 0`

#### Example:
```xml
<capacities>
  <PassengerVehicleCapacity version="any" id="PassengerVehicleCapacity/id/1">
    <VehicleCategory>car</VehicleCategory>
    <VehicleCapacity>4</VehicleCapacity>
  </PassengerVehicleCapacity>

  <PassengerCapacity version="any" id="PassengerCapacity/id/1">
    <FareClass>firstClass</FareClass>
    <SeatingCapacity>8</SeatingCapacity>
  </PassengerCapacity>

  <PassengerCapacity version="any" id="PassengerCapacity/id/2">
    <FareClass>secondClass</FareClass>
    <TotalCapacity>220</TotalCapacity>
    <SeatingCapacity>207</SeatingCapacity>
    <StandingCapacity>275</StandingCapacity>
    <WheelchairPlaceCapacity>2</WheelchairPlaceCapacity>
    <PramPlaceCapacity>3</PramPlaceCapacity>
    <BicycleRackCapacity>33</BicycleRackCapacity>
    <PrioritySeatingCapacity>25</PrioritySeatingCapacity>
  </PassengerCapacity>
</capacities>
```

### Length
Total length of the vehicle, including the bumpers of a coach. For vehicles see [ISO 612:1978](https://cdn.standards.iteh.ai/samples/4729/98970c4607e74d369a7d7781d6c0111f/ISO-612-1978.pdf).
System for units can be specified on frame. Default is metres as defined [here](http://www.ordnancesurvey.co.uk/xml/resource/units.xml).

#### Example:

```xml
<Length>20.05</Length>
```

### Width
Total width of the vehicle (excluding the vehicle's rear mirrors). For vehicles see [ISO 612:1978](https://cdn.standards.iteh.ai/samples/4729/98970c4607e74d369a7d7781d6c0111f/ISO-612-1978.pdf).
System for units can be specified on frame. Default is metres as defined [here](http://www.ordnancesurvey.co.uk/xml/resource/units.xml).
**Note:** This is not *DELFI 3090* see `EdgeToTrackCenterDistance` instead.

#### Example:

```xml
<Width>2.926</Width>
```

### Height
Total height of the vehicle, excluding any none fixed parts like pantographs. For vehicles see [ISO 612:1978](https://cdn.standards.iteh.ai/samples/4729/98970c4607e74d369a7d7781d6c0111f/ISO-612-1978.pdf).
System for units can be specified on frame. Default is metres as defined [here](http://www.ordnancesurvey.co.uk/xml/resource/units.xml).

#### Example:

```xml
<Height>4.26</Height>
```

### Weight
TBD. System for units can be specified on frame. Default is kilos as defined [here](http://www.ordnancesurvey.co.uk/xml/resource/units.xml).

```xml
<Weight>56</Weight>
```

### facilities

This allows the specification of features available on a vehicle, like does the vehicle have air conditioning or is there an onboard bistro.

The `ServiceFacilitySet` shall be defined directly under `facilities` like so:

```xml
<VehicleType>
  <facilities>
    <ServiceFacilitySet>
      ...
    </ServiceFacilitySet>
  </facilities>
</VehicleType>
```
