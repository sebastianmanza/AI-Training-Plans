import SwiftUI

let numQuestions: CGFloat = 11

struct SurveyViews: View {
 @StateObject private var vm = SurveyViewModel()
 @State private var currentStep: Step = .introPage
 let onSurveyComplete: () -> Void

    
 enum Step {
   case introPage
   case dateOfBirth
   //case sex
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
           //Task { await vm.submit() }
         }

       case .dateOfBirth:
         DatePage(label: "Date of Birth", date: $dobDate) {
           vm.dateOfBirth = dobFormatter.string(from: dobDate) // convert to string
           onSurveyComplete()
         }

      //  case .sex:
      //    SexPage(
      //      label: "Sex?",
      //      selection: $vm.sex,
      //      options: ["Male", "Female", "Other"]
      //    ) {
      //      // currentStep = .experience
      //      Task { await vm.submit() }
      //    }

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

 let onStartTapped: ()->Void

 var body: some View {
   ZStack() {
    //Background for survey
    Image("surveyBackground")
      .resizable() 
      .scaledToFill() 
      .edgesIgnoringSafeArea(.all) 

    // Overlay with content
      Spacer()
      VStack(alignment: .leading, spacing: 45) {
        // Top text
        VStack(alignment: .leading, spacing: -15){
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

        Text("""
              Help us get a sense of 
              where you're at. Take 
              the survey to start your
              personalized training
              plan.
              """)
          .font(.custom("MADEOkineSansPERSONALUSE-Regular", size: 24))
          .foregroundColor(.white)
        
        LogInButton(buttonTitle: "START", action: onStartTapped, color: Color(red: 0, green: 54/255, blue: 104/255))
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
 let onNext: ()->Void

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

      SurveyButton(action: onNext, color: Color(red: 0/255, green: 54/255, blue: 104/255))
        .padding(.top, 30)
      CompletionBar(background: .white, fill: Color(red: 0, green: 54/255, blue: 104/255), width: 350, height: 15, percentComplete: 1/(numQuestions))
        .padding(.top, 10)
       
      }
      .frame(maxWidth: .infinity, maxHeight: .infinity, alignment: .bottom)
      .padding(.bottom, 80)
    }
  }
}

// struct SexPage: View {
//  let label: String
//  @Binding var selection: String
//  let options: [String]
//  let onNext: ()->Void

//  var body: some View {
//    ZStack {
//      Color.black.ignoresSafeArea()

//      VStack(spacing: 40) {
//        Text(label)
//          .font(.title2)
//          .foregroundColor(.white)

//        Picker(label, selection: $selection) {
//          ForEach(options, id: \.self) { option in
//            Text(option).tag(option)
//          }
//        }
//        .pickerStyle(.segmented)
//        .padding(.horizontal)
//        .accentColor(.white)
//        .background(Color(.darkGray))

//        Button("Next") {
//          onNext()
//        }
//        .buttonStyle(BasicButton())
//      }
//      .frame(maxWidth: .infinity, maxHeight: .infinity, alignment: .center)
//    }
//  }
// }


// struct SurveyView: View {
//  @StateObject private var vm = SurveyViewModel()

//  var body: some View {
//    NavigationView {
//      Form {
//        Section("Basic Info") {
//          TextField("Date of Birth (YYYY-MM-DD)", text: $vm.dateOfBirth)
//          TextField("Sex", text: $vm.sex)
//          TextField("Experience (e.g. “5 years”)", text: $vm.experience)
//        }

//        Section("Training Habits") {
//          Stepper("Days per week: \(vm.daysPerWeek)", value: $vm.daysPerWeek, in: 1...7)
//          TextField("Days of week (comma-sep)", text: $vm.daysOfWeekText)
//          TextField("Time of day most train", text: $vm.mostTimeDay)
//          HStack {
//            Text("5K fitness (min)")
//            TextField("e.g. 20.5", value: $vm.current5k, format: .number)
//              .keyboardType(.decimalPad)
//          }
//        }

//        Section("Injuries") {
//          TextField("Major injuries", text: $vm.majorInjuries)
//          TextField("Most recent injury", text: $vm.recentInjury)
//        }

//        Section {
//          Button {
//            Task { await vm.submit() }
//          } label: {
//            if vm.isSubmitting {
//              ProgressView()
//            } else {
//              Text("Submit Survey")
//            }
//          }
//          .disabled(vm.isSubmitting)
//        }

//        if let resp = vm.response {
//          Section("Response") {
//            ForEach(resp.keys.sorted(), id: \.self) { key in
//              Text("\(key): \(String(describing: resp[key]!))")
//                .font(.caption)
//            }
//          }
//        }

//        if let err = vm.errorMessage {
//          Section {
//            Text(err)
//              .foregroundColor(.red)
//          }
//        }
//      }
//      .navigationTitle("Prelim Survey")
//    }
//  }
// }
