# Equipment

## Location

```
PublicationDelivery/dataObjects/ResourceFrame/equipments
```

## General properties

Properties that can be added to any equipment.

### Name

A name to identify the equipment.

#### Example

```xml
<Name>Lift - PALFINGER CL300</Name>
```

### Description

Description or other comment targeted at the passenger.

#### Example

```xml
<Description>The lift is operated by the driver. Notify the driver by pushing the green button.</Description>
```

### Note

Description or other comment targeted at internal people like the operator of the equipment.

#### Example

```xml
<Note>The lift must be unlocked via the special toolkit, ...</Note>
```

### Image

URI pointing to an image of the equipment.

#### Example

```xml
<Image>URI</Image>
```

## PassengerInformationEquipment

An equipment to describe features related to passenger information.

```xml
<PassengerInformationEquipment version="any" id="321">
  ...
</PassengerInformationEquipment>
```

### PassengerInformationEquipmentList
The exact passenger information equipment(s) available.

#### Values (`PassengerInformationEquipmentEnumeration`):
- timetablePoster
- fareInformation
- lineNetworkPlan
- lineTimetable
- stopTimetable
- journeyPlanning
- interactiveKiosk
- informationDesk
- networkStatus
- realTimeDisruptions
- realTimeDepartures
- stationMap
- acousticStationMap
- tactileStationMap
- other

#### Example
```xml
<PassengerInformationEquipmentList>nextStopIndicator stopAnnouncements</PassengerInformationEquipmentList>
```

### InductionLoops

Whether the equipment provides induction loops.

#### Example
```xml
<InductionLoops>false</InductionLoops>
```

### TactileInterfaceAvailable

Whether the equipment provides a tactile interface.

#### Example
```xml
<TactileInterfaceAvailable>false</TactileInterfaceAvailable>
```

### AudioInterfaceAvailable

Whether the equipment provides an audio interface.

#### Example
```xml
<AudioInterfaceAvailable>true</AudioInterfaceAvailable>
```

### WheelchairSuitable

Whether the equipment can be used while seated in a wheelchair.

#### Example
```xml
<WheelchairSuitable>true</WheelchairSuitable>
```

### PassengerInformationFacilityList

The facilities this equipment provides.

#### Values (`PassengerInformationFacilityEnumeration`):
-  nextStopIndicator
-  stopAnnouncements
-  passengerInformationDisplay
-  realTimeConnections
-  other

#### DELFI

- 3020 ↦ `nextStopIndicator`
- 3021 ↦ `destinationDisplay` (See [NeTEx Proposal](https://github.com/NeTEx-CEN/NeTEx/issues/882))
- 3030 ↦ `stopAnnouncements`
- 3031 ↦ `routeAnnouncements` (See [NeTEx Proposal](https://github.com/NeTEx-CEN/NeTEx/issues/882))

#### Example
```xml
<PassengerInformationFacilityList>nextStopIndicator stopAnnouncements</PassengerInformationFacilityList>
```

## SanitaryEquipment

An equipment to describe features related to sanitary such as toilets.

```xml
<SanitaryEquipment version="any" id="321">
  ...
</SanitaryEquipment>
```

### Gender

Specifies if this sanitary facility is limited to a specific gender.

#### Values (`GenderLimitationEnumeration`):
- both
- femaleOnly
- maleOnly
- sameSexOnly

#### Example
```xml
<Gender>both</Gender>
```

### SanitaryFacilityList

The facilities this equipment provides.

#### Values (`SanitaryFacilityEnumeration`):
- none
- toilet
- washbasin
- wheelchairAccessToilet
- shower
- washingAndChangeFacilities
- babyChange
- wheelchairBabyChange
- shoeShiner
- other

#### DELFI

- 3060 ↦ `toilet`
- 3061 ↦ `wheelchairAccessToilet`

#### Example

```xml
<SanitaryFacilityList>toilet wheelchairAccessToilet</SanitaryFacilityList>
```

### NumberOfToilets

The number of toilets available in this sanitary facility.

#### Example
```xml
<NumberOfToilets>1</NumberOfToilets>
```

### FreeToUse

Whether the sanitary facility can be used without a fee.

#### Example
```xml
<FreeToUse>true</FreeToUse>
```

### Charge

The fee one must pay for using the sanitary facility. The currency can be specified via the `Currency` property otherwise it uses the frame's default value.

Defaults can be set on any frame like `ResourceFrame` via
```xml
<FrameDefaults>
  <DefaultCurrency>EUR</DefaultCurrency>
</FrameDefaults>
```

#### Example
```xml
<Charge>0.5</Charge>
```

### Currency

Type of currency. Based on ISO 4217 values e.g. EUR or USD.

#### Example
```xml
<Currency>EUR</Currency>
```

### PaymentMethods

The accepted payment methods to pay the fee.

#### Values (`PaymentMethodEnumeration`)
- cash
- cashExactChangeOnly
- cashAndCard
- coin
- banknote
- cheque
- travellersCheque
- postalOrder
- companyCheque
- creditCard
- debitCard
- cardsOnly
- travelCard
- contactlessPaymentCard
- contactlessTravelCard
- directDebit
- bankTransfer
- epayDevice
- epayAccount
- sms
- mobilePhone
- mobileApp
- voucher
- token
- warrant
- mileagePoints
- other

#### Example
```xml
<PaymentMethods>cash debitCard</PaymentMethods>
```

### ChangeAvailable

Whether change is available.

#### Example
```xml
<ChangeAvailable>false</ChangeAvailable>
```

### WheelchairTurningCircle

Turning circle radius for a wheelchair.

#### Example
```xml
<WheelchairTurningCircle>0.9</WheelchairTurningCircle>
```
### SupportBarHeight

The height of the support bar if one exists.

#### Example
```xml
<SupportBarHeight>0.5</SupportBarHeight>
```

### CallButtonAvailable

Whether there is an assistance or emergency call button.

#### Example
```xml
<CallButtonAvailable>true</CallButtonAvailable>
```

### SharpsDisposal

Whether there is a dedicated disposal for sharps and syringes. Sharps are classified as biohazardous waste and therefore require a special disposal.

#### Example
```xml
<SharpsDisposal>false</SharpsDisposal>
```

### HandWashing

Whether there is a sink allowing hand washing with soap.

#### Example
```xml
<HandWashing>true</HandWashing>
```
### DrinkingWater

Whether the tap inside the sanitary facility supplies drinking water.

#### Example
```xml
<DrinkingWater>false</DrinkingWater>
```

### ToiletsType

The toilet types available at this sanitary facility.

#### Values (`ToiletsTypeEnumeration`)
- seated
- urinal
- squat
- seatedAndUrinal

#### Example
```xml
<ToiletsType>seated</ToiletsType>
```

## TicketingEquipment

An equipment to describe features related to ticketing, like ticket machines or ticket counters.

```xml
<TicketingEquipment version="any" id="321">
  ...
</TicketingEquipment>
```

### TicketMachines

Whether ticket machines are available.

#### DELFI

- 3070 ↦ `TicketMachines = true/false`

#### Example
```xml
<TicketMachines>true</TicketMachines>
```

### NumberOfMachines

#### Example
```xml
<NumberOfMachines>2</NumberOfMachines>
```

### HeightOfMachineInterface

Height of the ticket machine interface.

#### Example
```xml
<HeightOfMachineInterface>0.8</HeightOfMachineInterface>
```

### TicketCounter

Whether there is a ticket counter. Mostly relevant for ferries.

#### Example
```xml
<TicketCounter>false</TicketCounter>
```

### PaymentMethods

The accepted payment methods when buying a ticket.

#### Values (`PaymentMethodEnumeration`)
- cash
- cashExactChangeOnly
- cashAndCard
- coin
- banknote
- cheque
- travellersCheque
- postalOrder
- companyCheque
- creditCard
- debitCard
- cardsOnly
- travelCard
- contactlessPaymentCard
- contactlessTravelCard
- directDebit
- bankTransfer
- epayDevice
- epayAccount
- sms
- mobilePhone
- mobileApp
- voucher
- token
- warrant
- mileagePoints
- other

#### Example
```xml
<PaymentMethods>cash debitCard</PaymentMethods>
```

### TicketTypesAvailable

#### Values (`TicketTypeEnumeration`)
- standard
- promotion
- concession
- group
- season
- carnet
- travelCard
- other
- all

#### Example
```xml
<TicketTypesAvailable>standard group</TicketTypesAvailable>
```

### ScopeOfTicketsAvailable

The scope of the tickets sold at this facility.

#### Values (`ScopeOfTicketEnumeration`)
- unknown
- localTicket
- nationalTicket
- internationalTicket

#### Example
```xml
<ScopeOfTicketsAvailable>localTicket nationalTicket</ScopeOfTicketsAvailable>
```

### LowCounterAccess

Whether there is a low counter for accessibility.

#### Example
```xml
<LowCounterAccess>false</LowCounterAccess>
```

### HeightOfLowCounter

Height of the counter.

#### Example
```xml
<HeightOfLowCounter>0.8</HeightOfLowCounter>
```

### InductionLoops

Whether the ticket counter or ticket machine provides induction loops.

#### Example
```xml
<InductionLoops>false</InductionLoops>
```

### TactileInterfaceAvailable

Whether the ticket machine provides a tactile interface.

#### Example
```xml
<TactileInterfaceAvailable>false</TactileInterfaceAvailable>
```

### AudioInterfaceAvailable

Whether the ticket machine provides an audio interface.

#### Example
```xml
<AudioInterfaceAvailable>true</AudioInterfaceAvailable>
```

### WheelchairSuitable

Whether the ticket machine can be used while seated in a wheelchair.

#### Example
```xml
<WheelchairSuitable>true</WheelchairSuitable>
```

## AccessVehicleEquipment

An equipment to describe features related to vehicle access such as steps, entrance and more.

```xml
<AccessVehicleEquipment version="any" id="321">
  ...
</AccessVehicleEquipment>
```

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

#### DELFI

- 3101 ↦ `BoardingHeight from AccessVehicleEquipment where Kneeling == true`

#### Example

```xml
<BoardingHeight>0.32</BoardingHeight>
```

### Kneeling

Whether BoardingHeight and FloorHeight values reflect the height when kneeling is active/inactive.

#### Example

```xml
<Kneeling>true</Kneeling>
```

### FloorHeight

Height of the inner entry point (floor next to the entrance), measured from the ground of the road or top of the rail. Together with `BoardingHeight` this describes the lowest and highest point of an entrance. (See [NeTEx Proposal](https://github.com/NeTEx-CEN/NeTEx/issues/900))

#### DELFI

- 3100 ↦ `FloorHeight from AccessVehicleEquipment where Kneeling == true`

#### Example

```xml
<FloorHeight>0.75</FloorHeight>
```

### EdgeToTrackCenterDistance

Distance from the outer entry point (including any fixed outer steps) to the vehicle center (center point between axles). Can be used to calculate the horizontal gap in conjunction with the EdgeToTrackCenterDistance from Quay. (See [NeTEx Proposal](https://github.com/NeTEx-CEN/NeTEx/issues/900))

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

## RetractableStepVehicleEquipment

A special vehicle equipment for sliding and folding steps which reduce the horizontal and partially vertical gap between vehicle and platform. (See [NeTEx Proposal](https://github.com/NeTEx-CEN/NeTEx/issues/873))

#### DELFI

- 3113 ↦ Existence of `RetractableStepVehicleEquipment`

```xml
<RetractableStepVehicleEquipment version="any" id="321">
  ...
</RetractableStepVehicleEquipment>
```

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

## RampVehicleEquipment

A special equipment to model ramps used to bridge the horizontal and vertical gap between vehicle and platform. (See [NeTEx Proposal](https://github.com/NeTEx-CEN/NeTEx/issues/873))

#### DELFI

- 3120 ↦ Existence of `RampVehicleEquipment`

```xml
<RampVehicleEquipment version="any" id="321">
  ...
</RampVehicleEquipment>
```

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
