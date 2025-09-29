# TicketingEquipment

An equipment to describe features related to ticketing, like ticket machines or ticket counters.

```xml
<TicketingEquipment version="any" id="321">
  ...
</TicketingEquipment>
```

**XSD:** [`xsd/netex_part_1/part1_ifopt/netex_ifopt_equipmentTicketing_version.xsd`](https://github.com/NeTEx-CEN/NeTEx/blob/next/xsd/netex_part_1/part1_ifopt/netex_ifopt_equipmentTicketing_version.xsd#L90)

## Location
```
PublicationDelivery/dataObjects/ResourceFrame/equipments
```

## Properties

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
