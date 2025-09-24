# Equipment

## Location

```
PublicationDelivery/dataObjects/ResourceFrame/equipments
```

## PassengerSafetyEquipment

An equipment to describe passenger safety related facilities like CCTV or audio announcements.

```xml
<PassengerSafetyEquipment version="any" id="321">
  ...
</PassengerSafetyEquipment>
```

### Cctv

Whether there is CCTV.

#### Example
```xml
<Cctv>true</Cctv>
```

### SosPanel

Whether there is an SOS panel.

#### Example
```xml
<SosPanel>true</SosPanel>
```

### HeightOfSosPanel

The height of the SOS panel.

#### Example
```xml
<HeightOfSosPanel>1</HeightOfSosPanel>
```

### AudioAnnouncements

Whether there are audio announcements.

#### Example
```xml
<AudioAnnouncements>true</AudioAnnouncements>
```

### AudioAnnouncementType

When the audio announcements are announced.

#### Values (`AudioAnnouncementTypeEnumeration`)
- onDemand
- automatic

#### Example
```xml
<AudioAnnouncementType>automatic</AudioAnnouncementType>
```

### AudioAnnouncementsTrigger

How the audio announcements are triggered.

#### Values (`AudioTriggerMethodEnumeration`)
- presenceDetector
- mobileApp
- internetPage
- specificDevice
- pushButton
- other

#### Example
```xml
<AudioAnnouncementsTrigger>mobileApp</AudioAnnouncementsTrigger>
```
