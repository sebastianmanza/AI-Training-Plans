import SwiftUI

struct SurveyView: View {
  @StateObject private var vm = SurveyViewModel()

  var body: some View {
    NavigationView {
      Form {
        Section("Basic Info") {
          TextField("Date of Birth (YYYY-MM-DD)", text: $vm.dateOfBirth)
          TextField("Sex", text: $vm.sex)
          TextField("Experience (e.g. “5 years”)", text: $vm.experience)
        }

        Section("Training Habits") {
          Stepper("Days per week: \(vm.daysPerWeek)", value: $vm.daysPerWeek, in: 1...7)
          TextField("Days of week (comma-sep)", text: $vm.daysOfWeekText)
          TextField("Time of day most train", text: $vm.mostTimeDay)
          HStack {
            Text("5K fitness (min)")
            TextField("e.g. 20.5", value: $vm.current5k, format: .number)
              .keyboardType(.decimalPad)
          }
        }

        Section("Injuries") {
          TextField("Major injuries", text: $vm.majorInjuries)
          TextField("Most recent injury", text: $vm.recentInjury)
        }

        Section {
          Button {
            Task { await vm.submit() }
          } label: {
            if vm.isSubmitting {
              ProgressView()
            } else {
              Text("Submit Survey")
            }
          }
          .disabled(vm.isSubmitting)
        }

        if let resp = vm.response {
          Section("Response") {
            ForEach(resp.keys.sorted(), id: \.self) { key in
              Text("\(key): \(String(describing: resp[key]!))")
                .font(.caption)
            }
          }
        }

        if let err = vm.errorMessage {
          Section {
            Text(err)
              .foregroundColor(.red)
          }
        }
      }
      .navigationTitle("Prelim Survey")
    }
  }
}