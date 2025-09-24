# Equipment

## Location

```
PublicationDelivery/dataObjects/ResourceFrame/equipments
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
<PassengerInformationEquipmentList>timetablePoster lineTimetable</PassengerInformationEquipmentList>
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
