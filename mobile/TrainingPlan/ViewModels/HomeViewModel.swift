import SwiftUI
import os

@MainActor
class HomeViewModel: ObservableObject {
  @Published var homeData: HomeData?
  @Published var errorMessage: String?
  private let logger = Logger(subsystem: "com.ai.trainingplans", category: "HomeViewModel")

  func load(session: Session) async {
    logger.debug("load() called")
    do {
      homeData = try await APIClient.shared.fetchHomeData(session: session)
      logger.info("Loaded home data")
    } catch {
      errorMessage = error.localizedDescription
      logger.error("Failed to load home data: \(error.localizedDescription)")
    }
  }
}
