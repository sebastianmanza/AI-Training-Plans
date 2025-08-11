import SwiftUI

@MainActor
class HomeViewModel: ObservableObject {
  @Published var homeData: HomeData?
  @Published var errorMessage: String?

  func load() async {
    // print("[HomeViewModel] load() called")
    do {
      homeData = try await APIClient.shared.fetchHomeData()
    } catch {
      errorMessage = error.localizedDescription
    }
  }
}
