import Foundation

struct SurveyIn: Codable {
    let date_of_birth: String
    let sex: String
    let running_experience: String
    let days_per_week: Int
    let days_of_week: [String]
    let most_time_day: String
    let current_5k_fitness: Int
    let major_injuries: String
    let most_recent_injury: String
}