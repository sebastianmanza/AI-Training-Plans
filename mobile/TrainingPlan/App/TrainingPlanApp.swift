//
//  TrainingPlanApp.swift
//  TrainingPlan
//
//  Created by Sebastian Manza on 6/25/25.
//

import SwiftUI

@main
struct TrainingPlanApp: App {
    /* Check if the start screen has been seen */
    @StateObject private var appState = AppScreens()

    /* Main App */
    var body: some Scene {
        WindowGroup {
            NavigationStack {
                switch appState.currentScreen {
                case .start:
                    StartView(
                        onSignUpTapped: {
                            appState.currentScreen = .signup
                        },
                        onLogInTapped: {
                            appState.currentScreen = .login 
                        }
                    )
                case .signup:
                    SignUpView (
                        onSignUpDone: {
                            appState.currentScreen = .survey
                        },
                        onLogInTapped: {
                            appState.currentScreen = .login
                        }
                    )
                case .login:
                    LoginView(
                        onLoginDone: {
                            appState.currentScreen = .survey
                        },
                        onSignUpTapped: {
                            appState.currentScreen = .signup
                        }
                    )
                case .survey:
                    UpdatedSurveyView{
                        appState.currentScreen = .start
                    }
                }
            }
            .environmentObject(appState) // Pass the app state to the environment
        }
    }
}
