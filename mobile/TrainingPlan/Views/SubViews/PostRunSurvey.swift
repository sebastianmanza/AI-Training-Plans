import SwiftUI

struct PostRunSurvey: View {

  // @StateObject private var vm = PostRunViewModel()
  @State private var currentStep: Step = .rpe
  // let onSurveyComplete: () -> Void

  enum Step {
    case rpe
    //    case completionbool
    //    case completionquestions
  }

  var body: some View {
    VStack {
      switch currentStep {
      case .rpe:
        RPEView()
      //   case .completionbool:
      //     CompletionBoolView(onNext: {
      //       currentStep = .completionquestions
      //     })
      //      case .completionquestions:
      //     CompletionQuestionsView(onNext: {
      //       // Handle completion of the survey
      //       print("Survey completed")
      //})
      }
    }
  }

  struct RPEView: View {
    // var onNext: () -> Void

    var body: some View {
      ZStack {
        // Background gradient
        LinearGradient(
          gradient: Gradient(colors: [
            Color(red: 126 / 255, green: 247 / 255, blue: 209 / 255),
            Color(red: 217 / 255, green: 217 / 255, blue: 217 / 255),
            Color(red: 217/255, green: 217/255, blue: 217/255)
          ]),
          startPoint: .top,
          endPoint: .bottom
        )
        .ignoresSafeArea()

        // Foreground content
        VStack (spacing: 20) {
            @State private var rpeval: Double = 5
            Text("What was your \nRPE today?")
              .font(.custom("MADEOkineSansPERSONALUSE-Bold", size: 32))
              .foregroundColor(.black)
              .multilineTextAlignment(.leading)

            Text("\(rpeval, specifier: "%.1f")")
                .font(.custom("MADEOkineSansPERSONALUSE-Bold", size: 64))
                .foregroundColor(.black)



            
        }
      }
    }
  }
}
