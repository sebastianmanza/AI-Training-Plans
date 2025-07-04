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
                    SurveyViews(
                        onSurveyComplete: {
                            appState.currentScreen = .home // Go back to start after survey
                        }
                    ) //Placeholder

                case .home:
                    HomeView(
                        onCompleted: {
                            appState.currentScreen = .start // Placeholder for next action
                        },
                        onDidNotComplete: {
                            appState.currentScreen = .start
                        },
                        onQuestionMark: {
                            appState.currentScreen = .start
                        },
                        onCalendarTapped: {
                            appState.currentScreen = .start // Placeholder for calendar action
                        },
                        onProfileTapped: {
                            appState.currentScreen = .start // Placeholder for profile action
                        })
                }
            }
            .environmentObject(appState) // Pass the app state to the environment
        }
    }
}
