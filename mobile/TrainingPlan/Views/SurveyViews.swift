import SwiftUI

let numQuestions: CGFloat = 10

struct SurveyViews: View {
  @StateObject private var vm = SurveyViewModel()
  @State private var currentStep: Step = .introPage
  let onSurveyComplete: () -> Void

  enum Step {
    case introPage
    case dateOfBirth
    case sex
    case experience
    case daysPerWeek
    case daysOfWeek
    case mostTimeDay
    case current5k
    case majorInjuries
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
          //Task { await vm.submit() }
        }

      case .dateOfBirth:
        DatePage(label: "Date of Birth", date: $dobDate) {
          vm.dateOfBirth = dobFormatter.string(from: dobDate)  // convert to string
          currentStep = .sex
        }

      case .sex:
        SexPage(
          label: "Sex",
          selection: $vm.sex,
          options: ["Male", "Female", "Other"]
        ) {
          currentStep = .experience
        }

      case .experience:
        ExperiencePage(
          label: "Experience",
          selection: $vm.experience,
          options: ["Intermediate", "Advanced"]
        ) {
          currentStep = .daysPerWeek
        }
      case .daysPerWeek:
        DaysPerWeekPage(
          label: "Days per week",
          selection: $vm.daysPerWeek,
          options: [5, 6, 7]
        ) {
          currentStep = .daysOfWeek
        }

      case .daysOfWeek:
        DaysOfWeekPage(
          label: "Days of week",
          selection: $vm.daysOfWeek,
          options: ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        ) {
          currentStep = .mostTimeDay
        }

      case .mostTimeDay:
        MostTimeDayPage(
          label: "Most time of day",
          selection: $vm.mostTimeDay,
          options: ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        ) {
          currentStep = .current5k
        }

      case .current5k:
        Current5KPage(
          label: "Current 5K fitness",
          totalSeconds: $vm.current5k
        ) {
          currentStep = .majorInjuries
        }

      case .majorInjuries:
        MajorInjuriesPage(
          label: "Major injuries",
          selection: $vm.majorInjuries,
          options: ["0", "1-2", "3+"]
        ) {
          onSurveyComplete()
          // currentStep = .recentInjury
        }

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

  let onStartTapped: () -> Void

  var body: some View {
    ZStack {
        
      Color(red: 20 / 255, green: 18 / 255, blue: 50 / 255)
            .ignoresSafeArea()
        
      LinearGradient(
        gradient: Gradient(stops: [
            .init(color: Color(red:   0/255, green: 106/255, blue: 255/255), location: 0.0),
            .init(color: Color(red:   0/255, green: 226/255, blue: 188/255).opacity(0.2), location: 0.55),
            .init(color: Color(red:   0/255, green: 226/255, blue: 188/255).opacity(0), location: 0.7)
        ]),
        startPoint: .top,
        endPoint: .bottom
      )
      .ignoresSafeArea()

      // Overlay with content
      Spacer()
      VStack(alignment: .leading, spacing: 45) {
        // Top text
        VStack(alignment: .leading, spacing: -15) {
          Text("READY TO").font(.custom("MADEOkineSansPERSONALUSE-Bold", size: 48))
            .foregroundColor(.white)
          Text("START").font(.custom("MADEOkineSansPERSONALUSE-Bold", size: 48))
            .foregroundColor(.white)
          Text("YOUR").font(.custom("MADEOkineSansPERSONALUSE-Medium", size: 48))
            .foregroundColor(.white)
          Text("RUNNING").font(.custom("MADEOkineSansPERSONALUSE-Bold", size: 48))
            .foregroundColor(.white)
          Text("JOURNEY?").font(.custom("MADEOkineSansPERSONALUSE-Bold", size: 48))
            .foregroundColor(.white)
        }

        Rectangle()
          .fill(Color.white)
          .frame(height: 1.5)
          .frame(maxWidth: .infinity)
          .padding(.trailing, 35)

        Text(
          """
          Help us get a sense of 
          where you're at. Take 
          the survey to start your
          personalized training
          plan.
          """
        )
        .font(.custom("MADEOkineSansPERSONALUSE-Regular", size: 24))
        .foregroundColor(.white)

        LogInButton(
          buttonTitle: "START", action: onStartTapped,
          color: Color(red: 0, green: 54 / 255, blue: 104 / 255)
        )
        .padding(.leading, 35)
        .padding(.top, 25)

      }
      .padding(.leading, 35)
      .padding(.bottom, 10)
      .frame(maxWidth: .infinity, maxHeight: .infinity, alignment: .leading)
      Spacer()
    }
  }
}

struct DatePage: View {
  let label: String
  @Binding var date: Date
  let onNext: () -> Void

  var body: some View {
    ZStack {
      Image("surveyQuestionBackground")
        .resizable()
        .scaledToFill()
        .edgesIgnoringSafeArea(.all)

      // foreground
      VStack(spacing: 40) {
        Text("When were \nyou born?")
          .font(.custom("MADEOkineSansPERSONALUSE-Bold", size: 48))
          .foregroundColor(.white)
          .multilineTextAlignment(.leading)
          .frame(maxWidth: .infinity, alignment: .leading)
          .padding(.leading, 30)

        Rectangle()
          .fill(.white)
          .frame(height: 1.5)
          .frame(maxWidth: .infinity)
          .padding(.horizontal, 30)

        DatePicker("", selection: $date, displayedComponents: .date)
          .datePickerStyle(WheelDatePickerStyle())
          .labelsHidden()
          .colorScheme(.dark)
          .cornerRadius(8)

        SurveyNextButton(
          action: onNext, color: Color(red: 0 / 255, green: 54 / 255, blue: 104 / 255)
        )
        .padding(.top, 30)
        CompletionBar(
          background: .white, fill: Color(red: 0, green: 54 / 255, blue: 104 / 255), width: 350,
          height: 15, percentComplete: 1 / (numQuestions)
        )
        .padding(.top, 10)

      }
      .frame(maxWidth: .infinity, maxHeight: .infinity, alignment: .bottom)
      .padding(.bottom, 80)
    }
  }
}

struct SexPage: View {
  let label: String
  @Binding var selection: String
  let options: [String]
  let onNext: () -> Void

  @State private var isEditingOther = false
  @State private var otherText = ""
  @FocusState private var otherFieldFocused: Bool
  @State private var keyboardHeight: CGFloat = 0

  private let themeColor = Color(red: 40 / 255, green: 40 / 255, blue: 40 / 255)

  var body: some View {
    ZStack {
      Image("surveyQuestionBackground")
        .resizable()
        .scaledToFill()
        .edgesIgnoringSafeArea(.all)
        .onTapGesture {
          if isEditingOther {
            selection = otherText
          }
          otherFieldFocused = false
          isEditingOther = false
        }

      VStack(spacing: 40) {
        /* If other is not being edited, show the fields */
        if !isEditingOther {
          Text("How do you identify?")
            .font(.custom("MADEOkineSansPERSONALUSE-Bold", size: 48))
            .foregroundColor(.white)
            .frame(maxWidth: .infinity, alignment: .leading)
            .padding(.leading, 30)

          Rectangle()
            .fill(Color.white)
            .frame(height: 1.5)
            .frame(maxWidth: .infinity)
            .padding(.horizontal, 30)
        }

        VStack(spacing: 10) {
          if isEditingOther {
            // inline text field, styled just like the selected button
            TextField("Please specify:", text: $otherText)
              .focused($otherFieldFocused)
              .multilineTextAlignment(.center)
              .font(.custom("MADEOkineSansPERSONALUSE-Regular", size: 20))
              .foregroundColor(.white)
              .frame(minWidth: 300, minHeight: 70)
              .background(
                RoundedRectangle(cornerRadius: 20, style: .continuous)
                  .fill(themeColor)
              )
              .overlay(
                RoundedRectangle(cornerRadius: 20, style: .continuous)
                  .stroke(Color.white, lineWidth: 2)
              )
              // slide up when keyboard appears
              .padding(.bottom, keyboardHeight)

          } else {
            // show only Male/Female/Other buttons
            ForEach(options, id: \.self) { option in
              if option == "Other" {
                let isCustom = (!selection.isEmpty && selection != "Male" && selection != "Female")
                let title = isCustom ? selection : "Other"
                SurveySelectionButton(
                  title: title,
                  isSelected: isCustom,
                  height: 70
                ) {
                  isEditingOther = true
                  otherText = isCustom ? selection : ""
                }
              } else {
                SurveySelectionButton(
                  title: option,
                  isSelected: selection == option,
                  height: 70
                ) {
                  selection = option
                  otherText = ""
                }
              }
            }
          }
        }

        SurveyNextButton(
          action: {
            // when Next tapped, if in Other-mode commit the text
            if isEditingOther {
              selection = otherText
            }
            onNext()
          }, color: Color(red: 0, green: 54 / 255, blue: 104 / 255)
        )
        .padding(.top, 30)

        CompletionBar(
          background: .white,
          fill: Color(red: 0, green: 54 / 255, blue: 104 / 255),
          width: 350,
          height: 15,
          percentComplete: 2 / numQuestions
        )
        .padding(.top, 10)
      }
      .frame(maxWidth: .infinity, maxHeight: .infinity, alignment: .bottom)
      .padding(.bottom, 80)

      // keyboard height listeners
      .onReceive(
        NotificationCenter.default
          .publisher(for: UIResponder.keyboardWillShowNotification)
      ) { note in
        if let r = note.userInfo?[UIResponder.keyboardFrameEndUserInfoKey] as? CGRect {
          keyboardHeight = r.height - 50
        }
      }
      .onReceive(
        NotificationCenter.default
          .publisher(for: UIResponder.keyboardWillHideNotification)
      ) { _ in
        keyboardHeight = 0
      }
    }
  }
}

struct ExperiencePage: View {
  let label: String
  @Binding var selection: String
  let options: [String]
  let onNext: () -> Void

  private let themeColor = Color(red: 40 / 255, green: 40 / 255, blue: 40 / 255)

  var body: some View {
    ZStack {
      Image("surveyQuestionBackground")
        .resizable()
        .scaledToFill()
        .edgesIgnoringSafeArea(.all)

      VStack(spacing: 40) {
        Text("What is your \ncurrent level \nof running \nexperience?")
          .font(.custom("MADEOkineSansPERSONALUSE-Bold", size: 48))
          .foregroundColor(.white)
          .frame(maxWidth: .infinity, alignment: .leading)
          .padding(.leading, 30)

        Rectangle()
          .fill(Color.white)
          .frame(height: 1.5)
          .frame(maxWidth: .infinity)
          .padding(.horizontal, 30)

        VStack(spacing: 10) {
          ForEach(options, id: \.self) { option in
            SurveySelectionButton(
              title: option,
              isSelected: selection == option,
              height: 80
            ) {
              selection = option
            }
          }
        }
        SurveyNextButton(
          action: onNext, color: Color(red: 0 / 255, green: 54 / 255, blue: 104 / 255)
        )
        .padding(.top, 30)
        CompletionBar(
          background: .white, fill: Color(red: 0, green: 54 / 255, blue: 104 / 255), width: 350,
          height: 15, percentComplete: 3 / (numQuestions)
        )
        .padding(.top, 10)
      }
      .frame(maxWidth: .infinity, maxHeight: .infinity, alignment: .bottom)
      .padding(.bottom, 80)
    }
  }
}

struct DaysPerWeekPage: View {
  let label: String
  @Binding var selection: Int
  let options: [Int]
  let onNext: () -> Void

  private let themeColor = Color(red: 40 / 255, green: 40 / 255, blue: 40 / 255)

  var body: some View {
    ZStack {
      Image("surveyQuestionBackground")
        .resizable()
        .scaledToFill()
        .edgesIgnoringSafeArea(.all)

      VStack(spacing: 40) {
        Text("How many \ndays per week \nwould you like \n to run?")
          .font(.custom("MADEOkineSansPERSONALUSE-Bold", size: 48))
          .foregroundColor(.white)
          .frame(maxWidth: .infinity, alignment: .leading)
          .padding(.leading, 30)

        Rectangle()
          .fill(Color.white)
          .frame(height: 1.5)
          .frame(maxWidth: .infinity)
          .padding(.horizontal, 30)

        VStack(spacing: 10) {
          ForEach(options, id: \.self) { option in
            SurveySelectionButton(
              title: String(option),
              isSelected: selection == option,
              height: 70
            ) {
              selection = option
            }
          }
        }
        SurveyNextButton(
          action: onNext, color: Color(red: 0 / 255, green: 54 / 255, blue: 104 / 255)
        )
        .padding(.top, 20)
        CompletionBar(
          background: .white, fill: Color(red: 0, green: 54 / 255, blue: 104 / 255), width: 350,
          height: 15, percentComplete: 4 / (numQuestions)
        )
        .padding(.top, 10)
      }
      .frame(maxWidth: .infinity, maxHeight: .infinity, alignment: .bottom)
      .padding(.bottom, 80)
    }
  }
}

struct DaysOfWeekPage: View {
  let label: String
  @Binding var selection: [String]
  let options: [String]
  let onNext: () -> Void

  private let themeColor = Color(red: 40 / 255, green: 40 / 255, blue: 40 / 255)

  var body: some View {
    ZStack {
      Image("surveyQuestionBackground")
        .resizable()
        .scaledToFill()
        .edgesIgnoringSafeArea(.all)

      VStack(spacing: 40) {
        Text("What days of the \nweek can you \ncommit at least \nan hour for a run?")
          .font(.custom("MADEOkineSansPERSONALUSE-Bold", size: 36))
          .foregroundColor(.white)
          .frame(maxWidth: .infinity, alignment: .leading)
          .padding(.leading, 30)

        Rectangle()
          .fill(Color.white)
          .frame(height: 1.5)
          .frame(maxWidth: .infinity)
          .padding(.horizontal, 30)

        VStack(spacing: 10) {
          ForEach(options, id: \.self) { option in
            SurveySelectionButton(
              title: String(option),
              isSelected: selection.contains(option),
              height: 35
            ) {
              if let i = selection.firstIndex(of: option) {
                selection.remove(at: i)
              } else {
                selection.append(option)
              }
            }
          }
        }
        SurveyNextButton(
          action: onNext, color: Color(red: 0 / 255, green: 54 / 255, blue: 104 / 255)
        )
        // .padding(.top, 10)
        CompletionBar(
          background: .white, fill: Color(red: 0, green: 54 / 255, blue: 104 / 255), width: 350,
          height: 15, percentComplete: 5 / (numQuestions)
        )
        .padding(.top, 10)
      }
      .frame(maxWidth: .infinity, maxHeight: .infinity, alignment: .bottom)
      .padding(.bottom, 80)
    }
  }
}

struct MostTimeDayPage: View {
  let label: String
  @Binding var selection: String
  let options: [String]
  let onNext: () -> Void

  private let themeColor = Color(red: 40 / 255, green: 40 / 255, blue: 40 / 255)

  var body: some View {
    ZStack {
      Image("surveyQuestionBackground")
        .resizable()
        .scaledToFill()
        .edgesIgnoringSafeArea(.all)

      VStack(spacing: 40) {
        Text("What day do\nyou have the\nmost time for\na run?")
          .font(.custom("MADEOkineSansPERSONALUSE-Bold", size: 36))
          .foregroundColor(.white)
          .frame(maxWidth: .infinity, alignment: .leading)
          .padding(.leading, 30)

        Rectangle()
          .fill(Color.white)
          .frame(height: 1.5)
          .frame(maxWidth: .infinity)
          .padding(.horizontal, 30)

        VStack(spacing: 10) {
          ForEach(options, id: \.self) { option in
            SurveySelectionButton(
              title: String(option),
              isSelected: selection == option,
              height: 35
            ) {
              selection = option
            }
          }
        }
        SurveyNextButton(
          action: onNext, color: Color(red: 0 / 255, green: 54 / 255, blue: 104 / 255)
        )
        // .padding(.top, 10)
        CompletionBar(
          background: .white, fill: Color(red: 0, green: 54 / 255, blue: 104 / 255), width: 350,
          height: 15, percentComplete: 6 / (numQuestions)
        )
        .padding(.top, 10)
      }
      .frame(maxWidth: .infinity, maxHeight: .infinity, alignment: .bottom)
      .padding(.bottom, 80)
    }
  }
}

struct Current5KPage: View {

  let label: String
  // the total number of seconds of the 5k
  @Binding var totalSeconds: Int
  let onNext: () -> Void

  /// Local state for the two wheels
  @State private var minutes: Int = 0
  @State private var seconds: Int = 0

  private let maxMinutes = 59
  private let maxSeconds = 59

  private var minuteWheel: some View {
    Picker("", selection: $minutes) {
      ForEach(12...maxMinutes, id: \.self) { v in
        Text(String(format: "%02d", v))
          .font(.custom("MADEOkineSansPERSONALUSE-Bold", size: 25))
          .foregroundColor(.white)
          .tag(v)
      }
    }
    .pickerStyle(.wheel)
    .buttonStyle(.borderless)
    .scaleEffect(2)
    .frame(width: 100, height: 60)
    .clipped()
  }

  // 2) And the second‐wheel too
  private var secondWheel: some View {
    Picker("", selection: $seconds) {
      ForEach(0...maxSeconds, id: \.self) { v in
        Text(String(format: "%02d", v))
          .font(.custom("MADEOkineSansPERSONALUSE-Bold", size: 25))
          .foregroundColor(.white)
          .tag(v)
      }
    }
    .background(.gray.opacity(0))
    .pickerStyle(.wheel)
    .buttonStyle(.borderless)
    .scaleEffect(2)
    .frame(width: 100, height: 60)
    .clipped()
  }

  var body: some View {
    ZStack {
      Image("surveyQuestionBackground")
        .resizable()
        .scaledToFill()
        .edgesIgnoringSafeArea(.all)

      // foreground
      VStack(spacing: 40) {
        Text("What is your \ncurrent \nestimated 5k \nfitness?")
          .font(.custom("MADEOkineSansPERSONALUSE-Bold", size: 48))
          .foregroundColor(.white)
          .multilineTextAlignment(.leading)
          .frame(maxWidth: .infinity, alignment: .leading)
          .padding(.leading, 30)

        Rectangle()
          .fill(.white)
          .frame(height: 1.5)
          .frame(maxWidth: .infinity)
          .padding(.horizontal, 30)

        HStack(spacing: 0) {
          minuteWheel

          Text(":")
            .font(.custom("MADEOkineSansPERSONALUSE-Bold", size: 60))
            .foregroundColor(.white)
            .frame(width: 30)
          secondWheel
        }
        .frame(maxWidth: .infinity)

        SurveyNextButton(
          action: {
            totalSeconds = minutes * 60 + seconds
            onNext()
          },
          color: Color(red: 0 / 255, green: 54 / 255, blue: 104 / 255)
        )
        .padding(.top, 75)
        CompletionBar(
          background: .white, fill: Color(red: 0, green: 54 / 255, blue: 104 / 255), width: 350,
          height: 15, percentComplete: 7 / (numQuestions)
        )
        .padding(.top, 10)

      }
      .frame(maxWidth: .infinity, maxHeight: .infinity, alignment: .bottom)
      .padding(.bottom, 80)

      .onAppear {
        minutes = totalSeconds / 60
        seconds = totalSeconds % 60
      }
      // 6) Keep binding live if wheel spins before Next
      .onChange(of: minutes) { newMin in
        totalSeconds = newMin * 60 + seconds
      }
      .onChange(of: seconds) { newSec in
        totalSeconds = minutes * 60 + newSec
      }
    }
  }
}

struct MajorInjuriesPage: View {
  let label: String
  @Binding var selection: String
  let options: [String]
  let onNext: () -> Void

  private let themeColor = Color(red: 40 / 255, green: 40 / 255, blue: 40 / 255)

  var body: some View {
    ZStack {
      Image("surveyQuestionBackground")
        .resizable()
        .scaledToFill()
        .edgesIgnoringSafeArea(.all)

      VStack(spacing: 40) {
        Text("How many major \ninjuries have you \nhad in the past 2 \nyears?")
          .font(.custom("MADEOkineSansPERSONALUSE-Bold", size: 36))
          .foregroundColor(.white)
          .frame(maxWidth: .infinity, alignment: .leading)
          .padding(.leading, 30)

        Rectangle()
          .fill(Color.white)
          .frame(height: 1.5)
          .frame(maxWidth: .infinity)
          .padding(.horizontal, 30)

        VStack(spacing: 10) {
          ForEach(options, id: \.self) { option in
            SurveySelectionButton(
              title: String(option),
              isSelected: selection == option,
              height: 70
            ) {
              selection = option
            }
          }
        }
        SurveyNextButton(
          action: onNext, color: Color(red: 0 / 255, green: 54 / 255, blue: 104 / 255)
        )
        .padding(.top, 20)
        CompletionBar(
          background: .white, fill: Color(red: 0, green: 54 / 255, blue: 104 / 255), width: 350,
          height: 15, percentComplete: 8 / (numQuestions)
        )
        .padding(.top, 10)
      }
      .frame(maxWidth: .infinity, maxHeight: .infinity, alignment: .bottom)
      .padding(.bottom, 80)
    }
  }
}
