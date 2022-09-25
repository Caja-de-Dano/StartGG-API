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


