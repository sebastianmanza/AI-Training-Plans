import SwiftUI

/* A view that allows users to sign up for the Endorphin app.
    It includes fields for email, username, and password, and provides options to log in or view terms and conditions.
    */
struct LoginView: View {

  // the current focused field
  enum Field { case username, password }
  @FocusState private var focusedField: Field?
  @State private var username = ""
  @State private var password = ""

  @State private var keyboardHeight: CGFloat = 0

  @State private var isLoading = false
  @State private var loginError: String?

  @EnvironmentObject var session: Session

  var onLoginDone: () -> Void
  var onSignUpTapped: () -> Void
  var onDebugger: () -> Void

  var body: some View {

    var extraFieldOffset: CGFloat {
      switch focusedField {
      case .password: return 58
      default: return 0
      }
    }
    GeometryReader { geo in
      ZStack {
        //background
        Image("signupBackground")
          .resizable()
          .scaledToFill()
          .edgesIgnoringSafeArea(.all)
          .blur(radius: focusedField != nil ? 12 : 0)
          .animation(.easeInOut(duration: 0.25), value: focusedField)

        //overlay stack
        ScrollViewReader { proxy in
          ScrollView(showsIndicators: false) {
            VStack(spacing: 0) {
              VStack(alignment: .leading, spacing: -30) {
                Text("MAKE")
                Text("THE")
                Text("DAYS")
                Text("COUNT.")
              }
              .font(.custom("MADEOkineSansPERSONALUSE-Bold", size: 90))
              .foregroundColor(Color.headertext)
              .frame(maxWidth: .infinity, alignment: .topLeading)
              .padding(.leading, 20)
              .opacity(focusedField == nil ? 1 : 0)  //make the text invisible when typing in a capsule

              /* Signup fields */
              ZStack {
                RoundedRectangle(cornerRadius: 30)
                  .fill(.ultraThinMaterial)
                  .opacity(focusedField == nil ? 1 : 0)

                VStack(spacing: 18) {
                  Image("Logo")
                    .resizable()
                    .scaledToFit()
                    .frame(width: 30, height: 30)
                    .opacity(focusedField == nil ? 1 : 0)

                  CapsuleTextField(
                    prompt: "Username", text: $username, height: 40, width: 273,
                    background: Color.bodytext, accentColor: Color.headertext, fontSize: 16,
                    overlayImage: Image(systemName: "person")
                  )
                  .focused($focusedField, equals: .username)
                  .opacity(focusedField == .username || focusedField == nil ? 1 : 0)
                  .offset(y: focusedField == .username ? -extraFieldOffset : 0)
                  .id(Field.username)  // make sure the username field is scrollable

                  CapsulePasswordField(
                    prompt: "Password", text: $password, height: 40, width: 273,
                    background: Color.bodytext, accentColor: Color.headertext, fontSize: 16,
                    overlayImage: Image(systemName: "lock")
                  )
                  .focused($focusedField, equals: .password)
                  .opacity(focusedField == .password || focusedField == nil ? 1 : 0)
                  .offset(y: focusedField == .password ? -extraFieldOffset : 0)
                  .id(Field.password)  // make sure the password field is scrollable

                  VStack {
                    Button {
                      Task {
                        loginError = nil
                        isLoading = true
                        let payload = LoginIn(
                          username: username,
                          password: password)
                        do {
                          let result = try await APIClient.shared.login(payload)
                          isLoading = false

                          if let userId = result.user_id {
                            // Save userID to the session
                            session.setUserID(userId)
                            onLoginDone()
                          } else if let code = result.error_code {
                            // map your backend error codes to messages:
                            loginError =
                              code == 1
                              ? "Username and password do not match"
                              : "Unknown error code: \(code)"
                          } else {
                            loginError = "Unknown server response"
                          }
                        } catch {
                          isLoading = false
                          loginError = "Network error: \(error.localizedDescription)"
                        }
                      }
                    } label: {
                      if isLoading {
                        ProgressView()
                          .progressViewStyle(CircularProgressViewStyle())
                          .frame(maxWidth: .infinity)
                          .foregroundColor(.white)
                      } else {
                        Text("Login")
                          .font(.custom("MADEOkineSansPERSONALUSE-Bold", size: 16))
                          .foregroundColor(Color.headertext)
                          .frame(maxWidth: min(273, geo.size.width * 0.85), minHeight: 40)
                          .background(Color.accent)
                          .clipShape(Capsule())
                      }
                    }
                    .disabled(isLoading)
                    .opacity(focusedField == nil ? 1 : 0)
                    if let error = loginError {
                      Text(error)
                        .foregroundColor(.red)
                        .font(.custom("MADEOkineSansPERSONALUSE-Regular", size: 12))
                        .multilineTextAlignment(.center)
                        .padding(.horizontal, 20)
                    }
                  }

                  VStack {
                    Text("Don't have an account?")
                      .font(.custom("MADEOkineSansPERSONALUSE-Light", size: 14))
                      .foregroundColor(.white)
                      .blur(radius: focusedField != nil ? 12 : 0)

                    Button(action: onSignUpTapped) {
                      Text("Sign up")
                        .font(.custom("MADEOkineSansPERSONALUSE-Bold", size: 16))
                        .foregroundColor(.white)
                        .frame(maxWidth: min(275, geo.size.width * 0.85), minHeight: 40)
                        .background(Color.mainbackground)
                        .clipShape(Capsule())
                    }
                    .opacity(focusedField == nil ? 1 : 0)
                  }
                }
                //keyboard height adjustment
                .onReceive(
                  NotificationCenter.default
                    .publisher(for: UIResponder.keyboardWillShowNotification)
                ) { note in
                  if let r = note.userInfo?[UIResponder.keyboardFrameEndUserInfoKey] as? CGRect {
                    keyboardHeight = r.height
                  }
                }
                .onReceive(
                  NotificationCenter.default
                    .publisher(for: UIResponder.keyboardWillHideNotification)
                ) { _ in
                  keyboardHeight = 0
                }

              }
              .contentShape(Rectangle())
              .onTapGesture { focusedField = nil }
              .frame(width: geo.size.width * 0.85, height: geo.size.height * 0.45)
              Spacer()
            }
            .padding(.bottom, keyboardHeight)
            .onChange(of: focusedField) { field in
              guard let field = field else { return }
              withAnimation {
                proxy.scrollTo(field, anchor: .bottom)
              }
            }
          }
          .onTapGesture { focusedField = nil }
        }
        .frame(maxWidth: .infinity)
      }

    }
  }
}
