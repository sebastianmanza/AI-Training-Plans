import Combine
import Foundation

final class Session: ObservableObject {
  @Published var userID: Int? {
    didSet {
      UserDefaults.standard.set(userID, forKey: "userID")
    }
  }

  init() {
    let stored = UserDefaults.standard.integer(forKey: "userID")
    self.userID = stored == 0 ? nil : stored
  }

  func setUserID(_ id: Int) {
    self.userID = id
  }

  func signOut() {
    self.userID = nil
  }
}
