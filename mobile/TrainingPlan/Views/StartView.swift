import SwiftUI
import UIKit


/* The intro screen shown when the app launches for the first time: or if you haven't
    logged in recently */
struct StartView: View {

    var onSignUpTapped: () -> Void
    var onLogInTapped: () -> Void
    var onDebugger: () -> Void

    var body: some View {
        GeometryReader { geo in
            /* Create a full-screen image background with a vertical stack */
            ZStack {
                Image("background")
                .resizable() 
                .scaledToFill() 
                .edgesIgnoringSafeArea(.all)
            
                /* Title text */
                VStack {
                    Text("WELCOME TO").font(.custom("MADEOkineSansPERSONALUSE-Medium", size: 40))
                        .foregroundColor(.white)
                    
                    Text("ENDORPHIN").font(.custom("MADEOkineSansPERSONALUSE-Black", size: 48))
                        .foregroundColor(.white)
                }
                .foregroundColor(.white)
                // Position the entire VStack at 1/4 down the screen
                .position(x: geo.size.width / 2,
                          y: geo.size.height / 4)

                /* Add the logo */
                Image("Logo")
                    .resizable()
                    .scaledToFit()
                    .frame(width: 130, height: 130)
                    .position(x: geo.size.width / 2, y: geo.size.height / 2)

                /* Create log in and signup buttons */
                VStack(spacing: 20) {
                    LogInButton(buttonTitle: "SIGN UP", action: onSignUpTapped, color: Color(red: 0, green: 54/255, blue: 104/255))
                    LogInButton(buttonTitle: "LOG IN", action: onLogInTapped, color: Color(red: 153/255, green: 208/255, blue: 208/255))
                }
                .position(x: geo.size.width / 2, y: 3 * geo.size.height / 4)
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
