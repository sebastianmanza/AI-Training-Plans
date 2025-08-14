import Foundation

struct SurveyIn: Codable {
  let date_of_birth: String
  let sex: String
  let running_experience: String
  let major_injuries: Int
  let most_recent_injury: Int
  let longest_run: Int
  let goal_date: String
  let days_per_week: Int
  let days_of_week: [String]
  let most_time_day: String
  let current_5k_fitness: Int
}
