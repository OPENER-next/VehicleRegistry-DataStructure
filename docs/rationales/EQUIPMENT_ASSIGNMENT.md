# Equipment assignment

The vehicle registry needs a detailed description of vehicle (carriage, bus, ferry) types. In most cases this will map directly to a vehicle model (Volvo Bus 8500LE, Mercedes Citaro G). However there might be vehicle models that have been altered or upgraded e.g. because all the buses got equipped with an additional electrical ramp. So there can be a "Volvo Bus 8500LE" and a "Volvo Bus 8500LE with ramp".

According to the authors a `VehicleType` in NeTEx is a broad category mainly used to describe requirements for a specific journey a `Vehicle` must fulfill. Such a category can be thought of as "low floor bus" or "tram with ramp".
Therefore it is not possible to add detailed information via equipment directly to a `VehicleType` unlike `Vehicle`.

We need equipments on the `VehicleType` for two reasons:
- **Different levels of detail:** Not every `VehicleType` will have a `DeckPlan` but it should still be possible to model how the `VehicleType` is equipped e.g. which seats or what ramp it carries.
- **Not everything is located:** Some equipment such as passenger information speakers, or a portable ramp cannot or doesn't need to be located in a `DeckPLan`.

As the [proposal of adding equipment to `VehicleType`](https://github.com/NeTEx-CEN/NeTEx/issues/875) was declined, several alternative NeTEx compliant modelling options are proposed below.

## Modelling options

### Create dummy `DeckSpace`
The idea is to always assign a `DeckPlan` to a `VehicleType` and create a dummy `DeckSpace` encompassing the whole vehicle for the sole purpose of assigning equipments to it.

#### Example
```xml
<ResourceFrame version="any" id="ResourceFrame/id/1">
  <equipments>
    <AccessVehicleEquipment version="any" id="AccessVehicleEquipment/id/1">
      <NumberOfSteps>3</NumberOfSteps>
    </AccessVehicleEquipment>
  </equipments>

  <vehicleTypes>
    <VehicleType version="any" id="VehicleType/id/1">
      ...
    </VehicleType>
  </vehicleTypes>

  <deckPlans>
    <DeckPlan version="any" id="DeckPlan/id/1">
      <decks>
        <Deck version="any" id="Deck/id/1">
          <deckSpaces>
            <PassengerSpace version="any" id="PassengerSpace/id/1">
              <actualVehicleEquipments>
                <ActualVehicleEquipment>
                  <AccessVehicleEquipmentRef ref="AccessVehicleEquipment/id/1"/>
                </ActualVehicleEquipment>
              </actualVehicleEquipments>
            </PassengerSpace>
          </deckSpaces>
        </Deck>
      </decks>
    </DeckPlan>
  </deckPlans>
</ResourceFrame>
```

#### Pros:
- `DeckPlan` is already part of the data structure so reusing it keeps the data structure simple.
- Little overhead from a modelling perspective.

#### Cons:
- `DeckPlan` will almost always be used to render something to the user. Having functional equipment like access equipments or passenger information equipment assigned to it violates the separation of concerns.
- It is difficult to detect if the equipment is only assigned "as a workaround" or if the `DeckSpace` with the given equipment truly exists.

### Create dummy `Vehicle`
This idea was first proposed in the [DELFI  handbook "Barrierefreie Reiseketten in der Fahrgastinformation"](https://www.delfi.de/media/delfi_handbuch_barrierefreie_reiseketten_2._auflage_2024.pdf). The idea is to always create and export a `Vehicle` together with the `VehicleType`. The equipment is then assigned to the `Vehicle`.

#### Example
```xml
<ResourceFrame version="any" id="ResourceFrame/id/1">
  <equipments>
    <AccessVehicleEquipment version="any" id="AccessVehicleEquipment/id/1">
      <NumberOfSteps>3</NumberOfSteps>
    </AccessVehicleEquipment>
  </equipments>

  <vehicleTypes>
    <VehicleType version="any" id="VehicleType/id/1">
      ...
    </VehicleType>
  </vehicleTypes>

  <vehicles>
    <Vehicle version="any" id="Vehicle/id/1">
      <VehicleTypeRef ref="VehicleType/id/1"/>
      <actualVehicleEquipments>
        <ActualVehicleEquipment>
          <AccessVehicleEquipmentRef ref="AccessVehicleEquipment/id/1"/>
        </ActualVehicleEquipment>
      </actualVehicleEquipments>
    </Vehicle>
  </vehicles>
</ResourceFrame>
```

#### Pros:
- Relatively low overhead from a modelling perspective.

#### Cons:
- This is misusing the `Vehicle` concept as `Vehicle` should represent a single identifiable vehicle in the real world.

### Use `VehicleTypeRef` from `ActualVehicleEquipment`
The idea is to define the relation of the equipment and the `VehicleType` via `ActualVehicleEquipment` which allows referencing a `VehicleType` via `VehicleTypeRef`.

#### Example
```xml
<ResourceFrame version="any" id="ResourceFrame/id/1">
  <equipments>
    <AccessVehicleEquipment version="any" id="AccessVehicleEquipment/id/1">
      <NumberOfSteps>3</NumberOfSteps>
    </AccessVehicleEquipment>

    <ActualVehicleEquipment>
      <VehicleTypeRef ref="VehicleType/id/1"/>
      <AccessVehicleEquipmentRef ref="AccessVehicleEquipment/id/1"/>
    </ActualVehicleEquipment>
  </equipments>

  <vehicleTypes>
    <VehicleType version="any" id="VehicleType/id/1">
      ...
    </VehicleType>
  </vehicleTypes>
</ResourceFrame>
```

#### Pros:
- The `Units` element from `ActualVehicleEquipment` can be used to depict how many equipments are really present in the `VehicleType`.
- No additional concepts required.
- Little overhead from a modelling perspective.

#### Cons:
- After asking a NeTEx author, [this is likely a bug](https://github.com/NeTEx-CEN/NeTEx/issues/875#issuecomment-3258775136). `VehicleTypeRef` should be `VehicleRef` instead.
- Referencing with `ActualVehicleEquipment` is uncommon and feels backwards.

### Use `Tractive/TrailingElementType`
The idea is to use the `TractiveElementType` or `TrailingElementType` elements because they can hold equipment.

```xml
<ResourceFrame version="any" id="ResourceFrame/id/1">
  <trainElementTypes>
    <TrailingElementType version="any" id="TrailingElementType/id/1">
      <equipments>
        <AccessVehicleEquipment version="any" id="AccessVehicleEquipment/id/1">
          <NumberOfSteps>3</NumberOfSteps>
        </AccessVehicleEquipment>
      </equipments>
    </TrailingElementType>
  </vehicleTypes>
</ResourceFrame>
```

#### Pros:
- Least overhead from a modelling perspective.
- The equipment can even be defined directly (not just referenced) on the `Tractive/TrailingElementType`.

#### Cons:
- This is misusing `Tractive/TrailingElementType` as they are intended for trains (hence they are located under `trainElementTypes`).


### Use reference chain: `VehicleType` ⇢ `VehicleModel` ⇢ `VehicleEquipmentProfile` ⇢ `Equipment`
The idea is to reference equipments via an `VehicleEquipmentProfile`. This can be referenced by a `VehicleModel` which can be referenced (or reference) a `VehicleType`.

#### Example
```xml
<ResourceFrame version="any" id="ResourceFrame/id/1">
  <equipments>
    <AccessVehicleEquipment version="any" id="AccessVehicleEquipment/id/1">
      <NumberOfSteps>3</NumberOfSteps>
    </AccessVehicleEquipment>
  </equipments>

  <vehicleTypes>
    <VehicleType version="any" id="VehicleType/id/1">
      <ClassifiedAsRef ref="VehicleModel/id/1"></ClassifiedAsRef>
    </VehicleType>
  </vehicleTypes>

  <vehicleModels>
    <VehicleModel version="any" id="VehicleModel/id/1">
      <equipmentProfiles>
        <VehicleEquipmentProfileRef ref="VehicleEquipmentProfile/id/1"></VehicleEquipmentProfileRef>
      </equipmentProfiles>
    </VehicleModel>
  </vehicleModels>

  <vehicleEquipmentProfiles>
    <VehicleEquipmentProfile version="any" id="VehicleEquipmentProfile/id/1">
      <AccessVehicleEquipmentRef ref="AccessVehicleEquipment/id/1"></AccessVehicleEquipmentRef>
    </VehicleEquipmentProfile>
  </vehicleEquipmentProfiles>
</ResourceFrame>
```

#### Pros:
- Suggested by multiple NeTEx authors.
- The `Units` element from `VehicleEquipmentProfile` can be used to depict how many equipments are really present in the `VehicleType`.

#### Cons:
- Verbose modeling as it requires a `VehicleModel` just to stitch things together.

## Resolution

We choose the ["reference chain"](#Use%20reference%20chain%3A%20%60VehicleType%60%20%E2%87%A2%20%60VehicleModel%60%20%E2%87%A2%20%60VehicleEquipmentProfile%60%20%E2%87%A2%20%60Equipment%60) from the last suggestion as the only downside is the verbose modelling.

Since `VehicleType` and `VehicleModel` can reference each other the question was raised if `VehicleModel` should act as the core element while the other just acts as a helper element or vice versa.

Below is a comparison of the reference hierarchy:

<table>
<thead>
<tr>
  <th>
  VehicleType
  </th>
  <th>
  VehicleModel
  </th>
</tr>
</thead>
<tbody>
<tr>
  <td>
<pre>
VehicleType
  ↪ DeckPlan
  ↪ VehicleModel
    ↪ VehicleEquipmentProfile
      ↪ Equipment
</pre>
  </td>
  <td>
<pre>
VehicleModel
  ↪ VehicleType
    ↪ DeckPlan
  ↪ VehicleEquipmentProfile
    ↪ Equipment
</pre>
  </td>
</tr>
</tbody>
</table>


Using `VehicleModel` as the core element leads to a flatter reference hierarchy. Also different `VehicleModel`s may reference the same `VehicleType` as for example only some equipment changes, but not vice versa. Therefore we choose `VehicleModel` as the core element of the data structure while `VehicleType` acts more as a base type that multiple models might share.

