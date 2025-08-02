import Foundation

@MainActor
class SurveyViewModel: ObservableObject {
  // MARK: – Form fields
  @Published var userID: Int = 0
  @Published var dateOfBirth: String = ""  // "YYYY-MM-DD"
  @Published var sex: String = ""  // "Male" / "Female" / …
  @Published var experience: String = ""  // "Beginner" / "Advanced" / …
  @Published var majorInjuries: Int = 0
  @Published var recentInjury: Int = 0
  @Published var longestRun: Int = 0  // in miles
  @Published var goalDate: String = ""  // "YYYY-MM-DD"
  @Published var daysPerWeek: Int = 0
  @Published var daysOfWeek: [String] = []  // ["Mon","Wed","Fri"]
  @Published var mostTimeDay: String = ""  // e.g. "Morning"
  @Published var current5k: Int = 0  // 5k estimate in seconds

  // MARK: – UI state
  @Published var isSubmitting: Bool = false
  @Published var response: [String: Any]? = nil
  @Published var errorMessage: String? = nil

  func submit() async {
    errorMessage = nil
    isSubmitting = true
    defer { isSubmitting = false }

    // Build the payload matching FastAPI SurveyIn model:
    let survey = SurveyIn(
      user_id: userID,
      date_of_birth: dateOfBirth,
      sex: sex,
      running_experience: experience,
      major_injuries: majorInjuries,
      most_recent_injury: recentInjury,
      longest_run: longestRun,
      goal_date: goalDate,
      days_per_week: daysPerWeek,
      days_of_week: daysOfWeek,
      most_time_day: mostTimeDay,
      current_5k_fitness: current5k
    )

    do {
      let result = try await APIClient.shared.submitPrelim(survey)
      response = result
    } catch APIError.badURL {
      errorMessage = "Invalid server URL."
    } catch APIError.network(let err) {
      errorMessage = "Network error: \(err.localizedDescription)"
    } catch APIError.http(let code, let data) {
      let msg = String(data: data, encoding: .utf8) ?? "Unknown error"
      errorMessage = "Server \(code): \(msg)"
    } catch APIError.jsonDecoding(let err) {
      errorMessage = "Parsing error: \(err.localizedDescription)"
    } catch {
      errorMessage = error.localizedDescription
    }
  }
}
