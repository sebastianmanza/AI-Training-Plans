import Foundation

struct HomeData: Codable {
  let day: String
  let mileage: Float
  let pace: String
  let stimuli: String
  let goalRPE: String
  let time: String
  let upcoming: String
  let upcomingmileage: Float
  let upcomingtime: String

  enum CodingKeys: String, CodingKey {
    case day, mileage, pace, stimuli, time, upcomingmileage,
         upcomingtime
    case goalRPE   = "goal_rpe"
    case upcoming
  }
}
