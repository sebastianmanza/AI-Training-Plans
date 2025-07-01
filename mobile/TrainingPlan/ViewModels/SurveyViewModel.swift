import SwiftUI

@MainActor
class SurveyViewModel: ObservableObject {
  // form fields
  @Published var dateOfBirth = ""
  @Published var sex = ""
  @Published var experience = ""
    @Published var daysPerWeek: Int = 0
    @Published var daysOfWeek: [String] = []
  @Published var mostTimeDay = ""
    @Published var current5k: Int = 1110 // 5k estimate in seconds
  @Published var majorInjuries = ""
  @Published var recentInjury = ""
  
  // UI state
  @Published var isSubmitting = false
  @Published var response: [String: Any]?
  @Published var errorMessage: String?

  func submit() async {
    errorMessage = nil
    isSubmitting = true
    defer { isSubmitting = false }


    let survey = SurveyIn(
      date_of_birth: dateOfBirth,
      sex: sex,
      running_experience: experience,
      days_per_week: daysPerWeek,
      days_of_week: daysOfWeek,
      most_time_day: mostTimeDay,
      current_5k_fitness: current5k,
      major_injuries: majorInjuries,
      most_recent_injury: recentInjury
    )

    do {
      let result = try await SurveyAPI.submitPrelim(survey)
      response = result
    } catch let APIError.badURL {
      errorMessage = "Invalid server URL."
    } catch let APIError.network(err) {
      errorMessage = "Network error: \(err.localizedDescription)"
    } catch let APIError.http(code, data) {
      let msg = String(data: data, encoding: .utf8) ?? ""
      errorMessage = "Server \(code): \(msg)"
    } catch let APIError.jsonDecoding(err) {
      errorMessage = "Response parsing error: \(err.localizedDescription)"
    } catch {
      errorMessage = error.localizedDescription
    }
  }
}
