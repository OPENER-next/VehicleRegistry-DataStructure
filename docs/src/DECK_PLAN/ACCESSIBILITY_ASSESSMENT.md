# AccessibilityAssessment

Can be used to describe accessibility characteristics of an [ActualVehicleEquipment](EQUIPMENT/EQUIPMENT.md), [DeckSpace](DECK_PLAN/DECK_SPACE/DECK_SPACE.md) or [DeckEntrance](DECK_PLAN/DECK_ENTRANCE/DECK_ENTRANCE.md).

**XSD:** [`xsd/netex_framework/netex_genericFramework/netex_accessibility/netex_acsb_accessibility.xsd`](https://github.com/NeTEx-CEN/NeTEx/blob/next/xsd/netex_framework/netex_genericFramework/netex_accessibility/netex_acsb_accessibility.xsd#L128)

## Properties

### MobilityImpairedAccess

Useful to generally mark areas as accessible for mobility impaired people. A [DeckSpace](DECK_PLAN/DECK_SPACE/DECK_SPACE.md) could be colored or patterned differently on a visual deck plan.

#### Values (`LimitationStatusEnumeration`):
- true
- false
- unknown
- partial

#### Example
```xml
<MobilityImpairedAccess>true</MobilityImpairedAccess>
```

### suitabilities

Can be used to depict whether a certain facility is suitable or unsuitable for people with a specific need.

Per `Suitability` only one of the following properties can be present: `MobilityNeed`, `PsychosensoryNeed`, `MedicalNeed`, `EncumbranceNeed`.

#### Properties

##### MobilityNeed
A specific passenger mobility need.

###### Values (`MobilityEnumeration`):
- wheelchair
- assistedWheelchair
- motorizedWheelchair
- mobilityScooter
- roadMobilityScooter
- walkingFrame
- restrictedMobility
- otherMobilityNeed
- normal

###### Example
```xml
<MobilityNeed>motorizedWheelchair</MobilityNeed>
```

##### PsychosensoryNeed
A specific passenger psychosensory need.

###### Values (`PsychosensoryNeedEnumeration`):
- visualImpairment
- auditoryImpairment
- cognitiveInputImpairment
- averseToLifts
- averseToEscalators
- averseToConfinedSpaces
- averseToCrowds
- otherPsychosensoryNeed

###### Example
```xml
<PsychosensoryNeed>averseToConfinedSpaces</PsychosensoryNeed>
```

##### MedicalNeed
A specific passenger medical need.

###### Values (`MedicalNeedEnumeration`):
- allergic
- heartCondition
- otherMedicalNeed

###### Example
```xml
<MedicalNeed>allergic</MedicalNeed>
```

##### EncumbranceNeed
A specific passenger encumbrance need.

###### Values (`EncumbranceEnumeration`):
- luggageEncumbered
- pushchair
- baggageTrolley
- oversizeBaggage
- guideDog
- otherAnimal
- otherEncumbranceNeed

###### Example
```xml
<EncumbranceNeed>guideDog</EncumbranceNeed>
```

##### Suitable

Whether the facility is suitable for the specified `PassengerNeed` or not.

###### Values (`SuitableEnumeration`):
- suitable
- notSuitable

###### Example
```xml
<Suitable>suitable</Suitable>
```

#### Example
```xml
<suitabilities>
  <Suitability>
    <MobilityNeed>wheelchair</MobilityNeed>
    <Suitable>suitable</Suitable>
  </Suitability>
  <Suitability>
    <PsychosensoryNeed>visualImpairment</PsychosensoryNeed>
    <Suitable>notSuitable</Suitable>
  </Suitability>
  ...
</suitabilities>
```

### Comment

A free text containing additional information such as warnings or recommendations regarding accessibility.

#### Example
```xml
<Comment>
  <Text lang="en">Make sure to apply the brakes of your wheelchair.</Text>
</Comment>
```
