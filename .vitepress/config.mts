import { defineConfig } from 'vitepress'

// https://vitepress.dev/reference/site-config
export default defineConfig({
  srcDir: "docs",
  base: "/VehicleRegistry-DataStructure/",

  title: 'Vehicle Registry',
  description: "NeTEx based data structure definition for a national vehicle registry. ",
  lang: 'en-GB',
  themeConfig: {
    // https://vitepress.dev/reference/default-theme-config
    sidebar: [
      {
        text: 'Building Blocks',
        items: [
          { text: 'General', link: '/GENERAL.md' },
          { text: 'Vehicle Model', link: '/VEHICLE_MODEL.md' },
          { text: 'Vehicle Type', link: '/VEHICLE_TYPE.md' },
          { text: 'Vehicle Equipment Profile', link: '/VEHICLE_EQUIPMENT_PROFILE.md' },
          {
            text: 'Equipment',
            link: '/EQUIPMENT/EQUIPMENT.md',
            collapsed: true,
            items: [
              { text: 'Seat Equipment', link: '/EQUIPMENT/SEAT_EQUIPMENT.md' },
              { text: 'Luggage Spot Equipment', link: '/EQUIPMENT/LUGGAGE_SPOT_EQUIPMENT.md' },
              { text: 'Bed Equipment', link: '/EQUIPMENT/BED_EQUIPMENT.md' },
              { text: 'Access Vehicle Equipment', link: '/EQUIPMENT/ACCESS_VEHICLE_EQUIPMENT.md' },
              { text: 'Ramp Vehicle Equipment', link: '/EQUIPMENT/RAMP_VEHICLE_EQUIPMENT.md' },
              { text: 'Hoist Vehicle Equipment', link: '/EQUIPMENT/HOIST_VEHICLE_EQUIPMENT.md' },
              { text: 'Retractable Step Vehicle Equipment', link: '/EQUIPMENT/RETRACTABLE_STEP_VEHICLE_EQUIPMENT.md' },
              { text: 'Staircase Equipment', link: '/EQUIPMENT/STAIRCASE_EQUIPMENT.md' },
              { text: 'Entrance Equipment', link: '/EQUIPMENT/ENTRANCE_EQUIPMENT.md' },
              { text: 'Sanitary Equipment', link: '/EQUIPMENT/SANITARY_EQUIPMENT.md' },
              { text: 'Ticketing Equipment', link: '/EQUIPMENT/TICKETING_EQUIPMENT.md' },
              { text: 'Ticket Validator Equipment', link: '/EQUIPMENT/TICKET_VALIDATOR_EQUIPMENT.md' },
              { text: 'Passenger Information Equipment', link: '/EQUIPMENT/PASSENGER_INFORMATION_EQUIPMENT.md' },
              { text: 'Passenger Safety Equipment', link: '/EQUIPMENT/PASSENGER_SAFETY_EQUIPMENT.md' },
              { text: 'Help Point Equipment', link: '/EQUIPMENT/HELP_POINT_EQUIPMENT.md' },
              { text: 'Rubbish Disposal Equipment', link: '/EQUIPMENT/RUBBISH_DISPOSAL_EQUIPMENT.md' },
              { text: 'Place Lighting', link: '/EQUIPMENT/PLACE_LIGHTING.md' }
            ]
          },
          {
            text: 'Deck Plan',
            link: '/DECK_PLAN/DECK_PLAN.md',
            items: [
              { text: 'Deck', link: '/DECK_PLAN/DECK.md' },
              { text: 'Deck Level', link: '/DECK_PLAN/DECK_LEVEL.md' },
              {
                text: 'Deck Space',
                link: '/DECK_PLAN/DECK_SPACE/DECK_SPACE.md',
                collapsed: true,
                items: [
                  { text: 'Other Deck Space', link: '/DECK_PLAN/DECK_SPACE/OTHER_DECK_SPACE.md' },
                  { text: 'Passenger Space', link: '/DECK_PLAN/DECK_SPACE/PASSENGER_SPACE.md' }
                ]
              },
              {
                text: 'Deck Entrance',
                link: '/DECK_PLAN/DECK_ENTRANCE/DECK_ENTRANCE.md',
                collapsed: true,
                items: [
                  { text: 'Passenger Entrance', link: '/DECK_PLAN/DECK_ENTRANCE/PASSENGER_ENTRANCE.md' },
                  { text: 'Other Deck Entrance', link: '/DECK_PLAN/DECK_ENTRANCE/OTHER_DECK_ENTRANCE.md' },
                  { text: 'Deck Vehicle Entrance', link: '/DECK_PLAN/DECK_ENTRANCE/DECK_VEHICLE_ENTRANCE.md' }
                ]
              },
              { text: 'Deck Window', link: '/DECK_PLAN/DECK_WINDOW.md' },
              {
                text: 'Locatable Spot',
                link: '/DECK_PLAN/LOCATABLE_SPOT/LOCATABLE_SPOT.md',
                collapsed: true,
                items: [
                  { text: 'Passenger Spot', link: '/DECK_PLAN/LOCATABLE_SPOT/PASSENGER_SPOT.md' },
                  { text: 'Luggage Spot', link: '/DECK_PLAN/LOCATABLE_SPOT/LUGGAGE_SPOT.md' },
                  { text: 'Passenger Vehicle Spot', link: '/DECK_PLAN/LOCATABLE_SPOT/PASSENGER_VEHICLE_SPOT.md' }
                ]
              },
              { text: 'Actual Vehicle Equipment', link: '/DECK_PLAN/ACTUAL_VEHICLE_EQUIPMENT.md' },
              { text: 'Accessibility Assessment', link: '/DECK_PLAN/ACCESSIBILITY_ASSESSMENT.md' }
            ]
          }
        ]
      },
      {
        text: 'Rationales',
        items: [
          { text: 'Equipment assignment to vehicle types', link: '/rationales/EQUIPMENT_ASSIGNMENT.md' },
          { text: 'Facilities vs equipment', link: '/rationales/FACILITIES_VS_EQUIPMENT.md' },
          { text: 'DeckSpaces spanning multiple floors', link: '/rationales/DECK_SPACES_ACROSS_LEVELS.md' },
          { text: 'Wheelchair Vehicle Equipment', link: '/rationales/WHEELCHAIR_VEHICLE_EQUIPMENT.md' }
        ]
      }
    ],

    outline: {
      level: [2, 3],
      label: 'Outline'
    },

    socialLinks: [
      { icon: 'github', link: 'https://github.com/OPENER-next/VehicleRegistry-DataStructure' }
    ],

    editLink: {
      pattern: 'https://github.com/OPENER-next/VehicleRegistry-DataStructure/edit/main/docs/:path',
      text: 'Edit this page on GitHub'
    },

    search: {
      provider: 'local'
    },

    externalLinkIcon: true,
  }
})
