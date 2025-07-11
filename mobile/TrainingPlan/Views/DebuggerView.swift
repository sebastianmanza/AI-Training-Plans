import SwiftUI


/* A view that allows instant navigation to any screen, bypassing security */
struct DebuggerView: View {

  var onStartView: () -> Void
  var onSignUpView: () -> Void
  var onLogInView: () -> Void
  var onSurveyView: () -> Void
  var onHomeView: () -> Void

  var body: some View {
    GeometryReader { geo in
      ZStack {
        //background
        Image("signupBackground")
          .resizable()
          .scaledToFill()
          .edgesIgnoringSafeArea(.all)

        //overlay stack
          VStack(spacing: 40) {
              Spacer()
              
              //logo and name, sandwiched by spacers
              VStack(spacing: 16) {
                  Image("Logo")
                      .resizable()
                      .scaledToFit()
                      .frame(width: 120, height: 120)
                  Text("ENDORPHIN")
                      .font(.custom("MADEOkineSansPERSONALUSE-Bold", size: 32))
                      .foregroundColor(.white)
              }
              
              Spacer()
              // Debugger content
              ZStack {
                  Rectangle()
                      .fill(Color.white)
                      .frame(width: geo.size.width * 0.8, height: geo.size.height * 0.6)
                      .cornerRadius(20)
                      .shadow(radius: 10)
                  
                  // Buttons for navigation
                  VStack(spacing: 20) {
                      Button("Start View") {
                          onStartView()
                      }
                      Button("Sign Up View") {
                          onSignUpView()
                      }
                      Button("Log In View") {
                          onLogInView()
                      }
                      Button("Survey View") {
                          onSurveyView()
                      }
                      Button("Home View") {
                          onHomeView()
                      }
                  }
                  .font(.custom("MADEOkineSansPERSONALUSE-Regular", size: 20))
                  .foregroundColor(.black)
              }
          }
      }
    }
  }
}
