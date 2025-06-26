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
    @State private var started = false

    /* Main App */
    var body: some Scene {
        WindowGroup {
            if started {
                UpdatedSurveyView()
            } else {
                StartView { started = true }
            }
        }
    }
}
