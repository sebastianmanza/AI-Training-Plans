import SwiftUI

struct BasicButton: ButtonStyle {
  func makeBody(configuration: Configuration) -> some View {
    configuration.label
      .font(.headline)
      .foregroundColor(.white)
      .padding(.horizontal, 24)
      .padding(.vertical, 12)
      .background(Color(.darkGray))
      .cornerRadius(8)
      .opacity(configuration.isPressed ? 0.7 : 1)
  }
}

struct DateWheelPicker: View {
    @Binding var date: Date

    private let years  = Array(1900...Calendar.current.component(.year, from: Date()))
    private let months = Array(1...12)
    private let days   = Array(1...31)
    private let monthNames = Calendar.current.monthSymbols

    @State private var selectedYear: Int  = Calendar.current.component(.year, from: Date())
    @State private var selectedMonth: Int = Calendar.current.component(.month, from: Date())
    @State private var selectedDay: Int   = Calendar.current.component(.day, from: Date())

    // Which component’s sheet is showing?
    @State private var editing: Component?

    enum Component: String, Identifiable {
        case year, month, day
        var id: String { rawValue }
    }

    var body: some View {
        HStack(spacing: 16) {
            componentBox(label: "\(selectedYear)", .year)
            componentBox(label: monthNames[selectedMonth-1], .month)
            componentBox(label: "\(selectedDay)", .day)
        }
        .padding()
        .background(Color(.darkGray))
        .cornerRadius(12)
        .onAppear { syncFromDate() }
        .sheet(item: $editing) { item in
            wheelSheet(for: item)
        }
    }

    // A small box showing the current value
    private func componentBox(label: String, _ comp: Component) -> some View {
        Button {
            editing = comp
        } label: {
            Text(label)
              .font(.title2).bold()
              .foregroundColor(.white)
              .frame(width: 80, height: 40)
              .background(Color(.black))
              .cornerRadius(8)
        }
        .buttonStyle(.plain)
    }

    // The sheet that pops up with the wheel for that component
    @ViewBuilder
    private func wheelSheet(for comp: Component) -> some View {
        VStack(spacing: 20) {
            Text(title(for: comp))
              .font(.headline)
            Picker("", selection: binding(for: comp)) {
                switch comp {
                case .year:
                    ForEach(years, id: \.self) { Text("\($0)").tag($0) }
                case .month:
                    ForEach(0..<monthNames.count, id: \.self) {
                        Text(monthNames[$0]).tag($0+1)
                    }
                case .day:
                    ForEach(days, id: \.self) { Text("\($0)").tag($0) }
                }
            }
            .pickerStyle(.wheel)
            .labelsHidden()
            .frame(maxHeight: 200)

            Button("Done") {
                editing = nil
                syncDate()
            }
            .buttonStyle(.borderedProminent)
        }
        .padding()
        .background(Color.black.ignoresSafeArea())
    }

    private func title(for comp: Component) -> String {
        switch comp {
        case .year:  return "Select Year"
        case .month: return "Select Month"
        case .day:   return "Select Day"
        }
    }

    private func binding(for comp: Component) -> Binding<Int> {
        switch comp {
        case .year:  return $selectedYear
        case .month: return $selectedMonth
        case .day:   return $selectedDay
        }
    }

    // Combine back into the bound Date
    private func syncDate() {
        var comps = DateComponents()
        comps.year  = selectedYear
        comps.month = selectedMonth
        comps.day   = selectedDay
        if let new = Calendar.current.date(from: comps) {
            date = new
        }
    }

    // Seed the initial wheel states
    private func syncFromDate() {
        let comps = Calendar.current.dateComponents([.year, .month, .day], from: date)
        selectedYear  = comps.year  ?? selectedYear
        selectedMonth = comps.month ?? selectedMonth
        selectedDay   = comps.day   ?? selectedDay
    }
}


struct UpdatedSurveyView: View {
  @StateObject private var vm = SurveyViewModel()
  @State private var currentStep: Step = .introPage

  enum Step {
    case introPage
    case dateOfBirth
    case sex
//    case experience
//    case daysPerWeek
//    case daysOfWeek
//    case mostTimeDay
//    case current5k
//    case majorInjuries
//    case recentInjury
  }

  private let dobFormatter: DateFormatter = {
    let formatter = DateFormatter()
    formatter.dateFormat = "yyyy-MM-dd"
    return formatter
  }()

  @State private var dobDate: Date = Date()

  var body: some View {
    VStack {
      switch currentStep {
        case .introPage:
          IntroPage {
            /* Advance to next page */
            currentStep = .dateOfBirth
          }

        case .dateOfBirth:
          DatePage(label: "Date of Birth", date: $dobDate) {
            vm.dateOfBirth = dobFormatter.string(from: dobDate) // convert to string
            currentStep = .sex
          }

        case .sex:
          SexPage(
            label: "Sex?",
            selection: $vm.sex,
            options: ["Male", "Female", "Other"]
          ) {
            // currentStep = .experience
            Task { await vm.submit() }
          }

        // case .experience:
        //   ExperiencePage(
        //     label: "Experience",
        //     text: $vm.experience
        //   ) {
        //     currentStep = .daysPerWeek
        //   }

        // case .daysPerWeek:
        //   DaysPerWeekPage(
        //     label: "Days per week",
        //     value: $vm.daysPerWeek
        //   ) {
        //     currentStep = .daysOfWeek
        //   }

        // case .daysOfWeek:
        //   DaysOfWeekPage(
        //     label: "Days of week",
        //     text: $vm.daysOfWeekText
        //   ) {
        //     currentStep = .mostTimeDay
        //   }

        // case .mostTimeDay:
        //   MostTimeDayPage(
        //     label: "Most time of day",
        //     text: $vm.mostTimeDay
        //   ) {
        //     currentStep = .current5k
        //   }
        
        // case .current5k:
        //   Current5KPage(
        //     label: "Current 5K fitness",
        //     value: $vm.current5k
        //   ) {
        //     currentStep = .majorInjuries
        //   }

        // case .majorInjuries:
        //   MajorInjuriesPage(
        //     label: "Major injuries",
        //     text: $vm.majorInjuries
        //   ) {
        //     currentStep = .recentInjury
        //   }

        // case .recentInjury:
        //   RecentInjuryPage(
        //     label: "Most recent injury",
        //     text: $vm.recentInjury
        //   ) {
        //     Task { await vm.submit() }
        //   }

      }
    }
  }
}

struct IntroPage: View {

  let onNext: ()->Void

  var body: some View {
    ZStack {
      Color.black.ignoresSafeArea()
  
      VStack(spacing: 40) {
        Text("Please take this quick survey so we can personalize your training plan:")
              .font(.largeTitle)
          .foregroundColor(.white)
          .multilineTextAlignment(.center)

        Button("Go") { onNext() }
          .buttonStyle(BasicButton())
      }
      .frame(maxWidth: .infinity, maxHeight: .infinity, alignment: .center)
    }
  }
}

struct DatePage: View {
  let label: String
  @Binding var date: Date
  let onNext: ()->Void

  var body: some View {
    ZStack {
      Color.black.ignoresSafeArea()
  
      VStack(spacing: 40) {
        Text(label)
          .font(.title2)
          .foregroundColor(.white)

        DateWheelPicker(date: $date)

        Button("Next") { onNext() }
          .buttonStyle(BasicButton())
      }
      .frame(maxWidth: .infinity, maxHeight: .infinity, alignment: .center)
    }
  }
}

struct SexPage: View {
  let label: String
  @Binding var selection: String
  let options: [String]
  let onNext: ()->Void

  var body: some View {
    ZStack {
      Color.black.ignoresSafeArea()

      VStack(spacing: 40) {
        Text(label)
          .font(.title2)
          .foregroundColor(.white)

        Picker(label, selection: $selection) {
          ForEach(options, id: \.self) { option in
            Text(option).tag(option)
          }
        }
        .pickerStyle(.segmented)
        .padding(.horizontal)
        .accentColor(.white)
        .background(Color(.darkGray))

        Button("Next") {
          onNext()
        }
        .buttonStyle(BasicButton())
      }
      .frame(maxWidth: .infinity, maxHeight: .infinity, alignment: .center)
    }
  }
}


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
