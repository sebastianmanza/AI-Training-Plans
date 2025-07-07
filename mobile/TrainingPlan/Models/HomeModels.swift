import Foundation

struct HomeData: Codable {
  let day: String
  let mileage: Float
  let pace: String
  let stimuli: String
  let goalRPE: String
  let upcoming: String

  enum CodingKeys: String, CodingKey {
    case day, mileage, pace, stimuli
    case goalRPE   = "goal_rpe"
    case upcoming
  }
}