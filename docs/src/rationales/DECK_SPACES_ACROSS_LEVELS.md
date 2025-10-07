# DeckSpaces spanning multiple floors

`DeckPlan` elements can only belong to exactly one level. They cannot span multiple levels like it is possible with [OSM's Simple Indoor Tagging](https://wiki.openstreetmap.org/wiki/Simple_Indoor_Tagging#Multi-level_features_and_repeated_features).

Therefore it is necessary to recreate the respective room for each `DeckLevel`/`Deck`. To model the connectivity between decks each room must contain references (`DeckEntranceRef`) to each entrance the staircase is connected to. Each `DeckEntrance` element should be modeled on their respective `Deck` so that they "inherit" the `Deck`'s `DeckLevel`. Otherwise one has to separately specify the `DeckLevel` on the `DeckEntrance`.

## Example

This shows the modeling of a staircase spanning 2 floors.

```xml
<DeckPlan>
  <deckLevels>
    <DeckLevel id="0">
      <Label>Ground Floor</Label>
    </DeckLevel>
    <DeckLevel id="1">
      <Label>Upper Floor</Label>
  </deckLevels>
  <decks>
    <Deck>
      <DeckLevelRef ref="0"/>
      <deckSpaces>
        <!-- Staircase -->
        <PassengerSpace id="staircase-0">
          <deckEntrances>
            <PassengerEntrance id="lower-entrance">
              <!-- DeckLevelRef inherited from surrounding Deck -->
            </PassengerEntrance>
            <PassengerEntranceRef ref="upper-entrance"/>
          </deckEntrances>
        </PassengerSpace>
    </Deck>
    <Deck>
      <DeckLevelRef ref="1"/>
      <deckSpaces>
        <!-- Staircase -->
        <PassengerSpace id="staircase-1">
          <deckEntrances>
            <PassengerEntrance id="upper-entrance">
              <!-- DeckLevelRef inherited from surrounding Deck -->
            </PassengerEntrance>
            <PassengerEntranceRef ref="lower-entrance"/>
          </deckEntrances>
        </PassengerSpace>
    </Deck>
  </decks>
</DeckPlan>
```
