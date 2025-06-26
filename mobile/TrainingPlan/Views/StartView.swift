import SwiftUI
import UIKit


struct LogInButton: View {
    let buttonTitle: String
    let action: () -> Void
    let color: Color

    var body: some View {
        Button(buttonTitle, action: action)
            .frame(width: 275, height: 40) // Make the button wide
            .font(.custom("MADEOkineSansPERSONALUSE-Bold", size: 20)) // Custom font
            .foregroundColor(.white) // Text color
            .background(color) // Background color
            .clipShape(Capsule()) // Capsule shape
    }
}

struct StartView: View {

    var onBegin: () -> Void

    var body: some View {
        GeometryReader { geo in
            /* Create a full-screen image background with a vertical stack */
            ZStack {
                Image("background")
                .resizable() 
                .scaledToFill() 
                .edgesIgnoringSafeArea(.all)
            
                VStack {
                    Text("WELCOME TO").font(.custom("MADEOkineSansPERSONALUSE-Medium", size: 40))
                        .foregroundColor(.white)
                    
                    Text("ENDORPHIN").font(.custom("MADEOkineSansPERSONALUSE-Black", size: 48))
                        .foregroundColor(.white)
                }
                .foregroundColor(.white)
                // Position the entire VStack at 1/3 down the screen
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
                    LogInButton(buttonTitle: "SIGN UP", action: onBegin, color: Color(red: 0, green: 54/255, blue: 104/255))
                    LogInButton(buttonTitle: "LOG IN", action: onBegin, color: Color(red: 153/255, green: 208/255, blue: 208/255))
                }
                .position(x: geo.size.width / 2, y: 3 * geo.size.height / 4)
            }
        }
    }
}
