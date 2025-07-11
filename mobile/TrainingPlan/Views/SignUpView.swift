import SwiftUI

/* A view that displays the terms and conditions for the Endorphin app. */
struct TermsView: View {
  var body: some View {
    ScrollView {
      VStack(alignment: .leading, spacing: 16) {
        Text("TERMS AND CONDITIONS")
          .font(.title)
          .bold()
          .padding(.bottom, 10)

        Group {
          Text(
            "Welcome to Endorphin. By using this app, you agree to the following terms and conditions. If you do not agree, please do not use the app."
          )

          Text("1. No Medical Advice")
            .font(.headline)
          Text(
            "The Endorphin app is for informational and educational purposes only. It does not provide medical advice, diagnosis, or treatment. Always consult your physician or a qualified health provider before beginning any exercise program or making changes to your health regimen."
          )

          Text("2. Assumption of Risk")
            .font(.headline)
          Text(
            "By using this app, you acknowledge and agree that physical activity involves inherent risks, including injury, illness, or death. You voluntarily assume full responsibility for any risks, known or unknown, associated with your use of this app and its content."
          )

          Text("3. No Guarantees")
            .font(.headline)
          Text(
            "We do not guarantee that our recommendations will lead to any specific fitness or health outcome. All results vary based on individual conditions and effort."
          )

          Text("4. Limitation of Liability")
            .font(.headline)
          Text(
            "To the fullest extent permitted by law, Endorphin, its creators, affiliates, and partners shall not be liable for any direct, indirect, incidental, consequential, special, or punitive damages, including but not limited to injury, loss of use, data, or profits, arising out of or related to your use of the app."
          )

          Text("5. No Warranty")
            .font(.headline)
          Text(
            "This app and its content are provided “as is” and without warranties of any kind, whether express or implied."
          )

          Text("6. User Responsibility")
            .font(.headline)
          Text(
            "You are solely responsible for your health, actions, and any consequences that arise from following advice or plans provided in this app."
          )

          Text("7. Changes to These Terms")
            .font(.headline)
          Text(
            "We reserve the right to update or modify these Terms at any time without prior notice. Continued use of the app after changes constitutes acceptance of the new terms."
          )

          Text("8. Contact")
            .font(.headline)
          Text(
            "If you have any questions or concerns about these Terms, please contact us at [Insert Email or Contact Info]."
          )
        }

        Text(
          "By using this app, you acknowledge that you have read, understood, and agreed to these terms and conditions."
        )
      }
      .padding()
    }
    .navigationTitle("Terms & Conditions")
  }
}

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

  @State private var isLoading = false
  @State private var signupError: String?

  @EnvironmentObject var session: Session

  var onSignUpDone: () -> Void
  var onLogInTapped: () -> Void

  var body: some View {
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
              CapsuleTextField(prompt: "Email", text: $email)
                .focused($focusedField, equals: .email)
                .opacity(focusedField == .email || focusedField == nil ? 1 : 0)
                .offset(y: focusedField == .email ? 40 : 0)

              CapsuleTextField(prompt: "Username", text: $username)
                .focused($focusedField, equals: .username)
                .opacity(focusedField == .username || focusedField == nil ? 1 : 0)
                .offset(y: focusedField == .username ? -25 : 0)

              CapsulePasswordField(prompt: "Password", text: $password)
                .focused($focusedField, equals: .password)
                .opacity(focusedField == .password || focusedField == nil ? 1 : 0)
                .offset(y: focusedField == .password ? -90 : 0)

              // Sign up button below them, slight padding on top and bottom
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
                        ? "Username already exists"
                        : "Email already exists"
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
                } else {
                  Text("Sign up")
                    .font(.custom("MADEOkineSansPERSONALUSE-Bold", size: 16))
                    .foregroundColor(.white)
                    .frame(maxWidth: min(275, geo.size.width * 0.85), minHeight: 40)
                    .background(Color(red: 0, green: 54 / 255, blue: 104 / 255))
                    .clipShape(Capsule())
                }
              }
              .disabled(isLoading)
              .padding(.top, 10)
              .blur(radius: focusedField != nil ? 12 : 0)

              // Another Vstack for the already have an account/terms
              VStack {
                Text("Already have an account?")
                  .font(.custom("MADEOkineSansPERSONALUSE-Light", size: 14))
                  .foregroundColor(.black)
                  .blur(radius: focusedField != nil ? 12 : 0)

                Button(action: onLogInTapped) {
                  Text("Login")
                    .font(.custom("MADEOkineSansPERSONALUSE-Bold", size: 16))
                    .foregroundColor(.white)
                    .frame(maxWidth: min(275, geo.size.width * 0.85), minHeight: 40)
                    .background(Color(red: 153 / 255, green: 208 / 255, blue: 208 / 255))
                    .clipShape(Capsule())
                }
                .blur(radius: focusedField != nil ? 12 : 0)

                //TERMS LINK
                Button(action: { showingTerms = true }) {
                  Text("Terms and Conditions")
                    .underline()
                    .foregroundColor(.gray)
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
            .padding(.vertical, 30)
          }
          Spacer()
            .frame(maxWidth: .infinity, alignment: .center)
        }
        .contentShape(Rectangle())
        .onTapGesture { focusedField = nil }
      }
    }
  }
}
