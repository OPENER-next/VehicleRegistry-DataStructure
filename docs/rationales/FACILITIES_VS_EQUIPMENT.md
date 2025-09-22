# Facilities vs Equipment

Some properties can be assigned via facilities (`ServiceFacilitySet`) and via equipment.

Examples are
- `PassengerInformationFacilityList` is also included in `PassengerInformationEquipment`
- `SanitaryFacilityList` is also included in `SanitaryEquipment`

A decision was made to prefer using equipment over facilities in such scenarios because:
- equipment is already required in other parts
- equipment allows additional details
- equipment is used to describe e.g. stair or toilets in a DeckPlan so the defined equipment can be located in a DeckPlan if needed

For DELFI the following modelling approach could have been used instead of the equipment:

```xml
<VehicleType version="any" id="VehicleType/id/1">
  <facilities>
    <ServiceFacilitySet version="any" id="ServiceFacilitySet/id/1">
      <PassengerInformationFacilityList>
        <!-- DELFI 3020 --> nextStopIndicator<!---->
        <!-- DELFI 3021 - Proposal: https://github.com/NeTEx-CEN/NeTEx/issues/882
        destinationDisplay
        -->
        <!-- DELFI 3030 --> stopAnnouncements<!---->
        <!-- DELFI 3031 - Proposal: https://github.com/NeTEx-CEN/NeTEx/issues/882
        routeAnnouncements
        -->
      </PassengerInformationFacilityList>

      <SanitaryFacilityList>
        <!-- DELFI 3060 --> toilet<!---->
        <!-- DELFI 3061 --> wheelchairAccessToilet<!---->
      </SanitaryFacilityList>

      <TicketingFacilityList>
        <!-- DELFI 3070 --> ticketMachines
      </TicketingFacilityList>
    </ServiceFacilitySet>
  </facilities>
</VehicleType>
```