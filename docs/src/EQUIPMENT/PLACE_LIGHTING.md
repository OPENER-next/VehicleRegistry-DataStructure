# PlaceLighting

An equipment to describe the lighting of an area.

```xml
<PlaceLighting version="any" id="321">
  ...
</PlaceLighting>
```

## Location
```
PublicationDelivery/dataObjects/ResourceFrame/equipments
```

## Properties

### Lighting

Whether the place is lit or not.

#### Values (`LightingEnumeration`):
- wellLit
- poorlyLit
- unlit
- unknown
- other

#### Example
```xml
<Lighting>unlit</Lighting>
```

### LightingOnMethod

Describes when or how the light is switched on.

#### Values (`LightingOnMethodEnumeration`):
- movementDetector
- stepDetector
- switchOnTheWall
- atDoorOpening
- onlyAtNight
- alwaysOn (supersedes the `AlwaysLit` property)
- other

#### Example
```xml
<LightingOnMethod>alwaysOn</LightingOnMethod>
```
