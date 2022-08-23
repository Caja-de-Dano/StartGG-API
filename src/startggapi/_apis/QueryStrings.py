sets_query_by_event_id = """
  query FindSets($eventId: ID!) {
    event(id: $eventId) {
      sets(
        page: 1,
        perPage: 500,
        sortType: STANDARD
      ) {
        nodes {
          round
          fullRoundText
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

tournament_query_by_event_id = """
    query FindEventId($slug: String!) {
        tournament(slug: $slug) {
            id
            name
            events {
                id
                name
            }
        }
    }
"""

query_by_distance = """
  query Tournaments($perPage: Int, $coordinates: String!, $radius: String!) {
    tournaments(query: {
      perPage: $perPage
      filter: {
        location: {
          distanceFrom: $coordinates,
          distance: $radius
        }
      }
    }) {
      nodes {
        id
        name
        city
        numAttendees
        slug
        endAt
      }
    }
  }"""

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
        endAt
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
