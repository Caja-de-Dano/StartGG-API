sets_query_by_event_id = """
  query FindSets($eventId: ID!, $page: Int!) {
    event(id: $eventId) {
      sets(
        page: $page,
        perPage: 100,
        sortType: STANDARD
      ) {
        pageInfo {
          totalPages
        }
        nodes {
          fullRoundText
          totalGames
          slots {
            entrant {
              name
            }
          }
        }
      }
    }
  }

"""
tournament_contact_query_by_slug = """
    query FindEventId($slug: String!) {
        tournament(slug: $slug) {
            id
            name
            numAttendees
            startAt
            primaryContact
            primaryContactType
            owner {
              name
              email
              genderPronoun
              slug
              authorizations {
                type
                externalUsername
              }
            }
            streams {
              id
              streamName
              streamSource
            }
            events {
                id
                name
                videogame {
                    id
                    displayName
                    slug
                }
            }
        }
    }
"""
tournament_query_by_slug = """
    query FindEventId($slug: String!) {
        tournament(slug: $slug) {
            id
            name
            numAttendees
            startAt
            events {
                id
                slug
                name
                numEntrants
                videogame {
                    id
                    displayName
                    slug
                }
            }
            images{
              id
              url
              height
              width
            }
        }
    }
"""
tournaments_base_query = """
  query Tournaments(QUERY_PARAMS) {
    event(SEARCH_BY) {
      RESPONSE_KEYS
    }
  }
"""

query_by_distance = """
  query Tournaments($page: Int!, $perPage: Int, $coordinates: String!, $radius: String!) {
    tournaments(query: {
      perPage: $perPage
      page: $page
      filter: {
        location: {
          distanceFrom: $coordinates,
          distance: $radius
        }
      }
    }) {
      pageInfo {
          total
          totalPages
      }
      nodes {
        id
        name
        city
        numAttendees
        slug
        createdAt
        endAt
        images { id }
        links { facebook discord }
      }
    }
  }"""
general_tournament_search_query = """
  query Tournaments($perPage: Int, $beforeDate: Timestamp!, $afterDate: Timestamp!) {
    tournaments(query: {
      perPage: $perPage
      filter: {
        beforeDate: $beforeDate,
        afterDate: $afterDate,
        hasOnlineEvents: true,
        videogameIds: 43868
      }
    }) {
      nodes {
        name
        numAttendees
        slug
        endAt
        primaryContact
        primaryContactType

        links { facebook discord }
        owner {
          name
          genderPronoun
          authorizations {
            externalUsername
            type
          }
        }
      }
    }
  }
"""
query_by_distance_and_time = """
  query Tournaments($perPage: Int, $coordinates: String!, $radius: String!, $beforeDate: Timestamp!, $afterDate: Timestamp!) {
    tournaments(query: {
      perPage: $perPage
      filter: {
        location: {
          distanceFrom: $coordinates,
          distance: $radius
        },
        beforeDate: $beforeDate,
        afterDate: $afterDate
      }
    }) {
      nodes {
        id
        name
        city
        numAttendees
        slug
        createdAt
        endAt
        images { id url type }
        links { facebook discord }
        owner {
          email
          name
          genderPronoun
          authorizations {
            externalUsername
            type
          }
          tournaments {
            nodes {
              id
              name
              slug
              numAttendees
            }
          }
        }
      }
    }
  }
"""

base_query_tournaments = """
  query Tournaments(TOP_PARAMS) {
    tournaments(query: QUERY) {
      NODE_DEFINITION
    }
  }"""

event_base_query = """
  query EventEntrants(QUERY_PARAMS) {
    event(SEARCH_BY) {
      RESPONSE_KEYS
    }
  }
"""

event_entrants_names_query = """
  query EventEntrants($eventId: ID!, $page: Int!, $perPage: Int!) {
    event(id: $eventId) {
      id
      name
      entrants(query: {
        page: $page
        perPage: $perPage
      }) {
        pageInfo {
          total
          totalPages
        }
        nodes {
          id
          participants {
            id
            gamerTag
          }
        }
      }
    }
  }
"""

event_entrants_query = """
  query EventEntrants($eventId: ID!, $page: Int!, $perPage: Int!) {
    event(id: $eventId) {
      id
      name
      entrants(query: {
        page: $page
        perPage: $perPage
      }) {
        pageInfo {
          total
          totalPages
        }
        nodes {
          id
          participants {
            id
            gamerTag
            user {
              authorizations {
                type
                externalUsername
              }
            }
          }
        }
      }
    }
  }
"""

event_details_query = """
    query EventDetails($eventId: ID!) {
        event(id: $eventId) {
            id
            name
            competitionTier
            isOnline
            numEntrants
            prizingInfo
            rulesMarkdown
            rulesetId
            slug
            startAt
            state
        }
    }
"""

videogame_details_by_id_query = """
    query VideogameDetails($id: ID!) {
        videogame(id: $id) {
            id
            name
            slug
            images{
              id
              height
              width
              ratio
              type
              url
            }
            characters{
              id
              name
              images{
                id
                height
                width
                ratio
                type
                url
              }

            }
        }
    }
"""

videogame_details_by_slug_query = """
    query VideogameDetails($slug: String!) {
        videogame(slug: $slug) {
            id
            name
            slug
            images{
              id
              height
              width
              ratio
              type
              url
            }
            characters{
              id
              name
              images{
                id
                height
                width
                ratio
                type
                url
              }

            }
        }
    }
"""

# This query gets a lot of information from all events of tournaments
# Anthology : tournament -> events -> phases (or in other terms pools like "Pool A1")
tournament_query_by_slug_heavy = """
  query GetTournamentInfo($tourneySlug: String!) {
    tournament(slug: $tourneySlug) {
      id
      name
      slug
      shortSlug
      numAttendees
      startAt
      events {
        id
        slug
        name
        numEntrants
        videogame {
          id
          displayName
          slug
        }
        phases {
          id
          name
          phaseGroups(query: { page: 1, perPage: 100 }) {
            nodes {
              id
              displayIdentifier
            }
          }
        }
      }
    }
  }
"""

# This query gets sets from a phase group
# So if you want to get the sets from group A1 you need to input the ID of this group.
# There will always be a phase group even if your tournament only have one tree, so you can always use this to get sets
# from an event
sets_query_from_phaseGroup_from_phase = """
  query PhaseGroupSets($phaseId: ID!, $page: Int!){
    phaseGroup(id: $phaseId){
      sets(page: $page, perPage: 100, sortType: STANDARD) {
        pageInfo {
          totalPages
        }
          nodes {
            id
            fullRoundText
            identifier
            totalGames
            slots {
              entrant {
                id
                name
              }
            }
         }
      }
    }
  }
"""
