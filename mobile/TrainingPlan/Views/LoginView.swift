import SwiftUI

struct LoginView: View {

    @State private var username = ""
    @State private var password = ""

    var onLoginDone: () -> Void
    var onSignUpTapped: () -> Void

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
                        .frame(width: geo.size.width * 0.85, height: geo.size.height * 0.5)
                        .cornerRadius(40)
                    
                    VStack {
                        CapsuleTextField(prompt: "Username", text: $username)
                            .padding(.bottom, 10)
                    
                        CapsulePasswordField(prompt: "Password", text: $password)
                            .padding(.bottom, 20)

                        Button(action: onLoginDone) {
                            Text("Login")
                                .font(.custom("MADEOkineSansPERSONALUSE-Bold", size: 16))
                                .foregroundColor(.white)
                                .frame(width: 275, height: 40)
                                .background(Color(red: 0, green: 54/255, blue: 104/255))
                                .clipShape(Capsule())
                        }
                            .padding(.bottom, 30)
                        
                        Text("Need an account?")
                            .font(.custom("MADEOkineSansPERSONALUSE-Light", size: 14))
                            .foregroundColor(.black)

                        Button(action: onSignUpTapped) {
                            Text("Sign up")
                                .font(.custom("MADEOkineSansPERSONALUSE-Bold", size: 16))
                                .foregroundColor(.white)
                                .frame(width: 275, height: 40)
                                .background(Color(red: 153/255, green: 208/255, blue: 208/255))
                                .clipShape(Capsule())
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