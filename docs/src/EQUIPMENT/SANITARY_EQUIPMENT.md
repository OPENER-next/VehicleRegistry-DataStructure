# Equipment

## Location

```
PublicationDelivery/dataObjects/ResourceFrame/equipments
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
