import SwiftUI

struct LoginView: View {

  enum Field { case username, password }
  @FocusState private var focusedField: Field?

  @State private var username = ""
  @State private var password = ""

  var onLoginDone: () -> Void
  var onSignUpTapped: () -> Void
  var onDebugger: () -> Void

  var body: some View {
    GeometryReader { geo in
      /* Create a full-screen image background with a vertical stack */
      ZStack {
        Image("signupBackground")
          .resizable()
          .scaledToFill()
          .edgesIgnoringSafeArea(.all)
          .blur(radius: focusedField != nil ? 12 : 0)
          .animation(.easeInOut(duration: 0.25), value: focusedField)

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
          .blur(radius: focusedField != nil ? 12 : 0)
          .animation(.easeInOut(duration: 0.25), value: focusedField)

          Spacer()

          // The white rectangle that took an amazing amount of work
          ZStack {
            RoundedRectangle(cornerRadius: 40)
              .fill(Color.white)
              .frame(width: geo.size.width * 0.85)
              .blur(radius: focusedField != nil ? 12 : 0)
              .animation(.easeInOut(duration: 0.25), value: focusedField)
            // .padding(.bottom, 45)

            // Capsule text fields for entering text, become clear when either of the other
            // two is pressed

            VStack(spacing: 15) {
              // Username and password fields
//              CapsuleTextField(prompt: "Username", text: $username)
//                .focused($focusedField, equals: .username)
//                .opacity(focusedField == .username || focusedField == nil ? 1 : 0)
//                .offset(y: focusedField == .username ? 25 : 0)
//
//              CapsulePasswordField(prompt: "Password", text: $password)
//                .focused($focusedField, equals: .password)
//                .opacity(focusedField == .password || focusedField == nil ? 1 : 0)
//                .offset(y: focusedField == .password ? -40 : 0)

              // Sign up button below them, slight padding on top and bottom
              Button(action: onLoginDone) {
                Text("Login")
                  .font(.custom("MADEOkineSansPERSONALUSE-Bold", size: 16))
                  .foregroundColor(.white)
                  .frame(maxWidth: min(275, geo.size.width * 0.85), minHeight: 40)
                  .background(Color(red: 0, green: 54 / 255, blue: 104 / 255))
                  .clipShape(Capsule())
              }
              .padding(.top, 10)
              .blur(radius: focusedField != nil ? 12 : 0)

              // Another Vstack for the already have an account/terms
              VStack {
                Text("Don't have an account?")
                  .font(.custom("MADEOkineSansPERSONALUSE-Light", size: 14))
                  .foregroundColor(.black)
                  .blur(radius: focusedField != nil ? 12 : 0)

                Button(action: onSignUpTapped) {
                  Text("Sign up")
                    .font(.custom("MADEOkineSansPERSONALUSE-Bold", size: 16))
                    .foregroundColor(.white)
                    .frame(maxWidth: min(275, geo.size.width * 0.85), minHeight: 40)
                    .background(Color(red: 153 / 255, green: 208 / 255, blue: 208 / 255))
                    .clipShape(Capsule())
                }
                .blur(radius: focusedField != nil ? 12 : 0)
              }
            }
            .padding(.vertical, 30)
          }
          Spacer()
            .frame(maxWidth: .infinity, alignment: .center)
        }
        .contentShape(Rectangle())
        .onTapGesture { focusedField = nil }
      }
      .overlay(alignment: .topLeading) {
        Button {
          onDebugger()
        } label: {
          Color.black.opacity(0.001)
        }
        .frame(width: 50, height: 50)
        .contentShape(Rectangle())
        .buttonStyle(.plain)
      }

    }
  }
}
