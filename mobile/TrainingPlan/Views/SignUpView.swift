import SwiftUI

/* A view that allows users to sign up for the Endorphin app.
    It includes fields for email, username, and password, and provides options to log in or view terms and conditions.
    */
struct SignUpView: View {

  // the current focused field
  enum Field { case email, username, password }
  @FocusState private var focusedField: Field?

  @State private var email = ""
  @State private var username = ""
  @State private var password = ""
  @State private var showingTerms = false

  @State private var keyboardHeight: CGFloat = 0

  @State private var isLoading = false
  @State private var signupError: String?

  @EnvironmentObject var session: Session

  var onSignUpDone: () -> Void
  var onLogInTapped: () -> Void
  var onDebugger: () -> Void

  var body: some View {

    var extraFieldOffset: CGFloat {
      switch focusedField {
      case .username: return 58
      case .password: return 116
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
                    prompt: "Email", text: $email, height: 40, width: 273,
                    background: Color.bodytext,
                    accentColor: Color.headertext, fontSize: 16,
                    overlayImage: Image(systemName: "envelope")
                  )
                  .focused($focusedField, equals: .email)
                  .opacity(focusedField == .email || focusedField == nil ? 1 : 0)
                  .id(Field.email)  // make sure the email field is scrollable

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
                        signupError = nil
                        isLoading = true
                        let payload = SignupIn(
                          email: email,
                          username: username,
                          password: password)
                        do {
                          let result = try await APIClient.signup(payload)
                          isLoading = false

                          if let userId = result.user_id {
                            // Save userID to the session
                            session.setUserID(userId)
                            onSignUpDone()
                          } else if let code = result.error_code {
                            // map your backend error codes to messages:
                            signupError =
                              code == 0
                              ? "Username already exists."
                              : "Email already exists."
                          } else {
                            signupError = "Unknown server response"
                          }
                        } catch {
                          isLoading = false
                          signupError = "Network error: \(error.localizedDescription)"
                        }
                      }
                    } label: {
                      if isLoading {
                        ProgressView()
                          .progressViewStyle(CircularProgressViewStyle())
                          .frame(maxWidth: .infinity)
                          .foregroundColor(.white)
                      } else {
                        Text("Sign up")
                          .font(.custom("MADEOkineSansPERSONALUSE-Bold", size: 16))
                          .foregroundColor(Color.headertext)
                          .frame(maxWidth: min(273, geo.size.width * 0.85), minHeight: 40)
                          .background(Color.accent)
                          .clipShape(Capsule())
                      }
                    }
                    .disabled(isLoading)
                    .opacity(focusedField == nil ? 1 : 0)
                    if let error = signupError {
                      Text(error)
                        .foregroundColor(.red)
                        .font(.custom("MADEOkineSansPERSONALUSE-Regular", size: 12))
                        .multilineTextAlignment(.center)
                        .padding(.horizontal, 20)
                    }
                  }

                  VStack {
                    Text("Already have an account?")
                      .font(.custom("MADEOkineSansPERSONALUSE-Light", size: 14))
                      .foregroundColor(.white)
                      .blur(radius: focusedField != nil ? 12 : 0)

                    Button(action: onLogInTapped) {
                      Text("Login")
                        .font(.custom("MADEOkineSansPERSONALUSE-Bold", size: 16))
                        .foregroundColor(.white)
                        .frame(maxWidth: min(275, geo.size.width * 0.85), minHeight: 40)
                        .background(Color.mainbackground)
                        .clipShape(Capsule())
                    }
                    .opacity(focusedField == nil ? 1 : 0)
                    Button(action: { showingTerms = true }) {
                      Text("Terms and Conditions")
                        .underline()
                        .foregroundColor(Color.bodytext)
                        .font(.custom("MADEOkineSansPERSONALUSE-Light", size: 8))
                        .frame(maxWidth: .infinity, alignment: .leading)
                        .padding(.horizontal, 55)
                    }
                    .sheet(isPresented: $showingTerms) {
                      TermsView()
                    }
                    .blur(radius: focusedField != nil ? 12 : 0)
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
              .frame(width: geo.size.width * 0.85, height: geo.size.height * 0.5)
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
        // .edgesIgnoringSafeArea(.all)
      }

    }
  }
}
