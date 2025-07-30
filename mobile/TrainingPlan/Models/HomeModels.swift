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
  let weeknum: [Int]
  let weekmileage: [Float]
  let weekpctcomplete: [Float]
  let weekstimuli: [String]

  enum CodingKeys: String, CodingKey {
    case day, mileage, pace, stimuli, time, upcomingmileage,
         upcomingtime, upcoming, weeknum, weekmileage, weekpctcomplete, weekstimuli
    case goalRPE   = "goal_rpe"
  }
}
