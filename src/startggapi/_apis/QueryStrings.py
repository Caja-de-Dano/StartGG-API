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
        endAt
      }
    }
  }
"""