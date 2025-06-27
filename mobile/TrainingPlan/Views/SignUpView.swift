import SwiftUI

struct TermsView: View {
    var body: some View {
        ScrollView {
            VStack(alignment: .leading, spacing: 16) {
                Text("TERMS AND CONDITIONS")
                    .font(.title)
                    .bold()
                    .padding(.bottom, 10)

                Group {
                    Text("Welcome to Endorphin. By using this app, you agree to the following terms and conditions. If you do not agree, please do not use the app.")

                    Text("1. No Medical Advice")
                        .font(.headline)
                    Text("The Endorphin app is for informational and educational purposes only. It does not provide medical advice, diagnosis, or treatment. Always consult your physician or a qualified health provider before beginning any exercise program or making changes to your health regimen.")

                    Text("2. Assumption of Risk")
                        .font(.headline)
                    Text("By using this app, you acknowledge and agree that physical activity involves inherent risks, including injury, illness, or death. You voluntarily assume full responsibility for any risks, known or unknown, associated with your use of this app and its content.")

                    Text("3. No Guarantees")
                        .font(.headline)
                    Text("We do not guarantee that our recommendations will lead to any specific fitness or health outcome. All results vary based on individual conditions and effort.")
                }

                Group {
                    Text("4. Limitation of Liability")
                        .font(.headline)
                    Text("To the fullest extent permitted by law, Endorphin, its creators, affiliates, and partners shall not be liable for any direct, indirect, incidental, consequential, special, or punitive damages, including but not limited to injury, loss of use, data, or profits, arising out of or related to your use of the app.")

                    Text("5. No Warranty")
                        .font(.headline)
                    Text("This app and its content are provided “as is” and without warranties of any kind, whether express or implied.")

                    Text("6. User Responsibility")
                        .font(.headline)
                    Text("You are solely responsible for your health, actions, and any consequences that arise from following advice or plans provided in this app.")

                    Text("7. Changes to These Terms")
                        .font(.headline)
                    Text("We reserve the right to update or modify these Terms at any time without prior notice. Continued use of the app after changes constitutes acceptance of the new terms.")

                    Text("8. Contact")
                        .font(.headline)
                    Text("If you have any questions or concerns about these Terms, please contact us at [Insert Email or Contact Info].")
                }

                Text("By using this app, you acknowledge that you have read, understood, and agreed to these terms and conditions.")
            }
            .padding()
        }
        .navigationTitle("Terms & Conditions")
    }
}


struct SignUpView: View {

    @State private var email = ""
    @State private var username = ""
    @State private var password = ""
    @State private var showingTerms = false

    var onSignUpDone: () -> Void
    var onLogInTapped: () -> Void

    var body: some View {
        GeometryReader { geo in
            /* Create a full-screen image background with a vertical stack */
            ZStack {
                Image("signupBackground")
                .resizable() 
                .scaledToFill() 
                .edgesIgnoringSafeArea(.all)

                ZStack {
                    Rectangle()
                        .fill(Color.white)
                        .frame(width: geo.size.width * 0.85, height: geo.size.height * 0.65)
                        .cornerRadius(40)
                    
                    VStack {
                        CapsuleTextField(prompt: "Email", text: $email)
                            .padding(.bottom, 10)
                    
                        CapsuleTextField(prompt: "Username", text: $username)
                            .padding(.bottom, 10)
                    
                        CapsulePasswordField(prompt: "Password", text: $password)
                            .padding(.bottom, 20)

                        Button(action: onSignUpDone) {
                            Text("Sign up")
                                .font(.custom("MADEOkineSansPERSONALUSE-Bold", size: 16))
                                .foregroundColor(.white)
                                .frame(width: 275, height: 40)
                                .background(Color(red: 0, green: 54/255, blue: 104/255))
                                .clipShape(Capsule())
                        }
                            .padding(.bottom, 30)
                        
                        Text("Already have an account?")
                            .font(.custom("MADEOkineSansPERSONALUSE-Light", size: 14))
                            .foregroundColor(.black)

                        Button(action: onLogInTapped) {
                            Text("Login")
                                .font(.custom("MADEOkineSansPERSONALUSE-Bold", size: 16))
                                .foregroundColor(.white)
                                .frame(width: 275, height: 40)
                                .background(Color(red: 153/255, green: 208/255, blue: 208/255))
                                .clipShape(Capsule())
                        }

                        Button(action: {
                            showingTerms = true
                            }) {
                            Text("Terms and Conditions")
                            .underline()
                            .foregroundColor(.gray)
                            .font(.custom("MADEOkineSansPERSONALUSE-Light", size: 8))
                            .frame(maxWidth: .infinity, alignment: .leading)
                            .padding(.horizontal, 64)
                            }
                            .sheet(isPresented: $showingTerms) {
                        TermsView()
                            }
                    }
                }
                .position(x: geo.size.width / 2, y: 2 * geo.size.height / 3)
                
                
                VStack {
                    Image("Logo")
                        .resizable()
                        .scaledToFit()
                        .frame(width: 115, height: 115)

                    Text("ENDORPHIN")
                        .font(.custom("MADEOkineSansPERSONALUSE-Bold", size: 32))
                        .foregroundColor(.white)
                }
                .position(x: geo.size.width / 2, y: geo.size.height / 5)

                
            }
        }
    }
}
