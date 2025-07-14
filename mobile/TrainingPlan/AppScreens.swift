import SwiftUI

/* An enumeration of possible screens in the app */
enum currentView {
    case start
    case survey
    case signup
    case login
    case home
    case debugger
}

class AppScreens: ObservableObject {
    @Published var currentScreen: currentView = .debugger
}