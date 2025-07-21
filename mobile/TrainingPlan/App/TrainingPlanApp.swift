//
//  TrainingPlanApp.swift
//  TrainingPlan
//
//  Created by Sebastian Manza on 6/25/25.
//

import SwiftUI

@main
struct TrainingPlanApp: App {
  /* App State */
  @StateObject private var appState = AppScreens()
  /* Session info */
  @StateObject private var session = Session()

  /* Main App */
  var body: some Scene {
    WindowGroup {
      /* Main Navigation Stack */
      NavigationStack {
        switch appState.currentScreen {
        case .debugger:
          DebuggerView(
            onStartView: {
              appState.currentScreen = .start
            },
            onSignUpView: {
              appState.currentScreen = .signup
            },
            onLogInView: {
              appState.currentScreen = .login
            },
            onSurveyView: {
              appState.currentScreen = .survey
            },
            onHomeView: {
              appState.currentScreen = .home
            }
          )
        case .start:
          StartView(
            onSignUpTapped: {
              appState.currentScreen = .signup
            },
            onLogInTapped: {
              appState.currentScreen = .login
            },
            onDebugger: {
                appState.currentScreen = .debugger
            }
          )
        case .signup:
          SignUpView(
            onSignUpDone: {
              appState.currentScreen = .survey
            },
            onLogInTapped: {
              appState.currentScreen = .login
            },
            onDebugger: {
              appState.currentScreen = .debugger
            }
          )
        case .login:
          LoginView(
            onLoginDone: {
              appState.currentScreen = .home
            },
            onSignUpTapped: {
              appState.currentScreen = .signup
            },
            onDebugger: {
              appState.currentScreen = .debugger
            }
          )
        case .survey:
          SurveyViews(
            onSurveyComplete: {
              appState.currentScreen = .home  // Go back to start after survey
            }
          )  //Placeholder

        case .home:
          HomeView(
            onDidNotComplete: {
              appState.currentScreen = .home
            },
            onCalendarTapped: {
              appState.currentScreen = .start  // Placeholder for calendar action
            },
            onProfileTapped: {
              appState.currentScreen = .start  // Placeholder for profile action
            },
            onDebugger: {
              appState.currentScreen = .debugger
            })
        }
      }
      .environmentObject(appState)  // Pass the app state to the environment
      .environmentObject(session)  // Pass the session to the environment
      .task {
        /* Override the current screen if we have a userID */
        if session.userID != nil && appState.currentScreen == .start {
          appState.currentScreen = .home
        }
      }
    }
  }
}
