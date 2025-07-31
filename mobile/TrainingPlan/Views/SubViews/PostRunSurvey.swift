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
        RPEView(
          onNext: {
            currentStep = .rpe
          },
          rpeval: $rpeval)
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
    var onNext: () -> Void
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
        VStack(spacing: 15) {

          Text("What was your\nRPE today?")
            .font(.custom("MADEOkineSansPERSONALUSE-Bold", size: 40))
            .foregroundColor(.black)
            .multilineTextAlignment(.leading)
            .frame(maxWidth: .infinity, alignment: .leading)
            .padding(.leading, 50)

          Text("\(rpeval, specifier: "%.1f")")
            .font(.custom("MADEOkineSansPERSONALUSE-Bold", size: 84))
            .foregroundColor(.black)

          RPESliderView(value: $rpeval, range: 0...10, step: 0.5)
            .padding(.horizontal, 50)
            .introspect(.slider, on: .iOS(.v17, .v18)) { slider in
              slider.thumbTintColor = UIColor(
                red: 57 / 255, green: 57 / 255, blue: 57 / 255, alpha: 1)
              slider.minimumTrackTintColor =
                UIColor(red: 195 / 255, green: 195 / 255, blue: 195 / 255, alpha: 1)
              slider.maximumTrackTintColor =
                UIColor(red: 195 / 255, green: 195 / 255, blue: 195 / 255, alpha: 1)
            }
            .frame(maxHeight: 30)

          Spacer()
          // Next button
          SurveyNextButton(
            action: onNext, color: Color(red: 130 / 255, green: 245 / 255, blue: 209 / 255),
            foreground: .black
          )
          .shadow(color: .black.opacity(0.1), radius: 20, x: 0, y: 0)
          .padding(.bottom, 50)
        }
      }
    }
  }
}
