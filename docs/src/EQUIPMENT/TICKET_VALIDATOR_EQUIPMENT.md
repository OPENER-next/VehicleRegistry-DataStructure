# Equipment

## Location

```
PublicationDelivery/dataObjects/ResourceFrame/equipments
```

## TicketValidatorEquipment

An equipment to describe a ticket validator.

```xml
<TicketValidatorEquipment version="any" id="321">
  ...
</TicketValidatorEquipment>
```
### TicketValidatorType

The type of ticket validator.

#### Values (`TicketValidatorEnumeration`)
- paperStamp
- contactLess
- magnetic
- other

#### Example
```xml
<TicketValidatorType>paperStamp contactLess</TicketValidatorType>
```

### AudioValidationFeedback

Whether the ticket validator provides audio feedback on validation.

#### Example
```xml
<AudioValidationFeedback>true</AudioValidationFeedback>
```

### VisualValidationFeedback

Whether the ticket validator provides visual feedback on validation.

#### Example
```xml
<VisualValidationFeedback>true</VisualValidationFeedback>
```
### TactileValidationFeedback

Whether the ticket validator provides tactile feedback on validation.

#### Example
```xml
<TactileValidationFeedback>false</TactileValidationFeedback>
```
### ValidationGuidance

Free text describing how to use the ticket validator.

#### Example
```xml
<ValidationGuidance>The magnetic strip should point forward when inserting into the validator.</ValidationGuidance>
```
