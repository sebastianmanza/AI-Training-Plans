import SwiftUI

@MainActor
class HomeViewModel: ObservableObject {
  @Published var homeData: HomeData?
  @Published var errorMessage: String?

  func load(session: Session) async {
    // print("[HomeViewModel] load() called")
    do {
      homeData = try await APIClient.shared.fetchHomeData(session: session)
    } catch {
      errorMessage = error.localizedDescription
    }
  }
}
