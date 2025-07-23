import SwiftUI
import SwiftUIIntrospect

struct PostRunSurvey: View {

  // @StateObject private var vm = PostRunViewModel()
  @State private var currentStep: Step = .rpe
  @Binding var rpeval: Double
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
        RPEView(rpeval: $rpeval)
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
    @Binding var rpeval: Double

    var body: some View {
      ZStack {
        // Background gradient
        LinearGradient(
          gradient: Gradient(colors: [
            Color(red: 126 / 255, green: 247 / 255, blue: 209 / 255),
            Color(red: 217 / 255, green: 217 / 255, blue: 217 / 255),
            Color(red: 217 / 255, green: 217 / 255, blue: 217 / 255),
          ]),
          startPoint: .top,
          endPoint: .bottom
        )
        .ignoresSafeArea()

        // Foreground content
        VStack(spacing: 20) {

          Text("What was your \nRPE today?")
            .font(.custom("MADEOkineSansPERSONALUSE-Bold", size: 32))
            .foregroundColor(.black)
            .multilineTextAlignment(.leading)

          Text("\(rpeval, specifier: "%.1f")")
            .font(.custom("MADEOkineSansPERSONALUSE-Bold", size: 64))
            .foregroundColor(.black)

          RPESliderView(value: $rpeval, range: 0...10, step: 0.5)
            .accentColor(Color(red: 195 / 255, green: 195 / 255, blue: 195 / 255))
            .cornerRadius(10)
            .padding(.horizontal, 50)
            .introspect(.slider, on: .iOS(.v17, .v18)) { slider in
              slider.thumbTintColor = UIColor(
                red: 57 / 255, green: 57 / 255, blue: 57 / 255, alpha: 1)
              slider.minimumTrackTintColor =
                UIColor(red: 195 / 255, green: 195 / 255, blue: 195 / 255, alpha: 1)
              slider.maximumTrackTintColor =
                UIColor(red: 195 / 255, green: 195 / 255, blue: 195 / 255, alpha: 1)
            }
            .frame(maxWidth: .infinity, maxHeight: 50)

        }
      }
    }
  }
}
